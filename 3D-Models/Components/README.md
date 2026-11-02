# Components

Each component is one independently identifiable **physical part design**. Its folder groups the readable record, editable source information and any exports of that same design.

Suggested structure:

```text
SS-NNN/
  README.md
  source/
  exports/
```

Use the [component record template](../../Documentation/templates/component-record.md). Document where the part connects, which source file produces its exports, the revision and the validation status.

Do not rename externally referenced SolidWorks or Fusion files without confirming that linked assemblies still resolve correctly. If a filename must remain unchanged, record the stable component identifier in the registry and its documentation.
