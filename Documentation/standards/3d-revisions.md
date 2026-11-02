# 3D Design Revision and Manufacturing Traceability

A revision history explains **what changed, why, who made the decision and what exact design/print was tested**. It should be available for every controlled 3D asset without forcing revision suffixes into the permanent filename.

## Three different histories

| History | What it answers | Primary record |
| --- | --- | --- |
| **CAD development** | How geometry and assembly relationships were edited; recoverable source states | Original SolidWorks/Fusion project and saved versions |
| **Controlled item revision** | What officially changed between documented versions; interface compatibility and approval | Component/assembly README and revision register |
| **Manufacturing / testing** | How a particular physical part was fabricated; which result worked | Print project, test record and installed build register |

**Do not confuse Git's file commit history with Fusion's cloud saved-version history.** A downloaded `.f3d` may contain the feature timeline when history was enabled, but it does not give a new user the complete version list from the original Fusion cloud project.

## Identifiable release evidence

Record, at minimum: controlled ID, revision, effective date, author, source-system project and revision, format-specific exports, linked assembly revision, Git commit SHA, manufacturing file integrity where necessary, verification results, reviewer/approver and any known incompatibilities.

Exact release identifiers (tags, commit SHAs or saved references) matter because a GitHub URL pointing to `main` always shows the latest file, not necessarily the one used in a prior validated build.

## When to revise?

Geometry, mounting-point locations, clearances, physical interfaces and material requirements affecting the controlled design generally require a new design revision. Cosmetic file exports, reprints, color changes and ordinary slicer trials generally do not, although a **validated manufacturing process** can have its own controlled revision.

Where a change is experimental, label it development/prototype. Do not mark it released until suitability has been checked and recorded.

## Revision summary template

| Revision | Date | Specific changes | Reason | Source CAD save/version | Git reference | Compatibility / test outcome | Reviewer |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

## Special considerations

- **SolidWorks:** Assembly links and external part references may be stored using names/paths. Rename or relocate linked files with appropriate CAD-native tools and then reopen/verify assemblies.
- **Fusion:** Design timeline and cloud versions are distinct. Linked designs and multi-file exports require explicit source mapping.
- **STEP:** Exchange geometry may lose original feature-tree/edit history. Retain the original CAD master.
- **STL:** A mesh is normally not an editable parametric source. GitHub mesh visual diffs can help reveal geometry changes but cannot document why.
- **3MF:** A slicer project may contain several designs and print instructions. A change to plate composition does not automatically change a component's geometry revision.

## Print and equipment outcomes

A physical print record should identify printer, method (filament/resin/etc.), slicer version, material, settings, part revision, print/run date and measured fit or failure. Record **installed, in stock and fabricated** status separately. Source-file existence never proves the part is manufactured.

References: [intake-to-release procedure](../procedures/3d-intake-and-release.md), [print tracker](../../tracking/print-projects.csv), [build configurations](../../tracking/build-configurations.csv).
