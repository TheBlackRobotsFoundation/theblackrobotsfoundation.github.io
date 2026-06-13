import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // Sidebar principal de Proyectos
  proyectosSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Plotter',
      customProps: {icon: '/img/proyectos/iconos/plotter.svg'},
      link: {type: 'doc', id: 'plotter/plotter-intro'},
      items: [
        'plotter/plotter-hardware',
        'plotter/plotter-firmware',
        'plotter/plotter-montaje-shield',
        'plotter/plotter-vref',
        'plotter/plotter-ugs',
        'plotter/plotter-primer-dibujo',
      ],
    },
    // Rover oculto temporalmente: solo la página "Próximamente" (sin las sub-páginas de rover-web)
    'rover',
    'drone',
  ],
};

export default sidebars;
