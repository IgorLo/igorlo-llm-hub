# Shared engineering conventions

For every change, identify the user-visible need, the owner of the behavior and other places affected by the same cause. Scale the investigation to the change. Surface a broader fix for decision when it would expand the agreed scope.

Apply the project's local contracts, commands and release policy. Read only the routes that match the task, at the same hub revision.

| Trigger | Read |
| --- | --- |
| Start a frontend application or explicitly migrate its stack | [Frontend profile](profiles/frontend.md) |
| Change behavior, fix a regression, set up CI or assess coverage | [Testing profile](profiles/testing.md) |
| Select a specialist skill for Svelte, UI, testing or verification | [Upstream skills](skills/catalog.md) |
| Report a defect or request a capability from its owner | [File an issue](skills/file-issue/SKILL.md) |
| Evaluate, implement or close incoming feedback | [Handle an issue](skills/handle-issue/SKILL.md) |
| Update dependencies in a project or across maintained repositories | [Coordinate updates](skills/update-projects/SKILL.md) |
| A local decision looks reusable, or an existing convention needs revision | [Propose a convention](skills/propose-convention/SKILL.md) |

Changes to this hub take effect after Igor reviews and merges the PR. Keep private research and deployment details local.
