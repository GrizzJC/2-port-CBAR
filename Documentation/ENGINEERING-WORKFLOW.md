# Engineering workflow: from proposed change to reproducible rig

**Use this guide to make or review actual changes.** It is an operating process for the repository, not an assertion that the apparatus has been validated.

## Where to work

- `main`: provisional shared engineering baseline. Avoid unreviewed component changes on `main`.
- `work/<brief-topic>`: development branch for a defined change, such as `work/spout-bracket-fit` or `work/3d-print-review`. A branch holds history within this repository; do not create separate folders or alternative naming rules for working files. Merge reviewed changes, then delete the completed branch.
- [Engineering files](../Rig-Engineering-Files/): authoritative hardware, electronics, code and manufacturing assets.
- [Rig assembly and operation guide](../Rig-Assembly-and-Operation-Guide/README.md): instructions and integrated setup diagrams, **not duplicate designs**.
- [Master working inventory](https://docs.google.com/spreadsheets/d/1gD6PC8YFJGNSHkLBSL6r_NcwHOtmynXgbYKcXxWVr7A/edit): editable file-status and print-review data. The root [inventory.csv](../inventory.csv) is a **GitHub snapshot**, not a second workbook for independently maintaining the same facts.

## 1. Propose an addition or change

Create a GitHub issue using the engineering-change template, or start a documented change with a clear rationale. Identify the target functional area and component group. For an existing part, cite its complete stable file ID. For a new independent item, allocate an unused ID from [the numbering rules](NAMING-AND-FILE-RULES.md). Record affected assemblies and dependencies.

In **Quick Review**, record the original source filename, the existing candidate as Proposed Filename and any suggested change to that proposed name. The **Repository Filename (Live)** field in File Inventory records what is *actually* on GitHub; changing a proposed name does not change that file. Do not treat preliminary names as approval.

## 2. Work on the branch, not on uncontrolled copies

Create `work/<topic>` from current `main`. Commit actual changes to the corresponding `Rig-Engineering-Files/<area>/<file-type>/<component-group>/` directory. Keep **one authoritative project source**. An editable CAD model, compiled output, prepared 3MF job and original STL may be related but are not necessarily interchangeable or duplicates.

Check native CAD assembly references, slicer project contents, software dependencies and wiring references before renaming, moving, replacing or deleting files. Do not change a stable ID for a revision of the same item. Use new IDs for new independently maintained parts or separate print jobs.

## 3. Record test evidence

For **3D printing**, capture intended quantity, the parts contained in a 3MF job, printer, material, print profile, latest result, actual date and reviewer evidence in the existing workbook. A successful print does **not** prove the printed part fits the current rig.

For **system-specific images and diagrams**, store the actual photograph or diagram once in the relevant functional area's `Images-and-Diagrams` location and allocate a `VIS` ID if it needs independent version tracking. For **whole-rig guide images**, keep one copy in the assembly guide and link to source designs.

For **CNC**, preserve the source geometry and machine program and document the tool/material and dimensional check. For **electronics**, preserve circuit source files and verified wiring/board revision. For **software**, preserve runnable source, necessary dependencies, configuration, test procedures and data-output format. Specific technical subgroups should appear only after real files exist.

Do not record historical source-file commit dates as physical print or use dates. Use `Unverified` until there is evidence for a stronger status. An accepted repository organization does not approve individual components.

## 4. Review and merge

Open a pull request against `main` using the prefilled checklist. Explain the change, affected IDs, compatibility, tests, source licenses and any proposed renames. Repository checks validate paths, IDs and inventory references automatically. A human reviewer must assess engineering safety, physical fit, print-job objects, test outcomes and any experimental protocol changes. Obtain Tim/Chad review as lab policy requires; no automatic approval is implied.

After approval, merge into `main`, update **Repository Filename (Live)**, GitHub URL and repository paths in the workbook and export the matching root inventory snapshot. Remove finished work branches and stale placeholders when real files are added.

## 5. Keep the two inventories consistent

**Primary editable record:** Google Sheets [CBAR Master Engineering File Inventory](https://docs.google.com/spreadsheets/d/1gD6PC8YFJGNSHkLBSL6r_NcwHOtmynXgbYKcXxWVr7A/edit). It has a compact review sheet and the detailed printing ledger. Both reference records by immutable file ID.

**Repository snapshot:** `inventory.csv` is used for repository validation and offline identification, and must reflect the committed filenames/paths. To update it after approved changes, export the **File Inventory** tab as CSV, then use `python tools/sync_inventory.py path/to/File-Inventory.csv` to preview and `python tools/sync_inventory.py path/to/File-Inventory.csv --write` to update the root CSV. Review the resulting Git diff before commit. The sync command does not rename manufacturing files or approve any component.

Avoid manually maintaining competing status registers. File review data that does not belong in the root GitHub snapshot stays in the existing Google Sheet. The CSV keeps separate **Original Source Blob SHA** (historical provenance) and **Current Blob SHA** (actual file revision). The automatic check validates the current hash. After an approved design change, update the Sheet's File SHA from Git and then synchronize. A reclassified design may keep its existing ID even if the old ID digits no longer match its current folder.

## 6. Tag a reproducible milestone

Create an **annotated tag** on a reviewed **commit**, not a tag per individual file status. Use `v0.x.y` for documented developmental configurations and `v1.0.0` only when lab verification supports a first validated release. The release notes should list exact file IDs/commit, tested physical configuration, relevant firmware/software, controlled dependencies and where the assembly, calibration and validation evidence can be found.

Git tags label repository snapshots; they do **not** capture an uncommitted local CAD file, printer firmware, laboratory measurements or external Google Sheet history automatically.

## 7. Reproduce or transfer the apparatus

Use a documented tag or commit rather than downloading arbitrary latest files. Obtain all required manufacturing sources, purchased-parts details, verified hardware and electronics schematics, tested code plus dependencies, 3MF printing settings, quantities, assembly instructions, calibration criteria and experiment protocol. Confirm which are available; missing evidence remains explicitly **not documented**.

When transferring to a lab GitHub organization, use GitHub repository transfer rather than copying into a brand-new unrelated repository so history and issues can be preserved. Configure people/permissions and branch protection through the GitHub interface when the lab chooses maintainers. Never publish credentials, animal records or restricted data.
