# 2-Port Chemosensory Brief-Access Rig (CBAR)

Engineering and laboratory documentation for the **Samuelsen Lab's two-port chemosensory brief-access task**. The repository can hold the mechanical designs, fabrication projects, electronics, control software, experimental protocols, manuals and maintenance information required to build and maintain the system.

The *two-port task* defines the repository's scope. The current number of bottles, motors, valves or printable parts does **not** define a component's permanent identity.

## Find what you need

| Location | Use |
| --- | --- |
| **[File organization and naming register](FILE-ORGANIZATION.md)** | Complete indexed list of files presently in this repository, file-placement rules, identifiers and status definitions |
| [3D model library](3D-Models/README.md) | Where part sources, exports, assemblies, print projects and vendor references belong |
| [Functional 3D system map](3D-Models/Systems/README.md) | Eleven physical system categories, independent of file type and printing process |
| [Assembly grouping](3D-Models/Assemblies/Groups/README.md) | How components connect and which assemblies they belong to |
| [Documentation](Documentation/README.md) | Naming, CAD source history, 3D release control, printing and storage guidelines |
| [Tracking](tracking/README.md) | CSV registers for component/file intake, dependencies, build configurations and manufacturing records |
| [Work batches](tracking/work-batches.md) | How to inventory, evaluate, place and verify assets without losing dependencies |

## How a design is registered

1. Confirm the file represents a real **two-port** component, multi-part assembly, print preparation or external reference.
2. Identify its original editable source and every derived file.
3. Classify it by **stable physical function**, then assign an identifier only after the identity is verified.
4. Preserve engineering dependencies and native source filenames when renaming them would break references.
5. Store or link the authoritative design, record the revision and make an exact release snapshot.
6. Record the manufacturing method, print/test outcome and compatibility with the relevant rig build.

The working ID format is **`SS-NNN`** (two-digit functional-system code, three-digit number within that system). The convention is defined in [3D identification](Documentation/standards/3d-identifiers.md). No actual numeric system codes or part IDs have yet been allocated.

## Current rig concept versus future hardware

The task uses two access ports with independently controlled shutters and a stimulus-selection mechanism. The current setup uses two two-bottle assemblies and two trial-selection positions with a HOME position. These are **configuration properties** tracked in the [build register](tracking/build-configurations.csv), not identifiers or filename prefixes.

## Technical source control

GitHub records committed files. The editable CAD project may reside in Autodesk Fusion, SolidWorks or another CAD system; save the authoritative source reference and an exact release copy where needed. The [dependency guide](Documentation/guides/renames-and-references.md) explains why a GitHub rename does not repair internal links in a CAD assembly or program.

## Current inventory state

The repository contains technical documentation and **tracking templates**, but no verified new two-port STL, 3MF, STEP, Fusion or SolidWorks model files have been committed. A system directory is a **location for future assets**, not proof a part exists, is installed or has been approved.

## License and ownership

No repository-wide license is specified. Imported/reused designs and code require attribution, permission and existing-license review before redistribution.
