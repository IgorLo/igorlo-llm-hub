---
name: file-issue
description: Prepare a new issue or contribute evidence to an existing report when a project or dependency cannot meet a user need.
---

# File an issue

For creating a Hub convention proposal after adoption of its policy, use the separate [proposal workflow](../propose-convention/PROPOSALS.md). Until adoption, and for evidence comments without existing task authorization, use the approval steps below. Defects and capability requests also follow these steps.

1. Identify the user task, the owning repository and the exact affected revision or package version. Use [repository ownership](../../profiles/repositories.md#trace-ownership-and-consumers) when the cause crosses project boundaries. Read that version's contract and the target repository's issue template. For Svelte ASCII UI, use the installed package's `docs/agents/using.md` and its feedback guide.
2. Search open and closed issues using the symptom and the affected API. Compare likely matches. If a report covers the same behavior, link it and propose a comment only when there is new evidence. If search is unavailable, record that limitation.
3. Reproduce the defect through the smallest public interface. For a capability request, demonstrate the task and the limitation of the available options. Isolate application configuration from shared behavior. For intermittent failures or an unclear cause, use [bug diagnosis](../catalog.md#bug-diagnosis). Mark observations, suspected causes and unknowns distinctly.
4. Show the complete draft and destination to the user. Use the repository's language. Include a searchable title, user impact, expected and observed behavior, revision, reproduction, checks for acceptance and related reports. Add environment details, variants, workaround and attachments where they affect the diagnosis. Use examples cleared for the destination's audience.
5. Publish when the user has approved this draft and destination. If substantive content or destination changes, show the revised draft for review. Recheck the tracker before retrying a failed submission. Return the resulting URL, or return the complete draft with the reason submission is pending.
