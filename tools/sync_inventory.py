#!/usr/bin/env python3
"""Export 'File Inventory' tab as CSV, then preview or write the GitHub inventory snapshot.

No files are renamed, no status is approved and no Google Sheet is modified.
"""
import argparse
import csv
import hashlib
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "inventory.csv"
LIBRARY = ROOT / "Rig-Engineering-Files"

def read(path):
    with path.open(newline="", encoding="utf-8-sig") as fh:
        rdr = csv.DictReader(fh)
        return list(rdr.fieldnames or []), list(rdr)

def git_blob_sha(file):
    content = file.read_bytes()
    return hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("exported_csv", type=Path)
parser.add_argument("--write", action="store_true", help="Write inventory.csv after reviewing the preview")
args = parser.parse_args()
columns, spreadsheet = read(args.exported_csv)
old_columns, old_rows = read(DEST)
needs = (
    "File ID", "Current Filename (Original Source)", "Repository Filename (Live)",
    "Repository Path", "File Status", "Format", "File Role", "Functional Area",
    "Component Group",
)
for col in needs:
    if col not in columns:
        parser.error("Expected export of 'File Inventory' tab; missing: " + col)
if "Original Source Blob SHA" not in old_columns or "Current Blob SHA" not in old_columns:
    parser.error("Repository CSV schema needs original and current content hashes")
older = {r["File ID"]: r for r in old_rows}
if len(older) != len(old_rows):
    parser.error("Duplicate File IDs already exist in repository CSV")

result, seen = [], set()
for row in spreadsheet:
    fid = row["File ID"].strip()
    if not fid:
        continue
    if fid in seen:
        parser.error("Duplicate spreadsheet file ID: " + fid)
    seen.add(fid)
    live_name = row["Repository Filename (Live)"].strip()
    rel = row["Repository Path"].strip()
    file = (ROOT / rel).resolve()
    if file.name != live_name or not file.is_relative_to(LIBRARY.resolve()) or not file.is_file():
        parser.error(f"Live filename/path does not match GitHub checkout: {fid} {rel}")
    sha = git_blob_sha(file)
    expected = (row.get("File SHA") or "").strip()
    if expected and expected != sha:
        parser.error(f"Spreadsheet SHA needs update for {fid}: actual file changed")
    before = older.get(fid)
    if before is None:
        before = dict.fromkeys(old_columns, "")
        before["File ID"] = fid
        before["Original Source Blob SHA"] = sha
        before["Verification Status"] = "Unverified"
    current = dict(before)
    updates = {
        "Current Filename": live_name,
        "Current Path": rel,
        "Format": row["Format"],
        "File Role": row["File Role"],
        "Functional System": row["Functional Area"],
        "Subgroup": row["Component Group"],
        "Verification Status": row["File Status"] or "Unverified",
        "Current Blob SHA": sha,
    }
    for dest, source in (
        ("Original Filename", "Current Filename (Original Source)"),
        ("Original Source URL", "Original Source URL"),
        ("Original Source Path", "Original Source Path"),
        ("Revision Pending", "Revision Pending"),
        ("Rig Status", "Rig Status"),
        ("Last Verified", "Last Verified"),
        ("Related Parts / Notes", "Notes / Issues"),
    ):
        value = (row.get(source) or "").strip()
        if value:
            updates[dest] = value
    date = (row.get("Last Used") or "").strip() or (row.get("Last Printed") or "").strip()
    if date:
        updates["Last Used or Printed"] = date
    current.update(updates)
    result.append(current)
if set(older) - seen:
    parser.error("Spreadsheet is missing registered IDs; retire a file explicitly instead of silently deleting its inventory record")
changed = sum(result_row != older.get(result_row["File ID"]) for result_row in result)
new_ids = [r["File ID"] for r in result if r["File ID"] not in older]
print(f"{len(result)} records; {changed} changes; {len(new_ids)} new IDs.")
if not args.write:
    print("Preview only. Use --write after reviewing changes, then inspect git diff and run the validator.")
else:
    with NamedTemporaryFile("w", encoding="utf-8-sig", newline="", dir=DEST.parent, delete=False) as fh:
        writer = csv.DictWriter(fh, fieldnames=old_columns)
        writer.writeheader()
        writer.writerows(result)
        tmp = fh.name
    os.replace(tmp, DEST)
    print("Updated inventory.csv; review the Git diff before committing.")
