# Portfolio Design Spec — Refined Dark (Option A)

**Date:** 2026-05-27  
**Status:** Selected — pending implementation  
**Owner:** Muhammad Adi Putra

---

## Summary

Evolve the existing dark portfolio from "solid and professional" to "premium and distinctive" — without structural changes or risk to the fintech hiring manager audience. The design stays dark (appropriate for tech/fintech) but becomes more editorial, typographically bolder, and visually differentiated from generic PM portfolios.

Target audience: hiring managers and recruiters at fintech companies in Jakarta and SEA.

---

## Color & Visual Identity

| Token | Current | Proposed |
|---|---|---|
| Primary bg | `#0f172a` | `#0a0f1e` |
| Surface cards | `bg-white/5` | `bg-white/[0.04]` + `border-white/8` |
| Accent (primary) | `#2563EB` | `#3B82F6` |
| Accent (highlight) | — | `#F59E0B` amber for stat callouts & domain labels |
| Hero overlay | single soft glow | radial gradient glow + CSS grain texture |
| Body font | Outfit 400–800 | Outfit 400–800 (unchanged) |
| Mono font | none | JetBrains Mono for tags, code snippets, labels |

---

## Hero Section

- Name (`h1`) scales to `text-8xl` with `tracking-tighter`
- Above the name: a monospace amber label `> Senior PM · Fintech · Payments` using JetBrains Mono
- Subheading tightens to one punchy sentence
- Background: CSS grain texture at `opacity-[0.03]` + two layered radial glows (blue left, faint amber right)
- Profile photo: `ring-2 ring-[#3B82F6]/30` + soft glow `shadow-[0_0_40px_#3B82F6/15]`

---

## Case Study Cards

- Left border accent on hover: `border-l-2 border-[#3B82F6]` animates in on hover
- Featured card: darker inner surface `bg-white/[0.06]`
- Tags: switch from `rounded-full` to `rounded-md`; domain tags (Fintech, Payments) use amber tint, others use blue
- "Read case study →" arrow slides right on hover with extended gap transition

---

## Navigation

- `AP` logo badge gets `shadow-[0_0_12px_rgba(59,130,246,0.5)]`
- Nav links: `text-slate-400` default → `text-white` on hover (higher contrast than current)
- Mobile menu: unchanged

---

## Footer

- Single horizontal rule with left-to-right gradient fade (`from-slate-800 to-transparent`)
- Social/contact icons use amber on hover

---

## Typography Scale

| Element | Spec |
|---|---|
| `h1` | Outfit ExtraBold 800, `clamp(4rem, 8vw, 6rem)`, `tracking-tighter` |
| `h2` | Outfit Bold 700, `text-3xl`, `tracking-tight` |
| Body prose | Outfit Regular 400, `text-slate-400`, `leading-relaxed` |
| Labels/tags/badges | JetBrains Mono 500, `text-xs uppercase tracking-wider` |
| CTA buttons | Outfit SemiBold 600, `px-8 py-4` |

---

## What This Is Not

- No structural page changes (no new pages, no nav changes)
- No layout restructuring (sections stay in current order)
- No content changes (copy, case studies, skills unchanged)

---

## Implementation Notes

- Add `JetBrains Mono` from Google Fonts to `Layout.astro`
- Update CSS custom properties in `global.css`
- Update accent color references across all `.astro` files
- Add grain texture as a CSS `background-image` on the hero section
- Update card hover states in `CaseStudyCard.astro`
