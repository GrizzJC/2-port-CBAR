#!/usr/bin/env python3
"""Preview or synchronize the GitHub inventory snapshot from the existing Google Sheet export.

Export only the 'File Inventory' tab as CSV. Does not rename files or approve status.
"""
import argparse
import csv
from pathlib import Path
from tempfile import NamedTemporaryFile
import os
import sys

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "inventory.csv"

def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("exported_csv", type=Path)
parser.add_argument("--write", action="store_true", help="Update inventory.csv after a clean preview")
args = parser.parse_args()
heads, source = read_rows(args.exported_csv)
existing_heads, saved = read_rows(DEST)
needed = ["File ID", "Repository Filename (Live)", "Repository Path", "File Status", "Original Source Path", "File SHA"]
missing = [field for field in needed if field not in heads]
if missing:
    parser.error("Export must be from the 'File Inventory' tab; missing: " + ", ".join(missing))
index = {row["File ID"]: row for row in saved}
if len(index) != len(saved):
    parser.error("GitHub inventory has duplicate IDs")
seen = set()
changed = 0
result = []
for record in source:
    fid = record["File ID"].strip()
    if not fid:
        continue
    if fid in seen:
        parser.error(f"Duplicate spreadsheet ID {fid}")
    seen.add(fid)
    if fid not in index:
        parser.error(f"New ID {fid} requires manual intake with source/provenance first")
    previous = dict(index[fid])
    current = record["Repository Filename (Live)"].strip()
    path = record["Repository Path"].strip()
    real_path = ROOT / path
    if real_path.name != current or not real_path.is_file():
        parser.error(f"File not found or name mismatch for {fid}: {path}. Proposals are NOT live filenames.")
    if previous["Source Blob SHA"] != record["File SHA"].strip():
        parser.error(f"Blob identifier mismatch for {fid}; review modified source and update tracking explicitly")
    previous.update({
        "Current Filename": current,
        "Current Path": path,
        "Verification Status": record["File Status"].strip() or "Unverified",
        "Revision Pending": record.get("Revision Pending", previous.get("Revision Pending", "")),
        "Rig Status": record.get("Rig Status", previous.get("Rig Status", "")),
        "Last Verified": record.get("Last Verified", ""),
        "Last Used or Printed": record.get("Last Printed", "") or record.get("Last Used", ""),
        "Related Parts / Notes": record.get("Notes / Issues", ""),
    })
    result.append(previous)
    if previous != index[fid]:
        changed += 1
if seen != set(index):
    parser.error("Mismatch: spreadsheet and repository snapshots must contain the same registered IDs")
print(f"{len(result)} records; {changed} records differ from the repository snapshot.")
if not args.write:
    print("Preview only; pass --write after reviewing the source and upcoming Git diff.")
    sys.exit(0)
with NamedTemporaryFile("w", encoding="utf-8", newline="", dir=DEST.parent, delete=False) as tmp:
    writer = csv.DictWriter(tmp, fieldnames=existing_heads, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(result)
    temp_name = tmp.name
os.replace(temp_name, DEST)
print("Updated inventory.csv; inspect git diff and run python tools/validate_repository.py.")
