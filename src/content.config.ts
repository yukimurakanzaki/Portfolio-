import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const caseStudies = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/case-studies' }),
  schema: z.object({
    title: z.string().min(1).max(100),
    company: z.string().min(1),
    subtitle: z.string().optional(),
    summary: z.string().min(1).max(300),
    tags: z.array(z.string()).min(1).max(8),
    readTime: z.string().regex(/^\d+ min read$/),
    slug: z.string().min(1).max(80).regex(/^[a-z0-9-]+$/),
    order: z.number().int().min(1),
  }),
});

export const collections = { 'case-studies': caseStudies };
