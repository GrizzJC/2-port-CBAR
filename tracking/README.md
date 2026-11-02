# 3D Asset Tracking and File Organization

This directory contains complementary machine-readable CSV files. The `[FILE-ORGANIZATION.md](../FILE-ORGANIZATION.md)` page is the human-readable navigator; `[repository-file-index.csv](repository-file-index.csv)` is the **one-row-per-file** inventory of repository paths.

## Registers

| Register | Unit of record | Purpose |
| --- | --- | --- |
| [repository-file-index.csv](repository-file-index.csv) | One tracked GitHub file | Complete current path/file catalog, category and role |
| [2-port-3d-assets.csv](2-port-3d-assets.csv) | One candidate or registered 3D file representation | Permanent item ID, formats, authoritative source and dependency risk |
| [intake-queue.csv](intake-queue.csv) | One external 3D-file candidate | Source discovery, owner/provenance, format and classification queue |
| [3d-placement-plan.csv](3d-placement-plan.csv) | One functional system | Physical 3D-placement rules and associated work batch |
| [assembly-membership.csv](assembly-membership.csv) | One assembly/component relationship | Quantities, parts, revision compatibility and interfaces |
| [print-projects.csv](print-projects.csv) | One print plate / component relation | 3MF projects, printer settings and test records |
| [reference-geometry.csv](reference-geometry.csv) | One third-party reference file | Source, model number, license and linked assets |
| [build-configurations.csv](build-configurations.csv) | One build/component relationship | Actual rig installation, revision and fit status |
| [revision-ledger.csv](revision-ledger.csv) | One documented design revision | Change summary, CAD source, Git commit and validation |
| [batch-status.csv](batch-status.csv) | One work batch | Workload, evidence and blockers |

The [batch workflow](work-batches.md) explains the sequence of review and workload planning.

## Rename-risk controls

The asset tracker has **Filename or Path Dependency?**, **Dependency Mechanism**, **Required Check Before Rename** and **Rename Verification** columns. `Unknown` is never treated as `No`. A SolidWorks part may be referred to inside an assembly and an Arduino/MATLAB script may rely on specific filenames. GitHub renames do not update external references.

## Distinct status dimensions

`Source file located` ≠ `Design identity verified` ≠ `Manufacturing verified` ≠ `Printed` ≠ `Fit tested` ≠ `Installed` ≠ `Released`. Preserve each stage independently.

## Keeping the file list accurate

`repository-file-index.csv` is a **snapshot** of GitHub's actual file tree as of the index date, not an automatically self-updating spreadsheet. Refresh after adding/moving/removing files and ensure each path resolves on `main`. A new repository Markdown page is a file record, not a new 3D component.
