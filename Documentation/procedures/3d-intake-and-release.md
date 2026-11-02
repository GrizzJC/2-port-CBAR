# 3D File Intake, Classification and Release Procedure

## Scope

Follow this sequence whenever a new CAD design, purchased-part model, print plate or updated model enters the rig's repository.

## 1 — Intake and provenance

Identify original file name/extension, source URL or file location, author/creator, received date, available native design and exact version. Preserve old source paths. Confirm redistribution/license permissions. Avoid importing a former three-port file solely because its name resembles a new two-port component.

Log the file or design in [intake-queue.csv](../../tracking/intake-queue.csv). Do not assign an ID simply to make filenames sequential.

## 2 — Classify the design

Determine if each file represents:
- a single component design,
- a multi-component mechanical assembly,
- a prepared print/manufacturing project,
- purchased/vendor reference geometry,
- a drawing/export or documentation supporting another controlled item.

A 3MF might contain several different objects, so inspect project content rather than relying on the extension.

## 3 — Determine functional home and identifier

Choose the primary **stable function** via the [system map](../../3D-Models/Systems/README.md). Record additional cross-system uses. Confirm any already registered part/export relation before creating a new ID. Register the controlled component, assembly or print project under its ID-stable directory.

## 4 — Inspect source/dependency risks

Record CAD authoring program, origin, source project and saved design version. Identify SolidWorks assembly references, Fusion linked designs, slicer associations, code references and documentation links. Do not rename source files before the [rename-safety checks](../guides/renames-and-references.md).

## 5 — Validate geometry and manufacturing representation

Confirm units and scale, orientation, mating points and tolerances. Inspect mesh manifold/mesh suitability when relevant; compare any exported representation against its source. Record what the part connects to, installation orientation, accessible maintenance clearances and whether it is intended to be manufactured by filament, resin, machining or another method.

## 6 — Build relationships

Record assemblies (components, quantities, roles and revision compatibility) in [assembly-membership.csv](../../tracking/assembly-membership.csv). For 3MF print plates, link all included parts and their revisions in [print-projects.csv](../../tracking/print-projects.csv).

## 7 — Record revisions and test outcomes

Update the asset record's revision summary and [revision-ledger.csv](../../tracking/revision-ledger.csv), keeping development saves distinct from controlled revisions. A print trial belongs in the manufacturing history; a fit test must identify a physical sample and exact design source.

## 8 — Release and configuration

Use source-system reference, exact Git commit/hash, verified exports, assembly links and print/test outcomes to identify what can be reproduced. Update the [build configuration](../../tracking/build-configurations.csv) if a part is installed in a particular rig. Mark source located, modeling verified, printed, fit-tested, installed and approved **separately**.

## Gate: sufficient information to progress

An asset cannot be called released based on filename or repository presence alone. Required minimum evidence includes source provenance, uniquely identified item, dependencies checked, precise revision information and appropriate validation for its intended use.
