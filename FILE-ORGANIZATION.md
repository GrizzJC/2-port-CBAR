# Repository File Organization and Naming Register

This is the **one-stop organization guide** for the GitHub repository. It provides the exact placement rules, permanent-ID convention and links to the [complete file-by-file CSV index](tracking/repository-file-index.csv). It is independent of the Excel workbook, so anyone browsing GitHub can understand the library.

## Current organization

| Root | Meaning | Contents |
| --- | --- | --- |
| [3D-Models](3D-Models/README.md) | Registered and future 3D assets | Components, Assemblies, Print-Projects, Reference-Geometry, Build-Configurations, Systems |
| [Documentation](Documentation/README.md) | Engineering standards and procedures | Standards, Guides, Procedures, Templates |
| [tracking](tracking/README.md) | Machine-readable file and asset records | All CSV trackers, placement plan and workload batches |
| [README.md](README.md) | Repository orientation | Current task, links and scope |
| [.gitignore](.gitignore) | Exclusion rules for temporary files | Computer/autosave/cache patterns |

**Every tracked file path** is listed in [repository-file-index.csv](tracking/repository-file-index.csv). The file index does not pretend that registered 2-port models exist before their source files are obtained. The [3D asset tracker](tracking/2-port-3d-assets.csv) will hold one record per engineering representation once actual designs are located.

## Permanent identity

Working pattern: **`SS-NNN`** (example: `01-023`), two-digit functional system plus a three-digit unique number. `00` is reserved. **No system-number allocation or part ID is assigned by creating a category folder.**

The **ID is permanent**. The component's name, physical location, source application and design revision can change; they are documented as metadata. An individual part can have CAD source, STEP export, STL mesh and a related print project. These are not automatically four physical parts. Assemblies and multi-object print plates are registered as their own controlled objects with links to included part IDs.

### Filenames

| Example path or file | Meaning | Rename consideration |
| --- | --- | --- |
| `Components/SS-NNN/README.md` | Canonical part description, interfaces and revision history | Path changes only if ID assignment error; avoid ordinary renaming |
| `Components/SS-NNN/source/...` | Authoritative editable CAD or a source snapshot | Preserve linked source filename unless dependency check passes |
| `Components/SS-NNN/exports/SS-NNN.stl` | Derived printable mesh for one verified part | GitHub preview limit applies; link to source revision |
| `Components/SS-NNN/exports/SS-NNN.step` | Interchange CAD geometry | Confirm units, source and export revision |
| `Assemblies/SS-NNN/` | Controlled multi-part mechanical model | Check all linked component names and saved paths |
| `Print-Projects/SS-NNN/project/...` | Prepared slicer/build plate | May contain multiple objects and printer-specific settings |
| `Reference-Geometry/<vendor-item>/` | Third-party reference CAD | Check rights; not proof of actual installation |
| `Build-Configurations/<build-label>/` | Exact list of installed part/assembly revisions | Never duplicate arbitrary copies of all CAD part files here |

These are example patterns, not live fabricated parts. The [naming standard](Documentation/standards/3d-identifiers.md), [CAD dependency guide](Documentation/guides/renames-and-references.md), [design revisions](Documentation/standards/3d-revisions.md) and [storage guidance](Documentation/guides/file-formats-and-storage.md) contain the full rules and justifications.

## Functional placement for 3D files

The [systems index](3D-Models/Systems/README.md) contains eleven functional groups:
- **[Animal-Chamber-and-Access-Face](3D-Models/Systems/Animal-Chamber-and-Access-Face/README.md):** Animal enclosure, access face and related removable parts.
- **[Structural-Frame-and-Mounts](3D-Models/Systems/Structural-Frame-and-Mounts/README.md):** Base supports, towers, brackets, rails and structural connections.
- **[Port-Doors-and-Actuators](3D-Models/Systems/Port-Doors-and-Actuators/README.md):** Independent shutters, door guides, actuator mounts and stops.
- **[Bottles-and-Reservoirs](3D-Models/Systems/Bottles-and-Reservoirs/README.md):** Modular bottles/reservoir supports and retention hardware.
- **[Positioning-and-Motion](3D-Models/Systems/Positioning-and-Motion/README.md):** Motor, stage, coupling, guide and homing hardware.
- **[Spouts-and-Stimulus-Delivery](3D-Models/Systems/Spouts-and-Stimulus-Delivery/README.md):** Spouts, delivery interfaces and fine alignment.
- **[Valves-and-Fluid-Handling](3D-Models/Systems/Valves-and-Fluid-Handling/README.md):** Liquid flow and valve-related structural geometry.
- **[Pressure-and-Air](3D-Models/Systems/Pressure-and-Air/README.md):** Pressure/air/gas support where used.
- **[Rinse-Vacuum-and-Waste](3D-Models/Systems/Rinse-Vacuum-and-Waste/README.md):** Cleaning, rinse, vacuum and waste handling where used.
- **[Electronics-and-Sensor-Mounts](3D-Models/Systems/Electronics-and-Sensor-Mounts/README.md):** Physical electronics housings, sensor and cable mounts.
- **[Fixtures-Jigs-and-Test-Tools](3D-Models/Systems/Fixtures-Jigs-and-Test-Tools/README.md):** Manufacturing, alignment and inspection tools.

These pages provide organized navigation without moving the same physical part between folders whenever its application changes. The detailed [placement CSV](tracking/3d-placement-plan.csv) maps each system to its verification batch.

## Assembly placement

[Assembly groups](3D-Models/Assemblies/Groups/README.md) include integrated rig, chamber/ports, reservoir selection, fluid delivery, actuation/sensing and utilities. Actual assembly source files go in registered assembly-ID folders, not in the navigation pages.

## Version and release control

A change to the **modeling geometry** should have a design revision record. A **printing attempt** has a manufacturing/test record. A **Git commit** identifies an exact repository snapshot. A **Fusion saved cloud version** or SolidWorks source design history is separate from those. Stable filenames should not contain an editable revision suffix.

## Work batches

[Work-batches.md](tracking/work-batches.md) groups the complete 3D organization effort into a source/intake phase, a dependency/identity phase, mechanical functional groups, integration and release validation. The [batch-status.csv](tracking/batch-status.csv) is the checklist of actual progress. No design batch is claimed as reviewed or tested while its sources remain unavailable.

## How to keep this page and the index current

When adding, editing, renaming or deleting tracked files, update the master path index. Check that indexed paths resolve on `main`, and update the controlled asset record only if the file represents an actual engineering asset or a revision to one.

Do not use the number of README documentation files as a count of individual mechanical parts.
