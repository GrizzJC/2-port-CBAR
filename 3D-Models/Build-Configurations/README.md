# Rig Build Configurations

A build configuration records the exact **installed, validated or proposed combination** of component and assembly revisions for one equipment configuration. It does **not** change individual part identifiers.

## Fields to record

- Rig/build designation, date and physical equipment location/identifier
- Number of access ports; actuator mechanism for each port
- Reservoir module layout and current number of bottles
- Position-selection mapping, motor home reference and limits
- Component and assembly IDs, **specific revisions and quantities**
- Mating/compatibility restrictions and supporting drawings
- CAD source revisions, Git commit or release reference
- Print/installation/functional checks and who verified them

The present working configuration uses two access ports, two bottle assemblies of two bottles each, and two experimental selection positions plus HOME. These details can change with a future build while the component's stable identifier remains intact.

Actual configuration records should be indexed in [build-configurations.csv](../../tracking/build-configurations.csv). Do not mark a configuration tested solely because the CAD or spreadsheet entries exist.
