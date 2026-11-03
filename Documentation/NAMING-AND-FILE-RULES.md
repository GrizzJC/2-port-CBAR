# Naming, file classification and change rules

## 1. Purpose and naming format

A filename should be recognizable, have a stable identifier and point to one maintained source. A file's **purpose** determines its family, not its extension, modeling application or whether a manufactured item is plastic, resin or metal.

**Identifier:** `TYPE-S-GNN` (example `3DP-1-201`). `TYPE` is the file-purpose family, `S` is one of the seven systems, `G` is its numbered subgroup (1–9) and `NN` is a two-digit sequence (01–99). Subgroup 0 is reserved, not used in the current collection. A complete identifier is unique. Prefix families have independent sequences, so `3DP-1-201` and `CNC-1-201` are different IDs. Always cite the full ID, never just `201`.

| Family | Purpose | Representative sources |
| --- | --- | --- |
| `3DP` | Additive manufacturing: filament, resin and other printable processes | STL, prepared 3MF, printing-oriented native design source |
| `CNC` | Subtractive CNC machining, regardless of material | CNC program, machine project, cutting drawing |
| `SW` | Software and executable control logic | MATLAB, Arduino, program dependencies |
| `EL` | Electronics and circuit design | KiCad, wiring diagrams, circuit board designs |

Native SolidWorks, Fusion and STEP are **not a separate family by default**. Assign them according to the intended deliverable. Preserve required native filenames and assembly dependencies; register the identifier separately when renaming the file would break relationships.

## 2. Why numbered subgroup blocks

A fixed batch of ten numbers breaks when a design gains, splits or combines parts. With the subgroup as the hundreds place, each category has **99 numbered positions**. Related files are allocated adjacent numbers initially, but new files later take the next free number in the same subgroup without renumbering other parts. Folder names and the master inventory, not numerical adjacency alone, express assembly membership.

Seven systems and their subgroups are listed in the [seven-system map](../README.md). An ID retains its original assigned number if a design is relocated or reclassified. Do not recycle retired IDs.

### Capacity at the imported printing-file baseline

The busiest currently classified subgroup is **5.3 Spout Drain Assembly with 23 STL/3MF files**. Three times that number is **69**, below its capacity of **99**, leaving **30 positions**. Thus its present intake could grow to about **4.30× the current size**, equivalent to **about 330% additional files**. All other imported printing subgroups are smaller. This supports a **3× increase in the current 112-file printing collection if its subgroup proportions remain similar**, not a claim about unreviewed CAD libraries, old software or unbalanced future growth. If an actual subgroup approaches 99, explicitly extend or allocate an additional logical subgroup without changing old identifiers.

## 3. Changes, splits, merges and print jobs

| Change | Rule | Reason |
| --- | --- | --- |
| Update the same model or print job | Keep its ID; track the committed state and revalidate as needed | References remain stable |
| Create another independent component | Assign a new ID | It is a distinct part |
| Split one component into independently manufactured parts | New ID for each new part; cross-reference the predecessor | One original ID cannot describe two different parts |
| Combine independent parts into a new single part | New ID for the new part, preserve predecessor links | New engineering identity |
| Arrange one or several components in a 3MF | Separate `3DP` file ID, related to the component meshes | A print job is not the same as a mesh |
| Improve the same prepared 3MF arrangement | Keep the 3MF ID; recheck when settings or material change | Avoid needless new file identities |
| Maintain different printer/build-plate arrangements simultaneously | Give each a separate ID | Both remain independently usable |
| Move a file to another functional group | Keep ID, update inventory and link from the former location | Avoid breaking previous references |

Every imported **3MF** is classified as a **prepared print job**, including a single-object job. Record actual objects, quantities, printer, material, bed space, support and adhesion constraints only when verified. Do not assume filename similarity proves a 3MF contains the corresponding STL.

## 4. Status and local development

| Verification status | Meaning |
| --- | --- |
| `Unverified` | File exists; applicability or expected function not established |
| `Working` | Provisional current working version |
| `Validated` | Passed documented manufacturing or functional checks |
| `Approved` | Accepted for a specified application |
| `Do Not Use` | Not suitable for current use due to identified problem or restriction |
| `Retired` | Superseded or discontinued |

**Revision Pending** is one separate flag for a known forthcoming local or unpublished correction/replacement. It does **not** itself make the current file unsafe. Mark `Do Not Use` when the existing version should be withheld. Avoid duplicate Update Pending and Replacement Pending columns.

**Rig Status** describes physical components: In Use, Installed, Spare, Not Installed, Unknown, Not Applicable. It does not describe whether a digital file is installed. **Last Used** refers to actual physical use, and **Last Printed** to actual printing of a prepared job. Do not infer either from a GitHub commit date; leave unknown dates blank.

Approval belongs to a particular tested design/configuration. A substantial local change or new commit may require verification again. Git history is separate from native CAD cloud saves and physical testing.

## 5. One authoritative copy and dependency safety

Store a file once, in its primary functional location. Other systems link to it rather than keeping stale duplicates. If an external tool absolutely requires a duplicate, label it as a non-authoritative `COPY` and record its source path; do not independently mark that copy as approved.

Before changing a SolidWorks/Fusion source, 3MF project or executable MATLAB/Arduino file name, check references using the [dependency guide](FILE-DEPENDENCIES.md). No automated GitHub move repairs links inside external programs.

## 6. Single inventory and provenance

The root [inventory.csv](../inventory.csv) is the **single authoritative file and component register**. It holds original names, original paths, current paths, source references, status and recorded test/use facts. System READMEs should explain equipment and relationships rather than duplicate the entire changing inventory. When verified non-print assets are added, use the same inventory or a carefully justified extension rather than another manually synchronized register.

The imported source is a three-port version; none of its copied files should be described as compatible with the current two-port apparatus without appropriate evidence.

## 7. Intake and maintenance

When adding a file, identify its intended function and manufacturing role, preserve original source/provenance, check filename dependencies, allocate an available subgroup ID, place only the actual file and update the [master inventory](../inventory.csv). Keep the source project's version or commit reference where it matters for reproducibility. Record testing or physical-use dates only from actual evidence; a committed file is not automatically approved.

Keep `README.md` files only where they supply useful system or operating information. **Do not maintain duplicate inventories, redundant revision ledgers or placeholder READMEs for empty component subgroups.** Empty locations for CNC, electronics, software and system-specific illustrations are represented by `.gitkeep`, with their purpose explained in each system's README. Once real files are added, remove the `.gitkeep` for that folder.

GitHub stores committed changes, not unsaved local edits. Source CAD versions, Git history and physical validation remain distinct. Keep source attribution and licenses intact. Do not commit sensitive research or animal records to a public repository without permission. A later transfer to a laboratory organization should preserve repository history and verify access, dependencies and ownership first.
