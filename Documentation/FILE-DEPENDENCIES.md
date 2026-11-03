# File Dependencies and Safe Renaming

Moving a GitHub file does **not** update references in external software. Review dependent files before changing names or paths.

| File or environment | Possible dependency | Necessary verification |
| --- | --- | --- |
| SolidWorks part or assembly | Assembly mates, drawings and linked components | Use CAD-native reference tools; reopen dependent assemblies |
| Fusion linked design | Inserted designs, cloud references and feature history | Review and test linked projects |
| STL, STEP and 3MF | Slicer imports, project dependencies and object references | Reopen print project; verify scale, objects and orientation |
| MATLAB (`.m`) | Function filename, callers, paths and loaded resources | Preserve required names; check callers and run tests |
| Arduino / C / C++ | Includes, imports, build configuration and library paths | Build and run relevant tests |
| Markdown and visuals | Relative links | Verify the rendered link resolves |

## Before changing a path

1. Locate the original and current paths in the [inventory](../inventory.csv).
2. Identify whether another file or device refers to that name/path.
3. Preserve source filenames when their dependencies cannot be safely changed.
4. When a change is necessary, use the authoring software to update native references.
5. Verify the result, then update the inventory and any affected links.

For IDs, manufacturing process, print jobs, file splitting/merging and status, use the [single naming standard](NAMING-AND-FILE-RULES.md).
