# Two-Port Chemosensory Brief-Access Rig

This repository contains technical files and reference instructions for the Samuelsen Lab's two-port experimental apparatus. **There are seven functional areas.**

## Find the right file

**Open [Rig-Engineering-Files](Rig-Engineering-Files/), choose a numbered functional area, choose a file type and then choose a component group.**

```text
Rig-Engineering-Files/
  01-Behavioral-Chamber/        ← functional area
    3D-Printing/                ← file type
      01-Cage-Structure/        ← component group
        3DP-1-101_....3mf       ← actual manufacturing file
```

| Location | Contents |
| --- | --- |
| [Rig-Engineering-Files](Rig-Engineering-Files/) | **Technical files:** printing, CNC, code, electronics and component diagrams organized by function |
| [inventory.csv](inventory.csv) | **Master inventory:** file IDs, exact paths, original filenames, source and status |
| [Setup-and-Operation](Setup-and-Operation/README.md) | **Whole-rig guide:** assembly, setup, calibration and maintenance |
| [Documentation](Documentation/) | **File-management rules:** naming, dependencies and source attribution |
| [Templates](Templates/README-TEMPLATE.md) | Reusable README outline |

## The seven functional areas

| # | Area | Imported STL and 3MF files |
| --- | --- | ---: |
| 01 | [Behavioral Chamber and Animal Interface](Rig-Engineering-Files/01-Behavioral-Chamber/README.md) | 20 |
| 02 | [Stimulus Presentation and Access](Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/README.md) | 28 |
| 03 | [Stimulus Storage and Selection](Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/README.md) | 18 |
| 04 | [Valves and Sound Attenuation](Rig-Engineering-Files/04-Valves-and-Sound-Attenuation/README.md) | 11 |
| 05 | [Vacuum, Gas and Drainage](Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/README.md) | 29 |
| 06 | [Shared Structure and General Motion](Rig-Engineering-Files/06-Shared-Structure-and-Motion/README.md) | 0 |
| 07 | [Experimental Control, Sensing and Data](Rig-Engineering-Files/07-Experimental-Control-Sensing-and-Data/README.md) | 6 |
| | **Total** | **112** |

Inside each functional area you will find `3D-Printing/`, `CNC/`, `Code/`, `Electronics/` and `Images-and-Diagrams/`. A `.gitkeep` file means the directory is reserved but **has no real technical files yet**. Only the 3D-printing directories currently contain imported manufacturing files.

**Verification:** The 112 imported STL and 3MF files originated in the [earlier three-port rig repository](https://github.com/neuroMoth/3-Port-4-Bottle-Rig). Their fit and suitability for the current two-port rig have **not** been verified. The inventory preserves source names and paths.

[File naming and status rules](Documentation/NAMING-AND-FILE-RULES.md) · [Dependency safety](Documentation/FILE-DEPENDENCIES.md) · [Source MIT notice](Documentation/SOURCE-LICENSE-MIT.txt)
