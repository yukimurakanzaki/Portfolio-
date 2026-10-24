import type { CollectionEntry } from 'astro:content';

export type Study = CollectionEntry<'case-studies'>;

// "Role (Official Title: …) · Mon YYYY – Mon YYYY" → role + "2022–2023"
export function studyMeta(study: Study) {
  const [rawRole = '', rawDates = ''] = (study.data.subtitle ?? '').split(' · ');
  const role = rawRole.replace(/\s*\(.*\)/, '');
  const years = [...new Set(rawDates.match(/\d{4}/g) ?? [])];
  if (/present/i.test(rawDates)) years.push('present');
  return { role, years: years.join('–'), company: study.data.company };
}

export function sortStudies(studies: Study[]) {
  return [...studies].sort((a, b) => a.data.order - b.data.order);
}
