---
title: "Cutting Requirement-to-Development Cycle Time in Half"
company: "PT Bussan Auto Finance (BAF)"
subtitle: "Product Manager (Official Title: Product Owner & UI/UX Specialist) · Sep 2023 – Present"
summary: "Built Agile delivery infrastructure and sprint governance from scratch across 3 teams — roughly halving BRD-to-development cycle time."
tags: ["Process", "Delivery"]
readTime: "5 min read"
slug: "cutting-cycle-time"
order: 3
---

## Context

| Attribute | Detail |
|-----------|--------|
| **Company** | PT Bussan Auto Finance (BAF) — a multi-finance subsidiary of Mitsui & Co. |
| **Product** | BAF's digital product portfolio (Mobile App, Web Portal, Internal Tools) |
| **Role** | Product Manager (Official Title: Product Owner & UI/UX Specialist) responsible for delivery process across 3 engineering teams |
| **Timeline** | September 2023 – Present |
| **Team** | Three engineering squads, without dedicated Scrum Master, BA, or TPM support |
| **Stakeholders** | Engineering and Product leadership, Business Unit Heads, Engineering Leads |

When I joined BAF's product team, the organization was in the middle of a healthy transition — it had recently restructured from a project-based to a product-based model, and the delivery processes were still maturing to match. There was no consistent sprint cadence yet, no standardized way to translate business requirements into development-ready specifications, and limited visibility into delivery timelines for stakeholders.

The result: business stakeholders would submit a Business Requirements Document (BRD), and it would take several weeks before engineering began development — with little predictability on when work would actually start or finish.

## Problem

The lengthy BRD-to-development cycle time was a symptom of several interconnected process gaps:

1. **No refinement process** — BRDs arrived as lengthy documents written in business language with no technical decomposition. Engineers had to interpret requirements themselves, leading to back-and-forth clarification cycles that consumed a large chunk of the timeline.

2. **No sprint structure** — Teams worked in an ad-hoc manner. There was no sprint planning, no backlog grooming, and no predictable delivery cadence. Work started when someone decided it was important enough to escalate.

3. **No capacity planning** — Without sprint velocity data, nobody could reliably answer "when will this be done?" Business stakeholders escalated frequently because they had limited visibility into engineering capacity or priorities.

4. **No definition of ready** — Requirements entered development in varying states of completeness. Engineers frequently discovered missing acceptance criteria, undefined edge cases, or unresolved dependencies mid-sprint, causing context-switching and rework.

5. **No cross-team coordination** — The squads had interdependencies (shared APIs, shared databases) but no mechanism to identify or resolve conflicts before they became blockers.

## Approach

### Step 1: Assess and Baseline

Before changing anything, I spent a few weeks measuring the current state:

- Tracked a sample of recent features from BRD submission to first commit, documenting every handoff and wait state
- Found that the majority of the cycle was **wait time** (waiting for clarification, prioritization, or availability) — not active work
- Interviewed the engineering leads and business stakeholders to understand pain points from both sides
- Mapped the informal process that existed (even if undocumented) to understand what was working vs. what was friction

**Key insight**: The problem wasn't engineering speed — it was the absence of a structured intake and refinement process that created unnecessary wait states.

### Step 2: Design the Sprint Framework

I designed and implemented a lightweight Agile framework tailored to BAF's context (no dedicated Scrum Master, engineers wary of "heavy process"):

**Sprint cadence**: 2-week sprints synchronized across all teams, with aligned ceremonies:
- **Monday Week 1**: Sprint Planning
- **Friday Week 1**: Backlog Refinement
- **Friday Week 2**: Sprint Review + Retro
- **Daily**: short standup (async on chat for remote days)

**Definition of Ready** (DoR) — a checklist that every ticket must satisfy before entering a sprint:
- User story with acceptance criteria
- Technical approach documented (by engineer, reviewed by lead)
- Dependencies identified and resolved or explicitly accepted as risks
- Design assets attached (if UI work)
- Estimated in story points by the team

**Definition of Done** (DoD):
- Code reviewed and merged
- Unit tests passing
- QA sign-off on staging
- Documentation updated (if API change)
- Product sign-off on acceptance criteria

### Step 3: Build the Refinement Pipeline

The biggest cycle time reduction came from creating a structured refinement pipeline between BRD submission and sprint entry:

**Stage 1 (Intake)**: I receive the BRD, conduct an initial feasibility assessment, identify questions and gaps, and schedule a stakeholder clarification session.

**Stage 2 (Decomposition)**: Break the BRD into user stories with acceptance criteria. Technical spike if needed. Dependency mapping across teams.

**Stage 3 (Ready for Sprint)**: Stories meet the DoR, are estimated by the team, and prioritized in the backlog — ready for the next sprint planning.

This structured pipeline replaced the previous unstructured drift. The key difference: every stage has a clear owner, a clear output, and a clear SLA.

### Step 4: Implement Visibility and Governance

To maintain stakeholder trust and sustain the new process:

- **Jira board** configured with swim lanes per team, visible to all stakeholders
- **Weekly status email** to product leadership and business unit heads showing what shipped, what's in progress, what's coming next sprint, and any blockers
- **Monthly delivery metrics** report: velocity per team, cycle time trend, scope change rate, blocker resolution time
- **Quarterly retro** with all teams together to identify cross-team process improvements

## Outcome

- **Roughly halved BRD-to-development cycle time** within a few months of implementation
- **Sprint predictability** went from effectively none (no sprints existed) to consistently high within months
- **Stakeholder escalations dropped sharply** — visibility into delivery timelines eliminated most "when will this be done?" interruptions
- **Consistently met regulatory deadlines** in the months following implementation
- **Engineering satisfaction improved** — retro feedback consistently cited "clarity on what to work on" and "fewer mid-sprint changes" as top improvements
- **Cross-team blockers became rare**, thanks to the dependency identification step in refinement

## Reflection

**What I'd Do Differently:**

I would have introduced the Definition of Ready more gradually. Rolling it out fully at once created initial friction — teams felt like I was adding bureaucracy. In hindsight, starting with just a few DoR criteria and expanding over time as teams saw the value would have reduced resistance and built buy-in more organically.

I'd also invest earlier in automation. For the first few months, I was manually tracking cycle time metrics in a spreadsheet. Building a Jira dashboard with automated cycle time calculations from the start would have freed up several hours per week and given stakeholders self-serve access to delivery data.

Finally, I underestimated the importance of celebrating wins publicly. The teams were doing significantly better work with the new process, but I didn't create enough visibility for their improvements with senior leadership. More deliberate "show and tell" moments would have reinforced the behavior change and built team morale.

**What This Demonstrates:**

- Ability to diagnose process problems through data and observation rather than assumptions
- Designing lightweight Agile frameworks appropriate to organizational context (no SM/BA/TPM)
- Change management — introducing process change to skeptical teams by demonstrating value incrementally
- Cross-functional coordination across multiple engineering teams with interdependencies
- Metrics-driven approach to process improvement with clear before/after measurement
- Stakeholder management — converting escalation-driven communication into structured, proactive visibility
