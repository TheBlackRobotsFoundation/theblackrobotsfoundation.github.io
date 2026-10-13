---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

El emisor ilumina la superficie con luz infrarroja. Lo que pasa después depende del color:

<img src="/img/guias/sensores/infrarrojos/reflexion.svg" alt="Una superficie blanca refleja la luz hacia el receptor; una línea negra la absorbe" />

- **Superficie blanca o clara**: refleja mucha luz, el receptor la capta
- **Línea negra**: absorbe casi toda la luz, al receptor llega muy poca

## Las dos salidas

### AO: la medida tal cual

La salida analógica da una tensión que depende de cuánta luz llega al receptor. Se lee con `analogRead()`. En la mayoría de módulos, **más reflejo = valor más bajo**: el blanco da números bajos y el negro, altos. Compruébalo con el tuyo.

Es la salida que conviene usar cuando quieres saber **cuánto** del sensor está sobre la línea, por ejemplo para girar más o menos según lo desviado que vaya el robot.

### DO: la decisión ya tomada

El módulo lleva un **comparador** (el chip LM393) que compara la medida con el umbral que marca el potenciómetro y da una respuesta digital:

| Debajo hay | LED indicador | DO |
|---|---|---|
| blanco (reflejo) | encendido | **LOW** |
| negro (sin reflejo) | apagado | **HIGH** |

Es la forma más fácil de empezar: un `digitalRead()` y listo.

## Ajustar el potenciómetro

1. Coloca el sensor sobre el **blanco**, a la altura a la que irá en el robot
2. Gira el potenciómetro hasta que el LED indicador se **encienda**
3. Pásalo sobre la **línea negra**: el LED debe **apagarse**
4. Si no cambia, gira un poco hacia el otro lado y repite

## Lo que afecta a la medida

- **La altura**: entre 2 y 5 mm del suelo funciona mejor. Más lejos, el contraste baja mucho
- **La luz del sol**: tiene mucha luz infrarroja y puede confundir al receptor. En interior funciona mejor
- **El material**: una cinta negra brillante puede reflejar más de lo esperado. La cinta aislante mate es la clásica
