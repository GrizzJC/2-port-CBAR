#!/usr/bin/env python3
"""Inspect 3D manufacturing files and produce a reproducible, read-only audit.

Python standard library only. Does not approve, rename or alter source assets.
Run: python tools/inspect_3d.py --out .generated/3d-audit
Run: python tools/inspect_3d.py --out .generated/3d-audit --compare 3DP-1-201 3DP-1-203
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import itertools
import json
import math
from pathlib import Path
import re
import struct
import sys
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "inventory.csv"
PRINT_ROOT = ROOT / "Rig-Engineering-Files"
PREFIX = re.compile(r"^(3DP-[1-7]-[1-9]\d\d)_")
FINGERPRINT_PRECISION = 4  # Relative coordinates rounded to 0.0001 model units.
GEOMETRY_LIMIT = 180000
CONFIG_KEYS = {
    "layer_height", "first_layer_height", "nozzle_diameter", "printer_model",
    "printer_settings_id", "print_settings_id", "filament_settings_id",
    "filament_type", "filament_colour", "filament_vendor", "fill_density",
    "perimeters", "support_material", "support_material_auto", "brim_width",
    "bed_temperature", "temperature", "first_layer_temperature",
    "first_layer_bed_temperature", "filament_diameter", "filament_density",
    "first_layer_speed", "infill_speed", "external_perimeter_speed",
    "skirts", "raft_layers", "support_material_contact_distance"
}

def rounded(x, places=5):
    return round(float(x), places)

def digest_triangles(faces, minimum):
    # Sorting face vertex coordinates makes this invariant to triangle and
    # vertex ordering, winding direction, and whole-model translation.
    # It is NOT invariant to rotation or small geometric modifications.
    pieces = []
    for tri in faces:
        pts = sorted(tuple(round(p[k] - minimum[k], FINGERPRINT_PRECISION) for k in range(3)) for p in tri)
        pieces.append(repr(tuple(pts)).encode("ascii"))
    digest = hashlib.sha256()
    for piece in sorted(pieces):
        digest.update(piece)
        digest.update(b"\n")
    return digest.hexdigest()

def mesh_stats(faces):
    if not faces:
        return {"triangle_count": 0, "warning": "No mesh triangles"}
    low, high = [math.inf] * 3, [-math.inf] * 3
    area, signed_vol = 0.0, 0.0
    vertices, parent, edges = {}, [], Counter()

    def index(point):
        key = tuple(round(float(v), 5) for v in point)
        if key not in vertices:
            vertices[key] = len(parent)
            parent.append(len(parent))
        return vertices[key]

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(a, b):
        ra, rb = root(a), root(b)
        if ra != rb:
            parent[rb] = ra

    for tri in faces:
        a, b, c = tri
        for p in tri:
            for k in range(3):
                low[k] = min(low[k], p[k])
                high[k] = max(high[k], p[k])
        v = [index(p) for p in tri]
        union(v[0], v[1])
        union(v[1], v[2])
        for i, j in ((0, 1), (1, 2), (2, 0)):
            edges[tuple(sorted((v[i], v[j])))] += 1
        ab = tuple(b[k] - a[k] for k in range(3))
        ac = tuple(c[k] - a[k] for k in range(3))
        cross = (
            ab[1]*ac[2]-ab[2]*ac[1],
            ab[2]*ac[0]-ab[0]*ac[2],
            ab[0]*ac[1]-ab[1]*ac[0]
        )
        area += math.sqrt(sum(x*x for x in cross)) / 2
        signed_vol += (a[0]*(b[1]*c[2]-b[2]*c[1])
                       -a[1]*(b[0]*c[2]-b[2]*c[0])
                       +a[2]*(b[0]*c[1]-b[1]*c[0])) / 6

    boundary = sum(v == 1 for v in edges.values())
    nonmanifold = sum(v > 2 for v in edges.values())
    components = len({root(i) for i in range(len(parent))})
    euler = len(vertices) - len(edges) + len(faces)
    closed = boundary == 0 and nonmanifold == 0
    genus = (2 * components - euler) / 2 if closed else None
    return {
        "triangle_count": len(faces),
        "vertex_count_welded": len(vertices),
        "component_count": components,
        "bbox_min": [rounded(v) for v in low],
        "bbox_max": [rounded(v) for v in high],
        "bbox_size": [rounded(high[k]-low[k]) for k in range(3)],
        "surface_area_model_units_squared": rounded(area, 3),
        "signed_volume_model_units_cubed": rounded(signed_vol, 3),
        "boundary_edges": boundary,
        "nonmanifold_edges": nonmanifold,
        "watertight_edge_test": closed,
        "euler_characteristic": euler,
        "through_tunnel_genus_estimate": int(genus) if genus is not None and genus >= 0 and float(genus).is_integer() else None,
        "translation_invariant_geometry_hash": digest_triangles(faces, low),
        "fingerprint_precision": FINGERPRINT_PRECISION,
    }

def read_stl(path):
    data = path.read_bytes()
    if len(data) >= 84:
        n = struct.unpack_from("<I", data, 80)[0]
        if len(data) == 84 + n*50:
            faces = []
            for i in range(n):
                off = 84+i*50+12
                points = struct.unpack_from("<9f", data, off)
                faces.append((points[0:3], points[3:6], points[6:9]))
            return faces
    # ASCII STL fallback, with explicit rejection of incomplete triangles.
    text = data.decode("utf-8", errors="replace")
    nums = re.findall(r"^\s*vertex\s+([-+\d.eE]+)\s+([-+\d.eE]+)\s+([-+\d.eE]+)\s*$", text, re.M)
    if not nums or len(nums) % 3:
        raise ValueError("Cannot parse as binary or ASCII STL")
    points = [tuple(map(float, v)) for v in nums]
    return [tuple(points[i:i+3]) for i in range(0, len(points), 3)]

def model_meshes(content):
    root = ET.fromstring(content)
    unit = root.attrib.get("unit", "millimeter")
    metadata = [{"name": x.attrib.get("name", ""), "value": (x.text or "")[:120]}
                for x in root.iter() if x.tag.endswith("}metadata") or x.tag == "metadata"]
    objects = []
    for element in root.iter():
        if element.tag.split("}")[-1] != "object":
            continue
        mesh = next((x for x in element if x.tag.split("}")[-1] == "mesh"), None)
        meshes = []
        if mesh is not None:
            verts = []
            tris = []
            for section in mesh:
                if section.tag.split("}")[-1] == "vertices":
                    verts = [tuple(float(v.attrib[k]) for k in ("x", "y", "z")) for v in section]
                if section.tag.split("}")[-1] == "triangles":
                    tris = [(int(t.attrib["v1"]), int(t.attrib["v2"]), int(t.attrib["v3"])) for t in section]
            meshes = [(verts[a], verts[b], verts[c]) for a, b, c in tris]
        comp = []
        for node in element.iter():
            if node.tag.split("}")[-1] == "component":
                comp.append({"object_id": node.attrib.get("objectid"),
                             "transform": node.attrib.get("transform", "identity")})
        objects.append({"id": element.attrib.get("id"),
                        "name": element.attrib.get("name", ""),
                        "type": element.attrib.get("type", ""),
                        "components": comp,
                        "mesh": mesh_stats(meshes) if meshes else None})
    placements = []
    for node in root.iter():
        if node.tag.split("}")[-1] == "item":
            placements.append({"object_id": node.attrib.get("objectid"),
                               "part_number": node.attrib.get("partnumber", ""),
                               "transform": node.attrib.get("transform", "identity")})
    return {"unit": unit, "objects": objects, "build_items": placements,
            "declared_metadata": metadata[:30]}

def config_from_archive(z):
    settings = {}
    sources = []
    for member in z.namelist():
        name = member.lower()
        if not (name.endswith(".config") or name.endswith(".ini") or name.endswith("project_settings.json")):
            continue
        if z.getinfo(member).file_size > 2_000_000:
            continue
        sources.append(member)
        raw = z.read(member).decode("utf-8", errors="replace")
        if raw.lstrip().startswith("{"):
            try:
                obj = json.loads(raw)
                for k, v in obj.items():
                    if k.lower() in CONFIG_KEYS:
                        settings[k] = v if isinstance(v, (str, int, float, bool, list)) else str(v)[:120]
            except json.JSONDecodeError:
                pass
        else:
            for line in raw.splitlines():
                if "=" in line and not line.lstrip().startswith(("#", ";")):
                    k, v = line.split("=", 1)
                    if k.strip().lower() in CONFIG_KEYS:
                        settings[k.strip()] = v.strip()[:250]
    return {"settings_sources": sources, "available_slicer_settings": settings}

def read_3mf(path):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        models, others = [], []
        for member in names:
            info = z.getinfo(member)
            if info.file_size > 50_000_000:
                others.append({"file": member, "error": "skipped large member"})
                continue
            if member.lower().endswith(".model"):
                try:
                    models.append({"path": member, **model_meshes(z.read(member))})
                except Exception as e:
                    models.append({"path": member, "error": str(e)[:200]})
        config = config_from_archive(z)
        return {"model_parts": models, "archive_members": len(names),
                "other_member_names": [x for x in names if not x.lower().endswith(".model")][:35],
                **config, "analysis_notes": [
                    "Slicer settings are SAVED PROJECT METADATA, not proof of a physical print.",
                    "Build items and transforms are recorded separately from reusable mesh objects.",
                    "Extensions, implicit geometry and external references may require a specialist 3MF reader."
                ]}

def find_duplicate_meshes(details):
    fingerprints = defaultdict(list)
    for item in details:
        fid = item["file_id"]
        geom = item.get("geometry")
        if geom and geom.get("translation_invariant_geometry_hash"):
            fingerprints[geom["translation_invariant_geometry_hash"]].append(fid)
        for part in item.get("project", {}).get("model_parts", []):
            for obj in part.get("objects", []):
                geom = obj.get("mesh") or {}
                if geom.get("translation_invariant_geometry_hash"):
                    fingerprints[geom["translation_invariant_geometry_hash"]].append(
                        fid + "/object:" + str(obj["id"]))
    return [{"fingerprint": fp, "possible_matches": values}
            for fp, values in fingerprints.items() if len(values) > 1]

def changed_mesh_regions(faces_a, faces_b):
    """Bounding regions of facets that changed after removing whole-model translation.

    Mesh axes are not rotationally aligned. Boundaries are *candidate areas of
    changed triangulation*, not proven hole centers or exact hole sizes.
    """
    def normalized_facets(faces):
        low = [min(p[k] for tri in faces for p in tri) for k in range(3)]
        triples = Counter()
        for tri in faces:
            key = tuple(sorted(
                tuple(round(p[k]-low[k], FINGERPRINT_PRECISION) for k in range(3))
                for p in tri))
            triples[key] += 1
        return triples
    left, right = normalized_facets(faces_a), normalized_facets(faces_b)

    def describe(only):
        total = sum(only.values())
        if not total:
            return {"changed_triangles": 0, "region_bbox": None, "region_extent": None}
        coords = [p for triangle in only for p in triangle]
        lo = [min(p[k] for p in coords) for k in range(3)]
        hi = [max(p[k] for p in coords) for k in range(3)]
        return {"changed_triangles": total,
                "region_bbox": {"min": lo, "max": hi},
                "region_extent": [rounded(hi[k]-lo[k]) for k in range(3)]}
    old = left-right
    new = right-left
    return {
        "changed_regions_old": describe(old),
        "changed_regions_new": describe(new),
        "coordinate_frame": "each mesh translated to its own (0,0,0) bounding minimum",
        "interpretation_limit": "Candidate changed-triangle bounds only. Re-tessellation, rotation, geometry repair or a different mesh density can mark unchanged solid areas. Does not measure a hole's exact center or diameter."
    }


def compare(a, b):
    ga = a.get("geometry") or a.get("single_object_geometry")
    gb = b.get("geometry") or b.get("single_object_geometry")
    if not ga or not gb:
        return {"status": "Comparison unavailable", "reason": "No single parsed mesh in both files"}
    same = ga["translation_invariant_geometry_hash"] == gb["translation_invariant_geometry_hash"]
    dims_a, dims_b = ga["bbox_size"], gb["bbox_size"]
    res = {
        "file_a": a["file_id"], "file_b": b["file_id"],
        "result": "Same triangle geometry after translation (within rounding tolerance)" if same else "Mesh geometry differs",
        "same_normalized_triangle_mesh": same,
        "bounds_dimensions_delta": [rounded(v-u) for u, v in zip(dims_a, dims_b)],
        "bounds_min_delta": [rounded(v-u) for u, v in zip(ga["bbox_min"], gb["bbox_min"])],
        "triangle_count_delta": gb["triangle_count"]-ga["triangle_count"],
        "surface_area_delta": rounded(gb["surface_area_model_units_squared"]-ga["surface_area_model_units_squared"], 3),
        "volume_delta": rounded(gb["signed_volume_model_units_cubed"]-ga["signed_volume_model_units_cubed"], 3),
        "genus_estimates": [ga["through_tunnel_genus_estimate"], gb["through_tunnel_genus_estimate"]],
        "boundary_edge_counts": [ga["boundary_edges"], gb["boundary_edges"]],
        "limits": "A changed hash detects mesh difference even when triangle count/size/volume stay constant. It does NOT identify the specific moved hole or quantify Hausdorff distance; rotated geometries may appear different."
    }
    if ga["through_tunnel_genus_estimate"] is not None and gb["through_tunnel_genus_estimate"] is not None:
        res["topological_through_tunnel_change"] = ga["through_tunnel_genus_estimate"] != gb["through_tunnel_genus_estimate"]
    return res

def scan(root):
    with REGISTER.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    files = {p.relative_to(ROOT).as_posix(): p for p in PRINT_ROOT.rglob("*")
             if p.is_file() and p.suffix.lower() in (".stl", ".3mf")}
    details = []
    counts = Counter()
    groups = defaultdict(list)
    for row in rows:
        rel = row["Current Path"]
        path = files.get(rel)
        if path is None or not path.suffix.lower() in (".stl", ".3mf"):
            continue
        fid = row["File ID"]
        base = {"file_id": fid, "filename": path.name, "path": rel,
                "type": path.suffix[1:].upper(), "size_bytes": path.stat().st_size,
                "source_status": row.get("Verification Status", "Unverified"),
                "analysis_status": "success"}
        try:
            if path.suffix.lower() == ".stl":
                base["geometry"] = mesh_stats(read_stl(path))
                base["units"] = "NOT SPECIFIED BY STL"
            else:
                base["project"] = read_3mf(path)
                meshes = [obj["mesh"] for part in base["project"]["model_parts"]
                          for obj in part.get("objects", []) if obj.get("mesh")]
                if len(meshes) == 1:
                    base["single_object_geometry"] = meshes[0]
                base["units"] = sorted(set(part.get("unit", "unknown") for part in base["project"]["model_parts"]))
        except Exception as e:
            base["analysis_status"] = "error"
            base["analysis_error"] = str(e)[:350]
        details.append(base)
        counts[base["type"]] += 1
        match = PREFIX.match(path.name)
        if match:
            groups[match.group(1)[:-2]].append(int(match.group(1)[-2:]))
    candidates = find_duplicate_meshes(details)
    next_ids = []
    for key, nums in sorted(groups.items()):
        next_num = max(nums) + 1
        if next_num <= 99:
            next_ids.append({"group_prefix": key, "files": len(nums),
                             "next_sequential_id": key + f"{next_num:02d}",
                             "unused_numbers_below_max": [i for i in range(1, max(nums)) if i not in nums]})
    return details, counts, candidates, next_ids

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / ".generated/3d-audit")
    parser.add_argument("--compare", nargs=2, metavar=("ID_A", "ID_B"))
    args = parser.parse_args()
    details, counts, candidates, next_ids = scan(ROOT)
    output = args.out.resolve()
    output.mkdir(parents=True, exist_ok=True)
    by_id = {x["file_id"]: x for x in details}
    comparisons = []
    if args.compare:
        if any(x not in by_id for x in args.compare):
            parser.error("Unknown file ID in --compare; use the registered 3DP-* IDs")
        a, b = (by_id[x] for x in args.compare)
        result = compare(a, b)
        if a["type"] == b["type"] == "STL" and "geometry" in a and "geometry" in b:
            result.update(changed_mesh_regions(read_stl(ROOT / a["path"]), read_stl(ROOT / b["path"])))
        if a["type"] == b["type"] == "3MF" and "project" in a and "project" in b:
            def placements(x):
                return [{"model": model["path"], "build_items": model.get("build_items", [])}
                        for model in x["project"]["model_parts"]]
            result["build_placements_changed"] = placements(a) != placements(b)
            sa = a["project"].get("available_slicer_settings", {})
            sb = b["project"].get("available_slicer_settings", {})
            result["saved_slicer_settings_changed"] = {
                k: [sa.get(k), sb.get(k)] for k in sorted(set(sa)|set(sb)) if sa.get(k) != sb.get(k)
            }
        comparisons.append(result)
    errors = [x for x in details if x["analysis_status"] != "success"]
    result = {
        "scope": "read-only repository mesh audit; geometry is not physical validation",
        "counts": dict(counts), "files_processed": len(details), "files_with_errors": len(errors),
        "next_ids": next_ids, "geometry_match_candidates": candidates,
        "comparisons": comparisons, "files": details
    }
    (output / "3d-analysis.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    with (output / "3d-file-summary.csv").open("w", newline="", encoding="utf-8") as f:
        fieldnames = ["File ID","File Name","Format","Status","Triangles","Model Bounding Box","Mesh Components",
                      "Through Tunnel Genus (if manifold)","Boundary Edges","Geometry Fingerprint",
                      "3MF Build Instances","3MF Mesh Objects","Slicer Metadata Present","Analysis Error"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for x in details:
            g = x.get("geometry") or x.get("single_object_geometry") or {}
            project = x.get("project") or {}
            parts = project.get("model_parts", [])
            writer.writerow(dict(zip(fieldnames, [
                x["file_id"],x["filename"],x["type"],x["source_status"],
                g.get("triangle_count", ""),str(g.get("bbox_size", "")),
                g.get("component_count", ""),g.get("through_tunnel_genus_estimate", ""),
                g.get("boundary_edges", ""),g.get("translation_invariant_geometry_hash", ""),
                sum(len(p.get("build_items", [])) for p in parts),
                sum(len(p.get("objects", [])) for p in parts),
                bool(project.get("settings_sources")),x.get("analysis_error", "")
            ])))
    with (output / "suggested-next-ids.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["group_prefix","files","next_sequential_id","unused_numbers_below_max"])
        writer.writeheader()
        for item in next_ids:
            writer.writerow({**item,"unused_numbers_below_max":",".join(map(str,item["unused_numbers_below_max"]))})
    lines = ["# 3D File Analysis — Generated Report", "",
             "**Analysis only.** Never treat a geometric check as print approval or proof of fit.",
             "", "| Count | Value |","| --- | ---: |",
             f"| Registered STL files | {counts['STL']} |",
             f"| Registered 3MF files | {counts['3MF']} |",
             f"| Mesh/project analysis errors | {len(errors)} |",
             f"| Exact translation-normalized geometry match groups (not necessarily duplicate files) | {len(candidates)} |",
             "", "## Output files", "",
             "- `3d-analysis.json`: full object-by-object 3MF build items/transforms and saved slicer settings, plus STL topology.",
             "- `3d-file-summary.csv`: concise per-file numerical measurements.",
             "- `suggested-next-ids.csv`: numerical suggestions only; new IDs still require review.",
             "", "## Sample next IDs", "",
             "| Group prefix | Next consecutive ID |",
             "| --- | --- |"]
    for x in next_ids[:25]:
        lines.append(f"| {x['group_prefix']} | {x['next_sequential_id']} |")
    if candidates:
        lines += ["", "## Example matching geometries", "",
                  "These groups can include an STL mesh and a model embedded in a 3MF print job. They are **not** recommendations to delete files."]
        for item in candidates[:8]:
            lines.append("- " + ", ".join(item["possible_matches"][:12]))
    example = next((x for x in details if x["file_id"] == "3DP-7-202" and x.get("project")), None)
    if example:
        project = example["project"]
        parts = project.get("model_parts", [])
        objects = [o for p in parts for o in p.get("objects", [])]
        items = [o for p in parts for o in p.get("build_items", [])]
        settings = project.get("available_slicer_settings", {})
        lines += ["", "## Actual example: inside 3DP-7-202 (.3mf)", "",
                  f"- Declared model units: {', '.join(sorted(set(p.get('unit','unknown') for p in parts)))}",
                  f"- Embedded model objects: {len(objects)}",
                  f"- Print-bed build placements: {len(items)}",
                  f"- Stored slicer configuration files: {', '.join(project.get('settings_sources', [])) or 'None detected'}",
                  "- These fields are stored project information, **not evidence of an actual print**."]
        for item in items[:8]:
            lines.append(f"  - Build object ID {item.get('object_id')}, transform: {item.get('transform')}")
        for key in ["printer_model","printer_settings_id","print_settings_id","filament_type",
                    "nozzle_diameter","layer_height","fill_density","support_material"]:
            value = settings.get(key)
            if value not in (None, ""):
                lines.append(f"- Saved setting {key}: {str(value)[:100]}")
    if comparisons:
        x = comparisons[0]
        lines += ["", "## Requested mesh comparison", "",
                  f"- Files: `{x['file_a']}` and `{x['file_b']}`",
                  f"- Finding: **{x['result']}**",
                  f"- Bounding-dimension change: {x['bounds_dimensions_delta']}",
                  f"- Triangle count change: {x['triangle_count_delta']}",
                  f"- Approximate surface-area change in model units²: {x['surface_area_delta']}",
                  f"- Tunnel-genus estimates: {x['genus_estimates']}"]
        if "changed_regions_old" in x:
            lines += [
                f"- Changed-triangle candidates in first mesh: {x['changed_regions_old']}",
                f"- Changed-triangle candidates in second mesh: {x['changed_regions_new']}",
                "- Changed regions are **not** precise hole dimensions or registration results."
            ]
        if "build_placements_changed" in x:
            lines += [f"- 3MF bed placements changed: {x['build_placements_changed']}",
                      f"- Saved slicer profile fields changed: {len(x['saved_slicer_settings_changed'])}"]
    if errors:
        lines += ["", "## Parser limitations/errors", ""]
        for x in errors:
            lines.append(f"- `{x['file_id']}`: {x.get('analysis_error')}")
    lines += ["", "## What this analysis can and cannot detect", "",
              "Translation-normalized triangle fingerprints detect changed vertices/faces even when bounding dimensions,",
              "triangle count and volume remain unchanged. Moving a hole within an otherwise fixed part changes the fingerprint.",
              "A pure whole-model translation does not change that fingerprint; a rotation generally does.",
              "For watertight edge-manifold meshes, genus can suggest the number of through-tunnels.",
              "A blind hole, cavity, resized opening or repositioned cutout may change the fingerprint without changing genus.",
              "The changed-triangle region narrows attention to candidate altered facets for pairwise STL comparisons,",
              "but does not identify a precise hole center, diameter or volume. Arbitrary rotations need alignment.",
              "Volumetric/Boolean difference measurements require a geometry-aware tool and visual review.",
              "STL does not state units; 3MF model units and slicer metadata may be available.",
              "A slicer profile saved in 3MF is not evidence that this object was physically printed."]
    (output / "README.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    print("\n".join(lines[:15]))
    if errors:
        print("WARNING: Some files could not be analyzed; see report.", file=sys.stderr)

if __name__ == "__main__":
    main()
