# Manufacturing-file intake, verification and release

1. **Identify source and rights.** Record original filename/path, source, attribution and source version in [inventory.csv](../../inventory.csv).
2. **Classify by purpose.** Choose printing, CNC, software or electronics and one of the [seven systems](../../Systems/README.md). CAD format does not determine purpose.
3. **Check file role.** STL mesh, 3MF prepared printing job (one or several objects), native source, manufacturing instructions or purchased component.
4. **Check dependencies.** Before moving native CAD or code, verify assembly mates, slicer references, MATLAB function names, include paths and external links.
5. **Assign the permanent ID.** Apply [TYPE-S-GNN](../NAMING-AND-FILE-RULES.md) within the chosen system/subgroup; never reuse retired IDs.
6. **Verify actual manufacturing.** Check units, materials, machine compatibility, fit, functioning and any 3MF objects/build settings. A copied file is not automatically suitable for the current rig.
7. **Record outcome and use.** Update verification status, Revision Pending, Rig Status and real dates. Do not invent physical tests or usage.
8. **Release.** Preserve relevant source version, Git commit, author and links. Changes affecting fit or function require revalidation.
