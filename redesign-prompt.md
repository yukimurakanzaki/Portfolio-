# Portfolio redesign brief — "Meridian Noir"

You are redesigning my personal portfolio: this repo, Astro 6 + Tailwind CSS v4, deployed on Vercel. I'm a Product Manager in Jakarta (fintech: payments, lending, internal platforms) looking for Senior/Lead PM roles in Indonesia and SEA. The audience is fintech hiring managers and recruiters who give a portfolio 3–5 minutes, usually on a laptop, often arriving from LinkedIn on a phone.

The site works, but it reads like an AI-generated dark template. I want it to feel expensive: the restraint and typographic care of a well-made annual report or a long-form magazine feature, not a SaaS landing page. I'm not a developer. Make the technical decisions yourself, explain anything you need from me in plain language, and stop at the checkpoint below.

## Read first

- `meridian-noir-philosophy.md` (and `meridian-noir.pdf`): my design philosophy. This redesign finally implements it properly.
- `src/layouts/Layout.astro`, `src/styles/global.css`, everything in `src/components/` and `src/pages/`, `src/content.config.ts`, and every case study in `src/content/case-studies/`.
- `case-study-prompt.md`: the confidentiality and masking rules for anything published. They apply to every word you write.
- Ignore `.kiro/specs/portfolio-redesign/*` and `docs/superpowers/specs/2026-05-27-portfolio-design-refined-dark.md`. They describe the previous direction (Inter/Outfit, slate grays, `#2563EB`, "exactly six nav links"). This brief replaces them.

## Why it looks generated today (remove all of it)

1. `Logo.astro` is a blue→indigo→violet gradient with a glow filter and a pulsing dot, the best-known AI-design fingerprint. `public/favicon.svg` is still the default Astro logo.
2. The hero is the stock template: a tracked uppercase blue eyebrow, a giant ExtraBold name, a filled + ghost button pair, a circular photo with concentric rings, and a blurred blue orb.
3. Hierarchy comes from weight (Outfit 700–800 everywhere) instead of scale and space.
4. Blue is on everything (eyebrows, tags, links, buttons, borders, dots), so it means nothing. A second accent (amber pulsing dots) sneaks in. Text uses cool slate grays that fight the warm off-white of my palette.
5. Every section repeats one pattern: a blue uppercase label, a bold heading, then a bordered `rounded-2xl` box.
6. Pills are everywhere, and "Skills Snapshot" is a keyword cloud.
7. StoryForge gets a fake "sample output" JSON box. Services uses checkmark lists, icon-in-a-rounded-square cards, and hover lift + glow shadows.
8. A full-bleed saturated blue CTA band sits in the middle of a dark site, and a 2px blue line is pinned to the top of every page.
9. `PhoneMockupGroup` draws fake phone chrome, then tilts, floats and glows it.
10. The footer says "Built with Astro + Tailwind CSS". Buttons are Title Case ("Email Me"). The theme toggle is a sun/moon icon.
11. There are no design tokens: hex values are hard-coded per element (`#3B6EEF`, `#060610`, leftover `sky-400` on `how-i-built-this.astro`), each duplicated with `dark:` variants.
12. `global.css` has mobile overflow hacks (`* { min-width: 0 }`, plus `overflow-wrap: anywhere` and `max-width: calc(100vw - 4rem)` on all text) that hide layout bugs instead of fixing them.
13. `og:url` points to the homepage on every page and `og:image` is the headshot. Images are unoptimized (`home.jpg` is 763 KB) and have no width/height.

## Art direction

**Editorial, numerate, quiet.** Type does the work. There are almost no boxes, no glows and no gradients: a near-black "void", warm off-white text, and one point of blue only where it matters most. For mood (feel it, don't copy it), think of Stripe Press book pages, FT Weekend long reads, a private bank's annual report, and museum wall labels.

Three signature devices come from my philosophy. Use them quietly and consistently, never as gimmicks:

- **The meridian.** On screens ≥1024px, one 1px vertical hairline runs from the first section below the hero down to the footer. It sits on the boundary between a narrow label column (grid columns 1–3) and the content column (4–12). Section labels sit left of it and content sits right. The hero above it is free to span the full grid.
- **The north star.** The blue `signal` color appears in only these places: the small solid point beside my availability status (hero and contact), the reading-progress hairline on case studies, focus rings, text selection, and link underlines on hover. Everything else is ink, gray, or hairline. Active-nav and table-of-contents markers use ink, not blue.
- **Field notes.** These are small mono annotations that carry real information, like the labels on a scientific plate: section indices (`§01`), figure captions (`Fig. 2 — Payment method selection, BAF Mobile`), dates, Jakarta's coordinates (`6°10′S 106°49′E`), and live local time (WIB). A label must say something its heading doesn't. Never put "PRODUCT LEADERSHIP" above "Where I create leverage."

My initials spell MAP, which suits a cartography concept. Use that once or twice (favicon monogram, the 404 page), never as a pun in a headline.

## Design system

Define tokens once in `global.css`, with light values on `:root` and dark values under the existing `.dark` class. Register them with Tailwind v4's `@theme` so components use semantic utilities (`bg-void`, `text-ink`, `border-rule`). Components must not contain raw hex values or `dark:` color variants.

### Color

Dark is the default theme. Light is "paper", designed rather than inverted.

| Token | Dark | Light | Use |
|---|---|---|---|
| `void` | `#060610` | `#EDEBE6` | page background |
| `raised` | `#0D0D18` | `#E4E1DA` | rare surfaces (image plates only) |
| `ink` | `#EDEBE6` | `#060610` | primary text (~16.9:1) |
| `ink-2` | `#9C9A96` | `#5E5C58` | secondary text (≥5.5:1) |
| `ink-3` | `#6B6965` | `#8A8780` | large or decorative meta only (≥3:1) |
| `rule` | `rgb(237 235 230 / 0.12)` | `rgb(6 6 16 / 0.14)` | hairlines |
| `signal` | `#3B6EEF` | `#3B6EEF` | the north-star point, progress hairline, focus, selection |
| `signal-text` | `#5C86F5` | `#2B59D6` | blue as small text (rare) |

`#3B6EEF` measures about 4.48:1 on the dark void and 3.8:1 on paper, so it never carries small text. Use `signal-text` for that. All grays stay warm: no slate, zinc, pure black or pure white.

### Type

Load from Google Fonts with only these weights (`display=swap`; preconnect is already set up in `Layout.astro`):

- **IBM Plex Serif** 300, 400, 300 italic: display text and headings.
- **Instrument Sans** 400, 500: body and UI.
- **Geist Mono** 400: labels, data, numbers.

Nothing is bold at display sizes. Hierarchy comes from size, space and color, not weight.

| Role | Font | Size | Line height | Tracking |
|---|---|---|---|---|
| Hero | Plex Serif 300 | `clamp(2.75rem, 1.6rem + 4.6vw, 5.75rem)` | 1.02 | −0.025em |
| Page title | Plex Serif 300 | `clamp(2.25rem, 1.5rem + 3vw, 4rem)` | 1.05 | −0.02em |
| Section heading | Plex Serif 400 | `clamp(1.75rem, 1.35rem + 1.6vw, 2.5rem)` | 1.15 | −0.015em |
| Subheading | Instrument Sans 500 | 1.25rem | 1.3 | −0.01em |
| Lead | Instrument Sans 400 | 1.1875rem | 1.55 | 0 |
| Body | Instrument Sans 400 | 1.0625rem | 1.65 | 0 |
| Small | Instrument Sans 400 | 0.875rem | 1.5 | 0 |
| Label | Geist Mono 400, uppercase | 0.75rem | 1.4 | +0.06em |

- Use italic serif for emphasis, at most one phrase per heading.
- Set `text-wrap: balance` on headings and `text-wrap: pretty` on paragraphs.
- Use tabular lining figures for dates, ledgers, tables and times.
- Keep the body measure to 60–70ch.
- Use curly quotes and apostrophes, en dashes in ranges (2022–2023), and a non-breaking space between a number and its unit ("8 days").
- Use sentence case for every heading, button and link.

### Layout

- Use a 12-column grid with a max content width of 1280px, page gutters of `clamp(1.25rem, 4vw, 4rem)`, and a 24px column gap (16px on mobile).
- Make compositions left-aligned and asymmetric. Nothing is centered except the 404 page.
- Separate sections with space and a full-width hairline, never with a change of background color. Section spacing is `clamp(6rem, 12vw, 10rem)`, with the bottom slightly larger than the top.
- Use 0–2px radius on UI. Screenshots get one consistent radius. No `rounded-2xl` cards.
- Lists of things (work, roles, capabilities, services) are hairline-separated rows, not cards. Use a box only to hold an image.

### Components and states

- **Links:** ink text with a 1px underline in `rule` at a `0.2em` offset. On hover the underline turns `signal` (180ms).
- **Primary action (at most one per view):** a plain rectangle (ink background, void text, 2px radius), or a strong text link whose arrow moves 3px on hover. No pill buttons and no ghost + filled pairs.
- **Press and focus:** pressing moves the element `translateY(1px)`. Every interactive element gets a visible 2px `signal` focus outline with a 3px offset.
- **Theme toggle:** a small mono text button ("Light" / "Dark") instead of sun/moon. Keep the no-flash init script and the dark default.
- **Selection:** `::selection` uses `signal` with white text.

### Motion: slow, short and rare

- Hovers take 180–240ms and entrances 500–700ms, with easing `cubic-bezier(0.2, 0, 0, 1)`. No bounce or spring overshoot.
- **Page transitions:** use native cross-document View Transitions (`@view-transition { navigation: auto; }`) with a ~200ms fade. Give each case-study title the same `view-transition-name` on the index and detail pages so it morphs between them. This needs no JS, and unsupported browsers just navigate normally.
  - Do not use Astro's `<ClientRouter />`. Its client-side navigation stops the existing component scripts (theme toggle, menu, filters) from re-running on new pages.
- **Scroll reveals (optional):** at most once per section, a 12px rise + fade, done in CSS with `animation-timeline: view()` inside `@supports`. Content must be fully visible without JS and in unsupported browsers.
- `prefers-reduced-motion: reduce` turns all of this off, including the view transitions.

## Page by page

### Home (`index.astro`), in this order

1. **Hero.**
   - A mono meta row: "Product Manager — fintech, payments, lending" on the left; "Jakarta 6°10′S 106°49′E · 14:32 WIB" on the right, with the time live.
   - The headline tightens my existing positioning line ("I own the full product lifecycle — from half-formed requirements to production — in regulated fintech environments.") to 14 words or fewer: serif light, with one italic phrase.
   - A status line with the north-star point: "Open to Senior / Lead PM roles — Jakarta & SEA".
   - Actions: "Selected work ↓", my email (click to copy), and "CV — PDF, <real file size>".
   - The portrait is a 4:5 rectangle in black and white (`grayscale(1) contrast(1.05)`), secondary to the headline, placed asymmetrically, with a field-note caption.
   - At 390×844, the headline, status and one action must be visible without scrolling.
2. **§01 Selected work.** An editorial index, not cards.
   - Each row has the index number, the title (serif, large), a meta line (company · role · years), one outcome line, the read time, and an arrow.
   - The first row gets a plate of its real screenshots beneath it: straight, baseline-aligned, captioned, with no fake phone chrome.
   - It ends with "All case studies →".
3. **§02 Track record.** A ledger built from the About page data: years (tabular mono) · company · role · one line of scope. It covers SiCepat → Danamas → BAF, plus the pre-PM line.
4. **§03 Where I'm strongest.** This replaces the skills pill cloud.
   - Write 3–4 capability statements (payment rails, lending platforms, internal ops platforms, delivery systems).
   - Each is one or two plain sentences that link to the case study proving it.
   - Tools become one plain line of mono text.
5. **§04 Currently building: StoryForge.id.** Say what it is in one sentence and give its status. Link to it only if storyforge.id actually loads (it didn't on 2026-10-03). Use a real screenshot if one exists in the repo (otherwise ask me). Never use a fake code box.
6. **§05 Contact.**
   - A large serif closing line.
   - My email as a big underlined link: click to copy, with "Copied" feedback announced via `aria-live`.
   - LinkedIn and the CV.

### Case study page (`case-studies/[slug].astro`), the most important template

- **Header.**
  - The label column holds `Case study 02 / 04`, the company and the years.
  - The title is in display serif, with the shared `view-transition-name`.
  - A dek comes from `summary`.
  - A mono meta strip shows role · timeline · domains (plain text separated by " / ") · read time. No pills.
- **Screenshot plate** when `phoneScreens` exist. Rewrite `PhoneMockupGroup` as a static plate: straight, equal heights, one radius, hairline outline, and `Fig.` captions written from the alt text. No rotation, floating, glow or fake device chrome.
- **Body.** Keep it to 65–70ch and redo the prose styles in the new system:
  - h2 in serif, with its `§` number in the label column;
  - lists as hairline ledgers;
  - blockquotes as pull quotes (serif italic, large, hanging punctuation);
  - tables like a financial statement (tabular figures, hairlines only, no zebra stripes).
- **Table of contents.** On desktop, a sticky table of contents sits in the label column (Context, Problem, Approach, Outcome, Reflection), with the current section marked in ink.
- **Reading progress.** A 1px `signal` hairline replaces the 3px bar.
- **Ending.** Close on the next case study as a large serif link ("Next — <title>"), plus "All case studies".

### Case studies index (`case-studies.astro`)

- Use the same editorial index as Home, listing all studies.
- Filters become plain mono text toggles with counts (`All (4) · Payments (1) · …`) using `aria-pressed`.
- Keep the vanilla JS filter and the empty state.

### Other pages

- **About.**
  - Open with a serif lead paragraph, then the body.
  - Show the portrait as a captioned plate.
  - Turn career history into the ledger (no timeline dots).
  - Make "What I'm looking for" a definition list (term in the label column, text in the content column) instead of four bordered cards.
  - Keep StoryForge consistent with Home.
- **Services.**
  - Put the two offers side by side, separated by a vertical hairline.
  - Use plain hairline lists instead of checkmark icons.
  - Remove the icon squares and the lift/glow hover.
  - Keep "How conversations usually start" as numbered rows.
- **Contact.** The email is the hero element, followed by LinkedIn, the CV and local time. Keep copy-to-clipboard.
- **Playbook.**
  - Restyle only. The RICE calculator, the add-item form, the prioritization board, the delivery-flow items and the velocity chart must behave exactly as before.
  - Give inputs hairline bottom borders and mono numbers.
- **How I built this.**
  - Restyle it as a colophon and link it as "Colophon" from the footer. Keep the URL.
  - Add a short, factual colophon block: typefaces, colors, stack and hosting.
- **New `404.astro`.**
  - "Off the map": the one centered page, with the coordinates `0°00′N 0°00′E`.
  - Link home and to case studies.

### Site-wide elements

- **Nav.**
  - My name as a wordmark (sans 500) linking home.
  - Links: "Case studies", "Playbook", "Services", "About", "Contact", in `ink-2` turning `ink` on hover.
  - Mark the active page in ink and set `aria-current="page"`. Include the theme toggle.
  - Use a solid void background with a hairline bottom border and no blur.
  - On mobile, build a full-screen menu on the native `<dialog>` element (it traps focus and closes on Esc for free), with large serif links and section indices.
- **Footer.** One quiet line: © year and name · email · LinkedIn · CV · Colophon · coordinates. It stacks on mobile.
- **Mark and favicon.**
  - Replace `Logo.astro` and `public/favicon.svg` with a single-color mark: either the meridian line with its point, or a "MAP" monogram in the serif.
  - Use `currentColor` and make it legible at 16px. No gradient, filter or animation.
- **Company logos.** Don't use the raster logos in `Logo/`. Typeset company names look better than mismatched bitmaps.

## Content rules (hard)

- Never invent or "un-mask" a fact: no new metrics, clients, logos, testimonials or claims. Every number on the site must already be in my content. Verifiable facts such as file sizes, dates and coordinates are fine. Apply the `case-study-prompt.md` masking rules to anything new you write.
- You may rewrite headings, labels, buttons and microcopy. Don't rewrite case-study body text beyond typos.
- Avoid these clichés: elevate, seamless, unlock, unleash, empower, leverage, cutting-edge, next-gen, game-changer, delve, journey, passionate, "let's build something amazing". Use no exclamation marks.
- Flag these to me instead of fixing them:
  - The StoryForge copy says "Next.js 14" and "approaching beta". Its repo is on Next.js 16, and on 2026-10-03 storyforge.id didn't resolve. Ask me what status to show.
  - The About page states a 19-person team, which conflicts with my own masking rules.
- Product screenshots are public once shipped. Before you use any of them, including the raw sets in `src/Product/`:
  - check each one for personal or financial data (names, phone numbers, contract or account numbers, balances, ID numbers);
  - crop, blur or skip any that show it;
  - tell me what you found.

## Banned (these are why it looks generated)

- **Effects:**
  - gradients of any kind, especially blue→purple
  - blur orbs and glows
  - glassmorphism and backdrop blur
  - noise or grain overlays
  - drop shadows on cards
- **Layout:**
  - bento grids
  - three equal cards in a row
  - full-bleed colored bands
- **Components:**
  - icon-in-a-rounded-square feature cards
  - pill tags and pill buttons
  - ghost + filled button pairs
  - circular avatars
  - an uppercase eyebrow above every heading
  - floating or tilted mockups
- **Motion:**
  - pulsing dots and marquees
  - count-up numbers and typewriter text
  - custom cursors and magnetic buttons
  - parallax and smooth-scroll hijacking
- **Decoration:** emoji, and sprinkled icons. Use almost none: an arrow and the mark.

If a design skill you have (frontend-design, redesign-skill, taste-skill, …) suggests any of these, this brief wins.

## Constraints

- **Versions and dependencies.**
  - Keep Astro 6 and Tailwind v4 at their current versions, and ignore the "Astro 7 available" notice in the dev log.
  - Add no new npm dependencies without asking me: no GSAP, Framer Motion, Lenis, icon packs or UI kits.
- **Keep what exists.** Keep every existing URL, the CV file, the email and LinkedIn links, and the content collection with its existing fields. You may add optional fields such as `outcome`.
- **Images.**
  - Run photos and screenshots through Astro's built-in image pipeline (`astro:assets` plus the `image()` schema helper): AVIF/WebP, explicit dimensions, lazy-loaded below the fold.
  - No image over ~150 KB.
- **Overflow.** Fix layout overflow at its source and delete the global mobile hacks in `global.css`.
- **Code hygiene.**
  - Keep components small and readable. Create a new one only if it's used twice.
  - Delete what becomes dead (`PhoneMockupGroup`, `SkillTag`, `animate-float`, unused keyframes, the top blue line).
- **SEO.**
  - Give every page its own canonical and `og:url`.
  - Make a designed 1200×630 `public/og.png` in the new style: render a temporary page at that size, screenshot it (e.g. with the Playwright browser tool), then delete the page. If you can't, keep the photo and tell me.
  - Add `Person` JSON-LD to the home page.
- **Accessibility.** Add a skip link.
- **Preview.** Use the existing dev server config (`.claude/launch.json`, port 4321).

## How to work

0. **Prepare.** Run `git status`. If there are uncommitted changes, ask whether I want you to commit them first, so the redesign can be undone cleanly. Leave `src/Product/` out of any commit until its screenshots pass the privacy check. Then create the branch `redesign/meridian-noir`. Don't commit, push or deploy unless I ask.
1. **Baseline.** Confirm `npm run build` passes, then take "before" screenshots of every page at 1440×900 and 390×844.
2. **Phase 1: the system.** Tokens, fonts, base styles, `Layout`, `Nav`, `Footer`, mark, favicon, theme toggle, focus/selection and view transitions.
3. **Phase 2: Home.**
4. **Checkpoint: stop here.** Run the build. Screenshot Home at 1440 and 390 in both themes, run the slop test below, and fix what fails. Then show me before/after and wait for my go-ahead.
5. **Phase 3:** the case-study template and index, including the image pipeline and the screenshot privacy check.
6. **Phase 4:** About, Services, Contact, Playbook, Colophon, 404.
7. **Phase 5:** QA (below), then a final report.

## Slop test

Run this on every page at each checkpoint, and fix failures before showing me:

1. Swap my name for any other PM's. Is the page still true? Then it's generic: find what's specific to me.
2. Squint, or blur the screenshot. Is there exactly one focal point per viewport?
3. Is blue anywhere outside the north-star list?
4. Is every border, box, shadow and label doing a job? Delete any that isn't.
5. Can you point to where each number comes from in my content?
6. Is anything centered, rounded, glowing or moving without a reason?

## Done means

- **Build and console.** `npm run build` passes with zero errors, and no page logs console errors.
- **Responsive.** Screenshot every page at 375, 768, 1280 and 1440 wide, in dark and light, and confirm:
  - no horizontal scroll and no overlap;
  - no single orphaned word in a heading;
  - no word broken mid-word.
- **Keyboard.** Do a keyboard-only pass and confirm:
  - the skip link works and focus is visible everywhere;
  - the menu dialog traps focus and closes on Esc;
  - the filters are operable;
  - `aria-current` and `aria-pressed` are set.
- **Accessibility.**
  - All text meets WCAG AA contrast.
  - Reduced motion is respected.
  - Every image has meaningful alt text and dimensions.
- **Behavior.** The theme persists across pages without a flash, and every Playbook interaction still works.
- **Performance.** If Lighthouse is available, mobile scores are ≥95 for performance and 100 for accessibility, best practices and SEO.
- **Final report.** Write it in plain language for a non-technical owner, covering:
  - what changed;
  - what I should check myself;
  - anything you need me to decide;
  - exactly what to do next: how to preview it, and how to publish when I'm happy.
