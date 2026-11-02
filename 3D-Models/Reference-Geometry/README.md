# Reference Geometry

This area holds CAD used **for design context**, not necessarily components manufactured by the laboratory.

Typical sources: externally obtained motor and actuator CAD models, valve dimensions, bottles/reservoirs, bearings, fasteners, sensors, tubing and supplier mounting envelopes.

## Folder convention

```text
Reference-Geometry/
  <supplier-or-item>/
    README.md
    source/
```

Record supplier, product/model number, source URL, date obtained, file type, units, source-version information, license/reuse permissions, and whether the measurements match actual purchased parts. Use the [reference registry](../../tracking/reference-geometry.csv).

Reference geometry is **not proof of an installed component**. A modified reference that becomes a lab-manufactured part is a new controlled component with a link back to the reference.
