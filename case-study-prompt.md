# Case Study Generation Prompt

Paste the prompt below into a Claude.ai chat that contains your brainstorm / requirement
analysis (or attach that history to a new chat). It outputs a publish-ready, confidentiality-safe
case study that drops straight into `src/content/case-studies/`.

---

```
You are helping me turn a Claude.ai conversation into a portfolio case study.

CONTEXT
I'm a Product Manager building a public portfolio. The conversation above (or attached)
contains real brainstorming / requirement analysis I did on a project. Read ALL of it
carefully and extract the story into the EXACT format below. This will be saved as a Markdown
file in an Astro site, so the structure must match precisely.

⚠️ CONFIDENTIALITY — THIS IS PUBLIC AND MOST OF MY SOURCE MATERIAL IS UNDER NDA.
Before writing, mask anything confidential. Apply these rules:
- METRICS: Never publish exact internal numbers (revenue, NPS, conversion/collection rates,
  cycle times, deployment times, team sizes, user counts, percentages). Convert them to
  RELATIVE impact instead:
    "+12% collection rate"        → "double-digit improvement in collection rates"
    "NPS +18 → +52"               → "satisfaction improved substantially"
    "6 weeks → 3 weeks"           → "roughly halved the cycle time"
    "19 engineers, no SM/BA/TPM"  → "three squads, without dedicated SM/BA/TPM support"
- PARTNERS/VENDORS: Never criticize a named partner or vendor (e.g. "their sandbox was
  unstable", "their docs had gaps"). Reframe neutrally as a managed external dependency.
- INTERNAL SYSTEMS: Genericize internal architecture, tech stack specifics, internal data
  problems, and org structure. Say "an aging legacy system", not the exact stack/version.
- NO "THE COMPANY WAS BROKEN" FRAMING: Describe weak prior states as growth-stage context
  ("processes were still maturing"), and never imply prior compliance gaps (say "passed the
  audit cleanly", NOT "previously had findings").
- Company names ARE allowed (my employment is already public via my CV/LinkedIn). The risk is
  the internal detail, not the employer name.

HONESTY RULES
- Use ONLY facts and decisions that appear in the conversation.
- If a detail is NOT in the conversation, DO NOT invent it. Insert a placeholder like
  [DETAIL NEEDED: timeline] and list every placeholder at the very end under
  "## ❓ Gaps to fill before publishing".
- Masking ≠ inventing. Make real numbers vaguer; never fabricate achievements.

OUTPUT FORMAT — produce one Markdown file exactly like this:

---
title: "..."                # max 100 chars, the case study headline (relative claims only)
company: "..."              # real company / product name
subtitle: "Role · Mon YYYY – Mon YYYY"
summary: "..."              # max 300 chars, one-paragraph hook (no exact metrics)
tags: ["...", "..."]        # 1–8 tags, e.g. "0-to-1", "Platform", "Discovery", "Delivery"
readTime: "X min read"      # estimate, e.g. "6 min read"
slug: "lowercase-with-hyphens"   # url-safe, max 80 chars
order: 99                   # leave as 99, I'll set ordering myself
---

## Context
A short intro paragraph, then a Markdown table:
| Attribute | Detail |
|-----------|--------|
| **Company** | ... |
| **Product** | ... |
| **Role** | ... |
| **Timeline** | ... |
| **Team** | ... (generic composition, no headcount) |
| **Stakeholders** | ... (roles, not names) |

Then 1–2 paragraphs of background.

## Problem
One framing paragraph, then a numbered list of specific problems, each with a **bold lead-in**.

## Approach
### Step 1, ### Step 2, etc. — each a phase (discovery, architecture, delivery, rollout).
Pull the actual decisions, trade-offs, and reasoning from the conversation.

## Outcome
A bulleted list of results, each with a **bold relative headline** (no exact internal numbers).

## Reflection
**What I'd Do Differently:**
2–3 honest paragraphs.

**What This Demonstrates:**
A bulleted list of the PM skills this case study proves.

## ❓ Gaps to fill before publishing
List every [DETAIL NEEDED] placeholder AND flag anything you masked that I might want to
double-check before publishing.

TONE: first-person, confident but specific, no marketing fluff. Senior-PM voice for hiring
managers. Indonesian context (OJK, Rupiah, regulators) is fine where relevant.
```

---

## How to use
1. Open Claude.ai, go to the chat with your brainstorm/requirements (or attach it).
2. Paste the prompt above.
3. Review the output — especially **❓ Gaps to fill** and anything it masked.
4. Save the final Markdown into `src/content/case-studies/your-slug.md`, then set `order`
   and add phone screenshots.
