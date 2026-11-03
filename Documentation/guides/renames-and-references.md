# Filename and reference safety

Renaming or moving a file in GitHub does not automatically repair external references. Preserve necessary native filenames when they are required for code execution, linked CAD assemblies or slicer projects.

| File / system | Risk | Verification before renaming |
| --- | --- | --- |
| SolidWorks part/assembly | Broken component, assembly and drawing links | Use reference-aware CAD tools and reopen assemblies |
| Autodesk Fusion | Linked project and cloud design references | Check and reopen dependent designs |
| STL / STEP / 3MF | Slicer imports and model dependencies | Reopen jobs and verify contents/orientation |
| MATLAB `.m` | Function name, `addpath`, callers and loaded resources | Search names and callers, run the software checks |
| Arduino and related C/C++ | Imports, includes and build paths | Build and test with dependencies |
| Markdown / diagrams | Broken relative links | Check navigation and image rendering |

Before moving: locate the [original path](../../inventory.csv), identify dependencies, update relevant source software, validate the result and update inventory paths/status. Unknown dependencies mean **not yet safe to rename**. Use links to a single maintained copy for cross-system discovery.
