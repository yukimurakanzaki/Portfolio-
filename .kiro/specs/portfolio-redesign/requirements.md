# Requirements Document

## Introduction

A complete redesign of Muhammad Adi Putra's portfolio website, repositioning it from a general PM portfolio to a targeted showcase for Senior/Lead PM roles at fintech companies in Jakarta and SEA. The redesign introduces a content collection architecture for case studies, dark/light theme support, streamlined navigation retaining all key sections (including PM Playbook and Services), and a content-first layout optimized for hiring managers who spend 3-5 minutes evaluating candidates.

The site retains the existing Astro 6.0.4 + Tailwind CSS v4 stack deployed on Vercel, with Inter font from Google Fonts.

## Glossary

- **Portfolio_Site**: The Astro-based portfolio website being redesigned
- **Content_Collection**: Astro's built-in content collection system that reads structured markdown files from a defined directory with a schema
- **Case_Study**: A detailed narrative markdown file describing a product management achievement with context, approach, and outcomes
- **Theme_Toggle**: A UI control that switches between dark mode and light mode display
- **Tag_Filter**: A client-side vanilla JS filter mechanism on the case study index page that shows/hides case studies by category
- **Reading_Progress_Bar**: A visual indicator showing how far the user has scrolled through a case study page
- **Slug**: A URL-friendly string identifier derived from the case study title, used for dynamic routing
- **CTA_Strip**: A call-to-action section at the bottom of the homepage encouraging visitors to get in touch
- **Skills_Snapshot**: A grouped display of skill tags on the homepage showing PM competencies by category
- **StoryForge_Callout**: A section on the homepage highlighting the StoryForge.id side project

## Requirements

### Requirement 1: Content Collection Architecture

**User Story:** As a site maintainer, I want case studies stored as structured markdown files in an Astro content collection, so that I can add, edit, and reorder case studies without modifying component code.

#### Acceptance Criteria

1. THE Portfolio_Site SHALL define a content collection at `src/content/case-studies/` with a schema enforcing fields: title (string, 1–100 characters), summary (string, 1–300 characters), tags (array of strings, 1–8 items), readTime (string matching the pattern "<number> min read"), slug (string, 1–80 characters, lowercase alphanumeric and hyphens only), and order (integer, minimum 1)
2. WHEN a markdown file in the case-studies collection is missing a required schema field or a field value fails its type or constraint validation, THE Portfolio_Site SHALL produce a build-time validation error identifying the file and the invalid field
3. THE Portfolio_Site SHALL contain exactly three case study markdown files: "shipping-payment-gateway-integration", "rebuilding-fintech-lending-platform", and "cutting-cycle-time"
4. THE Portfolio_Site SHALL sort case studies by the order field in ascending numeric order when rendering lists
5. IF two or more case study files share the same order value, THEN THE Portfolio_Site SHALL sort those entries alphabetically by title as a secondary sort key

### Requirement 2: Case Study Content

**User Story:** As a hiring manager, I want to read detailed case studies that demonstrate end-to-end problem ownership and measurable outcomes, so that I can assess the candidate's fitness for a Senior PM role.

#### Acceptance Criteria

1. THE Portfolio_Site SHALL render each case study with five visible, labeled sections displayed in this order: Context, Problem, Approach, Outcome, and Reflection, where each section contains at least one paragraph of text
2. THE Portfolio_Site SHALL display the readTime value from the content collection schema on each case study page, formatted as a whole number followed by "min read" (e.g., "5 min read")
3. THE Portfolio_Site SHALL display associated tags from the content collection schema on each case study page, showing a minimum of 1 and a maximum of 6 tags per case study
4. WHEN a case study is rendered, THE Portfolio_Site SHALL pull all content from the Astro content collection and not from hardcoded component markup
5. IF a case study entry in the content collection is missing any of the five required sections, THEN THE Portfolio_Site SHALL fail the build and report an error indicating which section is absent

### Requirement 3: Homepage Layout

**User Story:** As a visitor, I want to see a concise homepage that immediately communicates who this person is and what they have achieved, so that I can decide within seconds whether to explore further.

#### Acceptance Criteria

1. THE Portfolio_Site SHALL render the homepage with sections in this order from top to bottom: Hero, Case Study Highlights, Skills Snapshot, StoryForge Callout, CTA Strip
2. WHEN the homepage is loaded, THE Portfolio_Site SHALL display the Case Study Highlights section by rendering a card for each case study entry, where each card displays the company name, case study title, a summary of no more than 200 characters, and at least 1 tag
3. IF the case study collection contains zero entries, THEN THE Portfolio_Site SHALL hide the Case Study Highlights section entirely
4. THE Portfolio_Site SHALL display the Skills Snapshot section with skill tags grouped by category, rendering at least 2 categories and at least 1 tag per category
5. THE Portfolio_Site SHALL display a StoryForge Callout section containing a heading, a descriptive sentence, and a hyperlink navigating to StoryForge.id
6. THE Portfolio_Site SHALL display a CTA Strip section containing a heading, a supporting sentence, and a link navigating to the contact page

### Requirement 4: Case Study Index Page

**User Story:** As a hiring manager, I want to filter case studies by domain tag, so that I can quickly find case studies relevant to my company's needs.

#### Acceptance Criteria

1. THE Portfolio_Site SHALL render a case study index page at the `/case-studies` route displaying all case studies from the content collection, where each case study entry shows at minimum the company name, case study title, and associated domain tags
2. THE Portfolio_Site SHALL display tag filter buttons with labels: All, Payments, 0-to-1, Platform, Delivery, Process
3. WHEN the page loads, THE Tag_Filter SHALL display all case studies with the "All" filter button in an active visual state
4. WHEN a tag filter button is clicked, THE Tag_Filter SHALL hide case studies whose tags array does not include the selected tag and visually indicate the clicked button as the active filter
5. WHEN the "All" filter button is clicked, THE Tag_Filter SHALL display all case studies regardless of tags
6. IF no case studies match the selected tag filter, THEN THE Tag_Filter SHALL display an empty-state message indicating no case studies match the selected filter
7. THE Tag_Filter SHALL use client-side vanilla JavaScript with no external dependencies

### Requirement 5: Individual Case Study Pages

**User Story:** As a hiring manager, I want to read a case study on a dedicated page with clear navigation, so that I can focus on the narrative without distraction.

#### Acceptance Criteria

1. THE Portfolio_Site SHALL generate dynamic routes at `/case-studies/[slug]` for each case study in the content collection, where the slug is derived by converting the case study title to lowercase, replacing spaces with hyphens, and removing non-alphanumeric characters other than hyphens
2. THE Portfolio_Site SHALL display each individual case study page with the case study's title, company name, subtitle, problem section, approach section, outcome section, tags, and key impact points
3. THE Portfolio_Site SHALL display a Reading_Progress_Bar fixed to the top of the viewport on each case study page, rendered as a horizontal bar that fills from 0% width at the top of the page to 100% width when the user has scrolled to the bottom of the page content
4. THE Portfolio_Site SHALL display bottom navigation on each case study page with a "Back to Case Studies" link navigating to `/case-studies` and a "Next Case Study" link navigating to the next case study in the content collection array order
5. IF the current case study is the last in the content collection array order, THEN THE Portfolio_Site SHALL display the "Next Case Study" link pointing to the first case study in the collection
6. IF a user navigates to a `/case-studies/[slug]` route where the slug does not match any case study in the content collection, THEN THE Portfolio_Site SHALL return a 404 Not Found page

### Requirement 6: Dark and Light Mode

**User Story:** As a visitor, I want to toggle between dark and light display modes, so that I can read comfortably in any lighting environment.

#### Acceptance Criteria

1. IF no theme preference exists in localStorage, THEN THE Portfolio_Site SHALL default to dark mode on first visit
2. WHEN the visitor clicks or activates the Theme_Toggle via keyboard, THE Theme_Toggle SHALL switch between dark mode and light mode without requiring a page reload
3. WHEN the theme preference is changed, THE Theme_Toggle SHALL persist the selection in localStorage
4. WHEN a returning visitor loads the site, THE Portfolio_Site SHALL apply the theme stored in localStorage before page content is visually rendered to prevent a flash of the incorrect theme
5. THE Portfolio_Site SHALL use Tailwind CSS dark: class strategy for theme switching
6. WHILE in dark mode, THE Portfolio_Site SHALL use background color #0f172a (slate-900) and text color #e2e8f0 (slate-200)
7. WHILE in light mode, THE Portfolio_Site SHALL use white (#ffffff) background and slate-900 (#0f172a) text
8. THE Theme_Toggle SHALL be visible and accessible on all pages of the site within the navigation header
9. IF the localStorage theme value is missing or invalid, THEN THE Portfolio_Site SHALL fall back to dark mode

### Requirement 7: Design System and Accent Color

**User Story:** As a visitor, I want a visually consistent site with clear interactive affordances, so that the design supports readability and trust.

#### Acceptance Criteria

1. THE Portfolio_Site SHALL use #2563EB (blue-600) as the text color for links, as the background color for primary CTA buttons, and as the border or text color for hover states on interactive elements
2. THE Portfolio_Site SHALL use the Inter font family (weights 400, 500, 600, 700, and 800) loaded from Google Fonts with `font-display: swap`, and SHALL fall back to the system sans-serif font stack if Google Fonts is unavailable
3. THE Portfolio_Site SHALL render content in a single-column layout at viewport widths of 375px and in a multi-column layout at viewport widths of 1280px, with no horizontal scrollbar appearing at any width between 375px and 1280px
4. THE Portfolio_Site SHALL not include animations that delay the first meaningful paint by more than 100 milliseconds, and SHALL not use animation to gate access to content (content must be visible without waiting for an animation to complete)
5. THE Portfolio_Site SHALL display a visible focus indicator with a minimum 2px outline on all interactive elements (links, buttons, form inputs) when focused via keyboard navigation

### Requirement 8: Navigation

**User Story:** As a visitor, I want clear navigation that directs me to all key sections, so that I can explore the full portfolio easily.

#### Acceptance Criteria

1. THE Portfolio_Site SHALL display exactly six navigation links in the following order from left to right: Home, Case Studies, PM Playbook, Services, About, Contact
2. THE Portfolio_Site SHALL remove the How I Built This navigation link from the header and mobile menu, while the corresponding page remains accessible via direct URL
3. WHILE the viewport width is 768px or greater, THE Portfolio_Site SHALL display the navigation links inline within the header
4. WHILE the viewport width is less than 768px, THE Portfolio_Site SHALL hide the navigation links and display a hamburger menu icon in the header
5. WHEN the visitor taps the hamburger menu icon, THE Portfolio_Site SHALL toggle the visibility of the navigation links as a vertically stacked list below the header

### Requirement 9: Component Structure

**User Story:** As a site maintainer, I want well-separated reusable components, so that I can maintain and extend the site efficiently.

#### Acceptance Criteria

1. THE Portfolio_Site SHALL contain the following component files within a `src/components/` directory: Nav.astro, Footer.astro, CaseStudyCard.astro, SkillTag.astro, ThemeToggle.astro
2. THE Portfolio_Site SHALL use Layout.astro (located in `src/layouts/`) as the page wrapper for every page, where Layout.astro imports and renders Nav.astro and Footer.astro
3. THE Portfolio_Site SHALL use CaseStudyCard.astro for rendering each case study preview on the homepage Featured Work section and on the case-studies index page, accepting at minimum a title, company name, description, and tags list as props
4. THE Portfolio_Site SHALL use SkillTag.astro for rendering each individual skill tag in the Skills Snapshot section, accepting at minimum a label string as a prop
5. THE Portfolio_Site SHALL use ThemeToggle.astro for the dark/light mode toggle control, rendering a single interactive button that switches the active color scheme
6. WHEN a component is rendered, THE Portfolio_Site SHALL produce no Astro build errors for that component's file

### Requirement 10: About and Contact Pages

**User Story:** As a visitor, I want dedicated About and Contact pages, so that I can learn more about the candidate and reach out.

#### Acceptance Criteria

1. WHEN a visitor navigates to the `/about` route, THE Portfolio_Site SHALL render a page that returns an HTTP 200 status and displays at minimum a heading, a biographical summary of the candidate, and a career history section
2. WHEN a visitor navigates to the `/contact` route, THE Portfolio_Site SHALL render a page that returns an HTTP 200 status and displays at minimum a heading and at least one actionable contact method (e.g., email link, messaging link, or contact form)
3. THE Portfolio_Site SHALL mark any placeholder content on the About and Contact pages with the literal text "[PLACEHOLDER]" rendered visibly in the page body without requiring browser developer tools to see
4. THE Portfolio_Site SHALL provide navigation links to both the `/about` and `/contact` pages from the site's global navigation so that visitors can discover them from any page

### Requirement 11: Build and Deployment Constraints

**User Story:** As a site maintainer, I want the site to build without errors and deploy reliably, so that the portfolio is always available to hiring managers.

#### Acceptance Criteria

1. WHEN the `astro build` command is executed, THE Portfolio_Site SHALL complete with exit code 0 and produce zero TypeScript type-checking errors
2. THE Portfolio_Site SHALL ship no JavaScript to the client browser except inline scripts authored within Astro component `<script>` tags, with no external JS libraries loaded via CDN or bundled from npm packages
3. THE Portfolio_Site SHALL retain the existing dependency versions specified in package.json: astro (^6.0.4), tailwindcss (^4.2.1), and @tailwindcss/vite (^4.2.1) without modifying their version ranges
4. THE Portfolio_Site SHALL use no additional npm dependencies beyond astro, tailwindcss, and @tailwindcss/vite in the dependencies or devDependencies fields of package.json
5. WHEN deployed to Vercel, THE Portfolio_Site SHALL serve all pages with HTTP 200 status responses within 10 seconds of deployment completion
