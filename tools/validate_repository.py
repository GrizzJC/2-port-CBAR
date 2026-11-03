#!/usr/bin/env python3
"""Verify the repository's lightweight file-inventory contract; no outside dependencies."""
import csv
import hashlib
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "inventory.csv"
PRINT_RE = re.compile(r"^3DP-(\d)-(\d)(\d\d)_.+\.(?:stl|3mf)$", re.I)
ID_RE = re.compile(r"^3DP-(\d)-(\d)(\d\d)$")
errors = []

def fail(message):
    errors.append(message)

def blob_sha(path):
    content = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()

with REGISTER.open(encoding="utf-8-sig", newline="") as handle:
    reader = csv.DictReader(handle)
    required = ("File ID", "Current Filename", "Format", "Current Path", "Source Blob SHA")
    if not set(required).issubset(reader.fieldnames or []):
        fail("inventory.csv is missing required columns: " + ", ".join(required))
        rows = []
    else:
        rows = list(reader)

ids = set()
registered = set()
for index, row in enumerate(rows, 2):
    fid = row["File ID"].strip()
    rel = row["Current Path"].strip()
    name = row["Current Filename"].strip()
    if fid in ids:
        fail(f"line {index}: duplicate File ID {fid}")
    ids.add(fid)
    if rel in registered:
        fail(f"line {index}: duplicate path {rel}")
    registered.add(rel)
    m = ID_RE.fullmatch(fid)
    expected = Path("Rig-Engineering-Files")
    if m is None:
        fail(f"line {index}: unexpected ID format {fid}")
        continue
    path = ROOT / rel
    parts = Path(rel).parts
    if len(parts) != 5 or parts[0] != str(expected) or not parts[1].startswith(f"0{m[1]}-") or parts[2] != "3D-Printing" or not parts[3].startswith(f"0{m[2]}-"):
        fail(f"line {index}: ID/system/subgroup/path mismatch: {rel}")
    if Path(rel).name != name or not name.startswith(fid + "_"):
        fail(f"line {index}: filename does not match record and ID: {name}")
    if name.rsplit(".", 1)[-1].upper() != row["Format"].strip().upper():
        fail(f"line {index}: extension/format mismatch for {name}")
    if not path.is_file():
        fail(f"line {index}: referenced file not found: {rel}")
    elif blob_sha(path) != row["Source Blob SHA"].strip():
        fail(f"line {index}: file contents differ from recorded Git blob: {rel}")

present = {p.relative_to(ROOT).as_posix() for p in (ROOT / "Rig-Engineering-Files").rglob("*") if p.is_file() and p.suffix.lower() in (".stl", ".3mf")}
for path in sorted(present - registered):
    fail("unregistered printing file: " + path)
for path in sorted(registered - present):
    fail("inventory path absent from printing files: " + path)

for placeholder in (ROOT / "Rig-Engineering-Files").rglob(".gitkeep"):
    if any(p.name != ".gitkeep" for p in placeholder.parent.iterdir()):
        fail("redundant .gitkeep in populated folder: " + str(placeholder.relative_to(ROOT)))

if errors:
    for message in errors:
        print("ERROR:", message, file=sys.stderr)
    print(f"FAILED: {len(errors)} problems.", file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(rows)} print-file records, all registered paths, IDs and content hashes match.")
