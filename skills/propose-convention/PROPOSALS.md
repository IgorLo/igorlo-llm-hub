# Hub convention proposals

A `proposal` records a reusable question whose evidence or scope is not ready for a shared rule. The issue is a decision record, not approval to implement the idea.

## Capture

1. Search open and closed issues and PRs in `IgorLo/igorlo-llm-hub` by the underlying cause and proposed decision. Read earlier dispositions. Link a matching proposal or pending PR when it already covers the case. Prepare an evidence comment only when it changes the decision; publish it under existing task authorization or the [issue approval process](../file-issue/SKILL.md).
2. Prefer a project-local correction when the behavior belongs to one product. For a plausible shared question, prepare a public-safe issue with the fields below. State observations, hypotheses and missing evidence separately. Exclude raw session logs, private paths, customer data, credentials and internal deployment details.
3. Once Igor has approved and merged this policy into Hub main, an agent may open a sanitized Hub `proposal` issue without per-draft approval, subject to stricter instructions for the current task. This permission covers creating that issue, not comments on existing reports, implementing a convention, posting to other repositories or merging. While the policy is a draft, show the complete issue and destination and get Igor's approval before posting, as required by the existing [issue approval process](../file-issue/SKILL.md).
4. Use the `proposal` label, creating it in this repository if absent when authorized posting begins (description: "Shared convention awaiting evidence or owner decision"). Recheck before retrying a failed submission and return the URL. Capture one issue per underlying question; there is no quota. If evidence cannot be safely shared, keep the draft local and ask Igor how to proceed.

Issue body:

```markdown
## Question
What agent decision might need to change, and who would benefit?

## Evidence
Observed behavior and its impact, affected revision/project type, public sources,
related proposals or PRs. Distinguish inference from observation.

## Uncertainty
What is missing? Where could the proposal produce a poor result?

## Next evidence
The cheapest useful investigation and the observation that would support or
reject the idea. State a concrete revisit trigger.
```

## Review

Run this branch when Igor asks to review proposals, including through reflect-session. Read the latest discussion, linked changes and current approved rule. Review each selected issue with an evidence-based recommendation. Igor's decision or an already-authorized disposition governs changes to its status.

| Disposition | Record and completion |
| --- | --- |
| Accept | Define the scope and acceptance check; use propose-convention for the exact wording and authorized PR. Keep open until Igor merges the linked change and its checks pass, then close with that evidence. |
| Need evidence | Keep open with the missing observation and a specific revisit trigger; the existing `question` label may help. Age alone does not decide the proposal. |
| Duplicate | Link the canonical issue or PR, carry over new evidence if authorized, and close as duplicate. |
| Decline | Record the reason, applicability boundary and what evidence could change it; close without turning the idea into a rule. |
| Already covered | Link the approved rule or merged change and verify the cited behavior before closing. |

The issue retains the decision history and `proposal` label. Review happens on request or within an existing authorized triage session; no new recurring schedule is implied.
