# Decision log and approval checklist

**Approval status:** Pending Tim or Chad. This branch provides a reviewable proposed structure, not a released lab standard.

| Decision | Working recommendation | Current status |
| --- | --- | --- |
| Repository | `GrizzJC/2-port-CBAR` as created; 2-port chemosensory brief-access task | Existing repository |
| Scope now | 3D files, asset ID planning and documentation only | In progress |
| 3-port reference | Keep separate; copy no old parts by default | Proposed |
| Permanent identifier | `NN-NNN`; 00 reserved, subsystem codes not assigned | Needs approval |
| File identity | Physical design vs assembly vs print plate distinguished | Needs approval |
| Filename exceptions | Keep CAD/source filenames if renaming breaks references | Needs approval |
| Revision history | In linked README/registry; exact release commits | Needs approval |
| Manufacturing records | Separate from design revisions | Needs approval |
| Source of truth | CAD system for editable master, GitHub for approved snapshots | Needs approval |
| License | None chosen until source ownership/reuse reviewed | Needs approval |
| Viewer/schematic | Later phase, not built in this branch | Deferred |

## Before accepting 2-port 3D files

- [ ] Obtain the actual 2-port source files and identify who owns the designs.
- [ ] Confirm whether a proposed asset is a new 2-port design or a reused 3-port component.
- [ ] Determine design sources and any linked SolidWorks/Fusion assembly references.
- [ ] Review `.3mf` for multi-component build plates and printer settings.
- [ ] Approve numbering categories; do not invent identifiers.
- [ ] Fill dependency-risk field, rename verification and any license/attribution conditions.
- [ ] Confirm the component fits or functions on the 2-port task; record print/test evidence.
- [ ] Document Tim or Chad's approval and date.

## Revision summary

| Date | Status | Summary |
| --- | --- | --- |
| 2026-11-02 | Proposal | Added initial review checklist and unresolved decisions. |
