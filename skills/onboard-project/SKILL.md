---
name: onboard-project
description: Connect a named repository to Hub conventions and fleet maintenance, or diagnose an expected project missing from the managed roster.
---

# Connect a project

Use the task's approved Hub revision. Establish the requested repository and whether the request covers shared instructions, fleet enrollment or both. Carry forward existing authorization. Report each part separately when access or a pending PR leaves onboarding incomplete.

## Inspect and connect

1. Verify the canonical repository, visibility, archive state and access. Read its local instructions, integration and production branches, package and runtime settings, CI and release triggers. Locate a checkout through [repository navigation](../../profiles/repositories.md). Apply [Git freshness](../../profiles/git.md) before edits. Preserve local work and use a task branch or worktree.
2. For requested shared-instruction setup, audit the applicable instructions with the [shared instruction profile](../../profiles/instructions.md). Add the exact [client pointer](../../clients/instruction.md) to the appropriate project instruction file, preserving local contracts and avoiding repeated copies in that file. Review a client adapter only where the installed client needs one. Read a UI dependency's installed consumer guide when its ownership rules apply. Propose shared policy through [propose-convention](../propose-convention/SKILL.md).
3. For requested fleet enrollment, add `igorlo-hub-managed` while preserving existing topics. Use the private owners configuration from [update-projects](../update-projects/SKILL.md#establish-the-run). Apply the user's existing enrollment authorization to the named targets. If enabling a new owner would expand the fleet beyond those targets, surface that additional scope for decision. Keep the allowlist, workspace map and roster private. A topic update can succeed while the instruction PR is pending, so retain that state in the result.
4. For fleet enrollment or a missing-roster diagnosis, rerun discovery with the last accepted private snapshot and reconcile the named target, canonical name, additions, missing entries and owner errors. Search a missing target directly for topic absence, rename, archival or visibility loss. Keep the prior baseline until the snapshot meets the acceptance rules in update-projects. Account for the expected target even if the generic topic search omitted it. An instruction-only request uses the explicit target directly.
5. For changed project instructions, open or update the instruction PR under the project's rules. Run checks appropriate to the changed files and confirm local links. Preserve the existing stack and quality gates. Record the integration base, PR head and which instruction version the entry-point checks exercised.

## Verify the entry points

For shared-instruction setup, exercise a fresh client context from the Hub, the target repository and a task worktree when used. In each case ask the agent to identify the Hub SHA, local instruction sources and the workflow for one representative task. Check the answer against the actual files. A routed skill can be read through its explicit pointer. Verify automatic selection separately if installation or a symlink is part of the setup.

If a client or entry point is unavailable, record the unverified case and the exact check to run. With offline access, use the fallback in [client instructions](../../clients/instruction.md). Keep the same Hub revision across the checks. Refresh the application base at the boundaries in the Git profile.

Return the topic state, discovery result, instruction PR, optional workspace-map update and each client check as applicable to the request. Distinguish connected, pending instruction merge, incomplete discovery and unverified client delivery. Onboarding is complete when the requested enrollment is discoverable and, for instruction setup, the applicable instruction change is integrated and its entry-point checks pass. Resume from the remaining step on a retry.
