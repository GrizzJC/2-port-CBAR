# Two-Port Chemosensory Brief-Access Rig

This repository is organized by **seven functions of the experimental rig**. Each functional system contains related component groups, actual manufacturing files and reserved locations for other file types.

## First: where is the file?

| Looking for | Open | What it contains |
| --- | --- | --- |
| **STL or 3MF printing file** | [Systems](Systems/README.md) → numbered system → numbered subgroup → **`3D-Printing/`** | **112 real imported STL/3MF files** across the systems; see subgroup links below |
| **CNC machining file** | [Systems](Systems/README.md) → system → **`CNC/`** | **PLACEHOLDERS only** for now |
| **Electronics design** | [Systems](Systems/README.md) → system → **`Electronics/`** | **PLACEHOLDERS only** for now |
| **MATLAB, Arduino or other software** | [Systems](Systems/README.md) → system → **`Software/`** | **PLACEHOLDERS only** for now |
| **Component photograph or schematic** | [Systems](Systems/README.md) → system → **`Visuals-and-Schematics/`** | **PLACEHOLDERS only** for now |
| **Whole-rig assembly, operating or calibration instructions** | [Setup and Operation](Setup-and-Operation/README.md) | **Documentation framework**, not manufacturing files |
| **Search, filter or verify a file** | [Master inventory](inventory.csv) | File IDs, names, original sources, actual paths and status |

**Example of an actual printing folder:** [Behavioral Chamber → Cage Structure → 3D-Printing](Systems/01-Behavioral-Chamber/01-Cage-Structure/3D-Printing/). It contains real STL/3MF files. A `README.md` explains a folder; it is **not** a print file. A folder marked **PLACEHOLDER** has no verified project or technical file yet.

## The seven systems

| # | System | Imported STL/3MF files |
| --- | --- | ---: |
| 01 | [Behavioral Chamber and Animal Interface](Systems/01-Behavioral-Chamber/README.md) | 20 |
| 02 | [Stimulus Presentation and Access](Systems/02-Stimulus-Presentation-and-Access/README.md) | 28 |
| 03 | [Stimulus Storage and Selection](Systems/03-Stimulus-Storage-and-Selection/README.md) | 18 |
| 04 | [Valves and Sound Attenuation](Systems/04-Valves-and-Sound-Attenuation/README.md) | 11 |
| 05 | [Vacuum, Gas and Drainage](Systems/05-Vacuum-Gas-and-Drainage/README.md) | 29 |
| 06 | [Shared Structure and General Motion](Systems/06-Shared-Structure-and-Motion/README.md) | 0 |
| 07 | [Experimental Control, Sensing and Data](Systems/07-Experimental-Control-Sensing-and-Data/README.md) | 6 |
| **Total** | | **112** |

**These are the only seven functional systems.** [Documentation](Documentation/README.md) contains technical rules, [Templates](Templates/README-TEMPLATE.md) contains a reusable README outline and [Setup and Operation](Setup-and-Operation/README.md) contains the integrated manual. They are **not additional systems**.

## File accuracy and status

The 112 printing files were imported from the [earlier three-port source repository](https://github.com/neuroMoth/3-Port-4-Bottle-Rig) and remain **Unverified** for the current two-port rig. The [inventory](inventory.csv) preserves original filenames and paths. Do not treat source presence or a placeholder as evidence of installation, compatibility or approval.

For file numbering, print-batch treatment, cross-system references and revision handling, see [Naming and File Rules](Documentation/NAMING-AND-FILE-RULES.md). Original author attribution and the [imported MIT notice](Documentation/SOURCE-LICENSE-MIT.txt) remain preserved; that notice does not license all new content automatically.
