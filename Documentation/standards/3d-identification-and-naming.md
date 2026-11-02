# Proposed standard: 3D asset identity and naming

**Document status:** WORKING DRAFT — pending Tim/Chad approval  
**Scope:** 3D components, assemblies and print-project relationships in the 2-port chemosensory brief-access rig.

## Why stable identifiers?

Git records the *path* and content state in a commit. Git can infer a rename from content similarity, but a rename changes URLs and can break external references, engineering assemblies, scripts and documentation. Treat names and paths as controlled interfaces.

## Candidate permanent ID

`NN-NNN` (for example `01-001`).

- Two-digit stable **functional subsystem code** `NN`, not the CAD application used to design the part.
- Three-digit permanent **item sequence** `NNN` within that subsystem.
- `00` remains reserved pending approval; `01` etc. are **not yet assigned**.
- Six characters including the hyphen. The identifier can fit inside a wider document-control system with prefixes without changing the laboratory ID.
- No 2-port configuration, bottle count, current machine, part description, dates or revision number embedded in this code.
- For systems that exceed 999 items, agree on an extension and transition rule **before** exhausting the allocation.

## Crucial identity decisions

**Proposed:** one component identity for one physical design, across its `.stl`, `.step` and authoring-file representations when those files are genuinely versions/formats of the *same controlled design*. Do **not** automatically reuse the same ID for an assembly or a multi-component 3MF print plate.

All files sharing an ID must have a verifiable relationship documented in the registry and component record.

## Filename and path policy

Suggested *only for independent export files after verification*: `NN-NNN.stl`, `NN-NNN.step`; no revision suffix. Human-readable labels live inside `README.md`, the asset register and component documentation.

**Do not blindly rename** `.sldprt`, `.sldasm`, linked Fusion designs or files called by scripts. CAD assembly paths/names and programmatic references may be functionally significant. Mark risk in **Filename/Path Dependency?** and list every check before renaming.

When a controlled item changes its purpose so significantly that it is a new independent part, request a **new ID** rather than reusing an unrelated old number.

## Registry fields

`Proposed Asset ID`, `Current File Name`, `File Format`, `Asset Kind`, `Functional Assembly`, `Component / Purpose`, `Current Source Location`, `Proposed GitHub Path`, `Related Design / Parent Assembly`, `Filename/Path Dependency?`, `Dependency Mechanism`, `Required Check Before Rename`, `Rename Verification`, `Design Revision`, `Release Status`, `Reviewer`, `Notes`.

Registry: [tracking/2-port-3d-assets.csv](../../tracking/2-port-3d-assets.csv).

## Preliminary subsystem groupings, not codes

Animal chamber, stimulus delivery, moving/positioning mechanisms, fluid and valve systems, and mounting/structural supports are candidate *functional groupings*. Assign codes only once actual new 2-port designs are inventoried. Avoid inferring an item belongs to the 2-port design just because the 3-port rig had a similarly named part.

## Revision summary

| Date | Proposed revision | Change | Decision |
| --- | --- | --- | --- |
| 2026-11-02 | Draft 0.1 | Introduced stable identifiers and rename-risk checks. | Pending Tim/Chad |
