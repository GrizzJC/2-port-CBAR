# 2-Port Chemosensory Brief-Access Rig (2-port CBAR)

> **Planning / proposed organization.** The 3D asset-control system in this branch is a working proposal awaiting review by Tim or Chad. It is not yet an approved laboratory standard.

This repository supports the Samuelsen Lab's **2-port chemosensory brief-access task**, including current and future rig designs. The task defines the repository's scope; the number of bottles, valves, motors or other replaceable hardware features does not define an asset's identity.

## Planned repository contents

| Area | Intended contents | Status |
| --- | --- | --- |
| [3D-Models](3D-Models/README.md) | Editable 3D sources, printable exports, assemblies and manufacturing projects | **Current planning focus** |
| [Tracking](tracking/README.md) | Permanent identifiers, filename/path dependency risks and review status | **Template only** |
| [Documentation](Documentation/README.md) | Decisions, standards, revision summaries and eventually manuals/protocols | **Working drafts** |
| Electronics / Control software / Experimental procedures | Future phases, not being organized yet | **Not started** |

**No verified new 2-port CAD, STL or 3MF component files have been added.** Files in the older 3-port repository must not be assumed to belong to this 2-port rig. See [legacy-reference policy](Documentation/legacy-3-port-reference.md).

## Working rules

1. Separate an item's **permanent identifier** from its human-readable description and revision.
2. Never put a potentially changeable hardware count in a permanent component filename.
3. Start with the proposed six-character `NN-NNN` identifier (for example `01-001`), but **do not assign numbers** until subsystem codes and identity rules are approved.
4. Record filename/path dependency risks before moving or renaming CAD sources or related code. A Git rename does not rewrite internal engineering references.
5. Keep revisions in a linked revision record. Differentiate design changes, approved releases and individual print attempts.
6. Do not copy 3-port files into current 2-port folders without an explicit reuse assessment.
7. Do not publish experiment data or animal identifiers in this repository without laboratory review.

## Getting started

- [3D file organization](3D-Models/README.md)
- [Identifier and naming proposal](Documentation/standards/3d-identification-and-naming.md)
- [3D revision / manufacturing history](Documentation/standards/3d-revision-and-manufacturing.md)
- [Storage, GitHub viewer and future Three.js rationale](Documentation/decisions/storage-and-viewer-rationale.md)
- [Review and approval checklist](Documentation/approval-checklist.md)
- [3D asset registry template](tracking/2-port-3d-assets.csv)

## Change summary

| Date | Status | Change | Approval |
| --- | --- | --- | --- |
| 2026-11-02 | Proposal | Added the initial 3D asset-control framework and documentation structure. | Pending Tim / Chad |

## License

No license has been chosen for this new repository. **Public visibility does not automatically grant permission to reuse files.** Before copying older designs or software, verify rights, attribution and any inherited license obligations with the lab.
