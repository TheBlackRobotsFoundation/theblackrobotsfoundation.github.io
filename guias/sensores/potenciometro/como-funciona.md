---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona por dentro

Dentro del potenciómetro hay una **pista resistiva** en forma de arco, con un extremo en cada pata exterior. Sobre ella desliza un contacto metálico, el **cursor**, unido al eje y a la pata central.

![Pista resistiva del potenciómetro con el cursor](/img/guias/sensores/potenciometro/pista.svg)

## Un divisor de tensión que gira

El cursor parte la pista en dos trozos, que funcionan como las dos resistencias de un [divisor de tensión](/guias/electronica/divisor-de-tension):

- Girado del todo hacia GND → el cursor da **0 V**
- En el centro → **2,5 V**
- Girado del todo hacia 5 V → **5 V**

Entre medias, la tensión cambia de forma proporcional al giro (en los potenciómetros **lineales**, marcados con una **B**, como `B10K`).

:::note[Lineal o logarítmico]
Los marcados con **A** (`A10K`) son **logarítmicos**: cambian poco al principio y mucho al final, y están pensados para el volumen de audio. Para robótica, elige siempre **lineales (B)**.
:::

## Lo que lee el Arduino

El pin analógico convierte esa tensión en un número entre **0 y 1023** (lo tienes explicado en [señales digitales y analógicas](/guias/electronica/digital-y-analogico)):

| Posición | Tensión | `analogRead()` |
|---|---|---|
| tope hacia GND | 0 V | 0 |
| centro | 2,5 V | ~512 |
| tope hacia 5 V | 5 V | 1023 |

Como la lectura depende del **reparto** de la pista y del valor total, la resistencia del potenciómetro (1 kΩ, 10 kΩ, 100 kΩ) apenas cambia el resultado.
