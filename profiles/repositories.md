# Repository ownership and navigation

Use this profile to find the owner of a shared behavior or coordinate a change across repositories. Start a product-only task in that product or a multi-repository task in the Hub. Both entry points use the task's pinned Hub revision and each target's local instructions.

## Find the targets

For a fleet request, use the roster and visibility checks in [update-projects](../skills/update-projects/SKILL.md#establish-the-run). An explicitly named repository is a task target even if it is awaiting enrollment. Use [onboard-project](../skills/onboard-project/SKILL.md) when enrollment is requested. Treat references to additional consumers as candidates to investigate and reconcile with the requested scope.

An optional private workspace map can locate existing clones and describe their roles. Read the file named by `IGORLO_HUB_WORKSPACE`, or `workspace.json` beside the run's private roster snapshot when available. Keep it outside tracked Hub files. Use GitHub repository identity as the key and record checkout hints with their evidence date.

```json
{
  "repositories": {
    "owner/library": {
      "path": "/local/code/library",
      "role": "shared-package",
      "checked_at": "YYYY-MM-DD"
    },
    "owner/application": {
      "path": "/local/code/application",
      "role": "application",
      "checked_at": "YYYY-MM-DD"
    }
  }
}
```

Verify the checkout's Git root and canonical remote before using it. Follow [Git freshness](git.md) for its branch and base. Reuse a verified clone and create a task worktree when isolation is needed. A missing clone can be created in the permitted workspace. Preserve existing local work. Reconcile renamed repositories and stale paths in the private map.

## Trace ownership and consumers

Read the target's `AGENTS.md` and its linked local contracts before assigning work. In a new worker, supply the repository identity, isolated checkout, base SHA, pinned Hub SHA, relevant local instructions, acceptance check and existing authorization for PRs and releases. Verify instruction delivery as described in [onboarding](../skills/onboard-project/SKILL.md#verify-the-entry-points).

Derive package relationships from the current manifests, lockfiles, registry metadata and installed consumer documentation. Confirm a producer from its package identity and repository metadata. For a UI kit, its public components, tokens and internal scrolling behavior belong to the library. Application composition, domain state and product-specific choices belong to the consumer. Read the installed version's consumer guide to establish the boundary for the actual case.

Record the task's responsibility map privately.

| Repository / base SHA | Owns the behavior | Consumes or publishes | Evidence | Acceptance check |
| --- | --- | --- | --- | --- |

Account for each target and dependent consumer with a disposition and the scope of the investigation. A manifest reference, an inaccessible repository and confirmed unenrollment are distinct findings. Keep discovery gaps visible in the handoff. Use [coordinated releases](../skills/update-projects/RELEASES.md) when a library change needs a new artifact before its consumers can finish.

## Reference behavior

The Hub's explicit links route to shared skills in `skills/`. For automatic skill discovery, use the client's supported installation or skill directory and test it from the intended entry point. Codex documents `.agents/skills`, user-scoped installation and symlink support. Its startup instruction chain covers the active project, so a worker moving to a sibling repository must explicitly read that target's local rules. [OpenAI instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md) · [OpenAI skills](https://learn.chatgpt.com/docs/build-skills) · [Git worktree](https://git-scm.com/docs/git-worktree)
