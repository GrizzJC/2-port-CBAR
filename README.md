# 2-Port Chemosensory Brief-Access Rig

Repository for the Samuelsen Lab's **2-port chemosensory brief-access task rig**. It brings together the designs, fabrication files, electronics, software and operating information needed to build, maintain and develop the experimental system.

The task defines the project's identity; the hardware configuration may change over time.

## Contents

| Area | Contents |
| --- | --- |
| [3D Models](3D-Models/README.md) | Components, multi-part assemblies and prepared 3D-print projects |
| [Documentation](Documentation/README.md) | File identification, revision practices, manufacturing references and reusable records |
| [Asset tracking](tracking/README.md) | 3D-file inventory and dependency checks before renaming or relocating files |

Other content such as experiment-control software, electronics, calibration, procedures and equipment manuals can be organized here as those materials are added.

## 3D file organization

The 3D library distinguishes three types of assets:

- **Component:** An individual part design. Editable CAD sources and exported formats may describe the same component.
- **Assembly:** A set of components and their mechanical relationships.
- **Print project:** A prepared manufacturing job, potentially containing multiple components and printer settings.

Use the [3D asset tracker](tracking/2-port-3d-assets.csv) to associate each file with its stable identifier, source, related parts, revision, status and any filename/path dependencies. An identifier is assigned only after the item's identity has been established.

## File identification and revisions

A compact **`SS-NNN`** scheme is used as the working identifier format: two-digit system/group code followed by a three-digit sequence. Group codes remain unassigned until the actual 2-port parts are classified. See [file identification](Documentation/standards/3d-identifiers.md).

Revisions and validation belong in component records and the asset tracker, **not in permanent identifiers**. For CAD models, retain references to the native editable design and its source-system history. For printed parts, retain printer and testing information separately. See [revision management](Documentation/standards/3d-revisions.md).

**Do not rename native CAD files or program files based solely on the identifier.** Some filenames and paths are used by assemblies or programs. Record and verify dependencies before changes.

## Repository usage

This repository is maintained on `main`. Documentation and folder structure can evolve as the rig develops. Model or program files should only be labeled validated after their relevant checks have been recorded.

## File formats and storage

See [engineering file formats and GitHub storage](Documentation/guides/file-formats-and-storage.md) for the STL viewer's 10 MB threshold, editing versus exported formats, and storage recommendations.

## Licensing

No repository-wide license has been selected. The permissions and attribution applicable to any contributed or reused source files should be checked before redistribution.
