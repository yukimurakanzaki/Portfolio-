import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const caseStudies = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/case-studies' }),
  schema: ({ image }) => z.object({
    title: z.string().min(1).max(100),
    company: z.string().min(1),
    subtitle: z.string().optional(),
    summary: z.string().min(1).max(300),
    // One line from the Outcome section, shown in the editorial index.
    outcome: z.string().max(160).optional(),
    tags: z.array(z.string()).min(1).max(8),
    readTime: z.string().regex(/^\d+ min read$/),
    slug: z.string().min(1).max(80).regex(/^[a-z0-9-]+$/),
    order: z.number().int().min(1),
    phoneScreens: z.array(z.object({
      src: image(),
      alt: z.string(),
      caption: z.string().optional(),
    })).length(3).optional(),
    phoneScreensLabel: z.string().optional(),
  }),
});

export const collections = { 'case-studies': caseStudies };
