# Functional system map

This is a **navigation index** for physical design responsibilities. Actual controlled CAD sources and manufacturing exports belong under the permanent-ID paths in [Components](../Components/README.md) or [Assemblies](../Assemblies/README.md).

A system page can link to a component used in more than one area without duplicating the file or changing its ID. The names below are descriptive and **are not an allocation of two-digit subsystem codes**.

| System | Typical 3D designs |
| --- | --- |
| [Animal chamber and access face](Animal-Chamber-and-Access-Face/README.md) | Chamber shells, animal-facing panels, removable lids, trays, approach openings, alignment guides and brackets that establish animal-facing geometry. |
| [Structural frame and mounts](Structural-Frame-and-Mounts/README.md) | Machine bases, towers, supports, rods, rails, mounting brackets, stand-offs, vibration isolation mounts and cross-assembly fasteners. |
| [Port doors and actuators](Port-Doors-and-Actuators/README.md) | Two port doors or shutters, guides, actuator clamps, hinges, rails, latches, travel stops and shields. |
| [Bottle and reservoir modules](Bottles-and-Reservoirs/README.md) | Bottle holders, collars, clamps, modular carriers, reservoir adaptors, mounts, service/retention features and changeover guides. |
| [Positioning and motion hardware](Positioning-and-Motion/README.md) | Motor mounts, stepper couplings, moving platforms, carriages, bearings, belts, lead screws, rails, stops, home-sensor brackets and motion guards. |
| [Spouts and stimulus delivery](Spouts-and-Stimulus-Delivery/README.md) | Spout holders, tubes/spacers, tip alignment, delivery brackets, outlet guides, precision connectors and service clips. |
| [Valves and fluid handling](Valves-and-Fluid-Handling/README.md) | Valve mounts, tubing guides, manifolds, fluid connectors, solenoid supports, isolation brackets and service housings. |
| [Pressure and air support](Pressure-and-Air/README.md) | Manifold brackets, regulator mounts, gas/air fittings, pressure-line clips and protective brackets. |
| [Rinse, vacuum and waste](Rinse-Vacuum-and-Waste/README.md) | Waste catch components, drain interfaces, rinse mounts, vacuum fittings, splash guards and liquid removal holders. |
| [Electronics and sensor mounts](Electronics-and-Sensor-Mounts/README.md) | Control board cases, cable-management parts, limit-switch supports, lick-detection sensor mounts, strain relief and cable clamps. |
| [Fixtures, jigs and test tools](Fixtures-Jigs-and-Test-Tools/README.md) | Drill guides, alignment tools, assembly jigs, dimensional gauges, calibration blocks and inspection holders. |

## How to classify a newly received model

1. Identify what physical thing the model represents and whether it is a part, assembly, prepared printing job or supplier reference.
2. Determine its **primary stable function**; record other uses as additional assembly relationships.
3. Verify the editable design source and relationships before assigning any permanent identifier.
4. Link the registered asset and its current approved revision here once verified.

## Applicable task configuration

The rig is for a two-port chemosensory brief-access task, currently using two independently actuated access shutters and a movable stimulus-selection stage. A current configuration includes two two-bottle assemblies. The file IDs must not encode changeable bottle quantity, motor choice or the active hardware configuration.
