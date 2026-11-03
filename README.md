# Two-Port Chemosensory Brief-Access Rig

Engineering and operational resources for the Samuelsen Lab's two-port behavioral apparatus. This repository groups work by **what each system does**, not by file extension, fabrication material or modeling software.

## Find what you need

| Location | Purpose |
| --- | --- |
| [Systems](Systems/README.md) | Seven shared functional systems covering physical equipment, printable models, machining, electronics, software and controls |
| [Master inventory](inventory.csv) | Registered printing files, original names, paths, identification and verification status |
| [3D-printing overview](3D-Models/README.md) | How STL and prepared 3MF print jobs are organized within the systems |
| [Setup and operation](Setup-and-Operation/README.md) | Rig-wide diagrams, assembly guidance, operation, calibration and troubleshooting |
| [Naming and file rules](Documentation/NAMING-AND-FILE-RULES.md) | Prefixes, identifier capacity, split/merge rules, status meanings and source handling |
| [Documentation](Documentation/README.md) | Engineering procedures and reference materials |
| [Templates](Templates/README-TEMPLATE.md) | Reusable eight-section README template |

## Seven functional systems

| No. | Functional system | Scope |
| --- | --- | --- |
| 1 | [Behavioral Chamber and Animal Interface](Systems/01-Behavioral-Chamber/README.md) | The rat enclosure, access face and animal-facing hardware. This is not the valve sound attenuation chamber. |
| 2 | [Stimulus Presentation and Access](Systems/02-Stimulus-Presentation-and-Access/README.md) | Spouts, delivery positioning at the animal-facing ports, shutters and access mechanisms. |
| 3 | [Stimulus Storage and Selection](Systems/03-Stimulus-Storage-and-Selection/README.md) | Stimulus holding, loading and selection, including dedicated movement for presenting chosen stimuli. |
| 4 | [Valves and Sound Attenuation](Systems/04-Valves-and-Sound-Attenuation/README.md) | Valves, their dedicated drivers and the enclosure that attenuates sound from noisy valve equipment. |
| 5 | [Vacuum, Gas and Drainage](Systems/05-Vacuum-Gas-and-Drainage/README.md) | Vacuum, gas, rinse, drainage and related fluid removal interfaces. |
| 6 | [Shared Structure and General Motion](Systems/06-Shared-Structure-and-Motion/README.md) | Shared-purpose framing, generic movement and mechanical fixtures not dedicated to another functional system. |
| 7 | [Experimental Control, Sensing and Data](Systems/07-Experimental-Control-Sensing-and-Data/README.md) | Experiment-wide controls, behavioral sensing, calibration, session logic and experimental data handling. |

## Status and provenance

The master inventory currently registers **112 imported manufacturing files (71 STL and 41 3MF)** copied unchanged from the earlier [three-port source repository](https://github.com/neuroMoth/3-Port-4-Bottle-Rig). Each row preserves its old name and location, original source path and content identifier. They have **not** been verified for physical compatibility with the present two-port rig. A copied source file is not evidence of an approved, installed or tested component.

Other repository areas are prepared for future verified content. An explanatory page or empty placeholder does not establish that a design, procedure, controller or test record exists.

Source authorship and licensing must be respected. See the [original source license](https://github.com/neuroMoth/3-Port-4-Bottle-Rig/blob/main/LICENSE) and the preserved imported notice. No license for all materials in this repository is inferred from source-file inclusion.
