# New frontend projects

Use these defaults when creating a site. In an existing repository, apply its approved configuration and propose stack or lint migrations as separate changes.

## Application and UI

Start with Svelte 5, SvelteKit, Vite and TypeScript. Use Svelte ASCII UI components and tokens. Before choosing a component or overriding its behavior, read the installed package's `docs/agents/using.md`. When a component needs a change, establish whether the application composition or the library owns it.

Build the primary task on a narrow touch screen first. Expand the layout when its content benefits from the available width. Exercise long labels, text enlargement and keyboard focus in the actual composition. Validate the main flow using the [testing profile](testing.md).

Organize application code with Feature-Sliced Design. Keep SvelteKit routes as the composition root. Import downward through each slice's public API and keep a slice's internal imports local. Run Steiger with the recommended FSD plugin. Give each rule exception the smallest applicable scope and record the concrete framework or architecture constraint.

Use Vercel by default. Choose the adapter after checking whether the routes require server runtime or can all be prerendered. Record the project's preview trigger and production branch. Opening a dependency PR authorizes its configured preview. Production follows the owner's release decision.

## Checks in a fresh checkout

Use the lockfile for the install. Run Prettier in check mode, type-aware ESLint with the typescript-eslint `strictTypeChecked` preset, Stylelint, Steiger, Svelte type checking, unit tests with coverage, a production build and browser tests against that build. Connect the same commands to PR CI. Configure warning-producing checks to fail on warnings.

Extend the generated SvelteKit TypeScript configuration with `strict: true` and `noUncheckedIndexedAccess: true`. Preserve the Svelte parser on components and give it the TypeScript parser for scripts. Enable typed linting for project source, including `.svelte` scripts. Verify the effective config against a real component whenever parser or config versions change. [typescript-eslint shared configurations](https://typescript-eslint.io/users/configs/)

Lint standalone CSS and component styles. This starting point for `stylelint.config.mjs` uses `stylelint`, `stylelint-config-standard` and `postcss-html`. Add a matching syntax if the project introduces a style preprocessor. [Stylelint setup](https://stylelint.io/user-guide/get-started/) · [PostCSS HTML syntax](https://github.com/ota-meshi/postcss-html)

```js
export default {
  extends: ['stylelint-config-standard'],
  overrides: [{ files: ['**/*.svelte'], customSyntax: 'postcss-html' }]
};
```

Exercise each quality gate when adopting the profile or changing its configuration. Use disposable edits to files found by the normal CI commands, inspect the diagnostic, then restore the files and rerun clean.

| Gate | Probe | Expected diagnostic |
| --- | --- | --- |
| TypeScript and Svelte | Access a property of a possibly missing array element | Possibly undefined value |
| Typed ESLint | Leave a floated promise in a TypeScript file and a component script | `no-floating-promises` in both files |
| Stylelint | Spell `color` as `colro` in a CSS file and a component's used style rule | `property-no-unknown` in both files |
| Steiger | Import from a higher FSD layer in a lower-layer slice | Forbidden layer dependency |
| Prettier | Change whitespace in a formatted source file | Format check fails |
