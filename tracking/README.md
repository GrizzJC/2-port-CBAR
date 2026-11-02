# 3D asset tracking

The repository's simple, editable index is [2-port-3d-assets.csv](2-port-3d-assets.csv). Open it in Excel or Google Sheets.

**No verified new 2-port model files exist in this repository as of the initial setup.** The CSV intentionally contains headers only; blank or hypothetical component IDs must not be presented as approved.

Important columns:
- **Filename/Path Dependency?**: Yes / No / Unknown / Review. Record whether moving/renaming could break SolidWorks references, Fusion links, scripts, slicer projects, GitHub links or downstream documents.
- **Dependency Mechanism** and **Required Check Before Rename**: Why the risk exists and what to test.
- **Rename Verification**: Not started / Pass / Fail / Not applicable.
- **Related Design / Parent Assembly**: Which other files or component IDs must stay linked.
- **Design Revision** and **Release Status**: Revision values are metadata; not suffixes in permanent filenames.

A more extensive Excel planning workbook may be maintained separately. If its fields are edited, ensure the published CSV and workbook are reconciled by asset ID before release. Do not claim that both files are automatically synchronized.

**Historical reference:** the separate old 3-port repository is not the new active 2-port inventory. See [reference policy](../Documentation/legacy-3-port-reference.md).
