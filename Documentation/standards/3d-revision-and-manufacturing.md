# Proposed standard: 3D design, release and print histories

**Status:** WORKING DRAFT — pending lab approval.

## Keep three histories distinct

1. **Design history:** modeling operations and cloud/project versions inside the original CAD system.
2. **Controlled revision history:** what changed, why, author, date, affected interfaces, tests, approval and the *exact* released files.
3. **Manufacturing history:** print job, process, machine, material, slicer/settings and acceptance/test result. Reprinting is not necessarily a new design revision.

## Authoritative source and recoverability

- Identify the original editable model: SolidWorks `.sldprt/.sldasm`, Autodesk Fusion `.f3d/.f3z`, or other source.
- A local `.f3d` archive may retain a design's feature timeline if captured with history enabled; **it does not by itself transfer the entire Fusion cloud saved-version history**.
- SolidWorks assemblies may reference filenames/paths of part files. Renaming in GitHub does not repair those references. Use CAD-native reference management and verify assemblies before publishing.
- For each approved revision, save an exact source reference (cloud revision identifier where relevant), Git commit/tag or release reference, exported mesh/STEP hash and verification outcome.
- **An STL is not a substitute for an original editable design.** Saving a new STL over the old one does not preserve a CAD feature timeline.

## Example revision record (illustrative; no real asset assigned)

| Revision | Date | Change / reason | CAD source revision | Git commit | Validation | Approved by |
| --- | --- | --- | --- | --- | --- | --- |
| R00 | — | Initial prototype | — | — | Not tested | Pending |

Do not add revision to the permanent filename. The table belongs in the component/assembly README and the master registry records the latest approved revision.

## When to make a new revision?

**Usually yes:** geometrical dimensional change, changed mounting hole position, changed fit or interface, altered mechanical function.

**Usually no:** different filament color, reprint of the same source, failed printing attempt, or temporary slicer tweak. Such events belong in the **print/test record**, though a formally controlled manufacturing process may itself require its own revision.

## Release checks

1. Identify authoritative editable source and licensing/ownership.
2. Record related component/assembly IDs and external dependencies.
3. Verify CAD-native assembly links and any path-dependent scripts.
4. Export and inspect appropriate STL, STEP or 3MF files without degrading manufacturing accuracy for a preview size threshold.
5. Record exact revision/commit/hash, print parameters where applicable and test result.
6. Mark prototype, validated or released; obtain relevant lab review before labeling approved.

## Revision summary

| Date | Revision | Change | Approval |
| --- | --- | --- | --- |
| 2026-11-02 | Draft 0.1 | Introduced separate CAD, revision and print histories. | Pending |
