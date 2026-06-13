import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Black Robots',
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

  onBrokenLinks: 'warn',

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
          exclude: ['**/rover/**', '**/rover'],
        },
        blog: {
          path: 'blog-posts',
          routeBasePath: 'noticias',
          blogTitle: 'Noticias y curiosidades',
          blogDescription: 'Novedades, curiosidades y noticias del mundo de la robótica',
          blogSidebarTitle: 'Entradas recientes',
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
          },
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'guias',
        path: 'guias',
        routeBasePath: 'guias',
        sidebarPath: './sidebarsGuias.ts',
      },
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
      title: 'Black Robots',
      logo: {
        alt: 'Black Robots Foundation Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'proyectosSidebar',
          label: 'Proyectos',
          position: 'left',
        },
        {
          label: 'Guías',
          to: '/guias/',
          position: 'left',
        },
        {
          label: 'Noticias',
          to: '/noticias',
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
            {
              label: 'Drone',
              to: '/proyectos/drone/',
            },
            {
              label: 'Plotter',
              to: '/proyectos/plotter/',
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
              href: 'https://instagram.com/black.robots',
            },
            {
              label: 'YouTube',
              href: 'https://youtube.com/@black.robots',
            },
            {
              label: 'TikTok',
              href: 'https://tiktok.com/@blackrobots',
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
