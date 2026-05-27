---
title: "Cutting Requirement-to-Development Cycle Time by 50%"
company: "PT Bussan Auto Finance (BAF)"
subtitle: "Product Manager (Official Title: Product Owner & UI/UX Specialist) · Sep 2023 – Present"
summary: "Built Agile delivery infrastructure and sprint governance from scratch across 3 teams — reducing BRD-to-development cycle time by 50%."
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
| **Team** | 3 engineering squads (19 engineers total), no Scrum Master, no BA, no TPM |
| **Stakeholders** | Head of Engineering, Head of Product, Business Unit Heads, Engineering Leads |

When I joined BAF's product team, the organization was in a transitional state. They had recently restructured from a project-based to a product-based model, but the delivery processes hadn't caught up. There was no consistent sprint cadence, no standardized way to translate business requirements into development-ready specifications, and no visibility into delivery timelines for stakeholders.

The result: business stakeholders would submit a Business Requirements Document (BRD), and it would take an average of 6 weeks before engineering began development — with no predictability on when work would actually start or finish.

## Problem

The 6-week BRD-to-development cycle time was a symptom of several interconnected process failures:

1. **No refinement process** — BRDs arrived as 20-40 page documents written in business language with no technical decomposition. Engineers had to interpret requirements themselves, leading to back-and-forth clarification cycles that consumed 2-3 weeks alone.

2. **No sprint structure** — Teams worked in an ad-hoc manner. There was no sprint planning, no backlog grooming, and no predictable delivery cadence. Work started when someone decided it was important enough to escalate.

3. **No capacity planning** — Without sprint velocity data, nobody could answer "when will this be done?" Business stakeholders escalated constantly because they had no visibility into engineering capacity or priorities.

4. **No definition of ready** — Requirements entered development in varying states of completeness. Engineers frequently discovered missing acceptance criteria, undefined edge cases, or unresolved dependencies mid-sprint, causing context-switching and rework.

5. **No cross-team coordination** — The 3 squads had interdependencies (shared APIs, shared databases) but no mechanism to identify or resolve conflicts before they became blockers.

## Approach

### Step 1: Assess and Baseline

Before changing anything, I spent 3 weeks measuring the current state:

- Tracked 15 recent features from BRD submission to first commit, documenting every handoff and wait state
- Identified that 60% of the 6-week cycle was **wait time** (waiting for clarification, waiting for prioritization, waiting for availability) — not active work
- Interviewed all 3 engineering leads and 5 business stakeholders to understand pain points from both sides
- Mapped the informal process that existed (even if undocumented) to understand what was working vs. what was friction

**Key insight**: The problem wasn't engineering speed — it was the absence of a structured intake and refinement process that created unnecessary wait states.

### Step 2: Design the Sprint Framework

I designed and implemented a lightweight Agile framework tailored to BAF's context (no dedicated Scrum Master, engineers resistant to "heavy process"):

**Sprint cadence**: 2-week sprints synchronized across all 3 teams, with aligned ceremonies:
- **Monday Week 1**: Sprint Planning (1.5 hours per team)
- **Friday Week 1**: Backlog Refinement (1 hour per team)
- **Friday Week 2**: Sprint Review + Retro (1 hour per team)
- **Daily**: 15-minute standup (async on Slack for remote days)

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

**Week 1 (Intake)**: I receive BRD, conduct initial feasibility assessment, identify questions and gaps, schedule stakeholder clarification session.

**Week 2 (Decomposition)**: Break BRD into user stories with acceptance criteria. Technical spike if needed. Dependency mapping across teams.

**Week 3 (Ready for Sprint)**: Stories meet DoR, estimated by team, prioritized in backlog. Ready for next sprint planning.

This 3-week pipeline replaced the previous unstructured 6-week drift. The key difference: every stage has a clear owner, a clear output, and a clear SLA.

### Step 4: Implement Visibility and Governance

To maintain stakeholder trust and sustain the new process:

- **Jira board** configured with swim lanes per team, visible to all stakeholders
- **Weekly status email** to VP Product and business unit heads showing: what shipped last week, what's in progress, what's coming next sprint, and any blockers
- **Monthly delivery metrics** report: velocity per team, cycle time trend, scope change rate, blocker resolution time
- **Quarterly retro** with all 3 teams together to identify cross-team process improvements

## Outcome

- **BRD-to-development cycle time reduced from 6 weeks to 3 weeks** (50% reduction) within 4 months of implementation
- **Sprint predictability** reached 82% (stories planned vs. stories completed) by Month 3, up from effectively 0% (no sprints existed)
- **Stakeholder escalations reduced by 70%** — visibility into delivery timelines eliminated most "when will this be done?" interruptions
- **Zero missed regulatory deadlines** in the 6 months following implementation (previously averaged 1 missed deadline per quarter)
- **Engineering satisfaction** improved — retro feedback consistently cited "clarity on what to work on" and "fewer mid-sprint changes" as top improvements
- **Cross-team blockers** reduced from average 3 per sprint to 0.5 per sprint through the dependency identification step in refinement

## Reflection

**What I'd Do Differently:**

I would have introduced the Definition of Ready more gradually. Rolling it out fully in Week 1 created initial friction — teams felt like I was adding bureaucracy. In hindsight, starting with just 2-3 DoR criteria and expanding over 2 months as teams saw the value would have reduced resistance and built buy-in more organically.

I'd also invest earlier in automation. For the first 3 months, I was manually tracking cycle time metrics in a spreadsheet. Building a Jira dashboard with automated cycle time calculations from Day 1 would have freed up 3-4 hours per week and given stakeholders self-serve access to delivery data.

Finally, I underestimated the importance of celebrating wins publicly. The teams were doing significantly better work with the new process, but I didn't create enough visibility for their improvements with senior leadership. More deliberate "show and tell" moments would have reinforced the behavior change and built engineering team morale.

**What This Demonstrates:**

- Ability to diagnose process problems through data and observation rather than assumptions
- Designing lightweight Agile frameworks appropriate to organizational context (no SM/BA/TPM)
- Change management — introducing process change to resistant teams by demonstrating value incrementally
- Cross-functional coordination across 3 engineering teams with interdependencies
- Metrics-driven approach to process improvement with clear before/after measurement
- Stakeholder management — converting escalation-driven communication into structured, proactive visibility
