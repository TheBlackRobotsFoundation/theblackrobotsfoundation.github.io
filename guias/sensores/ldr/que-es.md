---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es una fotorresistencia?

Una **fotorresistencia** o **LDR** (*Light Dependent Resistor*, resistencia dependiente de la luz) es una resistencia cuyo valor **cambia con la luz** que le llega. Con poca luz tiene una resistencia muy alta; con mucha luz, muy baja.

Es el sensor de luz más sencillo y barato que existe, y el que encontrarás en casi cualquier kit.

![Fotorresistencia con su pista fotosensible y sus dos patas](/img/guias/sensores/ldr/anatomia.svg)

## Cómo es

- Un disco pequeño con una **pista en zigzag** de un material sensible a la luz (sulfuro de cadmio)
- **Dos patas** sin polaridad: se puede conectar en cualquier sentido

## Valores típicos

Una LDR común (como la GL5528) da aproximadamente:

| Luz | Resistencia |
|---|---|
| Oscuridad total | ~1 MΩ |
| Habitación iluminada | ~10 – 20 kΩ |
| Luz directa | ~1 kΩ |

Los valores varían entre unidades. La LDR sirve muy bien para decidir **si hay más o menos luz** y para comparar; para medir la luz con precisión (en lux) existen sensores específicos como el BH1750.

## En robótica

- **Robot que sigue la luz**: dos LDR, una a cada lado; el robot gira hacia la que recibe más
- **Encendido automático**: las luces del robot se encienden al oscurecer
- **Detectar objetos**: un objeto que pasa entre un LED y la LDR le corta la luz

El [sensor sigue-líneas](/guias/sensores/infrarrojos) usa una idea muy parecida: medir cuánta luz vuelve de una superficie.
