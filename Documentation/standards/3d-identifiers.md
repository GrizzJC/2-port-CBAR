# 3D Asset Identification and Naming Standard

## Purpose and scope

A **permanent ID** answers *which controlled item is this?* A **description** answers *what does it do?* A **revision** answers *which design state is this?* A **file extension** answers *how is this digital information represented?*

These concepts must remain distinct so that hardware changes and file exports do not require renumbering.

## Candidate format: SS-NNN

| Segment | Meaning | Sample |
| --- | --- | --- |
| `SS` | Stable functional system group, two digits | `01` |
| `NNN` | Unique sequence within that group, three digits | `023` |
| `SS-NNN` | Permanent item identifier, six characters including hyphen | `01-023` |

The format can be incorporated into a wider identifier scheme without embedding changeable rig characteristics in the core number. This is a format, **not an allocation**. The first system numbers remain **unassigned**; reserve `00` pending a formal group table.

### Rules

1. Assign a new ID only after confirming an actual distinct controlled item and its primary stable function.
2. The two-digit system is **not** the CAD software, slicer, printing process, motor model or number of bottles.
3. Retain an ID through normal design revisions and changes of assembly use; do not recycle IDs.
4. Keep revisions (R01 etc.), dates, maker initials and words such as `final` or `new` out of the permanent ID.
5. If a design becomes a fundamentally different independent component, record its predecessor and issue a new identifier.
6. Use an **assembly** ID for multi-component relationships, not a reused ID from one included part.
7. Give a **print project** its own controlled identity when it is a managed manufacturing deliverable. A 3MF that merely exports a single component mesh may instead be a representation of that component.
8. Other file types can receive registry IDs without necessarily changing their functional filenames.

## Classification and cross-system use

Systems are described at [3D-Models/Systems](../../3D-Models/Systems/README.md). These human-readable pages are **not numeric code assignments**. If a bracket is used in two assemblies, retain one component ID and record the two assembly placements instead of renaming the bracket or creating duplicate numbers.

Because a two-digit code and three-digit sequence permit only 999 items per group, decide whether a future expansion rule is needed before reaching capacity.

## Folder, source and exported-file naming

Proposed stable asset path:

```text
3D-Models/Components/SS-NNN/
  README.md
  source/<original CAD filename, if external-reference dependent>
  exports/SS-NNN.stl
  exports/SS-NNN.step
```

The examples assume the exports genuinely describe the same component and do not collide. Where multiple variants, configurations or unit-specific outputs exist, use **additional linked controlled representations**, not ambiguous overwrites.

For SolidWorks assemblies and externally referenced designs, preserve their source filenames and manage dependencies with the CAD application. Renaming on GitHub alone does not update internal links. For MATLAB function files, names can be required by language rules: use the ID in a registry or metadata rather than breaking execution.

## Revision summaries

Record revision, date, author, summary, reason, affected interfaces, source CAD version, exact Git revision, test outcome and approval **inside an asset record**, not as part of the filename. Exported artifacts must be traceable to the exact released source state.

## Master registry

The [asset tracker](../../tracking/2-port-3d-assets.csv) holds original and proposed paths, descriptive names, identifiers, source provenance, file roles, dependencies, revision status and verification. The [file organization register](../../FILE-ORGANIZATION.md) contains the full working directory map.

## System allocation register

| Code | System | State |
| --- | --- | --- |
| `00` | Reserved | Not allocated |
| `01`–`99` | Functional groups, defined when actual parts are registered | Not allocated |

Do not treat directory positions or alphabetical order as approval of a numeric code.
