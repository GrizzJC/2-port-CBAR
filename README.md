# Two-Port Chemosensory Brief-Access Rig

This repository has two distinct purposes: **engineering files** used to make, modify and control the rig, and **a guide** explaining how the complete rig should be assembled and operated. The engineering files are organized into seven functional areas.

## Engineering files vs. the rig guide

**Need an STL, 3MF, CNC design, electronic circuit or code?** Open **[Rig-Engineering-Files](Rig-Engineering-Files/)**.

**Need instructions for assembling, connecting, operating, calibrating or maintaining the rig?** Open **[Rig-Assembly-and-Operation-Guide](Rig-Assembly-and-Operation-Guide/README.md)**. The guide is an outline until verified instructions and diagrams are added. It is **not** another functional area and does not contain duplicate manufacturing files.

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
| [Rig-Engineering-Files](Rig-Engineering-Files/) | **ACTUAL TECHNICAL FILES:** 3D printing, CNC, code, electronics and component diagrams organized by function |
| [inventory.csv](inventory.csv) | **Repository snapshot:** file IDs, exact paths, original filenames, source and status. Working changes are maintained in the existing [Google Sheet](https://docs.google.com/spreadsheets/d/1gD6PC8YFJGNSHkLBSL6r_NcwHOtmynXgbYKcXxWVr7A/edit) |
| [Rig-Assembly-and-Operation-Guide](Rig-Assembly-and-Operation-Guide/README.md) | **INSTRUCTIONS / GUIDE:** whole-rig assembly, setup, operation, calibration and maintenance (not yet validated) |
| [Documentation](Documentation/) | **File-management rules:** naming, dependencies and source attribution |
| [Templates](Templates/README-TEMPLATE.md) | Reusable README outline |

## Making changes, review and releases

Use the [Engineering Workflow](Documentation/ENGINEERING-WORKFLOW.md) for new files, development branches, review, print tests, inventory synchronization and reproducible version tags. The [GitHub change-request form](.github/ISSUE_TEMPLATE/change-request.yml) and [pull-request checklist](.github/PULL_REQUEST_TEMPLATE.md) are ready to use. The [automatic inventory check](.github/workflows/validate-repository.yml) checks administrative consistency but cannot validate physical compatibility.

## Development preview: automated 3D analysis

This is the **work/3d-print-review** branch. The approved `main` baseline remains separate. The [3D analysis guide](Documentation/3D-ANALYSIS.md) explains geometry fingerprints, moved holes, 3MF objects/settings and numerical ID suggestions. Run **[Inspect 3D models (development)](../../actions/workflows/inspect-3d.yml)** from the Actions tab, then open the completed run to read its **Summary** and download the **3d-file-audit** artifact (JSON, CSV and readable report). Reports are generated on demand, not stored as manually maintained copies.

These calculations are **technical screening only**, not physical print, fit, release or research validation. The source manufacturing files are not altered by this action.

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

**Verification:** The 112 imported STL and 3MF files originated in the [earlier three-port rig repository](https://github.com/neuroMoth/3-Port-Bpod-Rig). Their fit and suitability for the current two-port rig have **not** been verified. The inventory preserves source names and paths.

[File naming and status rules](Documentation/NAMING-AND-FILE-RULES.md) · [Dependency safety](Documentation/FILE-DEPENDENCIES.md) · [Source MIT notice](Documentation/SOURCE-LICENSE-MIT.txt)
