# 3D Asset Tracking

[Open the asset index](2-port-3d-assets.csv) to record 3D model files and their relationships. The CSV is intentionally empty until actual 2-port files have been identified.

**One row represents a registered file or controlled file representation.** Related rows can share an asset ID when they describe the same verified component design; assemblies and multi-part print jobs should have their own identities.

## Filename and path safety

The following tracker columns are required when a file is considered for renaming or relocation:

| Column | Purpose |
| --- | --- |
| `Filename/Path Dependency?` | Yes, No, Unknown or Review |
| `Dependency Mechanism` | SolidWorks part/assembly link, Fusion external design, file loaded by software, linked print job or other reference |
| `Required Check Before Rename` | Specific assembly, project or script that must be retested |
| `Rename Verification` | Not checked, Pass, Fail or Not applicable |

Do not classify a file as safe to rename merely because it is stored in GitHub. Check the source engineering application when necessary.

## Revision tracking

Each row should point to the design record with the latest revision and release evidence. For physical manufacture, record the correct print project separately.

The tracker can be opened in Excel, but if an additional workbook is used, update this index from the authoritative data and reconcile rows before publishing releases.
