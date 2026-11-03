# Functional system map

The **same seven systems** classify 3D printing, CNC work, electronics, software, purchased hardware, procedures and diagrams. A subgroup is a functional assembly or closely related set of equipment, not a file format.

| No. | System | Current subgroups |
| --- | --- | --- |
| 1 | [Behavioral Chamber and Animal Interface](01-Behavioral-Chamber/README.md) | 1. Cage Structure; 2. Cage Alignment; 3. Lid and Locks; 4. Waste Tray; 5. Animal-Facing Panels |
| 2 | [Stimulus Presentation and Access](02-Stimulus-Presentation-and-Access/README.md) | 1. Delivery Frame; 2. Access Doors and Actuators; 3. Spout Bodies and Spacers; 4. Spout Mounts and Clamps; 5. Spout Tools and Alignment |
| 3 | [Stimulus Storage and Selection](03-Stimulus-Storage-and-Selection/README.md) | 1. Bottles and Reservoirs; 2. Syringe and Chromaflex Holders; 3. Loading Frame; 4. Motorized Selection |
| 4 | [Valves and Sound Attenuation](04-Valves-and-Sound-Attenuation/README.md) | 1. Valve Sound Attenuation Chamber; 2. Valve Driver and Hardware; 3. Valve Interfaces and Mounts |
| 5 | [Vacuum, Gas and Drainage](05-Vacuum-Gas-and-Drainage/README.md) | 1. Vacuum and Air Fittings; 2. Gas Supply and Manifolds; 3. Spout Drain Assembly; 4. Rinse and Waste |
| 6 | [Shared Structure and General Motion](06-Shared-Structure-and-Motion/README.md) | 1. Shared Structural Supports; 2. General Motion Hardware; 3. Shared Tools and Fixtures |
| 7 | [Experimental Control, Sensing and Data](07-Experimental-Control-Sensing-and-Data/README.md) | 1. Sensors and Signal Conditioning; 2. Controllers and Wiring; 3. Experimental Software; 4. Calibration and Data; 5. Protocols and Operation |

**Classification rule:** Put a component with the assembly it was specifically designed to support. A dedicated spout bracket belongs with spout hardware even though it is mechanical. Shared-purpose brackets belong to shared structure. Dedicated stimulus-selection controller code belongs to system 3; session-wide protocols belong to system 7. The valve sound attenuation chamber isolates valve noise, not the whole behavioral chamber.

One authoritative file may serve multiple systems. Reference that file in another system's README or a schematic rather than maintaining competing copies. Preserve IDs when a file is later reclassified.

New physical equipment with no digital file should still be described in the relevant system README and, once verified, can be entered in the [master inventory](../inventory.csv).

[See naming and change rules](../Documentation/NAMING-AND-FILE-RULES.md).
