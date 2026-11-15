# Backend and shared infrastructure

Use this profile when adding server logic, persistent data or realtime, or connecting an application to a shared backend. Keep an existing project's approved stack and release contract; adopting this profile does not authorize migrating other applications.

## Starting point

For new small web applications, extend the [frontend profile](frontend.md) with SvelteKit server routes, server loads and actions. Keep UI and application server logic in the same product repository. A separate backend process needs a concrete requirement, such as an independent API, long-running work or a different runtime; record its owner and release boundary.

Use Vercel for the application and a shared Supabase Free backend for related small projects under the same owner. Supabase provides Postgres, Auth, Storage and Realtime. Each product keeps its own free deployment address. Use the [authentication profile](auth.md) for identity and access, and [database changes](database-changes.md) for schema, policies, stored files and recovery. A shared backend is a capacity and trust tradeoff; propose separate infrastructure when isolation, workload, availability or commercial terms require it.

Before provisioning, verify current official terms for every service: payment-card requirements, account-wide versus per-project quotas, inactivity, persistent storage, connection lifetime and exhaustion behavior. Use the no-card Free/Hobby configuration; a paid add-on or trial is a separate owner decision. Record dated evidence privately and the selected runtime/limits in the product contract. A free plan is not a promise of continuous availability or lossless recovery.

## Ownership and contracts

| Owner | Owns |
| --- | --- |
| Product repository | Domain behavior, public content, application API and UI composition |
| [Shared backend repository](https://github.com/IgorLo/igorlo-shared-backend) | One migration history, schema, grants/policies, OAuth client registry, infrastructure configuration, release and recovery procedures |
| Shared authentication service and adapter | Provider integration, protocol, per-application sessions and verified user/client identity |
| UI library | Reusable presentation and callbacks; server access decisions belong to the backend |

Keep the operational backend repository private. Read its `AGENTS.md` and current local contracts before operational changes. Public Hub files contain reusable conventions; account identifiers, resource addresses, credentials and user data remain in private project records. Apply [repository ownership](repositories.md) before moving a behavior between owners.

Maintain an application registry in the shared backend: owner, environment, verified client identity, data objects/buckets, allowed operations and contract revision. Each product proposes schema changes to that repository. Product builds do not independently push migrations to the shared database, and normal application credentials cannot perform DDL or administer other products.

Define public HTTP/realtime payloads once, with runtime validation and inferred/shared types where practical. Keep credentials and database administration in server-only modules. A database row is not automatically a public DTO; expose only the fields an operation needs. Use database constraints and transactions for ownership, unique names and concurrent updates. Define idempotency for retryable writes.

Store durable application data in the database and uploaded objects in object storage, with metadata and access rules. Deployment files and process memory are not durable storage. Persist messages before acknowledging success; reconnect reloads missed history and tolerates duplicates. Realtime delivery is not the sole record of a write.

## Environments and admission

Develop with local services or isolated staging and synthetic data. Production credentials, OAuth clients, encryption keys and file access are separate. Preview jobs cannot mutate production; untrusted PRs receive neither production secrets nor sensitive data. Check available free project capacity before allocating staging, and verify whether preview database branching is paid.

Before admitting a product or real user data, record evidence for all of these:

- Least-privilege access through direct API, RPC, storage and realtime paths; one user or client cannot cross its allowed boundary.
- Clean installation and upgrade with existing data, preserving old-client compatibility and neighboring applications.
- Independent database/file recovery with the owner's agreed recovery objectives, using the [database change procedure](database-changes.md#recovery-readiness).
- Authentication across two independent test origins, including voluntary sign-in, cancellation, refresh and revocation as specified in [auth acceptance](auth.md#acceptance).
- Failure behavior for provider outages, quota exhaustion and reconnect. Show a failed or pending write honestly; never acknowledge an unconfirmed write as saved. Bound payloads, file sizes, request rates and public-history reads, and monitor shared capacity.

Run behavioral checks through the [testing profile](testing.md). Record the tested SHA, environments and outcomes; a written policy is not evidence that its controls are implemented. Connect existing products one at a time only within their authorized task scope, after the shared foundation passes these gates.
