---
name: handle-issue
description: Triage an incoming issue, implement an agreed disposition, or close a report after verifying its outcome.
---

# Handle an issue

1. Read the issue, all comments, linked reports and the repository's maintenance instructions. Identify the user's objective and the proposed solution separately. For defects, check the reported version and the current integration branch. Record which revisions reproduced the issue and what remains unknown.
2. Trace the behavior to its owner. Inspect the application, public API, documentation and related consumers or components as relevant. Check a representative neighboring case to bound the cause. For a UI-kit report, use the kit's design review and maintenance guides for visual states, accessibility and package checks.
3. Give a disposition per issue with the evidence, owner, proposed scope and acceptance check. Options include a consumer correction, usage guidance, a component fix, a shared change, a duplicate, or a request for specific evidence. For intentional behavior or out-of-scope requests, give the reason and any supported alternative. Follow the repository's decision process. Proceed on an already agreed scope. Seek a decision when a finding materially changes it or when proposing closure without implementation.
4. Implement the agreed response. For a behavioral fix, capture the original failure in a regression check, demonstrate the corrected result and verify affected neighbors. For guidance, exercise the documented path. Link the PR and its checks, and keep separately discovered work visible with its own disposition.
5. For a fix or documentation change, confirm the PR merged into the repository's designated integration branch and that acceptance checks passed before closing. In the issue, link the integrated change and its verification. Distinguish integration, publication or deployment, and consumer retesting using the observed state of each. For an agreed duplicate or refusal, close with the canonical issue or rationale. Honor the separate project workflow for any release.
