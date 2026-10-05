# Implementation Plan: Portfolio Redesign

## Overview

Refactor the PM portfolio from a monolithic, dark-only Astro site into a content-driven, themeable architecture with extracted components, content collections for case studies, dark/light mode, and a new blue-600 design system. Implementation is ordered: design system → content collection → components → layout refactor → pages → interactivity.

## Tasks

- [x] 1. Design system and global styles
  - [x] 1.1 Update global.css with new design tokens
    - Replace accent color from sky-400 (#38bdf8) to blue-600 (#2563EB)
    - Remove navy color palette, add `--color-accent: #2563EB`
    - Keep `--font-sans: 'Inter', system-ui, sans-serif`
    - Add base layer rule for `html { scroll-behavior: smooth }`
    - Remove body background/color from CSS (moved to Tailwind classes in Layout)
    - _Requirements: 7.1, 7.2_

- [x] 2. Content collection setup
  - [x] 2.1 Create content.config.ts with Zod schema
    - Define `case-studies` collection using `glob` loader pointing to `./src/content/case-studies`
    - Schema fields: title (string 1–100), company (string), subtitle (optional string), summary (string 1–300), tags (array 1–8 strings), readTime (regex `^\d+ min read$`), slug (string 1–80, regex `^[a-z0-9-]+$`), order (int ≥ 1)
    - Export `collections` object
    - _Requirements: 1.1, 1.2_

  - [x] 2.2 Create three case study markdown files
    - Create `src/content/case-studies/shipping-payment-gateway-integration.md` (order: 1)
    - Create `src/content/case-studies/rebuilding-fintech-lending-platform.md` (order: 2)
    - Create `src/content/case-studies/cutting-cycle-time.md` (order: 3)
    - Each file must have valid frontmatter and five sections: Context, Problem, Approach, Outcome, Reflection
    - _Requirements: 1.3, 2.1, 2.4_

  - [ ]* 2.3 Write property test for schema validation round-trip
    - **Property 1: Schema validation round-trip**
    - **Validates: Requirements 1.1, 1.2**

  - [ ]* 2.4 Write property test for case study ordering
    - **Property 2: Case study ordering**
    - **Validates: Requirements 1.4, 1.5**

- [x] 3. Component extraction
  - [x] 3.1 Create ThemeToggle.astro component
    - Create `src/components/ThemeToggle.astro`
    - Render button with sun/moon SVG icons toggling via `dark:hidden`/`dark:block`
    - Inline script toggles `dark` class on `<html>` and persists to localStorage
    - Include focus ring (2px outline) for keyboard accessibility
    - _Requirements: 6.2, 6.3, 6.5, 6.8, 7.5, 9.5_

  - [x] 3.2 Create Nav.astro component
    - Create `src/components/Nav.astro`
    - Accept `currentPath` prop; render 6 nav links: Home, Case Studies, PM Playbook, Services, About, Contact
    - Remove "How I Built This" from nav (page still accessible via direct URL)
    - Import and render ThemeToggle in both desktop and mobile views
    - Desktop nav visible at md (768px+), hamburger menu below 768px
    - Mobile menu toggle with inline script
    - Active link highlighted with blue-600 color
    - All links have focus:ring-2 for keyboard accessibility
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 7.5, 9.1_

  - [x] 3.3 Create Footer.astro component
    - Create `src/components/Footer.astro`
    - Copyright line with dynamic year, "Built with Astro + Tailwind CSS"
    - Links: Contact, LinkedIn
    - Dark/light mode compatible colors
    - Focus indicators on links
    - _Requirements: 9.1, 7.5_

  - [x] 3.4 Create CaseStudyCard.astro component
    - Create `src/components/CaseStudyCard.astro`
    - Props: title, company, summary, tags (string[]), slug
    - Render as anchor link to `/case-studies/{slug}`
    - Include `data-tags` attribute with comma-joined tags for filtering
    - Display company name, title, summary (≤200 chars), and tag pills
    - Dark/light mode compatible styling with blue-600 accent
    - Focus ring on card link
    - _Requirements: 3.2, 9.3, 7.1, 7.5_

  - [x] 3.5 Create SkillTag.astro component
    - Create `src/components/SkillTag.astro`
    - Props: label (string)
    - Render span with blue-tinted background, blue-600 text, rounded-full
    - Dark/light compatible
    - _Requirements: 9.4_

  - [ ]* 3.6 Write property test for CaseStudyCard rendering
    - **Property 5: CaseStudyCard renders all required fields**
    - **Validates: Requirements 3.2, 9.3**

  - [ ]* 3.7 Write property test for SkillTag rendering
    - **Property 11: SkillTag renders label**
    - **Validates: Requirements 9.4**

- [x] 4. Layout refactor
  - [x] 4.1 Refactor Layout.astro to use extracted components
    - Import Nav.astro and Footer.astro
    - Add inline theme init script in `<head>` (before paint) to prevent FOUC
    - Set `class="dark"` on `<html>` element as default
    - Apply `bg-white dark:bg-[#0f172a] text-slate-900 dark:text-slate-200` on `<body>`
    - Pass `currentPath` to Nav component
    - Remove inline nav/footer markup (replaced by component imports)
    - _Requirements: 6.1, 6.4, 6.5, 6.6, 6.7, 6.9, 9.2_

  - [ ]* 4.2 Write property test for theme toggle round-trip
    - **Property 9: Theme toggle round-trip**
    - **Validates: Requirements 6.2, 6.3**

  - [ ]* 4.3 Write property test for theme fallback to dark
    - **Property 10: Theme fallback to dark for invalid localStorage**
    - **Validates: Requirements 6.1, 6.9**

- [x] 5. Checkpoint - Verify foundation
  - Ensure all tests pass, ask the user if questions arise.

- [x] 6. Homepage rebuild
  - [x] 6.1 Rebuild index.astro with 5-section layout
    - Import Layout, CaseStudyCard, SkillTag from components
    - Fetch case studies from content collection, sort by order ASC (title ASC tie-breaker)
    - **Hero section**: Name, title "Senior Product Manager — Jakarta", tagline, CTA buttons (View Case Studies → /case-studies, Get in Touch → /contact, Download CV → /MuhammadAdiPutra_CV.pdf)
    - **Case Study Highlights**: Grid of CaseStudyCard components; hide section if collection is empty
    - **Skills Snapshot**: Grouped SkillTag components by category (≥2 categories, ≥1 tag each)
    - **StoryForge Callout**: Heading, description, link to storyforge.id
    - **CTA Strip**: Heading, supporting text, link to /contact
    - All sections use dark/light Tailwind classes
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 1.4, 1.5_

  - [ ]* 6.2 Write property test for case study sections completeness
    - **Property 3: Case study sections completeness**
    - **Validates: Requirements 2.1**

- [x] 7. Case study pages
  - [x] 7.1 Create case study index page (src/pages/case-studies.astro)
    - Fetch all case studies from content collection, sort by order
    - Render CaseStudyCard for each entry
    - Add tag filter buttons: All, Payments, 0-to-1, Platform, Delivery, Process
    - "All" button active by default, all cards visible
    - Inline vanilla JS script for tag filtering (show/hide via `data-tags` attribute)
    - Empty-state message when no case studies match filter
    - Dark/light mode compatible
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7_

  - [x] 7.2 Create dynamic case study page (src/pages/case-studies/[slug].astro)
    - Use `getStaticPaths` to generate routes from content collection
    - Display title, company, subtitle, readTime, tags
    - Render markdown content (Context, Problem, Approach, Outcome, Reflection sections)
    - Add reading progress bar (fixed div at top, width 0-100% based on scroll)
    - Add bottom navigation: "Back to Case Studies" link → /case-studies, "Next Case Study" link with wraparound logic
    - Inline script for progress bar using requestAnimationFrame
    - Unknown slugs handled by Astro's static generation (404)
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 2.1, 2.2, 2.3_

  - [ ]* 7.3 Write property test for tag filter correctness
    - **Property 4: Tag filter correctness**
    - **Validates: Requirements 4.4, 4.5**

  - [ ]* 7.4 Write property test for reading progress calculation
    - **Property 7: Reading progress calculation**
    - **Validates: Requirements 5.3**

  - [ ]* 7.5 Write property test for case study navigation wraparound
    - **Property 8: Case study navigation wraparound**
    - **Validates: Requirements 5.4, 5.5**

  - [ ]* 7.6 Write property test for case study page content integrity
    - **Property 6: Case study page content integrity**
    - **Validates: Requirements 5.1, 5.2**

- [ ] 8. Existing pages update
  - [-] 8.1 Update playbook.astro styling
    - Keep existing content/functionality
    - Update accent color references from sky-400 to blue-600
    - Add dark/light mode Tailwind classes (dark: variants)
    - Ensure focus indicators on interactive elements
    - _Requirements: 7.1, 7.5_

  - [-] 8.2 Update services.astro styling
    - Keep existing content/functionality
    - Update accent color references from sky-400 to blue-600
    - Add dark/light mode Tailwind classes (dark: variants)
    - Ensure focus indicators on interactive elements
    - _Requirements: 7.1, 7.5_

  - [-] 8.3 Create About page placeholder (src/pages/about.astro)
    - Use Layout wrapper
    - Render heading, biographical summary with [PLACEHOLDER] marker, career history section with [PLACEHOLDER] marker
    - Dark/light mode compatible
    - _Requirements: 10.1, 10.3, 10.4_

  - [-] 8.4 Create Contact page placeholder (src/pages/contact.astro)
    - Use Layout wrapper
    - Render heading, at least one actionable contact method (email link)
    - Include [PLACEHOLDER] markers for content to be filled later
    - Dark/light mode compatible
    - _Requirements: 10.2, 10.3, 10.4_

- [~] 9. Checkpoint - Full integration
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 10. Build verification
  - [~] 10.1 Verify astro build completes with exit code 0
    - Run `astro build` and confirm zero TypeScript errors
    - Confirm no external JS files in build output (only inline scripts)
    - Confirm package.json has only astro, tailwindcss, @tailwindcss/vite as dependencies
    - _Requirements: 11.1, 11.2, 11.3, 11.4_

- [~] 11. Final checkpoint
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties from the design document
- Unit tests validate specific examples and edge cases
- No new npm dependencies — only astro, tailwindcss, and @tailwindcss/vite
- All JavaScript is inline `<script>` tags only (no external JS)
- Pages `playbook.astro` and `services.astro` retain content but get new design system styling
- `how-i-built-this.astro` remains at its URL but is removed from navigation

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["2.1", "3.5"] },
    { "id": 2, "tasks": ["2.2", "3.1", "2.3"] },
    { "id": 3, "tasks": ["3.2", "3.3", "3.4", "2.4"] },
    { "id": 4, "tasks": ["3.6", "3.7", "4.1"] },
    { "id": 5, "tasks": ["4.2", "4.3", "6.1"] },
    { "id": 6, "tasks": ["7.1", "7.2", "8.1", "8.2", "8.3", "8.4"] },
    { "id": 7, "tasks": ["6.2", "7.3", "7.4", "7.5", "7.6"] },
    { "id": 8, "tasks": ["10.1"] }
  ]
}
```
