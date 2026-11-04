# 3D File Analysis — Generated Report

**Analysis only.** Never treat a geometric check as print approval or proof of fit.

| Count | Value |
| --- | ---: |
| Registered STL files | 71 |
| Registered 3MF files | 41 |
| Mesh/project analysis errors | 0 |
| Exact translation-normalized geometry match groups (not necessarily duplicate files) | 29 |

## Output files

- `3d-analysis.json`: full object-by-object 3MF build items/transforms and saved slicer settings, plus STL topology.
- `3d-file-summary.csv`: concise per-file numerical measurements.
- `suggested-next-ids.csv`: numerical suggestions only; new IDs still require review.

## Sample next IDs

| Group prefix | Next consecutive ID |
| --- | --- |
| 3DP-1-1 | 3DP-1-107 |
| 3DP-1-2 | 3DP-1-204 |
| 3DP-1-3 | 3DP-1-309 |
| 3DP-1-4 | 3DP-1-404 |
| 3DP-2-1 | 3DP-2-106 |
| 3DP-2-2 | 3DP-2-212 |
| 3DP-2-3 | 3DP-2-305 |
| 3DP-2-4 | 3DP-2-407 |
| 3DP-2-5 | 3DP-2-503 |
| 3DP-3-2 | 3DP-3-219 |
| 3DP-4-1 | 3DP-4-107 |
| 3DP-4-2 | 3DP-4-204 |
| 3DP-4-3 | 3DP-4-303 |
| 3DP-5-1 | 3DP-5-105 |
| 3DP-5-2 | 3DP-5-203 |
| 3DP-5-3 | 3DP-5-324 |
| 3DP-7-1 | 3DP-7-103 |
| 3DP-7-2 | 3DP-7-205 |

## Example matching geometries

These groups can include an STL mesh and a model embedded in a 3MF print job. They are **not** recommendations to delete files.
- 3DP-1-201, 3DP-1-202/object:1
- 3DP-1-202/object:7, 3DP-1-203
- 3DP-1-307/object:1, 3DP-1-308
- 3DP-1-402, 3DP-1-403/object:1
- 3DP-2-101/object:1, 3DP-2-102
- 3DP-2-301/object:1, 3DP-2-302
- 3DP-2-303/object:1, 3DP-2-304
- 3DP-2-401/object:1, 3DP-2-401/object:2, 3DP-2-401/object:3, 3DP-2-402

## Actual example: inside 3DP-7-202 (.3mf)

- Declared model units: millimeter
- Embedded model objects: 2
- Print-bed build placements: 2
- Stored slicer configuration files: Metadata/Slic3r_PE.config, Metadata/Slic3r_PE_model.config
- These fields are stored project information, **not evidence of an actual print**.
  - Build object ID 1, transform: 1 0 0 0 1 0 0 0 1 125 92.35 7.5
  - Build object ID 2, transform: 1 0 0 0 -1 0 0 0 -1 125 126 7

## Requested mesh comparison

- Files: `3DP-1-201` and `3DP-1-203`
- Finding: **Mesh geometry differs**
- Bounding-dimension change: [0.0, 0.0, -56.14]
- Triangle count change: 0
- Approximate surface-area change in model units²: -4154.36
- Tunnel-genus estimates: [1, 1]
- Changed-triangle candidates in first mesh: {'changed_triangles': 10, 'region_bbox': {'min': [0.0, 68.0, 0.0], 'max': [25.0, 80.0, 91.6874]}, 'region_extent': [25.0, 12.0, 91.6874]}
- Changed-triangle candidates in second mesh: {'changed_triangles': 10, 'region_bbox': {'min': [0.0, 68.0, 0.0], 'max': [25.0, 80.0, 35.5474]}, 'region_extent': [25.0, 12.0, 35.5474]}
- Changed regions are **not** precise hole dimensions or registration results.

## What this analysis can and cannot detect

Translation-normalized triangle fingerprints detect changed vertices/faces even when bounding dimensions,
triangle count and volume remain unchanged. Moving a hole within an otherwise fixed part changes the fingerprint.
A pure whole-model translation does not change that fingerprint; a rotation generally does.
For watertight edge-manifold meshes, genus can suggest the number of through-tunnels.
A blind hole, cavity, resized opening or repositioned cutout may change the fingerprint without changing genus.
The changed-triangle region narrows attention to candidate altered facets for pairwise STL comparisons,
but does not identify a precise hole center, diameter or volume. Arbitrary rotations need alignment.
Volumetric/Boolean difference measurements require a geometry-aware tool and visual review.
STL does not state units; 3MF model units and slicer metadata may be available.
A slicer profile saved in 3MF is not evidence that this object was physically printed.
