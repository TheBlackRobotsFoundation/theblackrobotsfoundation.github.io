---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# LED RGB y tiras de LEDs

Si ya conoces el [LED](/guias/actuadores/led), aquí das el siguiente paso: **elegir el color**.

## El LED RGB

Un **LED RGB** lleva tres LEDs dentro de la misma cápsula: uno **rojo** (*Red*), uno **verde** (*Green*) y uno **azul** (*Blue*). Encendiendo cada uno con más o menos brillo, mezclas cualquier color.

<img src="/img/guias/actuadores/led-rgb/anatomia.svg" alt="LED RGB de cátodo común con sus cuatro patas" />

Tiene **4 patas**: una por color y una **común**, que es la más larga.

| Tipo | La pata común va a | Para encender un color |
|---|---|---|
| **Cátodo común** | GND | pin en HIGH |
| **Ánodo común** | 5V | pin en LOW |

El de **cátodo común** es el más habitual y el que usaremos.

:::tip
¿No sabes cuál tienes? Conecta la pata larga a GND y otra pata a 5V a través de una resistencia de 220 Ω. Si se enciende un color, es de cátodo común.
:::

## Las tiras de LEDs direccionables

Una **tira WS2812** (las famosas **NeoPixel**) es una fila de LEDs RGB en la que **cada LED lleva su propio chip**. Así se controlan uno a uno, cada cual con su color, usando **un solo pin** del Arduino.

<img src="/img/guias/actuadores/led-rgb/tira.svg" alt="Tira de LEDs WS2812 con la entrada, el sentido de los datos y las marcas de corte" />

- **3 conexiones**: 5V, GND y DIN (entrada de datos)
- **Sentido de los datos**: una flecha impresa indica hacia dónde viajan. Se conecta siempre por el extremo **de entrada**
- **Se puede cortar** por las líneas marcadas entre LEDs, y cada trozo sigue funcionando
- También existen en **anillos**, **matrices** y **LEDs sueltos**, todos con el mismo chip

## Cuál elegir

| | LED RGB | Tira WS2812 |
|---|---|---|
| LEDs | 1 | de uno a cientos |
| Pines del Arduino | 3 (con PWM) | 1 |
| Resistencias | una por color | una en la línea de datos |
| Programación | `analogWrite()` | librería |

## En robótica

- **Estado del robot**: verde todo bien, ámbar batería baja, rojo error
- **Intermitentes y luces**: en los laterales o el frontal de un robot móvil
- **Respuesta a sensores**: un color según la distancia o la temperatura
