---
title: "Shipping a Payment Gateway Integration Ahead of Plan"
company: "PT Bussan Auto Finance (BAF)"
subtitle: "Product Manager (Official Title: Product Owner & UI/UX Specialist) · 2023–2024"
summary: "Owned end-to-end integration of a third-party payment gateway into BAF Mobile — delivering well ahead of the original plan."
tags: ["Payments", "Delivery"]
readTime: "5 min read"
slug: "shipping-payment-gateway-integration"
order: 2
phoneScreens:
  - src: "/images/products/baf/home.jpg"
    alt: "BAF Mobile home screen showing loan contract and QRIS"
  - src: "/images/products/baf/payment.jpg"
    alt: "BAF Mobile payment method selection showing BLU, VA, autodebit options"
  - src: "/images/products/baf/success.jpg"
    alt: "BAF Mobile payment success confirmation screen"
phoneScreensLabel: "BAF Mobile — Payment Gateway Feature"
---

## Context

| Attribute | Detail |
|-----------|--------|
| **Company** | PT Bussan Auto Finance (BAF) — a multi-finance subsidiary of Mitsui & Co. |
| **Product** | BAF Mobile — customer-facing mobile app for loan payments and services |
| **Role** | Product Manager (Official Title: Product Owner & UI/UX Specialist) owning the payment feature roadmap |
| **Timeline** | Q3 2023 – Q1 2024 |
| **Team** | Cross-functional squad — product (me), backend, mobile, QA, and design, plus the external partner team |
| **Stakeholders** | Product leadership, Engineering Leads, Finance Operations, Compliance, and the payment partner |

BAF Mobile serves a large base of active borrowers making monthly loan repayments. The existing payment infrastructure relied on a single payment channel with limited payment method coverage, creating friction for customers who preferred e-wallets and virtual accounts. Leadership approved integrating a third-party payment gateway to expand payment method options and improve collection rates.

## Problem

The original project timeline allocated roughly half a year for the full integration — from contract signing through production launch. Several challenges made even that timeline ambitious:

1. **No existing integration pattern** — This was a first-of-its-kind third-party payment gateway integration for the team, so the supporting building blocks (an adapter layer, webhook handling, and a reconciliation pipeline) had to be designed from scratch.

2. **Regulatory complexity** — Payment integrations in Indonesian fintech require compliance checks, data residency validation, and specific audit trail requirements that added documentation overhead to every sprint.

3. **External partner dependency** — Part of the timeline depended on a third-party sandbox and API outside our direct control, which introduced coordination overhead and risk we had to actively manage.

4. **Concurrent feature pressure** — The mobile team was simultaneously shipping a redesigned home screen, meaning shared resources (QA, design review) were contested.

The business urgency was clear: every month without expanded payment methods meant customers abandoning payments due to limited options, with a direct impact on collection rates.

## Approach

### Step 1: Decompose and De-risk Early

Rather than treating the integration as a single monolithic delivery, I broke it into three independent workstreams that could progress in parallel:

- **Backend adapter layer** — Abstract the gateway's API behind an internal payment service interface, allowing future gateway swaps without mobile app changes
- **Webhook & reconciliation pipeline** — Build the async notification handler and daily reconciliation job independently of the payment flow
- **Mobile UI integration** — Design and build the payment method selection UI using mock responses while backend work progressed

This decomposition meant no workstream was blocked by another, and we could validate each piece independently.

### Step 2: Negotiate Scope with Stakeholders

The original plan included three payment methods (virtual account, e-wallet, and credit card). Credit card integration required additional PCI-DSS compliance work that would add weeks of lead time on its own. I presented data showing that virtual account and e-wallet together covered the large majority of customer payment preferences.

**Decision**: Ship VA + e-wallet first, defer credit card to Phase 2. This removed the longest-lead compliance item from the critical path.

### Step 3: Establish Partner Communication Cadence

Instead of ad-hoc, reactive coordination with the partner team, I established:
- Regular sync calls with their integration support team
- A shared tracking doc for every open question with an agreed response SLA
- A direct escalation path to their engineering lead for environment issues

This significantly reduced our average blocker resolution time and kept the external dependency from stalling the project.

### Step 4: Sprint Governance and Risk Tracking

I ran 2-week sprints with explicit risk registers. Each sprint retro included a "blockers killed" metric and a "days-at-risk" counter for any item that could slip the timeline. When an external dependency became temporarily unavailable mid-project, we had already identified it as a top risk and had a local mock server ready as a fallback, so development continued uninterrupted.

## Outcome

- **Delivered well ahead of the original plan** — production launch came months early
- **No critical defects** in the first weeks post-launch
- **Payment method coverage expanded** from a single channel to multiple payment methods across several banks and e-wallets
- **Collection rates improved meaningfully** in the first quarter after launch, as expanded payment options reduced customer payment friction
- **Reusable adapter pattern** later adopted by other teams for subsequent third-party integrations
- **Stakeholder trust earned** — was subsequently given ownership of the full payment domain roadmap

## Reflection

**What I'd Do Differently:**

If I could redo this project, I would have pushed for a dedicated QA engineer from Day 1 rather than sharing QA bandwidth with the home screen redesign team. We managed quality through rigorous code review and automated tests, but having dedicated QA earlier would have caught edge cases in the reconciliation pipeline sooner.

I'd also invest more upfront in contract testing against the partner's API. We relied on their sandbox for integration testing, but a contract test suite would have made us more resilient to environment instability and caught API mismatches earlier.

**What This Demonstrates:**

- Ability to decompose complex integrations into parallel, de-risked workstreams
- Stakeholder negotiation to reduce scope without sacrificing business value
- Proactive partner management that turns external dependencies into manageable risks
- Sprint governance that surfaces risks early and maintains delivery momentum
- Technical product thinking — designing for extensibility (adapter pattern) while shipping fast
