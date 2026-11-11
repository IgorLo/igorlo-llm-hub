# Upstream skills

Use the matching entry when its trigger applies. Prefer an installed copy matching the reviewed source. Otherwise read the linked instructions and their required references at the same revision. If a required tool is unavailable, run the equivalent project checks and report the remaining gap. This catalog grants no permission to post, merge or release.

## Svelte components

Write or change Svelte components: use [Svelte code writer](https://github.com/sveltejs/ai-tools/blob/d3e755be770277d8c75fe61109b103b801b12775/packages/opencode/skills/svelte-code-writer/SKILL.md). Match the installed Svelte version and read the installed UI kit's consumer guide.

## Behavioral tests

Add behavior or protect a regression: use [TDD](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/tdd/SKILL.md). Use the public testing boundary and coverage scope in the [testing profile](../profiles/testing.md).

## Interface review

Review layout, touch or accessibility: use [Web design guidelines](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/web-design-guidelines/SKILL.md). Its checklist is fetched from a moving upstream source. Record the checklist revision or retrieval date for a repeatable audit. Test the actual interaction at narrow and wide widths.

## Preview checks

Exercise a running preview: use [Playwright CLI](https://github.com/microsoft/playwright/blob/392ab0f0de39feb99dbe71eb5fea61e7ad07a480/packages/playwright-core/src/tools/skills/playwright-cli/SKILL.md). Run the main user journey on the PR deployment; preserve evidence for failures.

## Parallel updates

Delegate independent repositories: use [Dispatch parallel agents](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/dispatching-parallel-agents/SKILL.md). Use the [fleet workflow](update-projects/SKILL.md) for scope and handoff.

## Dependabot updates

Evaluate existing Dependabot PRs: use [Dependabot](https://github.com/github/awesome-copilot/blob/eaaffd5d020b756a2777a4b1b161d2bdc126d9a0/skills/dependabot/SKILL.md). Reuse compatible open PRs and observe the repository's release permissions.

## Verification

Report that a fix or update passed: use [Verification before completion](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md). Check the actual run and the revision it covered.

## Incoming issues

[Triage](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/triage/SKILL.md). Apply the investigation steps for incoming feedback. The [hub workflow](handle-issue/SKILL.md) defines project ownership, decision history and closure.

## Bug diagnosis

[Diagnosing bugs](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/diagnosing-bugs/SKILL.md). Use when a defect is intermittent, its cause is unclear or performance regresses. Establish a repeatable signal and test competing causes.

## Diff review

[Code review](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/code-review/SKILL.md). When reviewing a fix, supply the issue or agreed brief and the comparison base. Review project standards and requested behavior.

## Agent instructions

[Writing for agents](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/writing-for-agents/SKILL.md). Use when editing a skill, a routing instruction or a convention that an agent reads.

## Catalog changes

For a catalog change, inspect the actual skill, linked instructions and tools. Prefer the framework maintainer or an established repository with at least 100 stars. Record the reviewed commit and the local gap. Reuse a matching procedure by reference. Route a proposed new skill or revision through [owner review](propose-convention/SKILL.md).
