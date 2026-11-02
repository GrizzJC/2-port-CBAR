# 3D Design Revisions and Manufacturing Records

## Purpose

Preserve an exact, reproducible link between an editable design, its released manufacturing files and the physical parts produced from it.

## Three histories to track

| History | Records | Stored where |
| --- | --- | --- |
| Design development | Sketches, features, linked components and editable source-system saves | Native CAD project/tool |
| Controlled revision | What changed, why, author, affected interfaces, tests, approval and source snapshot | Component or assembly record and asset tracker |
| Manufacturing/test | Material, machine, slicer, orientation, settings, print outcome and fit testing | Print project or test record |

A new print attempt does not necessarily require a design revision.

## CAD source history

- **Autodesk Fusion:** An exported `.f3d` may retain the feature timeline when design history is enabled. It does **not** contain the complete saved cloud-version history of the original project.
- **SolidWorks:** `.sldprt` is a part file and `.sldasm` defines an assembly. External references between files may depend on names and saved paths.
- **STEP:** Useful for interoperable engineering geometry, but does not always preserve the source application's complete feature history.
- **STL:** Exported triangular mesh geometry, not an editable parametric design history.
- **3MF:** May be a prepared manufacturing job, including multiple parts and slicer settings.

For every approved release, document the authoritative editable design, its exact CAD revision or source reference and the GitHub commit/tag identifying its associated release files.

## Revision summary fields

| Field | What to record |
| --- | --- |
| Revision | Stable revision label (e.g. R01) |
| Date | Revision date |
| Change | Geometry, fit or interface change |
| Reason | Problem resolved or requirement addressed |
| Source revision | CAD project version, save or released archive |
| Git reference | Commit SHA or immutable release reference |
| Testing | Dimensional/fit/mechanical results |
| Author / reviewer | Responsible individuals |

Revisions are recorded in documentation rather than appended to the permanent design filename.

## Separate manufacturing changes

Examples that generally change a **design revision**: mounting hole relocation, new dimensions, geometry affecting fit or an updated mating interface.

Examples that generally belong in a **print record**: reprint, failed attempt, filament color, printer selection or slicer adjustments that do not change the controlled part geometry.

When a manufacturing process itself is validated and controlled, it may need its own revision history even if the part geometry is unchanged.

## Before releasing a file

1. Verify the correct CAD master and source revision.
2. Check linked files, names/paths and referenced component IDs.
3. Record the design change and its reason.
4. Generate the manufacturing exports and confirm intended units and geometry.
5. Record a reproducible Git reference for the exact exported files.
6. Complete fit, print or functional checks appropriate to the item.
7. Update the current-release status in the asset tracker.
