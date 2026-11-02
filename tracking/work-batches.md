# 3D Asset Organization — Work Batches

## Goal

Apply one reproducible process to every **verified new 2-port** design without losing editable source history, physical connections, filename-dependent CAD references or prior validated manufacturing results.

All work is performed on **`main`**. Work packages divide the *inventory and verification effort* into manageable groups; they are not development branches, hardware revisions, formal identifiers or separate repositories.

## Batch sequence, scope and completion criteria

| Batch | Scope | Workload / risk | Completion criteria |
| --- | --- | --- | --- |
| **B00** | Repository baseline and source discovery | Low-to-medium; foundational | Master source list plus item-level file URLs; no double-counted file formats |
| **B01** | Identity, duplication and rename-risk triage | High verification; blocking | Known part/assembly/print project roles; source-to-export links; rename-risk flags |
| **B02** | Chamber and structural parts | Medium mechanical workload; grouped shared geometry | Component candidates and assembly relationships; fit/mechanical requirements |
| **B03** | Port actuators and stimulus presentation | High interface complexity; coupled port/behavior geometry | Port clearance, mating maps, positioning checks, unique components |
| **B04** | Reservoir and motorized selection | High workload and high dependency | Carrier/motor/guide relationships, HOME and two selectable positions, expansion dependencies |
| **B05** | Fluid/pressure/rinse utilities | Conditional; only actual fitted subsystems | Verified flows, reusable part records, pressure/service fit checks |
| **B06** | Electronics mounts, fixtures and references | Medium; source rights and model fit checks | Mount/reference records, calibration/fabrication aids, source/license trace |
| **B07** | Assembly integration and configuration | High integration; depends on B02–B06 | Precise assembly BOM, revision compatibility, rig build manifest |
| **B08** | Release audit and reproducibility | High quality-assurance burden | Source hashes/Git refs, revision log, tested files, complete file index |

## Workload-balancing approach

The batches are ordered by **dependencies and verification effort**, not simply file count. The riskiest work is where native CAD references can break, several physical systems meet, or a physical fit must be inspected. A batch may be subdivided by assembly or by five to ten *unique controlled designs* at a time; one STL and one matching STEP are not two parts. Complex assemblies should be reviewed individually.

A practical unit of completion is a **controlled item** (component, assembly, print project or reference), with all source and export files linked. When a 3MF contains multiple items, its work is counted by the preparation project plus cross-referenced component relationships, not by filename alone.

## Steps within each batch

1. Inventory original filenames and full source paths (do not rename).
2. Identify authoritative editable CAD source, exports and derivative representations.
3. Classify asset type and stable functional system; flag ambiguous/incomplete cases.
4. Record all referenced files and effects of a rename or path change.
5. Map physical mating relationships and related assemblies.
6. Assign and check permanent ID only after the unique controlled item is verified and numbering is authorized.
7. Record design revision, source CAD save, Git reference, print manufacturing details and physical validation where available.
8. Update [3D asset tracker](2-port-3d-assets.csv), [assembly relationships](assembly-membership.csv) and [file index](repository-file-index.csv).
9. Mark complete only when evidence and acceptance checks have been documented.

## Active-scope facts

The available `GrizzJC/2-port-CBAR` repository currently contains planning documents and empty 2-port asset registers, **not the actual 2-port 3D source files**. The older neuroMoth three-port repository is historical context only and is not auto-migrated into the new two-port build.

No batch is claimed as completed based solely on creating the directories or templates. A source intake candidate is not an approved part, and an approved design file is not automatically an installed physical component.

## Progress records

Use [batch-status.csv](batch-status.csv) for each batch's state, number of files located, unique designs reviewed, designs registered, validated build references and blockers. Store supporting reasoning in the corresponding component or assembly README rather than in uncontrolled personal notes.

Work stops at the earliest unmet verification dependency, while independent files may continue into later batches.
