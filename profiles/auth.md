# Authentication and access

Use this profile for sign-in, sessions, authorization or a new client of the shared identity service. Follow the [backend profile](backend.md) for ownership and environment boundaries, and [database changes](database-changes.md) when changing identities, grants, policies or session data.

## User behavior

Public content remains readable without sign-in. Opening a public page does not redirect a guest to authentication. Offer an explicit sign-in action beside protected actions such as sending a message or adding a comment. The product defines which content is public; drafts, private files, email addresses and session data stay private.

After a successful sign-in, return to the initiating material. Cancellation or authentication failure preserves the guest experience. If a draft is retained, keep it out of authentication URLs, bound its lifetime and require the user to submit it after returning. Signing in never publishes a draft automatically.

The initial provider is Google, through shared Supabase Auth and a central OAuth/OIDC authorization UI. Request only identity scopes needed for sign-in. Each application has a separate registered client, callback and local session on its own deployment address. Reuse the central sign-in when the user explicitly starts login in another application; that application's initial consent may still be required. An existing session in one product does not force a guest in another product through a redirect.

Google's client authenticates the person to the identity service; the product clients receive their own application-scoped sessions. Keep these client registrations separate. Use the provider's supported OAuth/OIDC flow, with a common server adapter for products, rather than an ad hoc token-sharing protocol. [Supabase OAuth server](https://supabase.com/docs/guides/auth/oauth-server) · [Google provider](https://supabase.com/docs/guides/auth/social-sign-in/auth-google)

## Protocol and sessions

- Register trusted clients explicitly; dynamic client registration is disabled for this first-party ecosystem. Use exact HTTPS callback allowlists for hosted environments and development-only localhost entries. Broad deployment-domain wildcards and arbitrary return URLs are not allowed. Resolve post-login destinations from bounded, validated application state.
- Use authorization code with PKCE S256 and single-use, expiring state tied to the initiating client/session. Verify signature, issuer, audience, expiry and expected client identity; verify OIDC nonce when using an ID token. Reject replayed codes and mismatched state/verifiers. Callback URLs carry a short-lived code, never access/refresh tokens. Redact codes, cookies, tokens and secrets from logs and analytics; authentication and personalized session responses must not be cached by the CDN.
- Use a host-only session cookie for each hosted application, with `Secure`, `HttpOnly`, `SameSite=Lax` and `Path=/`. Keep refresh credentials encrypted behind the server boundary with application/environment-specific keys and least-privilege session-store access. Separate the central login session from product sessions. An opaque cookie identifier alone does not supply secure session storage; document and test the adapter's actual storage and refresh behavior before admission.
- Where browser realtime requires an access token, expose only the necessary short-lived, application-scoped token after validating the local session. Keep refresh credentials on the server. Protect cookie-authenticated mutations against CSRF and coordinate concurrent refreshes so parallel requests/tabs do not invalidate the session accidentally.
- Define separate local and ecosystem-wide logout. The ordinary action ends the current application's session; a clearly named global action revokes the central and affected product refresh sessions. Clear local credentials, handle revocation failures explicitly and do not report an unconfirmed global logout as successful.

Use server-side verification and the provider's supported session checks. Decoding a cookie or trusting an unverified session object does not establish identity. A revoked refresh session does not invalidate an already issued JWT before expiry. For protected writes, enforce a live-session/revocation check on every reachable write path, including direct data API/RPC calls; checking only the application route leaves a bypass. Record and test the cutoff for private reads and realtime subscriptions as well. [Supabase sessions](https://supabase.com/docs/guides/auth/sessions) · [Sign-out behavior](https://supabase.com/docs/guides/auth/signout)

## Identity and permissions

Use a stable internal user ID for content ownership. Keep provider identities and private account data separate from public profiles. A nickname belongs to that user through database uniqueness/transactions; a client-supplied name or email does not prove ownership. Google-only account recovery initially depends on the provider; additional providers, identity relinking or owner-assisted recovery need a separately defined, verified procedure.

Authenticate both the person and the calling application. Enforce the resource owner, allowed operation and verified client identity, such as Supabase's signed OAuth `client_id`, in the server and database access contract. A shared user ID or the `authenticated` role alone does not give a product rights to another product's data. Request-body `app_id`, CORS and origin names do not establish a trusted client. Ordinary products do not receive the shared service-role/admin credentials.

Give the central login service only its explicitly defined identity/consent operations. Direct provider sessions without a product client identity do not inherit product data permissions. Test that absence of `client_id` denies product-private operations unless a reviewed, narrow administrative path explicitly requires it.

Apply grants and row-level security to exposed data and storage policies to files. Public access is a deliberate read-only grant for selected fields and published resources. Check the combined policies: a broad permissive policy can defeat a narrower client condition. Views, RPC functions and realtime have to preserve the same boundary. Changes follow the [database change procedure](database-changes.md). [Supabase OAuth client policies](https://supabase.com/docs/guides/auth/oauth-server/token-security)

## Acceptance

Use synthetic data and two independent test origins before connecting a real product. Record the SHA and observed outcomes:

1. Guests can read permitted content on both origins without redirects; direct unauthenticated writes fail. Sign-in, cancellation and provider errors return to usable public content without publishing a draft.
2. Explicit login on the second origin resolves to the same user ID with a separate session. The flow works without third-party cookies and respects the consent contract.
3. Wrong client/environment, tampered callback/state, replayed code, invalid PKCE and forged resource ownership fail. Test API, RPC, storage and realtime directly, not just hidden UI controls.
4. Concurrent refresh, expired sessions, local/global logout and revocation meet the documented write/read/realtime cutoffs. Authentication failures do not expand permissions.
5. Verify actual Google callback, consent/publishing requirements and an ordinary allowed account outside the infrastructure team. Provider scopes and paid options match the approved configuration.

Follow the [testing profile](testing.md) for UI/browser checks. The product contract records precise session storage, revocation guarantees and recovery limits; unresolved guarantees block admission rather than becoming assumed provider behavior.
