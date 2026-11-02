# 3D Models — placement and file handling

The repository separates **asset identity** from *file format*, *manufacturing method* and *its use in a particular assembly*. This keeps permanent paths stable as experiments and hardware evolve.

## Where every type belongs

| Directory | Records / files | Does NOT belong |
| --- | --- | --- |
| [Components](Components/README.md) | Individual physical designs: native editable sources and controlled STL/STEP exports | Multi-part print jobs and duplicate source files |
| [Assemblies](Assemblies/README.md) | Native linked CAD assemblies, component relationships and verified assembly exports | A second uncontrolled copy of each component |
| [Print-Projects](Print-Projects/README.md) | Manufacturing-oriented 3MF, slicer projects, build-plate settings, print/test records | Primary CAD design source |
| [Reference-Geometry](Reference-Geometry/README.md) | Supplier models, purchased equipment envelopes and imported geometric references | Newly designed lab-manufactured components |
| [Build-Configurations](Build-Configurations/README.md) | Rig-level manifests: exact installed designs, revisions and placements | Replicated CAD and STL sets |
| [Systems](Systems/README.md) | Human-friendly placement across eleven rig functions | Duplicate CAD file copies |

## Controlled-folder pattern

```text
Components/SS-NNN/
  README.md
  source/      # CAD source or a manifest pointing to an authoritative CAD cloud version
  exports/     # controlled derived formats (STL, STEP, etc.)

Assemblies/SS-NNN/
  README.md
  source/      # linked native assembly + dependencies where appropriate
  exports/     # released assembly geometry

Print-Projects/SS-NNN/
  README.md
  project/     # 3MF or other controlled slicer project
```

These are **patterns**, not directories created with fictional identifiers. Use the permanent ID only after a real controlled asset is identified.

## Format decisions

- **SolidWorks part (.sldprt), Fusion design (.f3d), editable STEP:** component source or approved snapshot, preserving the authoritative source.
- **SolidWorks assembly (.sldasm), multi-file Fusion assembly (.f3z):** assembly source; list linked parts and check paths.
- **STL:** generally component-derived mesh export, not a parametric editable source.
- **3MF:** inspect contents first. A single design export might be a component representation; a print plate with several objects/settings is a print project.
- **OBJ / GLB / GLTF:** optional visualization or export geometry, with the same master-asset link. An optimized viewer mesh is not a manufacturing master.
- **DXF / DWG / technical drawing:** attach to the related design as a drawing/export, not a new physical component without a distinct deliverable identity.
- **STEP from a supplier:** reference geometry unless it has become a separate controlled lab-authored design.

A part printed in resin and in filament keeps the same design identity if its geometry/interface is the same; printing method and settings are tracked per print job.

## Workflow

Use [file intake and verification](../Documentation/procedures/3d-intake-and-release.md), the [rename-dependency guide](../Documentation/guides/renames-and-references.md) and the [workload batches](../tracking/work-batches.md). For each object, record its original name, origin, role, source files, geometry/export relationship, assembly connections, status, design revision and evidence before publishing it as current.
