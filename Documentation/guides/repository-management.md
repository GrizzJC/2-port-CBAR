# Repository Stewardship and Handoff

The repository is maintained under `GrizzJC/2-port-CBAR`. Its project name and directory structure are intended to remain suitable even if the experimental hardware changes.

## Maintenance practices

- Maintain a single authoritative `main` branch for the working organization.
- Preserve Git commits for reproducibility; avoid deleting established history and force-pushing changes unless a maintenance incident requires it.
- Organize **CAD source design** in the appropriate original engineering environment and use GitHub for the auditable record of approved or useful snapshots.
- Keep file identifiers, source provenance, derivative export links, print/test outcomes and equipment configurations in the [tracking directory](../../tracking/README.md).
- Protect experimental/animal-related data and identifiable or sensitive material according to laboratory policy. A public repository should not become the default location for research records containing sensitive information.
- Preserve third-party author attribution and license obligations. **Public is not the same as open licensed.**

## Repository ownership transfer

GitHub supports transferring a repository to another personal account or organization when the destination owner accepts it and the transfer satisfies GitHub's prerequisites. A transfer retains the repository's Git history, branches, issues and pull requests. Redirects usually preserve old repository URLs, but systems using the original namespace should still be checked.

When laboratory stewardship passes to **Tim's `neuroMoth` account**, the existing repository may be transferred instead of copied as a fresh repository. Before doing so, confirm the destination name is available, verify Tim can receive and administer the project, check linked integrations/permissions and make sure the correct source files, licenses and institutional ownership are documented.

Reference: https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository

## Inventory upkeep

The [FILE-ORGANIZATION.md](../../FILE-ORGANIZATION.md) page is the human-readable entry point. The [repository-file-index.csv](../../tracking/repository-file-index.csv) lists every tracked file at the time of its last regeneration. Update this index when repository content changes.

The asset registry records **controlled objects**, and is not replaced by the repository-path catalog. A CSV row per Markdown page is not the same as a registry entry per physical component.
