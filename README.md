# Two-Port Chemosensory Brief-Access Rig

This repository stores the hardware designs and working references for the Samuelsen Lab's two-port behavioral rig. **There are exactly seven functional systems.** Other top-level folders contain documentation or reusable templates, not more systems.

## Where to go

| Location | What it is | What you will find |
| --- | --- | --- |
| [Systems](Systems/) | **Hardware and technical file library** | Seven numbered system folders; actual STL/3MF files in `[system]/[subgroup]/3D-Printing/` |
| [inventory.csv](inventory.csv) | **Single file inventory** | Current and original filenames, file IDs, source locations and status |
| [Setup-and-Operation](Setup-and-Operation/README.md) | **Whole-rig manual** | Central setup and operations outline; diagrams have a dedicated location |
| [Documentation](Documentation/) | **Rules and reference instructions** | Naming rules, dependency safety and imported source license |
| [Templates](Templates/README-TEMPLATE.md) | **Reusable document template** | Optional standard README structure |

## The seven systems

| # | System | Actual STL/3MF files |
| --- | --- | ---: |
| 01 | [Behavioral Chamber and Animal Interface](Systems/01-Behavioral-Chamber/README.md) | 20 |
| 02 | [Stimulus Presentation and Access](Systems/02-Stimulus-Presentation-and-Access/README.md) | 28 |
| 03 | [Stimulus Storage and Selection](Systems/03-Stimulus-Storage-and-Selection/README.md) | 18 |
| 04 | [Valves and Sound Attenuation](Systems/04-Valves-and-Sound-Attenuation/README.md) | 11 |
| 05 | [Vacuum, Gas and Drainage](Systems/05-Vacuum-Gas-and-Drainage/README.md) | 29 |
| 06 | [Shared Structure and General Motion](Systems/06-Shared-Structure-and-Motion/README.md) | 0 |
| 07 | [Experimental Control, Sensing and Data](Systems/07-Experimental-Control-Sensing-and-Data/README.md) | 6 |
| | **Total** | **112** |

**Example: locating a real print file**

`Systems/01-Behavioral-Chamber/01-Cage-Structure/3D-Printing/`

The folder above contains actual STL and 3MF files. A `README.md` explains a folder; it is **not** a print file. `CNC/`, `Software/`, `Electronics/` and `Visuals-and-Schematics/` within each system currently contain only empty-directory placeholders.

**Do not mistake a placeholder for a finished design.** The 112 imported printing files originate from the earlier [three-port repository](https://github.com/neuroMoth/3-Port-4-Bottle-Rig) and are not yet verified for the current two-port rig.

[File naming and status rules](Documentation/NAMING-AND-FILE-RULES.md) · [File dependency safety](Documentation/FILE-DEPENDENCIES.md) · [Preserved source license](Documentation/SOURCE-LICENSE-MIT.txt)
