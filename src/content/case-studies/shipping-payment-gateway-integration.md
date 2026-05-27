---
title: "Shipping a Payment Gateway Integration 2 Months Ahead of Plan"
company: "PT Bussan Auto Finance (BAF)"
subtitle: "Product Manager (Official Title: Product Owner & UI/UX Specialist) · 2023–2024"
summary: "Owned end-to-end integration of AyoConnect payment gateway into BAF Mobile — delivering 2 months faster than the original plan."
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
| **Role** | Product Manager (Official Title: Product Owner & UI/UX Specialist) owning payment feature roadmap |
| **Timeline** | Q3 2023 – Q1 2024 |
| **Team** | 1 PM (me), 3 Backend Engineers, 4 Mobile Engineers, 1 QA, 1 Designer |
| **Stakeholders** | VP Product, Finance Operations, Compliance, AyoConnect partner team |

BAF Mobile serves hundreds of thousands of active borrowers making monthly loan repayments. The existing payment infrastructure relied on a single payment channel with limited payment method coverage, creating friction for customers who preferred e-wallets and virtual accounts. Leadership approved integrating AyoConnect as a payment gateway to expand payment method options and improve collection rates.

## Problem

The original project timeline allocated 6 months for the full integration — from contract signing through production launch. However, several challenges made even that timeline ambitious:

1. **No existing integration pattern** — BAF's backend had never integrated a third-party payment gateway. There was no reusable adapter layer, no webhook handling infrastructure, and no reconciliation pipeline.

2. **Regulatory complexity** — Payment integrations in Indonesian fintech require OJK compliance checks, data residency validation, and specific audit trail requirements that added documentation overhead to every sprint.

3. **Partner dependency** — AyoConnect's sandbox environment had known instability issues, and their API documentation contained gaps that required frequent clarification calls with their technical team.

4. **Concurrent feature pressure** — The mobile team was simultaneously shipping a redesigned home screen, meaning shared resources (QA, design review) were contested.

The business urgency was clear: every month without expanded payment methods meant measurable drop-off in collection rates as customers abandoned payments due to limited options.

## Approach

### Step 1: Decompose and De-risk Early

Rather than treating the integration as a single monolithic delivery, I broke it into three independent workstreams that could progress in parallel:

- **Backend adapter layer** — Abstract AyoConnect's API behind an internal payment service interface, allowing future gateway swaps without mobile app changes
- **Webhook & reconciliation pipeline** — Build the async notification handler and daily reconciliation job independently of the payment flow
- **Mobile UI integration** — Design and build the payment method selection UI using mock responses while backend work progressed

This decomposition meant no workstream was blocked by another, and we could validate each piece independently.

### Step 2: Negotiate Scope with Stakeholders

I identified that the original 6-month plan included three payment methods (virtual account, e-wallet, and credit card). Credit card integration required PCI-DSS compliance work that would add 8+ weeks alone. I presented data showing that virtual account and e-wallet covered 94% of customer payment preferences.

**Decision**: Ship VA + e-wallet first, defer credit card to Phase 2. This removed the longest-lead compliance item from the critical path.

### Step 3: Establish Partner Communication Cadence

Instead of ad-hoc Slack messages with AyoConnect's team, I established:
- Bi-weekly sync calls with their integration support team
- A shared Notion doc tracking every open question with SLA for response
- Direct escalation path to their engineering lead for sandbox issues

This reduced our average blocker resolution time from 5 days to 1.5 days.

### Step 4: Sprint Governance and Risk Tracking

I ran 2-week sprints with explicit risk registers. Each sprint retro included a "blockers killed" metric and a "days-at-risk" counter for any item that could slip the timeline. When the AyoConnect sandbox went down for 3 days in Sprint 4, we had already identified this as a top-3 risk and had a local mock server ready as a fallback for continued development.

## Outcome

- **Delivered 2 months ahead of the original 6-month plan** — production launch in Month 4
- **Zero critical defects** in the first 30 days post-launch
- **Payment method coverage** expanded from 1 channel to 3 (VA via 5 banks + 2 e-wallets)
- **Collection rate improvement** of 12% in the first quarter after launch, attributed to reduced payment friction
- **Reusable adapter pattern** adopted by 2 other teams for subsequent third-party integrations
- **Stakeholder trust earned** — was subsequently given ownership of the full payment domain roadmap

## Reflection

**What I'd Do Differently:**

If I could redo this project, I would have pushed for a dedicated QA engineer from Day 1 rather than sharing QA bandwidth with the home screen redesign team. We managed quality through rigorous code review and automated tests, but having dedicated QA earlier would have caught edge cases in the reconciliation pipeline sooner — we found two minor discrepancies in Week 2 post-launch that dedicated QA likely would have caught in staging.

I'd also invest more upfront in contract testing with AyoConnect's API. We relied on their sandbox for integration testing, but a contract test suite would have made us resilient to their sandbox instability and caught API version mismatches earlier.

**What This Demonstrates:**

- Ability to decompose complex integrations into parallel, de-risked workstreams
- Stakeholder negotiation to reduce scope without sacrificing business value
- Proactive partner management that turns external dependencies into manageable risks
- Sprint governance that surfaces risks early and maintains delivery momentum
- Technical product thinking — designing for extensibility (adapter pattern) while shipping fast
