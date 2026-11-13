# Shared instruction audit

Use this profile when connecting a project, consolidating repeated guidance or reviewing shared and local instructions. Use [writing for agents](../skills/catalog.md#agent-instructions) for the resulting text.

Read the selected repositories' `AGENTS.md`, `CLAUDE.md`, linked agent docs and applicable installed skills. Follow only the links relevant to the proposed consolidation. Compare the actual wording and the executable configuration behind each candidate. Keep the inventory private when it includes local paths or private projects.

| Material | Disposition |
| --- | --- |
| Shared policy | Compare with the approved Hub rule and propose one authoritative home. |
| Duplicate wording | Diff the copies and preserve their callers, useful behavior and exceptions before replacing them with a pointer. |
| Project contract | Keep its commands, domain constraints and release policy with the project. |
| Installed upstream skill | Reuse its installed or reviewed source through the [catalog](../skills/catalog.md). |
| Local variation | Establish whether it is an intentional exception or a candidate for shared review. |

The approved rule and the project's contract determine the intended behavior. Modification dates help investigate history. Record a conflict for decision when its resolution would change that behavior. A pointer names the source and its trigger, and is tested from the callers it replaces.

Return one row per candidate with its current source, semantic difference, proposed home, affected callers and verification. Apply changes already authorized in the task. Use [propose-convention](../skills/propose-convention/SKILL.md) for changes to shared policy and its proposal queue for unresolved generality. Keep agreed local instructions effective while the Hub change awaits review.

For client adapters, verify the installed client's loading rules. Codex and Claude Code can load different instruction chains and skill locations. Use one authoritative body with a tested pointer or import where supported. [OpenAI instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md) · [OpenAI skills](https://learn.chatgpt.com/docs/build-skills) · [Claude Code memory](https://code.claude.com/docs/en/memory)
