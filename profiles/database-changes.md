# Database changes and recovery

Use this procedure for schema/data migrations, grants or row-level security, exposed views/RPC, stored-file access/lifecycle changes and data recovery. Follow [Git freshness](git.md), the project's release contract and the [testing profile](testing.md). For a shared backend, read its registry and every affected product contract; [backend ownership](backend.md#ownership-and-contracts) identifies the schema/release owner.

## SQL readability and verification

For hand-written migrations, record the change in observable behavior and
explain non-obvious grants, role transitions and transaction boundaries.
Use named fixtures and expected outcomes in database tests. Pin a formatter
that handles the project's dialect, stored functions and test-runner commands.
Verify that formatting twice produces identical output and run the formatted
example against a disposable database before enabling autofix.

Apply formatting checks to new migrations and maintained SQL tests. Preserve
already applied migration files and document historical context in the migration
index. After replay, run function linting on every project-owned schema that
contains code. Include database behavior and upgrade tests in CI.

## Plan the change

State the user-visible need, owner, affected data/clients and compatibility requirement. Identify the current database/environment and contract revision without exposing credentials. Keep one repository and append-only migration history for the shared database. Product repositories propose changes there; one controlled release path owns DDL credentials.

Describe the desired schema, grants/policies, data transformation, constraints and file effects together. New objects are closed by default; explicitly review API exposure, default privileges, grants, RLS, function execution rights and storage policies. Check views and security-definer functions for bypasses; constrain privileged helpers to a documented operation, fixed search path and explicit execution grants. [Supabase API security](https://supabase.com/docs/guides/api/securing-your-api)

Prefer compatible expansion, bounded resumable backfill, application switch and a later removal. Record old/new client behavior, dependencies, expected locks/duration and the consequence of rollback. Destructive changes, identity reassignment and bulk deletion need a separate, concrete owner decision covering their data loss and recovery consequences.

Completion: a reviewer can identify the exact scope, expected data result, affected callers and recovery strategy before execution.

## Verify before release

Create new migration files in the schema owner's repository; applied files remain unchanged. Review the resulting schema and permissions diff, including generated statements. Routine changes go through these files, not remote Dashboard edits or write-capable MCP sessions. [Supabase migration workflow](https://supabase.com/docs/guides/deployment/database-migrations)

Using synthetic or properly sanitized data in an isolated target, prove:

- Clean installation from the full history and upgrade from the previous supported state with existing records.
- Data counts, relationships, constraints, unique names, repeatable retry behavior and file/metadata consistency as affected by the change.
- Old-client compatibility during expansion and isolation of neighboring products.
- Allowed and denied operations for guest, different users and different clients through the real API/RPC/storage/realtime paths. Owner-role SQL alone does not test RLS.
- Failure behavior: competing releases, wrong target, schema drift, failed backup, interrupted/partially applied migration and failed postchecks stop subsequent release steps.

Repeat the production procedure on staging using the same reviewed artifacts and relevant configuration. Measure locks, runtime and backfill batches; test timeouts and retry/resume behavior. Keep staging data and credentials separate from production.

Completion: record the tested SHA, base/target revisions, commands, evidence and unresolved limitations. Production remains blocked when integrity, isolation, compatibility or required recovery checks fail.

## Recovery readiness

Before real user data or a production data-changing release, agree with the owner on recovery point (acceptable age of the latest recoverable data), recovery time, backup frequency/retention, independent destination, encryption and key recovery. Verify no-card/storage/egress constraints and access when the owner's computer is off or the main provider account is unavailable. Do not invent a zero-loss guarantee or silently choose these objectives.

Maintain scheduled independent backups and a fresh pre-release copy covering the changed scope. Record a manifest/digest, schema/configuration revision, object coverage and any omitted data or credentials. A successful dump is not proof of recoverability: exercise restoration into a new isolated target, verify the required coverage and retain the recovery evidence. Recheck the affected restore path when a migration changes that coverage.

The recovery inventory includes:

| Inventory | Required evidence |
| --- | --- |
| Application data, schema, roles, grants and policies | Records/relationships and allowed/denied operations survive restoration |
| Auth users, provider identity mappings and application registry | The same external identity can recover access to its original content; preserve stable internal IDs |
| Storage metadata and object bytes | Objects exist, checksums match and access remains correct |
| OAuth/configuration, custom roles and secret recovery | Document what managed exports omit; keep encrypted secrets and recovery keys outside ordinary source/backup payloads |

Inspect the actual export tool's coverage of managed schemas, identities, role passwords and configuration. Copy file objects separately where a database backup only includes their metadata. Session restoration is not a goal: document safe invalidation/re-login after recovery. [Supabase backup coverage](https://supabase.com/docs/guides/platform/backups)

Completion: the independent copy is usable without the primary deployment and a tested restoration meets the agreed objectives. Missing objectives, key access, identity/file coverage or restoration evidence block real-data admission and the affected release.

## Apply one authorized release

Production authorization follows the existing release contract and session scope. A merge authorizes deployment only when that behavior is declared and authorized. Bind the release to the reviewed SHA, database/environment identity, expected current revision and ordered pending migrations; changes to those inputs require reassessment before applying them.

1. Acquire a lock for the target database in the single shared release path. All DDL actors use that path; concurrency groups in separate product repositories are not a global database lock. Keep DDL credentials out of ordinary application, push and preview jobs. Verify the chosen approval control is actually available for the repository's plan/visibility.
2. Under the lock, verify target identity, migration history and actual schema drift; create/check the fresh independent backup and its manifest. Block on missing or unexpected inputs, failed backup or failed prechecks. A backup is a snapshot, not proof that later concurrent writes are preserved; account for those writes before an incompatible change.
3. Apply the reviewed compatible migrations in order. Use transactions where the chosen operations support them and measured lock/statement timeouts. A whole release is not automatically atomic. Bound backfills and save progress for safe resume. Do not auto-cancel an active DDL step because a newer build arrived.
4. Run integrity, permission and old-client postchecks before deploying dependent application code from the verified SHA. Stop on failure. Retain the lock until the database stage and its postchecks complete, then record the actual revision and release outcome.
5. Exercise the affected user journey and a neighboring consumer, then monitor errors and shared quotas. Retire old structures only in a later authorized destructive change after every dependent client has moved.

Completion: the release record identifies applied migrations, backup, tested/deployed SHA and outcomes. A failed or partial release stays visibly incomplete; it is not retried until actual state and history are reconciled.

## Failure and emergency recovery

Stop further releases and affected writes as required; preserve the current data state, migration history and redacted diagnostics. Determine what committed before choosing a repair. Prefer a reviewed forward migration when it safely preserves data. Migration-history repair changes bookkeeping, not schema or lost records; use it only after verifying the actual state and capturing the corrective change.

For restoration, first preserve the current state and identify writes accepted after the backup. Restore into a separate target, validate integrity/identity/permissions and reconcile or explicitly account for those writes before an authorized cutover. Document the impacted applications, downtime and any unrecoverable interval. Rolling back application code does not roll back schema or data.

Show the owner the concrete repair/cutover, backup and consequences before an unapproved destructive emergency action. After the authorized repair, capture emergency changes as reproducible migrations/configuration and rerun the affected and neighboring checks. Production reset, blind reverse migrations and unreviewed destructive SQL are outside the normal release path.

Completion: verified application behavior and permissions are restored, accepted writes are accounted for, the migration history matches reality and the incident record states any loss or remaining limitation.
