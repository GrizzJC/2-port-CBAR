# Seven functional systems — directory index

**This is a navigation page, not an eighth system.** There are exactly **seven** numbered system folders. Open one to find the physical subgroups and their files.

## Open a system

| # | Functional system | Actual printing files | What it covers |
| --- | --- | ---: | --- |
| 01 | [Behavioral Chamber and Animal Interface](01-Behavioral-Chamber/README.md) | 20 | Contains and positions the rat, including the animal-facing access geometry. |
| 02 | [Stimulus Presentation and Access](02-Stimulus-Presentation-and-Access/README.md) | 28 | Presents the selected stimulus through the spouts and controls access to those ports. |
| 03 | [Stimulus Storage and Selection](03-Stimulus-Storage-and-Selection/README.md) | 18 | Holds and selects the intended stimulus, including storage, loading and dedicated positioning. |
| 04 | [Valves and Sound Attenuation](04-Valves-and-Sound-Attenuation/README.md) | 11 | Operates the valves and reduces sound from noisy valve equipment, not from the entire animal rig. |
| 05 | [Vacuum, Gas and Drainage](05-Vacuum-Gas-and-Drainage/README.md) | 29 | Provides vacuum and gas connections plus rinse and drainage equipment. |
| 06 | [Shared Structure and General Motion](06-Shared-Structure-and-Motion/README.md) | 0 | Covers shared supports and general-purpose mechanical hardware not dedicated to another system. |
| 07 | [Experimental Control, Sensing and Data](07-Experimental-Control-Sensing-and-Data/README.md) | 6 | Coordinates trials, collects responses and provides experiment-wide control, calibration and data handling. |

## Read a folder correctly

```text
Systems/                          ← ONLY the seven major functions
  01-Behavioral-Chamber/          ← ONE functional system
    README.md                     ← explanatory page, NOT a model
    01-Cage-Structure/            ← ONE subgroup / related assembly
      README.md                   ← subgroup explanation
      3D-Printing/                ← ACTUAL .stl and .3mf files
    CNC/                          ← PLACEHOLDER for CNC work
    Software/                     ← PLACEHOLDER for code
    Electronics/                  ← PLACEHOLDER for circuit designs
    Visuals-and-Schematics/       ← PLACEHOLDER for images and drawings
```

Other system folders follow the same pattern. **There is no second set of systems elsewhere.** The top-level [Setup-and-Operation manual](../Setup-and-Operation/README.md) is for whole-rig instructions, while the [master inventory](../inventory.csv) gives actual file locations.

A component that serves two systems has **one authoritative file** and links from the other system's documentation. Classify by the assembly the component was specifically designed to support. Shared-purpose mechanics belong to system 06. [Full classification and naming rules](../Documentation/NAMING-AND-FILE-RULES.md).
