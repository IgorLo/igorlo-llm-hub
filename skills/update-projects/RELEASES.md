# Coordinated package and consumer releases

Use this branch when the requested consumer behavior requires a change in a shared package. Apply the producer's contribution and release contracts and each consumer's local workflow. Carry forward the session's authorization per repository and action. Distinguish PR preparation, merge, package publication and application deployment in the run record.

## Establish the dependency

Build the [responsibility map](../../profiles/repositories.md#trace-ownership-and-consumers) for the selected targets. Locate the smallest owner of the behavior and record the required capability or fix, producer base and consumer acceptance checks. Use [file-issue](../file-issue/SKILL.md) when a report to another owner is needed. Apply the release-review and verification steps in [update-projects](SKILL.md) throughout this branch.

Check the registry, release metadata and the actual published artifact for the required behavior. Record its version, integrity or equivalent artifact identity, and the source release when available. An existing `latest` version may predate the required fix. Name the exact missing capability and producer change in that case. Recheck the registry before preparing a duplicate release.

## Producer and release candidate

Prepare or reuse the producer PR under its maintenance and release process. Verify its built or packed artifact in a real consumer, including the affected interaction and the producer's required visual approval. Record the candidate source SHA and test artifact identity separately from the registry version.

Consumers can prepare compatible migrations against the candidate in isolated checkouts. Keep registry-based manifests and lockfiles consistent with an available published version at handoff. Report candidate validation and readiness for the published dependency separately. Continue independent targets while a producer step awaits review, access or release.

## Published version and consumer migration

When package publication is authorized, follow the producer's release procedure and version policy. Wait for registry availability and inspect the published artifact for the required behavior. If publication needs an owner action, report that concrete step with the reviewed PR and candidate evidence.

After publication, update each affected consumer with its own package manager, read every intervening release as required by update-projects, and perform a clean install. Rerun the applicable checks and the affected user journey on the actual installed artifact. Verify the latest PR head and its preview. Reconcile every frozen target and any newly found consumer with the requested scope.

When merge or production deployment is authorized, follow each project's integration and release path. Refresh Git at these boundaries, verify the resulting SHA, monitor its CI and deployment, then exercise the live application. Report a failed or protected deployment with its evidence and recoverable next action. Use [testing acceptance](../../profiles/testing.md#browser-acceptance) for the browser checks.

## Handoff

| Target | Required behavior | Producer PR / candidate SHA | Published artifact | Consumer PR / head | Checks and preview | Release state / next action |
| --- | --- | --- | --- | --- | --- | --- |

Use concrete states such as producer review, waiting for publication, registry verified, consumer migration, verified PR and production verified. Include evidence for the state and the next owner action. A released package and an app deployment can have different states within the same run.
