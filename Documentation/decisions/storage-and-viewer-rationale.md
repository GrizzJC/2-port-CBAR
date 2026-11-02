# Decision rationale: storage, GitHub previews and future 3D visualization

**Status:** DESIGN PROPOSAL ONLY. No viewer, schematics or manufacturing files have been created.

## Roles of each system

| System | Recommended responsibility | Reason |
| --- | --- | --- |
| CAD authoring tool (SolidWorks / Autodesk Fusion) | Primary editable model, assembly links, CAD history | Preserves engineering relationships and design features. |
| GitHub | Reviewed releases, Markdown explanations, inventory CSV, code and exact committed snapshots | Team-visible audit trail, stable published references, browseable documentation. |
| University-approved shared drive | General office documents and files not suited to Git, subject to lab policy | Easier collaborative editing and managed institutional ownership. |

**One authoritative editable source per component.** Any GitHub copies of native CAD files should be clearly identified as release snapshots rather than silently becoming a parallel editable master.

## GitHub STL viewer size

GitHub's native interactive STL display has an approximately **10 MB preview threshold** documented for its 3D viewer. This is *not the same as* the repository's file-storage limit. Do not lower manufacturing mesh fidelity to make previews work.

For models too large or unsuitable for native preview, use a separate simple PNG/SVG schematic later (after approval), a lightweight viewer-optimized `.glb` if useful, or link to the authoritative source.

GitHub native previews `.stl`; GitHub does not natively offer equivalent interactive previews for `.3mf`, `.f3d`, `.sldprt` and `.step`. It can store them when within GitHub's limits. The technical accuracy of a printable file is more important than its web thumbnail.

## Binary-file Git limitations

Binary CAD/printing files often do not diff like text-based code. A new binary revision can add a substantial object to the repository history. Git Large File Storage (LFS) may help with file size but adds storage/bandwidth and setup considerations; do not enable it blindly.

Use GitHub for meaningful reviewed snapshots, not every automatic CAD save or slicer temporary file. Keep CAD project history in the authoring platform.

## Future optional visual layer

**Phase 1 (now):** stable IDs, asset registry, Markdown records, validation and source links.

**Phase 2 (later approval):** annotated static schematics in component README, identifying connection points, mating asset IDs, orientation, critical features and revision changes.

**Phase 3 (optional):** Three.js web viewer with orbit controls, selectable parts and stable anchored labels; later assembly selection / exploded views. GitHub Pages could host the viewer, but it is a separate web page, **not** a feature inside GitHub's ordinary STL file display.

The viewer is a convenience representation; not authoritative for dimensional verification or manufacturing.

## Links for source verification

- GitHub documentation, non-code files and STL preview: https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files
- GitHub limits: https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits
- Git LFS billing/storage: https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-git-large-file-storage
- Fusion documentation: https://help.autodesk.com/view/fusion360/ENU/
- SolidWorks help: https://help.solidworks.com/
- Three.js examples/manual: https://threejs.org/manual/
