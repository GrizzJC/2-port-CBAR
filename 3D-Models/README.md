# 3D Models

This folder organizes the rig's controlled 3D design and manufacturing assets by **what a file represents**, not by which program created it.

| Folder | Contents |
| --- | --- |
| [Components](Components/README.md) | Individual physical parts and their source/derived files |
| [Assemblies](Assemblies/README.md) | Multi-part models and the relationships among components |
| [Print Projects](Print-Projects/README.md) | Prepared 3D-print jobs, including multi-part 3MF projects |

## Recommended component layout

Once a component's permanent identifier is assigned, keep its records and exports together:

```text
Components/
  SS-NNN/
    README.md
    source/
    exports/
```

The `SS-NNN` notation is a placeholder. Do not create numbered component folders or assume that two files represent the same component without verifying their relationship.

The editable CAD file is the preferred source of design intent. STL represents exported mesh geometry, STEP generally serves interchange between CAD applications, and 3MF can contain a configured print job. These should not be treated as interchangeable simply because they are all 3D-related.

## Registering a part

1. Determine whether it is a component, assembly or manufacturing project.
2. Identify the source design and any related exports.
3. Record mating parts and dependencies on existing filenames or paths.
4. Assign a permanent identifier from the approved subsystem table.
5. Record the current design revision and the tests supporting its release.
6. Document print parameters separately from CAD design revisions.

Start from the [component record template](../Documentation/templates/component-record.md) or [assembly record template](../Documentation/templates/assembly-record.md). Keep the [asset tracker](../tracking/2-port-3d-assets.csv) up to date.

Printing with filament, resin or another process does not automatically change a part's identity. Manufacturing settings should be documented in the print record.
