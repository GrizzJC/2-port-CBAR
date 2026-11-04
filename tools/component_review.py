#!/usr/bin/env python3
"""Generate a human-readable 3D component review from scan results; no file edits."""
from collections import Counter, defaultdict
from pathlib import Path
import os
import re
import subprocess

def mesh_hash(obj):
    return (obj or {}).get("translation_invariant_geometry_hash")

def resolve_used_meshes(part):
    objects = {str(obj.get("id")): obj for obj in part.get("objects", [])}
    results, warnings = [], []
    def walk(obj_id, build_number, visited=()):
        key = str(obj_id)
        if key in visited:
            warnings.append("Cyclic component reference: " + key)
            return
        obj = objects.get(key)
        if obj is None:
            warnings.append("Unresolved component: " + key)
            return
        if obj.get("mesh"):
            results.append({"object_id": key, "build_item": build_number, "mesh": obj["mesh"]})
        for child in obj.get("components", []):
            walk(child.get("object_id"), build_number, visited+(key,))
    for i, item in enumerate(part.get("build_items", []), 1):
        walk(item.get("object_id"), i)
    return results, warnings

def normalized_part_name(item):
    base=Path(item["filename"]).stem
    base=re.sub(r"^3DP-\d-\d{3}_", "", base, flags=re.I)
    base=re.sub(r"^PrintJob-", "", base, flags=re.I)
    return re.sub(r"[^a-z0-9]", "", base.lower())

def bbox_approx_same(a,b):
    if not a or not b or len(a)!=3 or len(b)!=3:
        return False
    return all(abs(x-y) <= max(0.1,0.01*max(abs(x),abs(y))) 
               for x,y in zip(sorted(a),sorted(b)))

def analyze_links(details):
    stls = [x for x in details if x["type"] == "STL"]
    jobs = [x for x in details if x["type"] == "3MF"]
    geom_index = defaultdict(list)
    for item in stls:
        hash_value = mesh_hash(item.get("geometry"))
        if hash_value:
            geom_index[hash_value].append(item["file_id"])
    stl_to_jobs = defaultdict(set)
    job_info = {}
    for job in jobs:
        project = job.get("project", {})
        parts = project.get("model_parts", [])
        placements, mesh_objects, used, warnings = 0, 0, [], []
        for part in parts:
            placements += len(part.get("build_items", []))
            mesh_objects += sum(bool(obj.get("mesh")) for obj in part.get("objects", []))
            items, issues = resolve_used_meshes(part)
            warnings.extend(issues)
            for obj in items:
                h = mesh_hash(obj["mesh"])
                related = sorted(set(geom_index.get(h, [])))
                used.append({"object_id": obj["object_id"], "build_item": obj["build_item"],
                             "related_stl_ids": related})
                for ident in related:
                    stl_to_jobs[ident].add(job["file_id"])
        related_ids = sorted({name for obj in used for name in obj["related_stl_ids"]})
        unmatched_count = sum(not obj["related_stl_ids"] for obj in used)
        # Name and approximate-bounds matches are only candidates, not direct mesh relationships.
        same_name = sorted(x["file_id"] for x in stls
                           if Path(x["path"]).parent == Path(job["path"]).parent
                           and normalized_part_name(x)==normalized_part_name(job))
        dims_used = [
            obj.get("mesh",{}).get("bbox_size")
            for part in parts for obj in part.get("objects", [])
            if obj.get("mesh")
        ]
        same_size = sorted(x["file_id"] for x in stls if
                           Path(x["path"]).parent == Path(job["path"]).parent
                           and x["file_id"] not in related_ids
                           and any(bbox_approx_same(x.get("geometry",{}).get("bbox_size"),dims)
                                   for dims in dims_used))
        job_info[job["file_id"]] = {
            "placements":placements,"mesh_objects":mesh_objects,"used_meshes":used,
            "matching_stl_ids":related_ids,"unmatched_meshes":unmatched_count,
            "warnings":warnings,"same_name_stl_ids":same_name,
            "same_size_stl_ids":same_size,
            "slicer_sources":project.get("settings_sources", []),
            "slicer_settings":project.get("available_slicer_settings", {})
        }
    duplicated_stls = {h: sorted(ids) for h,ids in geom_index.items() if len(ids)>1}
    return job_info, stl_to_jobs, duplicated_stls

def push_changes(previous):
    if not previous or set(previous)=={"0"}:
        return None
    cmd=["git","diff","--name-status",previous+"...HEAD","--","Rig-Engineering-Files","inventory.csv"]
    p=subprocess.run(cmd, capture_output=True, text=True,
                     cwd=Path(__file__).resolve().parents[1], check=False)
    if p.returncode:
        return None
    return [(line.split("\t")[0], line.split("\t")[-1])
            for line in p.stdout.splitlines() if "\t" in line]

def proposed_3mf_name(item, links):
    if not links["used_meshes"] or links["unmatched_meshes"] or links["warnings"]:
        return ""
    m=re.fullmatch(r"(3DP-\d-\d{3})_(.+)\.3mf",item["filename"],re.I)
    if not m or m.group(2).lower().startswith("printjob-"):
        return ""
    return m.group(1)+"_PrintJob-"+m.group(2)+".3mf"

def make_report(details, previous=None):
    jobs, stl_jobs, duplicates=analyze_links(details)
    stls=sorted((x for x in details if x["type"]=="STL"),key=lambda x:x["file_id"])
    projects=sorted((x for x in details if x["type"]=="3MF"),key=lambda x:x["file_id"])
    fully=sum(bool(v["used_meshes"]) and not v["unmatched_meshes"] and not v["warnings"] for v in jobs.values())
    partial=sum(bool(v["matching_stl_ids"]) and v["unmatched_meshes"]>0 for v in jobs.values())
    with_no_match=sum(not v["matching_stl_ids"] for v in jobs.values())
    unmatched_stls=[x for x in stls if not stl_jobs.get(x["file_id"])]
    guessed_by_name = {x["file_id"]: sorted(jid for jid,v in jobs.items()
                                            if x["file_id"] in v["same_name_stl_ids"])
                       for x in stls}
    candidate_projects=sum(bool(v["same_name_stl_ids"]) and not v["matching_stl_ids"]
                           for v in jobs.values())
    multipart=sum(len(v["matching_stl_ids"])>1 for v in jobs.values())
    errors=[x for x in details if x.get("analysis_status")=="error"]
    groups=defaultdict(list)
    for item in details:
        pieces=Path(item["path"]).parts
        groups[pieces[1] if len(pieces)>1 else "Unknown"].append(item)
    lines=[
        "# Component and Print-Job Review — Automatically Generated",
        "",
        "**Technical evidence only, not approval or proof of mechanical fit.**",
        "This report groups all registered STL/3MF files by function and compares",
        "actual STL meshes to mesh objects referenced by 3MF build items.",
        "An exact translation-normalized geometry match is strong evidence",
        "of the same triangular mesh at 0.0001 model-coordinate precision.",
        "It is NOT proof that a physical print was completed or installed.",
        "",
        "## At a glance",
        "",
        "| Check | Count |","| --- | ---: |",
        f"| STL component files | {len(stls)} |",
        f"| 3MF print projects | {len(projects)} |",
        f"| Jobs with every referenced mesh matching an STL | {fully} |",
        f"| Jobs partially matched to STL meshes | {partial} |",
        f"| Jobs without exact matching STL geometry | {with_no_match} |",
        f"| STL files without an exact built-object 3MF match | {len(unmatched_stls)} |",
        f"| No-exact-match 3MF projects with a same-name STL candidate | {candidate_projects} |",
        f"| Jobs matching multiple distinct STL IDs | {multipart} |",
        f"| Identical-geometry STL ID groups | {len(duplicates)} |",
        f"| Parsing errors | {len(errors)} |",
        "",
        "## Changes from the latest triggering push", ""
    ]
    changes=push_changes(previous)
    if changes is None:
        lines.append("Previous revision unavailable (manual run or incomplete history).")
    elif not changes:
        lines.append("No actual engineering asset or inventory change in this push.")
    else:
        for status,path in changes[:100]:
            lines.append("- "+status+" : "+path)
        if len(changes)>100:
            lines.append("- Additional paths: "+str(len(changes)-100))
    lines += ["", "## Priority review questions", "",
              "1. Inspect every 3MF with unmatched or unresolved build geometry in the original slicer.",
              "2. Confirm which STL parts belong in multipart jobs and how many copies are needed.",
              "3. Check STL models without an exact 3MF match; they may be deliberately standalone.",
              "4. Compare genuinely repeated meshes before proposing a deletion or renamed design.",
              "5. Verify physical fit, actual printing settings, successful prints and approvals manually.",
              "",
              "## Full inventory and associations", ""]
    for area,items in sorted(groups.items()):
        lines += ["### "+area.replace("-"," "), "",
                  "| File ID | Actual file | Geometry-based relationship | Human review needed |",
                  "| --- | --- | --- | --- |"]
        for item in sorted(items,key=lambda x:x["file_id"]):
            fid=item["file_id"]
            path="../"+item["path"]
            title="["+item["filename"]+"]("+path+")"
            if item["type"]=="STL":
                links=sorted(stl_jobs.get(fid,set()))
                matching="Exact mesh in "+", ".join(links) if links else "No exact 3MF job match"
                if not links and guessed_by_name.get(fid):
                    matching += "; possible same-name print job "+", ".join(guessed_by_name[fid])
                equals=sorted({other for vals in duplicates.values() if fid in vals for other in vals if other!=fid})
                need="Confirm function, design revision and physical compatibility"
                if not links and guessed_by_name.get(fid):
                    need="Compare likely STL/3MF pair; meshes differ despite matching names"
                elif not links:
                    need="Check whether an existing prepared print job is appropriate"
                if equals:
                    need+="; same geometry as "+", ".join(equals)
            else:
                info=jobs[fid]
                matching=(str(info["placements"])+" build item(s); "+
                          str(len(info["used_meshes"]))+" built mesh reference(s); "+
                          ("STL: "+", ".join(info["matching_stl_ids"])
                           if info["matching_stl_ids"] else "no exact STL match"))
                if info["unmatched_meshes"]:
                    matching+="; "+str(info["unmatched_meshes"])+" unmatched"
                if not info["matching_stl_ids"] and info["same_name_stl_ids"]:
                    matching+="; possible same-name STL: "+", ".join(info["same_name_stl_ids"])
                if not info["matching_stl_ids"] and not info["same_name_stl_ids"] and info["same_size_stl_ids"]:
                    matching+="; approximate size candidates: "+", ".join(info["same_size_stl_ids"][:4])
                if info["warnings"]:
                    need="Inspect unresolved 3MF components: "+", ".join(info["warnings"])
                elif info["unmatched_meshes"] or not info["used_meshes"]:
                    need="Inspect unmatched/absent print-project geometry"
                    if info["same_name_stl_ids"]:
                        need+="; compare same-name mesh (different geometry)"
                    elif info["same_size_stl_ids"]:
                        need+="; compare similar-size meshes"
                elif len(info["matching_stl_ids"])>1:
                    need="Confirm multi-part count, fit and slicer settings"
                else:
                    need="Confirm copies, fit and slicer settings"
                if not info["slicer_sources"]:
                    need+="; no recognized slicer config found"
            lines.append("| "+fid+" | "+title+" | "+matching.replace("|","/")+" | "+need.replace("|","/")+" |")
        lines.append("")
    lines += ["## Suggested descriptive filenames — not applied", "",
              "For a 3MF that has been matched to STL meshes, adding a PrintJob- label",
              "can clarify that it is a saved printing project, not an individual part.",
              "Do NOT approve these candidates without checking actual job contents.",
              "",
              "| ID | Current 3MF filename | Naming candidate |",
              "| --- | --- | --- |"]
    possibilities=0
    for item in projects:
        suggestion=proposed_3mf_name(item,jobs[item["file_id"]])
        if suggestion:
            lines.append("| "+item["file_id"]+" | "+item["filename"]+" | "+suggestion+" |")
            possibilities+=1
    if not possibilities:
        lines.append("| — | — | No automatic candidates meet exact-mesh criteria |")
    if duplicates:
        lines += ["", "## STL files with matching normalized mesh geometry", ""]
        for vals in sorted(duplicates.values()):
            lines.append("- "+", ".join(vals)+" (review roles and orientation; NOT automatic duplicates for deletion)")
    lines += ["", "## What will update automatically?", "",
              "- The file lists, counts, exact geometry associations and candidate-name checks",
              "  rerun whenever the workflow is triggered by relevant committed branch changes.",
              "- The change list reflects the triggering Git push when prior history is available.",
              "- **Physical printing, actual print dates, installed/working status, approvals and",
              "  functional intent cannot be inferred from geometry or Git commits.**",
              "- Mesh matching is sensitive to rotation, tessellation and scale. Some 3MF",
              "  layouts contain composite objects, modifiers or proprietary slicer extensions.",
              "- Other details remain in the downloadable full JSON/CSV workflow artifacts.",
              ""]
    return "\n".join(lines),{
        "stl":len(stls),"3mf":len(projects),"fully_matched_jobs":fully,
        "partial_jobs":partial,"jobs_no_exact_match":with_no_match,
        "stls_no_exact_job":len(unmatched_stls),
        "multipart_jobs":multipart,"same_name_candidate_jobs":candidate_projects,
        "duplicate_geometry_groups":len(duplicates),
        "parser_errors":len(errors)
    }
