# 3D Asset Identifiers and Filenames

## Purpose

Give each controlled design a **stable identity** while allowing its descriptive name, export format and manufacturing process to change. Stable identifiers help preserve links across technical drawings, component references, inspection records and source-control history.

## Identifier structure

`SS-NNN`

| Segment | Description | Example |
| --- | --- | --- |
| `SS` | Two-digit functional system/group code | `01` |
| `NNN` | Three-digit item sequence within that group | `023` |
| `SS-NNN` | Six-character permanent identifier | `01-023` |

These examples are illustrative. **System codes have not yet been allocated.** `00` is reserved until the group table is established. Do not assign IDs until the actual parts and their roles are known.

The group code identifies a stable function or system, **not** the CAD application, printer, current experimental bottle count or file format.

## Identity rules

- An individual physical part design can have multiple representations, such as native CAD source, STEP and STL, associated with one component identifier.
- An assembly has its own identity because it represents relationships between multiple parts.
- A multi-part print project is a manufacturing asset and should link to its included parts rather than use one part's identifier as if it were the entire build plate.
- A fundamentally different replacement design or independently usable part may require a new identifier; a controlled change to the existing part generally changes its revision instead.
- Retired identifiers are not reused.

## Filenames and dependencies

The ID may be used in filenames of standalone exported assets, for example `01-023.stl` and `01-023.step`, **only when their meaning and relationship have been verified**.

Do not assume every source filename can be replaced with an ID. Native SolidWorks parts and assemblies, linked Fusion designs and code files may depend on a specific name/path. File renames in GitHub do not automatically modify these internal references.

Before changing a filename or folder path, complete the asset tracker's **Filename/Path Dependency?**, **Dependency Mechanism**, **Required Check Before Rename** and **Rename Verification** fields.

For stable code entry points, preserve names required by their programming environment. The permanent asset identifier can remain a registry value instead of becoming the actual script filename.

## Revision naming

Keep revision numbers and status out of the permanent identifier. Use the asset record to track revisions, source version IDs, published commits and the current verified release.

## Subsystem allocation table

| Code | Functional system | Status |
| --- | --- | --- |
| `00` | Reserved | Unassigned |
| `01`–`99` | Defined as actual systems are inventoried | Unassigned |

An identifier supports up to 999 values per group. If this limit might be exceeded, define an extension plan before assigning the final available number.
