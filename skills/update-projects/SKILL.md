---
name: update-projects
description: Coordinate a requested dependency update across supported projects or named repositories and return verified PRs and previews for owner review.
---

# Update supported projects

## Establish the run

Use the hub revision resolved for this task. For a fleet run, read the allowed GitHub owners from the private, comma-separated environment setting `IGORLO_HUB_OWNERS`. Enrollment requires the repository topic `igorlo-hub-managed`. Set that topic during owner-approved onboarding. Keep owner lists, snapshots and results containing private project names outside the public hub.

Run `python skills/update-projects/discover.py` from the hub checkout with authenticated GitHub CLI access. On later runs pass `--previous <private-snapshot.json>` using the last accepted roster. The helper checks the authenticated account, queries every configured owner, paginates topic results and excludes archived projects. For an explicit single-project request, use the named target. Freeze the visible roster at run start.

Report the account, owners, newly discovered targets, missing previous targets and owner errors. An account can see only its granted repositories. On first use, identify this as the first visible inventory. Investigate a missing project (access, archival, rename, removal of topic) and distinguish confirmed unenrollment from lost visibility. A failed owner search or unresolved disappearance makes discovery incomplete. Continue with verified targets. Store the accepted JSON roster privately for the next run, preserving the previous baseline while any disappearance remains unexplained.

## Dispatch independent repositories

Use [parallel dispatch](../catalog.md#parallel-updates) to assign one worker per repository with an isolated checkout, repository URL, run revision and the following contract. Bound concurrency to available workers. For coordinated library and consumer migrations, record the dependency and sequence the steps requiring a released version. Complete independent upgrades while waiting.

1. Read project instructions, CI, lockfile, package-manager and runtime settings. Identify the integration branch, production branch and all push, PR, tag and release deployment triggers before pushing. Use a branch with an allowed preview. If a push would publish to production or the behavior is unknown, keep the change local and report the specific decision needed.
2. Record the base SHA and run the project's baseline checks. Identify existing update PRs, including bot PRs. For Dependabot use the [Dependabot skill](../catalog.md#dependabot-updates). Reuse matching work where writable and use the project's normal update tools. Group compatible patch/minor packages that upgrade together. Put each major migration or tightly coupled major group in a separate PR. Capture any unrelated baseline failure and changes required for compatibility.
3. Read the upstream changelog for every release between the locked and target versions. Fill gaps from release notes, merged PR descriptions or commits between the release tags. Trace breaking changes, deprecations, changed defaults, fixes and new opt-ins to actual consumer code and user flows. Apply required migrations and adopt features that serve an existing product requirement. Record a reason for deferring a relevant change and surface product decisions that expand scope. If release evidence is incomplete, identify the gap in the PR.
4. Update the manifest and lockfile with the project's package manager. Perform a clean install. Run the project's format, lint, architecture, type, unit, coverage, build, browser and package checks as applicable. Follow the hub [testing profile](../../profiles/testing.md). Record absent coverage as unavailable and preserve test and coverage gates. A lockfile-only PR still runs the full project checks.
   For each adopted user-facing change, exercise the affected behavior in the built consumer. For example, when a design system adds themed scrollbars, find the elements that actually scroll, including the document, nested panes and component-owned overlays. Check their rendered styling and operate them on desktop and narrow touch screens. Track any surface that needs a producer release.
5. Open or update the PR against the project's integration branch. In its description, link the release evidence and summarize the consumer impact, adoption decisions and verification. Monitor remote checks and fix recoverable failures. Obtain the latest PR head SHA and confirm required checks and the hosting deployment correspond to it (or identify a CI test merge that includes it). On a new head, refresh the evidence. For a site, use [preview checks](../catalog.md#preview-checks) to open the preview for that SHA and exercise the primary scenario on narrow touch and desktop viewports. For a library, verify the packed artifact in a consumer and include a demo preview when available. Report protected or failed previews explicitly.
6. Return one result per PR, plus a row for every repository with no changes or a blocker. Include update group, head SHA, PR, CI link, tests/coverage outcome, preview URL or package-consumption evidence and a concrete manual review target. Mark a PR ready only after applicable checks and preview/consumer checks pass. Leave merge, production deployment and package publishing to the owner.

## Present the batch

Reconcile worker results with the frozen roster. Use [verification before completion](../catalog.md#verification) to inspect the current PR head, check runs and preview deployment before presenting links. Summarize discovery gaps separately. Put the preview and PR next to each other so the owner can open both in one pass.

| Project / update | Status | Preview | PR / head | CI and coverage | What to inspect |
| --- | --- | --- | --- | --- | --- |

Use distinct statuses for ready, no updates, failing checks, unavailable access, pending preview and coordinated migrations waiting on a release. A green build alone cannot establish visual readiness.
