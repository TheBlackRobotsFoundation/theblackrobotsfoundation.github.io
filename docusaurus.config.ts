import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'The Black Robots Foundation',
  tagline: 'make it simple, make it black',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://blackrobots.org',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'TheBlackRobotsFoundation', // Usually your GitHub org/user name.
  projectName: 'theblackrobotsfoundation.github.io', // Usually your repo name.
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'es',
    locales: ['es'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: 'proyectos',
          path: 'docs',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      defaultMode: 'dark',
      disableSwitch: true,
      respectPrefersColorScheme: false,
    },
    navbar: {
      title: 'The Black Robots Foundation',
      logo: {
        alt: 'Black Robots Foundation Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          label: 'Rover',
          to: '/proyectos/rover/',
          position: 'left',
        },
        {to: '/quienes-somos', label: 'Quiénes Somos', position: 'right'},
        {to: '/foro', label: 'Foro', position: 'right'},
        {
          href: 'https://github.com/TheBlackRobotsFoundation',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      links: [
        {
          title: 'Proyectos',
          items: [
            {
              label: 'Rover',
              to: '/proyectos/rover/',
            },
          ],
        },
        {
          title: 'Recursos',
          items: [
            {
              label: 'Foro',
              to: '/foro',
            },
          ],
        },
        {
          title: 'Enlaces',
          items: [
            {
              label: 'Quiénes Somos',
              to: '/quienes-somos',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/TheBlackRobotsFoundation',
            },
          ],
        },
        {
          title: 'Redes Sociales',
          items: [
            {
              label: 'Instagram',
              href: '#', // TODO: Agregar enlace de Instagram
            },
            {
              label: 'TikTok',
              href: '#', // TODO: Agregar enlace de TikTok
            },
            {
              label: 'YouTube',
              href: '#', // TODO: Agregar enlace de YouTube
            },
            {
              label: 'LinkedIn',
              href: '#', // TODO: Agregar enlace de LinkedIn
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Black Robots Foundation · Built with ♥ using Docusaurus`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
