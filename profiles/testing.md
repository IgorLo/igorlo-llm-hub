# Testing and coverage

Choose the smallest public boundary that can observe the user's behavior. Cover pure business rules and data transformations with Vitest. Use browser tests for focus, touch, component interactions and navigation. Follow the project's existing test layout and keep fixtures small enough to explain the expected result.

For a behavior change, use the [reviewed TDD skill](../skills/catalog.md#behavioral-tests). Name the action and observable outcome before writing the assertion. For a regression, reproduce the reported failure, run the test and observe the expected failure on the original behavior. Apply the fix, rerun the same test and exercise neighboring cases that share its cause.

## Browser acceptance

Run at least one complete primary user journey against the production build on both a narrow touch viewport and a desktop viewport. Use a named project or device for each. Check that the user can reach the action, operate it and see its result. For keyboard interactions also check focus order, activation and return focus where appropriate. Keep the scenario reproducible from a fresh session.

For a hosted preview, use [Playwright CLI](../skills/catalog.md#preview-checks) to repeat the primary journey on the deployment tied to the reviewed PR commit. Record the SHA, URL and outcome. For a library release candidate, exercise its public behavior through a real consumer of the built package and follow the library's own packaging checks.

## Coverage

For new applications enforce at least **80% lines and 80% branches across domain code** in CI. Map the rules and transformations to real source paths. Set an explicit Vitest `coverage.include` so unimported files count. For example, when all domain code lives in FSD model segments, merge this block into `test` in the Vitest configuration and install `@vitest/coverage-v8` at the same version as Vitest. Extend the globs for business rules elsewhere. [Vitest coverage configuration](https://vitest.dev/config/coverage)

```ts
coverage: {
  provider: 'v8',
  include: ['src/{entities,features}/**/model/**/*.ts'],
  exclude: ['**/*.{test,spec}.ts', '**/*.d.ts'],
  reporter: ['text', 'json-summary'],
  thresholds: { lines: 80, branches: 80 }
}
```

Run `vitest run --coverage` through the locked project toolchain. Confirm the report lists a real domain module, then add a temporary unimported domain function with a branch. Verify the module appears with zero coverage and remove the probe. If the site has no domain code yet, record coverage as inapplicable and wire the gate when its first business rule appears.

For existing applications, establish the actual baseline and agree on thresholds before adopting a gate. Keep critical branches covered even when the aggregate already passes. For lockfile-only PRs, run the entire applicable CI suite and report domain coverage. If a separate changed-lines metric exists, display it as inapplicable when the diff has no executable source lines.
