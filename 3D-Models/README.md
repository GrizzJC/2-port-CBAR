# 3D models — working organization

**Status: proposed; no 2-port model files uploaded yet.** This area is for 3D design and fabrication assets supporting the 2-port chemosensory brief-access task.

## Categories

| Folder | Represents | Example |
| --- | --- | --- |
| [Components](Components/README.md) | One independently identifiable physical design or part | A bracket or spacer |
| [Assemblies](Assemblies/README.md) | Relationships among multiple physical components | Spout carrier assembly |
| [Print-Projects](Print-Projects/README.md) | Prepared printer/slicer projects that may contain several designs | Multi-part 3MF build plate |

The folders are based on **asset meaning**, not whether fabrication uses filament or resin. A single design might have an editable source, one or more exported formats, and an approved print project.

The **component's stable folder identifier** should be a provisional `NN-NNN` after approval, e.g. `Components/01-001/`. Do not create IDs by guessing. Proposed component layout:

```text
Components/NN-NNN/
  README.md                 # Purpose, related parts, revision record and approvals
  source/                   # Editable authoritative CAD source if GitHub copy is approved
  exports/                  # STL, STEP and other controlled exports
```

A large 3MF print plate belongs in `Print-Projects` and links to all the component IDs on the plate, rather than being misrepresented as a single component.

**No automatic migration from the older 3-port rig.** Its design files are only a reference until reviewed, tested and authorized for reuse. [Policy](../Documentation/legacy-3-port-reference.md).

For each model, complete the [component documentation template](../Documentation/templates/component-record.md) and [registry](../tracking/2-port-3d-assets.csv). Keep revision numbers out of permanent filenames; use the controlled revision record and a pinned release reference instead.
