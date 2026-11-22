# Code navigation with Serena

At the start of source-code work in a local Git checkout, check whether Serena can serve that checkout. Prepare it on the first eligible task without waiting for a user reminder. Use [repository ownership](repositories.md) to decide which checkout owns the behavior and [Codex local setup](#codex-local-setup) when the launcher or MCP registration is missing.

## Prepare the checkout

1. **Identify the root and language.** Run `git rev-parse --show-toplevel` and use that absolute path for setup, indexing, and activation. Recheck when switching repositories or worktrees. Use the language servers that cover the affected source. For Svelte and SvelteKit start with `svelte`, which also handles JavaScript and TypeScript in those projects. For standalone TypeScript start with `typescript`. Check the project's toolchain and [Serena's language requirements](https://github.com/oraios/serena/blob/v2.1.0/docs/01-about/020_programming-languages.md).
2. **Keep generated state local.** Use the Serena profile that the client will launch. Prefer its existing external data location when it gives each checkout its own directory. Otherwise use the default `.serena/` in the checkout and check Git exclusions before letting Serena write. For a new, entirely local `.serena/`, add `/.serena/` to the local exclude file reported by `git rev-parse --path-format=absolute --git-path info/exclude`. If the repository already tracks Serena settings, preserve them and exclude the generated cache, logs, and other local state. Use `git ls-files -- .serena` to identify tracked paths and `git check-ignore` to verify generated paths. If generated paths are tracked or a local exclusion cannot be written, use a checkout-specific external location or fall back to ordinary search. [Serena data locations](https://github.com/oraios/serena/blob/v2.1.0/docs/02-usage/050_configuration.md#per-project-serena-folder-location)
3. **Warm the index once.** Reuse an existing prepared project and its cache. If setup is missing, create or register the project using the same launcher and `SERENA_HOME` as the client. For a new Svelte project, for example, run `serena project create --language svelte --name "<unique-project-name>" "<absolute-root>"`. With the language setup in place, run `serena project index "<absolute-root>"` when a successful initial index is not recorded for this checkout. Check the printed file counts and any reported per-file failures as well as the exit status. Record successful preparation in an ignored or external `hub-index.yml` beside the cache, with the checkout path, Serena version, and language servers. Reuse this result across ordinary source edits. Recheck when the cache is lost, the language setup changes, or Serena reports the index unusable. [Project setup and indexing](https://oraios.github.io/serena/02-usage/040_workflow.html#indexing)
4. **Verify before relying on it.** When using Serena, activate the exact checkout path and verify the active project against that path using the activation response or server log. Get the Serena session ID from `initial_instructions` if the activation tool requests one. Run a scoped symbol query against a known source file. For a new setup, also check `git status --short` for generated files. A newly registered MCP may require a fresh client session. Continue with ordinary search in the current task while the server or index is unavailable.

The lead owns setup and verification. If indexing will take time and a subagent can access the same local checkout and Serena state, give that worker the absolute root and the index command. Have it return the file counts and any errors while the lead continues independent work. Check for an index already running on the same checkout and reuse that run. Keep machine settings with the lead.

## Choose the tool for each step

- Use Serena when it helps resolve a definition, distinguish same-named symbols, inspect a large file by symbol, or trace callers through imports and re-exports. Scope queries to a file or directory once you know it.
- Use `rg` and direct reads for literals, configuration, docs, and discovery when a path is unknown. Use them to verify consequential reference lists against the actual source, tests, and dynamic uses. Finish with the project's normal checks.
- If Serena is unavailable, misidentifies the root, times out, or returns partial evidence, use ordinary search and continue. Retry setup when the host or checkout has changed or when there is a concrete fix. Bring up a setup issue with the user when it affects the task outcome.

## Codex local setup

Reuse a working local Serena MCP registration. If one is missing on a supported local host, set it up once in the client's user configuration when the host and task permissions allow. For a fresh installation the reviewed version is `serena-agent==2.1.0`, available with `uv tool install --python 3.13 "serena-agent==2.1.0"`. Resolve the installed executable to an absolute path. Preserve an existing user configuration and follow its supported configuration mechanism. If installation or registration is unavailable, continue with ordinary search.

Use local STDIO and an explicit activation path for each checkout. This sample can be added to the local Codex user config with the machine's executable path. If the user profile sets a custom `SERENA_HOME`, pass the same path to MCP and indexing. A project-scoped registration can instead pass an explicit absolute `--project` for that checkout.

```toml
[mcp_servers.serena]
command = "/absolute/path/to/serena"
args = [
  "start-mcp-server", "--transport", "stdio", "--context", "codex",
  "--agent-interface", "tools", "--language-backend", "LSP",
  "--add-mode", "no-memories", "--enable-web-dashboard", "false",
  "--enable-gui-log-window", "false",
]
startup_timeout_sec = 30
enabled_tools = [
  "initial_instructions", "activate_project", "get_current_config",
  "get_symbols_overview", "find_symbol", "find_declaration",
  "find_referencing_symbols",
]

[mcp_servers.serena.env]
SERENA_USAGE_REPORTING = "false"
PYTHONIOENCODING = "utf-8"
```

Use the navigation-only tool list for Hub setup. For a fresh Serena profile keep project execution trust at its empty default. Match the same telemetry and encoding environment when invoking the local CLI. Keep host paths, caches, setup records, generated memories and logs out of commits and PRs. [Serena's Codex setup](https://github.com/oraios/serena/blob/v2.1.0/docs/02-usage/030_clients.md#codex-cli-and-app) · [Codex MCP settings](https://learn.chatgpt.com/docs/config-file/config-reference) · [Serena security guidance](https://oraios.github.io/serena/02-usage/070_security.html)
