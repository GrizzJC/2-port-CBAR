# Source revisions, Git changes and physical verification

Source-system saves (SolidWorks/Fusion), GitHub commits and tested physical manufacturing runs are separate kinds of history. Git cannot see local edits that were not committed; a file's last commit date is not its last print or laboratory-use date.

Keep the same stable ID for updates to the same design or prepared 3MF job. Create new IDs for new independent parts, newly split/merged parts and distinct alternate jobs that coexist. Use the [naming and change rules](../NAMING-AND-FILE-RULES.md).

Approval is tied to the tested geometry, print process and intended application. An approved file that changes significantly is not automatically approved again. Use Revision Pending when a known replacement or major correction is being developed locally.

Record the current status, source references, documented test outcome and last actual use in [inventory.csv](../../inventory.csv). Do not maintain a parallel manual revision ledger repeating Git history.
