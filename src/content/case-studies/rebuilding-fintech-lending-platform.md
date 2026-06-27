---
title: "Rebuilding a Fintech Lending Platform from the Ground Up"
company: "PT Danamas (Sinarmas Group)"
subtitle: "Digital Product Manager · Aug 2022 – Sep 2023"
summary: "Led the full product lifecycle of migrating the Danamas Lender Platform from an aging legacy system to a modern web stack — without disrupting active lending operations."
tags: ["0-to-1", "Platform", "Delivery"]
readTime: "6 min read"
slug: "rebuilding-fintech-lending-platform"
order: 1
phoneScreens:
  - src: "/images/products/danamas/onboarding.jpg"
    alt: "Danamas lender onboarding showing curated investment products"
  - src: "/images/products/danamas/dashboard.jpg"
    alt: "Danamas lender dashboard showing Dana Siaga and Alokasi Investasi"
  - src: "/images/products/danamas/reksadana.jpg"
    alt: "Danamas Reksadana product list with returns and investment details"
phoneScreensLabel: "Danamas Lender Platform — Rebuilt on a Modern Web Stack"
---

## Context

| Attribute | Detail |
|-----------|--------|
| **Company** | PT Danamas — a P2P lending fintech subsidiary of Sinarmas Group |
| **Product** | Danamas Lender Platform — web application for institutional and retail lenders to fund loans |
| **Role** | Digital Product Manager owning the full lender-side product |
| **Timeline** | August 2022 – September 2023 |
| **Team** | Cross-functional squad — product (me), backend, frontend, QA, and design |
| **Stakeholders** | Executive leadership (product, finance, technology), Lending Operations, Compliance, and the financial regulator |

Danamas operated a P2P lending platform connecting lenders (both institutional and retail) with borrowers seeking personal and SME loans. The lender-facing platform — where lenders browse available loans, commit funds, and track portfolio performance — was built on an aging legacy system that had not kept pace with the business.

By 2022, the platform was struggling: it was slow, not mobile-responsive, and adding new features was difficult and time-consuming. Lender acquisition was stalling because the platform experience couldn't compete with newer fintech alternatives.

## Problem

The core challenge was executing a full platform rebuild while maintaining business continuity — lenders were actively using the existing platform daily to fund loans, and any disruption would directly impact loan disbursement volumes.

Specific problems included:

1. **Significant technical debt** — Years of incremental patches without architectural refactoring had made the platform fragile, slow to deploy, and hard to extend.

2. **Limited API foundation** — The legacy app was tightly coupled and lacked a modern API layer that a new frontend could consume, which meant the rebuild required building out the backend services as well.

3. **Regulatory constraints** — Indonesia's financial services authority requires P2P platforms to maintain specific audit trails, reporting capabilities, and data retention policies. The new platform had to satisfy all existing compliance requirements from Day 1.

4. **Lender trust at stake** — Institutional lenders managing substantial portfolio value needed zero disruption to their daily operations. Any data inconsistency or downtime during migration would erode trust and risk lender churn.

5. **Team ramp-up** — The engineering team was transitioning to a new technology stack, and most engineers had limited production experience with it.

## Approach

### Step 1: Discovery and Domain Mapping

I spent the first several weeks conducting deep discovery:

- **Shadowed lender operations** to understand actual workflows vs. documented ones — surfacing several critical workflows that existed in practice but weren't written down anywhere
- **Mapped every API endpoint** the new system would need, categorized by criticality (P0: blocks lending, P1: degrades experience, P2: nice-to-have)
- **Interviewed institutional lenders** to understand pain points and feature requests, which informed prioritization of the new platform's feature set
- **Documented the data models** and identified legacy data that would need careful handling during migration

This discovery phase produced a detailed PRD that became the single source of truth for the entire rebuild.

### Step 2: Parallel Architecture with the Strangler Fig Pattern

Rather than a big-bang rewrite, I advocated for a strangler fig approach:

- New features built exclusively on the new stack
- Existing features migrated module-by-module, starting with lowest-risk, highest-value screens
- Both systems ran in parallel with a routing layer directing traffic based on feature flags
- A data synchronization layer ensured both systems read from the same source of truth

**Migration order** (based on a risk/value matrix):
1. Portfolio dashboard (high value, low risk — read-only)
2. Transaction history (high value, low risk — read-only)
3. Loan browsing and filtering (high value, medium risk — involves search)
4. Fund commitment flow (highest value, highest risk — involves money movement)
5. Account settings and KYC (medium value, low risk)

### Step 3: Sprint Cadence and Stakeholder Management

I established a delivery rhythm designed for transparency and early feedback:

- **2-week sprints** with a demo every Friday to stakeholders
- **Monthly lender beta group** — a handful of institutional lenders given early access to new modules with a feedback channel
- **Regular compliance check-ins** to validate each module met regulatory requirements before production release
- **Weekly architecture review** with engineering leadership to ensure technical decisions aligned with platform strategy

Each module went through: Build → Internal QA → Beta lender testing → Compliance sign-off → Production release behind a feature flag → Full rollout.

### Step 4: Data Migration Strategy

The most critical workstream was migrating lender data (portfolios, transaction histories, account balances) without discrepancy:

- Built a reconciliation process that compared legacy and new system outputs for every lender account on a nightly basis
- Ran parallel writes for several weeks before cutover — every transaction written to both systems
- Established a rollback plan with a tight recovery-time objective if critical issues emerged post-migration
- Conducted multiple dry-run migrations on production-copy data before the actual cutover

## Outcome

- **Completed the full platform migration** in just over a year, with no data loss and no unplanned downtime
- **Cut page load times dramatically** — pages that previously took several seconds now load near-instantly
- **Mobile-responsive design** — a meaningful share of lender sessions shifted to mobile within months of launch
- **Deployment went from a slow, manual, multi-hour process to minutes** via a CI/CD pipeline
- **Lender satisfaction (NPS) improved substantially** based on quarterly surveys
- **Feature delivery accelerated several-fold** — work that took multiple sprints on the legacy system shipped in a single sprint on the new stack
- **Passed the subsequent regulatory audit cleanly**
- **Lender acquisition grew meaningfully** in the quarters following the migration, with the improved platform experience contributing to the growth

## Reflection

**What I'd Do Differently:**

The biggest lesson was around team ramp-up time. I underestimated how long it would take engineers to become productive on the new stack. The first couple of sprints delivered well below planned velocity. If I did this again, I'd budget a dedicated "stack bootcamp" before Sprint 1, with pair programming on real (but non-critical) features rather than tutorial exercises.

I'd also push harder for a dedicated DevOps engineer from the start. We had engineers context-switching between feature work and pipeline setup for the first few months, which created drag on both workstreams. A dedicated DevOps hire early on would have paid for itself in recovered engineering hours.

Finally, I'd establish the lender beta group earlier — having lender feedback sooner would have caught UX issues earlier and reduced rework in the fund commitment flow.

**What This Demonstrates:**

- Ability to lead a complex, high-stakes platform migration without disrupting active business operations
- Strategic use of the strangler fig pattern to de-risk a full rewrite
- Deep discovery discipline — investing upfront to avoid costly mid-project pivots
- Stakeholder management across technical, business, and regulatory dimensions
- Data migration rigor with reconciliation, parallel writes, and rehearsed rollback plans
- Team leadership through a technology transition, balancing delivery pressure with learning curves
