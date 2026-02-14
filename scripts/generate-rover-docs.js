#!/usr/bin/env node
/**
 * Script para generar documentación de la web desde el submodule Rover
 */

const fs = require('fs');
const path = require('path');

const ROVER_PATH = path.join(__dirname, '../docs/rover');
const OUTPUT_PATH = path.join(__dirname, '../docs/rover-web');

// Estructura workspace -> archivo salida
const workspaces = {
  'rover_core': 'core',
  'rover_drivers': 'drivers',
  'rover_control': 'control',
  'rover_navigation': 'navigation',
  'rover_simulation': 'simulation',
  'rover_bringup': 'bringup',
  'rover_tools': 'tools'
};

// Crear directorio de salida
if (!fs.existsSync(OUTPUT_PATH)) {
  fs.mkdirSync(OUTPUT_PATH, { recursive: true });
}
if (!fs.existsSync(path.join(OUTPUT_PATH, 'workspaces'))) {
  fs.mkdirSync(path.join(OUTPUT_PATH, 'workspaces'), { recursive: true });
}

// Generar index.md desde README principal
const mainReadme = fs.readFileSync(path.join(ROVER_PATH, 'README.md'), 'utf8');

// Reemplazar enlaces rotos
const fixedReadme = mainReadme
  .replace(/\(docs\//g, '(guides/')
  .replace(/\(LICENSE\)/g, '(https://github.com/TheBlackRobotsFoundation/Rover/blob/main/LICENSE)');

const indexContent = `---
sidebar_position: 1
id: rover-intro
title: Rover
---

${fixedReadme}
`;
fs.writeFileSync(path.join(OUTPUT_PATH, 'index.md'), indexContent);
console.log('✓ Generado index.md');

// Generar archivos para cada workspace
let position = 1;
Object.entries(workspaces).forEach(([wsDir, outputName]) => {
  const readmePath = path.join(ROVER_PATH, wsDir, 'README.md');
  if (fs.existsSync(readmePath)) {
    const content = fs.readFileSync(readmePath, 'utf8');
    const outputContent = `---
sidebar_position: ${position++}
title: ${wsDir.replace('rover_', '').charAt(0).toUpperCase() + wsDir.replace('rover_', '').slice(1)}
---

${content}
`;
    fs.writeFileSync(path.join(OUTPUT_PATH, 'workspaces', `${outputName}.md`), outputContent);
    console.log(`✓ Generado workspaces/${outputName}.md`);
  }
});

// Copiar carpeta docs/ entera (guías detalladas)
const docsSrc = path.join(ROVER_PATH, 'docs');
const docsDest = path.join(OUTPUT_PATH, 'guides');

function copyRecursive(src, dest) {
  if (fs.existsSync(src)) {
    if (!fs.existsSync(dest)) {
      fs.mkdirSync(dest, { recursive: true });
    }
    fs.readdirSync(src).forEach(item => {
      const srcPath = path.join(src, item);
      const destPath = path.join(dest, item);
      if (fs.lstatSync(srcPath).isDirectory()) {
        copyRecursive(srcPath, destPath);
      } else if (item.endsWith('.md')) {
        // Leer contenido y arreglar enlaces
        let content = fs.readFileSync(srcPath, 'utf8');
        content = content
          .replace(/\(\.\.\/guides\//g, '(./')
          .replace(/\(\.\.\/docs\//g, '(./')
          .replace(/\(guides\//g, '(./')
          .replace(/\(docs\//g, '(./');
        fs.writeFileSync(destPath, content);
      }
    });
  }
}

copyRecursive(docsSrc, docsDest);
console.log('✓ Copiado docs/ a guides/');

console.log('\n✅ Documentación generada exitosamente en docs/rover-web/');
