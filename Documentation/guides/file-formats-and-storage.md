# File formats and manufacturing classification

| Format | Typical use | Important limits |
| --- | --- | --- |
| STL | Printable geometry | Must verify dimension, mesh and material suitability |
| 3MF | Prepared printer/job configuration, one or several objects | Settings retained vary by slicer; inspect before relying on them |
| SolidWorks / Fusion / STEP | Editable design or exchanged geometry | Native references and full feature history may not transfer |
| DXF / C2D | Cut geometry and CNC projects | Verify material, units and machine setup |
| KiCad schematic / PCB | Electronic circuits | PCB and wiring files are not executable software |

A three-dimensional CAD source is **not always a 3D printing file**. Classify by intended fabrication or work product: `3DP` for additive manufacturing (filament or resin), `CNC` for subtractive machining (metal, plastic or other material), `EL` for electronics and `SW` for executable code. Avoid copying native autosaves and large temporary binary backups into Git.

GitHub can preview supported STL meshes, but preview does not establish dimensional accuracy or manufacturability. Git history, CAD source revision and physical validation must not be conflated.

[Authoritative rules](../NAMING-AND-FILE-RULES.md) · [dependency checks](renames-and-references.md).
