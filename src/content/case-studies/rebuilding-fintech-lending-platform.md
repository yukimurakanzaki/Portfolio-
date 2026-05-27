---
title: "Rebuilding a Fintech Lending Platform from the Ground Up"
company: "PT Danamas (Sinarmas Group)"
subtitle: "Digital Product Manager · Aug 2022 – Sep 2023"
summary: "Led the full product lifecycle of migrating Danamas Lender Platform from a legacy Java app to a modern React/Golang stack."
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
phoneScreensLabel: "Danamas Lender Platform — Rebuilt on React/Golang"
---

## Context

| Attribute | Detail |
|-----------|--------|
| **Company** | PT Danamas — a P2P lending fintech subsidiary of Sinarmas Group |
| **Product** | Danamas Lender Platform — web application for institutional and retail lenders to fund loans |
| **Role** | Digital Product Manager owning the full lender-side product |
| **Timeline** | August 2022 – September 2023 |
| **Team** | 1 PM (me), 4 Backend Engineers (Golang), 3 Frontend Engineers (React), 2 QA, 1 Designer |
| **Stakeholders** | CPO, CFO, CTO, Head of Lending Operations, Compliance, OJK regulatory body |

Danamas operated a P2P lending platform connecting lenders (both institutional and retail) with borrowers seeking personal and SME loans. The lender-facing platform — where lenders browse available loans, commit funds, and track portfolio performance — was built on a legacy Java monolith with a server-rendered JSP frontend circa 2017.

By 2022, the platform was struggling: page load times exceeded 8 seconds, the UI was not mobile-responsive, and adding new features required navigating a tangled codebase with minimal test coverage. Lender acquisition was stalling because the platform experience couldn't compete with newer fintech alternatives.

## Problem

The core challenge was executing a full platform rebuild while maintaining business continuity — lenders were actively using the existing platform daily to fund loans, and any disruption would directly impact loan disbursement volumes.

Specific problems included:

1. **Technical debt at critical mass** — The Java monolith had accumulated 5 years of patches without architectural refactoring. Database queries were unoptimized, session management was fragile, and the deployment process required manual steps that took 4+ hours.

2. **No API layer** — The legacy app used server-side rendering with direct database queries in controllers. There was no API that a modern frontend could consume, meaning the rebuild required building the entire backend API from scratch.

3. **Regulatory constraints** — OJK (Indonesia's financial services authority) requires P2P platforms to maintain specific audit trails, reporting capabilities, and data retention policies. The new platform had to satisfy all existing compliance requirements from Day 1.

4. **Lender trust at stake** — Institutional lenders managing billions of rupiah in portfolio value needed zero disruption to their daily operations. Any data inconsistency or downtime during migration would erode trust and risk lender churn.

5. **Team ramp-up** — The engineering team was being transitioned from Java to Golang/React. Most engineers had limited production experience with the new stack.

## Approach

### Step 1: Discovery and Domain Mapping

I spent the first 6 weeks conducting deep discovery:

- **Shadowed lender operations** for 2 weeks to understand actual workflows vs. documented ones (found 7 undocumented but critical workflows)
- **Mapped every API endpoint** the legacy system would need to expose, categorized by criticality (P0: blocks lending, P1: degrades experience, P2: nice-to-have)
- **Interviewed 12 institutional lenders** to understand pain points and feature requests, which informed prioritization of the new platform's feature set
- **Documented data models** and identified 3 data integrity issues in the legacy system that needed correction during migration

This discovery phase produced a 47-page PRD that became the single source of truth for the entire rebuild.

### Step 2: Parallel Architecture with Strangler Fig Pattern

Rather than a big-bang rewrite, I advocated for a strangler fig approach:

- New features built exclusively on the React/Golang stack
- Existing features migrated module-by-module, starting with lowest-risk, highest-value screens
- Both systems ran in parallel with a routing layer directing traffic based on feature flags
- Data synchronization layer ensured both systems read from the same source of truth

**Migration order** (based on risk/value matrix):
1. Portfolio dashboard (high value, low risk — read-only)
2. Transaction history (high value, low risk — read-only)
3. Loan browsing and filtering (high value, medium risk — involves search)
4. Fund commitment flow (highest value, highest risk — involves money movement)
5. Account settings and KYC (medium value, low risk)

### Step 3: Sprint Cadence and Stakeholder Management

I established a delivery rhythm designed for transparency and early feedback:

- **2-week sprints** with demo every Friday to stakeholders
- **Monthly lender beta group** — 5 institutional lenders given early access to new modules with a feedback channel
- **Bi-weekly compliance check-ins** with the legal team to validate each module met OJK requirements before production release
- **Weekly architecture review** with the CTO to ensure technical decisions aligned with platform strategy

Each module went through: Build → Internal QA → Beta lender testing → Compliance sign-off → Production release with feature flag → Full rollout.

### Step 4: Data Migration Strategy

The most critical workstream was migrating lender data (portfolios, transaction histories, account balances) without discrepancy:

- Built a reconciliation engine that compared legacy and new system outputs for every lender account nightly
- Ran parallel writes for 4 weeks before cutover — every transaction written to both systems
- Established a rollback plan with <15 minute RTO if critical issues emerged post-migration
- Conducted 3 dry-run migrations on production-copy data before the actual cutover

## Outcome

- **Full platform migration completed** in 13 months with zero data loss and zero unplanned downtime
- **Page load time reduced from 8+ seconds to under 1.5 seconds** (81% improvement)
- **Mobile-responsive design** — 34% of lender sessions shifted to mobile within 3 months of launch
- **Deployment time reduced from 4+ hours to 12 minutes** via CI/CD pipeline
- **Lender NPS improved from +18 to +52** based on quarterly survey
- **Feature velocity increased 3x** — new features that took 3-4 sprints on legacy shipped in 1 sprint on the new stack
- **Zero regulatory findings** in the subsequent OJK audit
- **Lender acquisition increased 28%** in the two quarters following full migration, attributed to improved platform experience

## Reflection

**What I'd Do Differently:**

The biggest lesson was around team ramp-up time. I underestimated how long it would take engineers to become productive in Golang after years of Java. The first two sprints delivered about 40% of planned velocity. If I did this again, I'd budget a dedicated 2-week "stack bootcamp" before Sprint 1, with pair programming on real (but non-critical) features rather than tutorial exercises.

I'd also push harder for a dedicated DevOps engineer from the start. We had engineers context-switching between feature work and CI/CD pipeline setup for the first 3 months, which created drag on both workstreams. A dedicated DevOps hire in Month 1 would have paid for itself in recovered engineering hours by Month 4.

Finally, I'd establish the lender beta group earlier — we started it in Month 4, but having lender feedback from Month 2 would have caught UX issues sooner and reduced rework in the fund commitment flow.

**What This Demonstrates:**

- Ability to lead a complex, high-stakes platform migration without disrupting active business operations
- Strategic use of strangler fig pattern to de-risk a full rewrite
- Deep discovery discipline — investing 6 weeks upfront to avoid costly mid-project pivots
- Stakeholder management across technical (CTO, engineers), business (operations, lenders), and regulatory (OJK, compliance) dimensions
- Data migration rigor with reconciliation, parallel writes, and rehearsed rollback plans
- Team leadership through a technology transition, balancing delivery pressure with learning curves
