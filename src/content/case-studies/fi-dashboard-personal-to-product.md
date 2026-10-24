---
title: "From personal finance tool to multi-tenant SaaS — in 8 days"
company: "FI Dashboard (Own Product)"
subtitle: "Product Owner & Solo PM · Jun – Jul 2026"
summary: "Took a single-user, local-only personal finance PWA and evolved it into a cloud-backed, multi-tenant household finance product — from beta through planned sunset of the local-first architecture — in just over a week."
outcome: "8 days from first commit to a cloud-syncing, multi-tenant beta."
tags: ["0-to-1", "SaaS", "Product Strategy", "Architecture"]
readTime: "7 min read"
slug: "fi-dashboard-personal-to-product"
order: 4
phoneScreensLabel: "FI Dashboard — From Local PWA to Cloud-Backed Household Finance Product"
---

## Context

| Attribute | Detail |
|-----------|--------|
| **Product** | FI Dashboard — a household finance app: net worth scoreboard, safe-to-spend waterfall, lane-based budgeting, and FI projection |
| **Role** | Product owner, sole PM, and requirements author — directing AI coding agents (Claude, Codex) to build |
| **Timeline** | June 28 – July 5, 2026 (8 days from first commit to cloud-syncing multi-tenant beta) |
| **Users** | Household of two (myself + partner) as primary; one friend household as beta validation target |
| **Stack** | React PWA (Vite), Supabase (Postgres + Auth + Edge Functions), IndexedDB (offline cache), Anthropic API |

I built FI Dashboard to solve my own problem: my wife and I had no shared, honest view of our combined finances — net worth, safe-to-spend, and when we could reach financial independence. The first version was a local-first PWA running entirely on-device with IndexedDB.

Within five sprints, the app had real depth: net worth tracking across four financial "lanes" (income-producing, store of value, debt, protected living), a safe-to-spend waterfall that enforced "pay yourself first," envelope budgeting, AI-assisted bank statement import, recurring item management, FI projection with two path strategies, and a spending decision lens that reframed purchases as opportunity cost.

But it was a single-device tool with a live security problem.

## Problem

The app worked for me — but it failed at the actual job: giving a **household** a shared financial picture.

1. **Single point of failure** — All financial data lived in one browser's IndexedDB. Clearing site data or losing the device meant losing everything.

2. **Live security exposure** — The AI chat feature stored a raw Anthropic API key unencrypted in IndexedDB and sent it directly from the browser (`dangerouslyAllowBrowser: true`). Anyone with device access or a malicious browser extension could exfiltrate a live, billable API key.

3. **No sharing** — One PIN, one browser, one device. My wife could only see the data by looking over my shoulder.

4. **Architecture documentation was already false** — `ARCHITECTURE.md` stated "No server, no auth, no sync" as a decision. But the app was already making direct browser-to-API calls to Anthropic and two market data providers. The decision was stale; the app was already networked.

5. **Zero tests, zero CI** — Five sprints of code with not one test file. The functions that tell you whether you can retire and what you can spend — `fiProjection.ts`, `safeToSpend.ts`, `savingsRate.ts` — had never been asserted against a single expected value.

The gap wasn't "add some features." It was "this app needs to become a product."

## Approach

### Phase 0: Requirements Elicitation Before Code

I stopped building and wrote requirements first — something that had never been done for this project. This was deliberate: every prior decision (no server, no auth, no sync) was made implicitly by whoever prompted the sprint, not deliberately by the product owner.

I produced two documents:

- **REQUIREMENTS.md** (v1.1) — A formal requirements baseline with stakeholder analysis, current state assessment, business requirements, solution requirements across three phases, non-functional requirements, transition requirements with explicit exit criteria, and accepted risks.

- **BRD v2.0** — A business requirements document that defined the pivot from personal tool to commercial multi-tenant product. This introduced the household as the tenant boundary, per-member allowances within a shared budget, cloud accounts with authentication, subscription/billing, and a staged go-to-market.

Key product decisions documented and locked:

- **The unit is the household, not the user.** Members share one net worth, one budget, one FI goal, with individual discretionary allowances.
- **Staged rollout:** dogfood own household → beta with one friend → public launch.
- **Freemium + per-household subscription.** Cloud/sharing features gated behind a paid plan.
- **Phased delivery is a requirement, not a suggestion.** The product owner explicitly rejected a one-sprint rewrite.

### Phase 1: Fix the Live Exposure (Day 1–2)

Before touching architecture, I tackled the security problem:

- **Moved the Anthropic API key server-side** via a Supabase Edge Function (`anthropic-proxy`), gated by Supabase Auth with JWT verification. The client never touches the key again.
- Added crash protection so the app doesn't break when Supabase environment variables are missing (graceful degradation for the local-first fallback).

This closed the most critical exposure in the current state assessment and pulled forward a thin slice of Phase 2 work at the product owner's request (my wife didn't want to manage a personal Anthropic key).

### Phase 2: Multi-Tenant Cloud Backend (Day 3–6)

With the security fix shipped, I executed the architecture pivot:

1. **Multi-tenant Postgres schema** — Every table scoped by `household_id`. Accounts, transactions, assets, recurring items, snapshots, milestones — all household-isolated. Schema designed so per-person attribution could be added later without a rebuild.

2. **Auth + household bootstrap** — Supabase Auth (email + password), household creation on first sign-up, member invitation flow. The existing device PIN repurposed as a local app lock on top of the Supabase session.

3. **Cloud sync engine** — UUID-based IDs, watermark-based push/pull synchronization. Offline writes queue locally and sync on reconnect. Fresh IndexedDB namespace (v7) to avoid collisions with legacy local data.

4. **Per-member allowances** — Each household member gets their own slice of the shared discretionary budget with an independent weekly safe-to-spend ceiling.

### Phase 3: Production Hardening (Day 7–8)

The last 48 hours were debugging real-world issues:

- **CORS fix** for the AI Manager edge function — preflight requests needed to reflect the requested headers.
- **Sync reliability** — writes weren't stamping `updated_at`, so rows silently failed to push. Fixed the sync layer to stamp on every write.
- **Build environment** — production deploys were missing the Supabase anon key at build time. Added a fallback to the real key.

## Outcome

- **From zero requirements to two formal documents** (REQUIREMENTS.md + BRD v2.0) that serve as the single source of truth for all future development.

- **Security exposure closed** — API key moved server-side behind JWT-gated Edge Function. No credentials in client storage.

- **Multi-tenant architecture shipped** — Postgres schema with household-scoped data isolation, authentication, and role-based access (Admin + Member).

- **Cloud sync working** — Two devices, two household members, one shared financial picture. Offline-capable with queue-and-sync on reconnect.

- **8 days from first commit to cloud-syncing multi-tenant beta** — Five sprints of local-only code evolved into a product architecture that can support multiple households.

- **Staged rollout on track** — Currently in P0 (dogfood with own household). P1 (friend beta) is next, validating data isolation and willingness to pay before any public launch.

## Reflection

**What I'd Do Differently:**

I'd write the requirements baseline *before* the first sprint, not after five. The "no server / no auth / no sync" decisions were never deliberate — they were defaults that became technical debt. The current state assessment revealed that the app was already violating its own architecture document. Starting with even a lightweight requirements pass would have caught the API key exposure before it shipped.

I'd also sequence the Anthropic key fix as Sprint 1, not Sprint 6. It was a live security problem from the day the chat feature merged. The fact that it took a formal requirements review to surface the urgency — when the code literally had `dangerouslyAllowBrowser: true` — is a process gap, not a technical one.

**What This Demonstrates:**

- Ability to step back from active development and do proper requirements work — even on your own product, even when there's momentum to "just keep building"
- Product thinking that reframes a personal tool as a commercial product: tenant boundaries, pricing, go-to-market staging, and accepted risks documented before code
- Architecture pivot from local-first IndexedDB to cloud-backed Supabase without losing offline capability or rewriting the UI layer
- Security-first prioritization — closing a live exposure before adding features
- Realistic self-assessment in the current state analysis (testing is decorative, architecture docs are stale, durability is a single point of failure) instead of minimizing problems
- Managing the full product lifecycle from beta to planned sunset of the legacy architecture, with explicit transition requirements and rollback plans
