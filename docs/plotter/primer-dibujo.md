---
id: plotter-primer-dibujo
title: Tu primer dibujo
sidebar_label: Tu primer dibujo
sidebar_position: 8
---

# Tu primer dibujo

:::warning[Página en construcción]
Esta sección todavía se está escribiendo. El proceso y la foto del dibujo de prueba se añadirán en cuanto estén listos.
:::

Con el plotter montado, configurado y calibrado, ya puedes dibujar. El proceso es siempre el mismo: **diseñar → convertir a G-code → enviar**.

## 1. Diseña el dibujo

Usa **Inkscape**, un editor de gráficos vectoriales gratuito. El dibujo tiene que estar hecho con **líneas vectoriales** (no sirve una foto), porque son esas líneas las que el plotter convertirá en trazos del lápiz.

## 2. Genera el G-code

Con la **extensión de G-code de Inkscape**, conviertes tu dibujo en un archivo `.gcode`: una lista de instrucciones que le dice al plotter por dónde mover el lápiz.

## 3. Cárgalo en UGS

Abre ese archivo `.gcode` en UGS. El **visor** te mostrará una previsualización del recorrido que hará el lápiz, para que compruebes que todo está bien antes de dibujar.

## 4. Coloca el papel y fija el origen

1. Pon el papel en la base del plotter
2. Con los botones de **jog**, mueve el cabezal hasta la esquina donde quieres que empiece el dibujo
3. Fija ahí el **origen** (el punto cero)

## 5. Envía el dibujo

Pulsa el botón de **enviar** (play) en UGS. El plotter empezará a moverse y a dibujar siguiendo el G-code.

![Dibujo de prueba](/img/plotter/dibujo-prueba.svg)
