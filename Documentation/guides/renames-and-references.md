# File Renames, CAD Links and Dependency Checks

## What GitHub does when a name changes

Git records files by content and path at each commit. Git can **detect a probable rename** by comparing contents, but file paths still change and GitHub does not repair internal references in other programs. GitHub revision history is therefore useful for traceability but does **not** make a rename automatically safe.

## Dependency matrix

| File / project | What may depend on its name or location? | Before a change |
| --- | --- | --- |
| SolidWorks `.sldprt` | `.sldasm` assembly components, derived parts, drawings and in-context references | Identify dependent projects; use SolidWorks reference-management tools; reopen the whole assembly; regenerate/check mates |
| SolidWorks `.sldasm` | Drawings, upper-level assemblies, exported projects and external build references | Verify all nested links and regenerate after moving |
| Fusion `.f3d` / linked design | Project links, assembly references and cloud-managed relationships | Review original cloud link graph; test opening all linked designs |
| STEP / STL / OBJ | Usually self-contained geometry, but may be used by slicer projects, scripts or linked documentation | Search downstream filenames and paths; verify scale/units and geometry after replacement |
| 3MF | Slicer jobs, plate/object references, stored machine setup and linked model sources | Inspect internal objects/projects and re-open in slicer after changes |
| MATLAB `.m` | Function name must match primary function filename; caller paths, `addpath`, `load` and `which` may depend on names | Search code and tests for references; retain required function filename |
| Arduino, Python, configuration | Imports/includes, build scripts, compiled entry points and external automation | Search include/import/file-path strings and run test/build |
| Markdown / images | Relative links to other repository pages and files | Verify every link and GitHub rendering |

## Rename-safety process

1. Identify the item, original path, repository source and any revision/commit that must remain retrievable.
2. Mark **Filename/Path Dependency?** as **Yes, No, Unknown or Review** in the tracker. Unknown is not safe.
3. List dependent assemblies, scripts, slicer projects, drawings, documentation and external consumers.
4. Decide if a rename is necessary. **Prefer preserving native source names** and assigning the stable ID in its parent directory and register.
5. If necessary, update dependencies through authoring software, not only GitHub's rename interface.
6. Export or open the changed design, validate geometry/mates/function and record Pass, Fail or Not applicable.
7. Update README links, asset registry, cross-references and release references in the same controlled change.

## Common pitfalls

- A CAD assembly that opens on the creator's machine may be resolving missing references from **local cached paths**, not from a portable package. Test on another machine or in a clean copied project.
- CAD projects may contain **external designs** that are not embedded inside a single part file.
- A file can be renamed without altering its geometry, but a slicer or automated script may still fail because its **path** no longer exists.
- Never let an automatically generated filename become a permanent identity without checking if it describes one part, multiple parts or only a temporary export.

Track results in [the asset registry](../../tracking/2-port-3d-assets.csv).
