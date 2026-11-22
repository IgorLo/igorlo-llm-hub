# Agent workflows

Choose the workflow from the cost of a missed issue, the available checks and the dependencies between pieces of work. One lead owns the result and revisits the choice when the scope, risk or dependencies change.

## Task readiness

When drafting or picking up an engineering task, use its issue, brief or current chat to capture the problem or purpose, expected outcome and an observable acceptance check. Add relevant evidence, sources of truth and constraints. Record blockers or assumptions when they could change the result. For a clear, small request, the request and its check can serve as the brief.

Before implementing or delegating implementation, confirm the expected outcome, scope and acceptance check for that work. Consult the relevant code, tests, issue history or project contracts to resolve missing facts. If a decision about behavior, scope or a costly trade-off remains, ask the owner a specific question and record the answer in the task before proceeding with dependent work. State any reversible assumption you make.

Start or delegate discovery when you can name the question, bound the investigation and say what evidence or decision it must return. Keep verified facts, hypotheses and open questions distinct. Update the task and recheck readiness when findings change the expected outcome, scope or acceptance check.

| Situation | Workflow |
| --- | --- |
| The behavior and its checks are clear, or the changes depend on one another | One implementer runs the project checks and self-reviews the result. |
| A consequential assumption remains open after an available direct check | Give an independent critic that assumption and ask for a concrete counterexample. Review the plan before edits if the answer would change the approach. Review the candidate if the question concerns the implementation. |
| The expected behavior is established and a weak check could hide a consequential mistake | Consider a separate test author for that behavior. Give them the source of the expectation, the public entry point and the base revision. For a regression, confirm that the test fails on the base for the expected reason before handing it off. Check the fix and neighboring behavior under the [testing profile](testing.md). |
| Work has stable inputs and separate acceptance checks | Run independent investigations or implementation slices in parallel. Sequence work that depends on a shared contract, another slice or a published artifact. Use [repository ownership](repositories.md) and the [fleet workflow](../skills/update-projects/SKILL.md) where applicable. |

## Review neighboring behavior

For a behavior or contract change, exercise the main scenario and a materially affected neighbor when one shares the cause. Trace the real entry points and consumers. Examples include a saved preset after a default changes, keyboard input after a pointer fix, and a consuming application after a library update. If the evidence favors a common fix, identify its owner, the affected callers and any expansion of the agreed scope.

Give the critic a fresh context with the original requirement, applicable contracts, the plan or diff and the specific risk. Ask for the scenario, supporting evidence and a way to verify it. Give an independent validator the agreed behavior and the exact candidate revision to check. Combine review and validation in one agent when both can be done well in one pass. The lead confirms findings and checks the required verification on the integrated revision. Follow the [review](../skills/catalog.md#diff-review) and [verification](../skills/catalog.md#verification) procedures.

## Coordinate multi-stage work

Use this workflow when multiple user journeys share a contract, contributors need to work across milestones, or revisiting prior decisions would make a long task difficult to resume.

1. **Define the first end-to-end slice.** The lead records the user journey, observable acceptance checks, owners of shared interfaces and open decisions. Delegate focused discovery when useful, such as tracing existing UI kit capabilities or checking how consumers rely on a shared API. Each investigation returns evidence and the decision it informs. Use a design critic before implementation if a disputed assumption affects several slices or would be expensive to reverse.
2. **Prove the shared boundaries.** Build a thin slice through the real entry points and check it before splitting work that relies on its interfaces. For a frontend, this can be one primary journey from navigation through a domain action to visible success and failure states. Apply the [frontend profile](frontend.md) and its browser checks. Assign a test author for a critical behavior with a stable expected result when the sequence above warrants it.
3. **Assign and integrate slices.** Give each worker the requirement, pinned Hub and base revisions, applicable local rules, owned paths and acceptance checks. Use isolated checkouts for concurrent edits and one owner for each shared contract. Each worker returns the change or tested SHA, verification evidence and unresolved issues. The lead exercises the integrated journey before calling a milestone complete. Use an independent validator for a high-impact scenario that crosses slice boundaries, such as preserving user state through navigation, retry and refresh.
4. **Keep a handoff across milestones.** Use the task's existing notes or one shared working note for decisions, slice owners and dependencies, open risks and evidence tied to commits. Refresh relevant revisions under [Git freshness](git.md) when resuming. Supply the current handoff and the relevant local contracts to a fresh agent so it can pick up work with a bounded context.

## Choose models by role

Use project commands for objective checks. Use a fast model for bounded discovery and evidence collection, a general-purpose model for implementation and tests against clear contracts, and a stronger model with higher reasoning effort for ambiguous architecture, high-impact critique, difficult test design and integration across contracts. Choose from the models available in the client. When separate agents are unavailable, give the lead a focused second pass and report which checks it performed.
