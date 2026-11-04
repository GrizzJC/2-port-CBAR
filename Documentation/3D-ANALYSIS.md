# 3D file analysis: development branch

Run from the repository root:

```bash
python tools/inspect_3d.py --out .generated/3d-audit
python tools/inspect_3d.py --compare 3DP-1-201 3DP-1-203
```

The **Inspect 3D models (development)** GitHub Actions workflow runs the test suite and inspects all available STL and 3MF files on a development branch. Open the workflow run's **Summary** for totals, next numerical file IDs and a sample comparison. Download the **3d-file-audit** artifact for all source-backed data. A concise generated report is published as `Documentation/3D-ANALYSIS-RESULTS.md` on this development branch. It is **generated, not manually maintained**. The detailed outputs remain attached to the workflow run, rather than being committed as a competing inventory.

**Outputs:** `3d-file-summary.csv`, `3d-analysis.json`, `suggested-next-ids.csv` and a generated report `README.md`. These are analysis artifacts, NOT reviewed or approved values in the master inventory. They do not change source files or the working Google Sheet.

## Comparing holes and moved features

Summary statistics (triangle count, bounding dimensions, surface area and volume) can remain constant even if a hole moves. This inspector creates a **translation-invariant geometry fingerprint** from every triangle's coordinates relative to the mesh bounds. A change to a hole's size or position changes this fingerprint even if its overall numerical summaries remain unchanged. A whole-object translation should leave the fingerprint unchanged; the bounding-box **minimum coordinate** still records the move. A **rotation is NOT normalized**, so a reoriented model may appear different.

For meshes with no boundary or nonmanifold edges, the program estimates topology using the Euler characteristic. This can indicate a change in the count of **through-holes/tunnels**, but is not a count of every drilled or blind hole. A moved blind hole can change the fingerprint while leaving topology, volume, surface area and triangle count unchanged.

**Limit:** A differing geometry fingerprint does not locate the edited hole, find its center/diameter, or calculate the exact geometric difference between the objects. Those tasks require mesh registration/alignment, a distance field or solid Boolean difference with visual confirmation. STL does not declare units. A mesh may be nonmanifold, self-intersecting or generated with different triangulation even when its intended solid is effectively identical, and this can produce changed fingerprints.

## 3MF analysis

A 3MF file is a ZIP container with one or more model parts. The script extracts the declared model **unit**, mesh object IDs, geometry dimensions, component references, build-item count and the **stored build transformations** when present. That can reveal an object moving on the print bed even when its source mesh did not change.

It also reads a safe subset of settings from supported slicer metadata (for example PrusaSlicer's `Metadata/Slic3r_PE.config` and JSON settings when present). Available settings can include printer profile, material, nozzle, layer height, infill and supports. A stored setting **does not establish that a print occurred**, that the listed printer was used or that the current machine's settings match. More complex Bambu/Orca extensions, modifiers, plates and external references require a slicer-specific review.

The 3MF parsing is intentionally a first-pass inspection based on the [3MF Core Specification](https://github.com/3MFConsortium/spec_core). For manufacturing decisions, open the 3MF in the original slicer and verify objects, plate arrangement, scale, materials and settings.

## File numbering and review

`suggested-next-ids.csv` calculates the next **unused sequential ID after the current maximum** per populated subgroup. A number is a proposal, not automatically reserved. It must be checked against the inventory and any concurrently developed branches. Never renumber an existing ID simply because its functional subgroup changes.

The full data remains in GitHub Actions artifacts; print results, verification and proposed names remain in the lab's chosen working inventory. **No automatic spreadsheet edits and no physical printing status inference.**
