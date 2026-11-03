#!/usr/bin/env python3
"""Check registered engineering files and paths. No third-party libraries."""
import csv
import hashlib
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory.csv"
LIBRARY = ROOT / "Rig-Engineering-Files"
FOLDERS = {"3DP": "3D-Printing", "CNC": "CNC", "SW": "Code", "EL": "Electronics", "VIS": "Images-and-Diagrams"}
ID_PATTERN = re.compile(r"^(3DP|CNC|SW|EL|VIS)-[1-7]-[1-9][0-9]{2}$")
issues = []

def error(message):
    issues.append(message)

def git_blob_sha(file):
    content = file.read_bytes()
    return hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()

with INVENTORY.open(newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    required = ("File ID", "Current Filename", "Current Path", "Format", "Current Blob SHA")
    if not set(required).issubset(reader.fieldnames or []):
        error("Missing required inventory columns: " + ", ".join(required))
        records = []
    else:
        records = list(reader)

seen_ids, seen_paths = set(), set()
for i, r in enumerate(records, 2):
    fid, rel = r["File ID"].strip(), r["Current Path"].strip()
    if fid in seen_ids:
        error(f"line {i}: duplicate file ID {fid}")
    if rel in seen_paths:
        error(f"line {i}: duplicate path {rel}")
    seen_ids.add(fid)
    seen_paths.add(rel)
    match = ID_PATTERN.fullmatch(fid)
    if not match:
        error(f"line {i}: invalid ID {fid}")
        continue
    parts = Path(rel).parts
    typ = match[1]
    if len(parts) not in (4, 5) or parts[0] != "Rig-Engineering-Files" or not re.match(r"^0[1-7]-", parts[1]) or parts[2] != FOLDERS[typ]:
        error(f"line {i}: wrong engineering folder for {fid}: {rel}")
    # The ID is intentionally stable after future functional reclassification.
    # Therefore its original system/subgroup digits need not match today's folder.
    name = Path(rel).name
    if name != r["Current Filename"].strip():
        error(f"line {i}: filename/path mismatch for {fid}")
    if name.rsplit(".", 1)[-1].upper() != r["Format"].strip().upper():
        error(f"line {i}: incorrect format for {name}")
    if typ == "3DP" and Path(name).suffix.lower() in (".stl", ".3mf") and not name.startswith(fid + "_"):
        error(f"line {i}: printing filename must include assigned ID: {name}")
    file = ROOT / rel
    if not file.is_file() or not file.resolve().is_relative_to(LIBRARY.resolve()):
        error(f"line {i}: registered file missing/unsafe path: {rel}")
    elif git_blob_sha(file) != r["Current Blob SHA"].strip():
        error(f"line {i}: recorded current content hash differs: {rel}")

actual = {
    f.relative_to(ROOT).as_posix()
    for f in LIBRARY.rglob("*")
    if f.is_file() and f.name != ".gitkeep" and f.name != "README.md"
}
for p in sorted(actual - seen_paths):
    error("Engineering file not registered in inventory: " + p)
for p in sorted(seen_paths - actual):
    error("Inventory file does not exist: " + p)
for p in LIBRARY.rglob(".gitkeep"):
    if any(f.name != ".gitkeep" for f in p.parent.iterdir()):
        error("Remove unused .gitkeep from populated folder: " + p.relative_to(ROOT).as_posix())
if issues:
    for msg in issues:
        print("ERROR:", msg, file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(records)} records, file paths and current content hashes verified.")
