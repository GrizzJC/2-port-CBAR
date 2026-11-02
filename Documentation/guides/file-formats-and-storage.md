# 3D File Formats, Storage and GitHub Previews

## File roles

| Format | Typical role | Native interactive GitHub preview? |
| --- | --- | --- |
| `.stl` | Triangular mesh for additive manufacturing | **Yes**, within GitHub's preview limits |
| `.3mf` | Manufacturing project / mesh and optional slicer data | No |
| `.step` / `.stp` | CAD geometry exchange | No |
| `.sldprt` / `.sldasm` | SolidWorks part / assembly | No |
| `.f3d` / `.f3z` | Autodesk Fusion design/archive | No |
| `.png` / `.svg` | Static schematic or component image | Yes, as image |
| `.md` | Descriptions, labels and revision records | Yes, rendered text |

## Why the GitHub STL viewer is not a source of truth

GitHub has a native interactive STL viewer, with a **10 MB STL preview limit**. A file exceeding that threshold may still be stored or downloaded, but it may not display in that built-in viewer.

**Do not simplify a manufacturing mesh merely to make it previewable.** A preview is for inspection and navigation, not a substitute for dimensional checks or validated print files.

GitHub can show STL changes in its non-code-file comparison interface, but visual differences do not explain *why* a revision changed. Keep the explanation in the revision history.

See GitHub's documentation: https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files

## Why not save every CAD autosave into Git?

Git excels at text changes. CAD and many print files are binary, so changes may produce large replacement file objects rather than readable line-by-line diffs. Extensive history of large binaries can inflate repository storage and complicate cloning.

Keep the **editable authoritative design** in the system used to author it and identify which snapshots were intentionally released. Store the exact exports needed to reproduce a validated build.

For very large binaries, evaluate Git Large File Storage (Git LFS) costs and access requirements rather than treating it as the default.

GitHub file and repository limits: https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits

## Model relationships and linked CAD references

An assembly may depend on external component files. Renaming or relocating parts directly in GitHub does **not** repair those links. Use source-software reference management and verify assembly resolution before changing tracked paths.

When an exported STL, STEP or 3MF corresponds to a native design, connect them using a **common asset identifier** in the tracker and in their individual records.

## Optional visual documentation

A component record can include a separate schematic or labeled image. If interactive browser visualization is later needed, a Three.js application can read optimized model representations, but its visualization should remain distinct from authoritative design and manufacturing data.
