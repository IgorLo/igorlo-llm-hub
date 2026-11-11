# Upstream skills

Use the matching entry when its trigger applies. Prefer an installed copy matching the reviewed source. Otherwise read the linked instructions and their required references at the same revision. If a required tool is unavailable, run the equivalent project checks and report the remaining gap. This catalog grants no permission to post, merge or release.

| Trigger | Reviewed source | Project-specific application |
| --- | --- | --- |
| Write or change Svelte components | [Svelte code writer](https://github.com/sveltejs/ai-tools/blob/d3e755be770277d8c75fe61109b103b801b12775/packages/opencode/skills/svelte-code-writer/SKILL.md) | Match the installed Svelte version and read the installed UI kit's consumer guide. |
| Add behavior or protect a regression | [TDD](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/tdd/SKILL.md) | Use the public testing boundary and coverage scope in the [testing profile](../profiles/testing.md). |
| Review layout, touch or accessibility | [Web design guidelines](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/web-design-guidelines/SKILL.md) | Its checklist is fetched from a moving upstream source. Record the checklist revision or retrieval date for a repeatable audit. Test the actual interaction at narrow and wide widths. |
| Exercise a running preview | [Playwright CLI](https://github.com/microsoft/playwright/blob/392ab0f0de39feb99dbe71eb5fea61e7ad07a480/packages/playwright-core/src/tools/skills/playwright-cli/SKILL.md) | Run the main user journey on the PR deployment; preserve evidence for failures. |
| Delegate independent repositories | [Dispatch parallel agents](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/dispatching-parallel-agents/SKILL.md) | Use the [fleet workflow](update-projects/SKILL.md) for scope and handoff. |
| Evaluate existing Dependabot PRs | [Dependabot](https://github.com/github/awesome-copilot/blob/eaaffd5d020b756a2777a4b1b161d2bdc126d9a0/skills/dependabot/SKILL.md) | Reuse compatible open PRs and observe the repository's release permissions. |
| Report that a fix or update passed | [Verification before completion](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md) | Check the actual run and the revision it covered. |

For a catalog change, inspect the actual skill, linked instructions and tools. Prefer the framework maintainer or an established repository with at least 100 stars. Record the reviewed commit and the local gap. Reuse a matching procedure by reference. Route a proposed new skill or revision through [owner review](propose-convention/SKILL.md).
