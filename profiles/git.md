# Git freshness

Use the project's designated integration branch and remote. Establish them from its contract, upstream and history. Keep the Hub revision pinned for the task; refreshing application history does not change that revision.

## Before editing

Fetch the relevant remote before the first edit. Inspect the working tree, current branch, upstream and fetched integration SHA. Compare ancestry: equal, ahead, behind or diverged. A cached remote-tracking ref alone does not establish freshness.

- For new work, branch from the fetched integration commit, preserving existing work separately.
- For continued work, integrate missing changes using the project's merge/rebase policy before editing affected paths. Use a fast-forward where possible. Preserve local and other agents' changes; shared branches retain their published history.
- If the requested behavior appears absent, check relevant recent remote changes before implementing it again or diagnosing the installed dependency. After integration, reconcile the lockfile/installed package and reread the matching contract.

Completion: the task's starting base is known, relevant missing changes are integrated, and the disposition of any remaining divergence or local work is explicit. If integration needs an owner decision, continue only work independent of that decision.

## Refresh at boundaries

Fetch and reassess before resuming after a pause/context switch, after news of parallel changes, and before publishing a PR, merging or releasing. Incorporate an advanced base using the same policy and verify the resulting tree; earlier checks prove the earlier tree. Record the reviewed/tested SHA when handing work over.

Choose these boundaries rather than a fixed polling interval. A fetch updates knowledge; merge/rebase happens at a safe working boundary. If the task explicitly targets a historical revision or maintained release branch, use that target and record the exception rather than moving it to current main.

If the remote is unavailable, record the last known SHA and unverified freshness. Continue useful local work within the agreed scope and recheck before a network-dependent integration or release.
