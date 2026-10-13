---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

## Mezcla de luz

La luz se mezcla de forma **aditiva**: sumando colores obtienes otros más claros, y los tres a la vez dan **blanco**.

![Mezcla aditiva de rojo, verde y azul y los valores de algunos colores](/img/guias/actuadores/led-rgb/mezcla.svg)

Cada canal va de **0** (apagado) a **255** (máximo brillo), igual que el [PWM](/guias/electronica/pwm) de `analogWrite()`. Con tres canales hay más de **16 millones** de combinaciones (256 × 256 × 256).

:::tip
Muchos programas de diseño y páginas web dan los colores en este mismo formato. Un selector de color online te dice los tres valores de cualquier tono que te guste.
:::

## LED RGB: tres LEDs, tres resistencias

Por dentro son tres LEDs independientes que comparten una pata. Cada uno necesita **su propia resistencia** para limitar la corriente, igual que un [LED normal](/guias/actuadores/led/como-funciona). Con 220 Ω en cada color a 5 V funciona bien.

El brillo de cada color se controla con PWM, así que los tres deben ir a **pines con `~`**.

:::note
El ojo es más sensible al verde que al azul o al rojo. Con los tres al 255 el blanco suele salir algo verdoso o azulado; se corrige bajando un poco el canal que destaque.
:::

## Tira WS2812: un mensaje que viaja

Cada LED de la tira tiene un chip con una **entrada** (DIN) y una **salida** (DOUT) de datos. El Arduino envía por DIN una ristra de colores, 24 bits por LED (8 de rojo, 8 de verde y 8 de azul):

1. El primer LED se queda con los **primeros 24 bits** y los usa para su color
2. Reenvía el resto por su salida al siguiente
3. El segundo hace lo mismo, y así hasta el final

Por eso la tira tiene un **sentido** y solo funciona conectándola por la entrada.

## El consumo

Cada LED WS2812 consume hasta **60 mA** en blanco a máximo brillo (20 mA por color). Se acumula muy rápido:

| LEDs | Consumo máximo |
|---|---|
| 8 | 0,5 A |
| 30 | 1,8 A |
| 60 | 3,6 A |

El pin 5V del Arduino alimentado por USB da unos 500 mA. Para más de 8 LEDs, o con brillo alto, usa una **fuente de 5 V** externa con [GND común](/guias/electronica/alimentacion). Bajar el brillo en el código también reduce el consumo, y a la vista apenas se nota.
