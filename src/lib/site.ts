import { statSync } from 'node:fs';

export const site = {
  name: 'Muhammad Adi Putra',
  email: 'muhammadadiputra789@gmail.com',
  linkedin: 'https://www.linkedin.com/in/m-adi-putra/',
  cv: '/MuhammadAdiPutra_CV.pdf',
  coords: '6°10′S 106°49′E',
  status: 'Open to Senior / Lead PM roles — Jakarta & SEA',
};

// Real size of the CV file, read at build time.
export const cvSize = `${Math.round(statSync('public/MuhammadAdiPutra_CV.pdf').size / 1024)} KB`;

export const nav = [
  { href: '/case-studies', label: 'Case studies' },
  { href: '/playbook', label: 'Playbook' },
  { href: '/services', label: 'Services' },
  { href: '/about', label: 'About' },
  { href: '/contact', label: 'Contact' },
];

// Typographic polish for content strings: curly apostrophes, and a non-breaking
// space between a number and its unit ("8 days").
export const typo = (s: string) =>
  s.replace(/(\w)'(\w)/g, '$1’$2').replace(/(\d) (?=[A-Za-z])/g, '$1 ');
