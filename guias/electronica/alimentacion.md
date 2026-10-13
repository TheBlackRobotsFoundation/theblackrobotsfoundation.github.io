---
sidebar_position: 6
sidebar_label: Alimentación
title: Cómo alimentar un robot
sidebar_custom_props:
  icon: /img/guias/iconos/requisitos.svg
---

# Cómo alimentar un robot

La mayoría de problemas raros en un robot (reinicios, sensores que fallan, motores que tiemblan) vienen de la **alimentación**. Con unas pocas reglas te los ahorras.

## Lo que da el Arduino UNO

| Salida | Corriente aproximada |
|---|---|
| Cada pin digital | **20 mA** recomendados (40 mA es el máximo absoluto) |
| Todos los pines a la vez | 200 mA en total |
| Pin **5V** alimentado por USB | unos 400 – 500 mA, compartidos con la placa |
| Pin **3.3V** | 50 mA |

Con eso alimentas sin problema LEDs, sensores y módulos pequeños. Los motores, servos grandes, tiras de LEDs y relés piden más, y necesitan su propia fuente.

## Regla 1: los motores, con su propia fuente

Un motor arrancando consume picos de corriente muy altos. Si sale del Arduino, la tensión cae, la placa se reinicia o el pin se daña. La solución:

- **Arduino**: por USB o por su jack (7 – 12 V)
- **Motores**: una batería o fuente aparte, a través de un **driver** ([L298N](/guias/actuadores/motores-dc), [A4988](/guias/actuadores/motores-paso-a-paso), [ESC](/guias/actuadores/brushless)...)

## Regla 2: GND común

Cuando usas dos fuentes, **une sus GND**. La tensión siempre se mide respecto a una referencia, y si cada parte tiene la suya, las señales llegan sin sentido.

<img src="/img/guias/electronica/gnd-comun.svg" alt="Arduino, driver y fuente de motores con todas las masas unidas" />

:::caution
Une las **masas (GND)**, y solo las masas. El positivo de la fuente de motores va únicamente al driver.
:::

## Regla 3: condensadores cerca de lo que consume

Un condensador hace de pequeño depósito que suaviza los picos. Por eso las guías te piden uno en el driver de un [motor paso a paso](/guias/actuadores/motores-paso-a-paso/conexion) o en una [tira de LEDs](/guias/actuadores/led-rgb/conexion). Respeta su **polaridad**: la franja marca la pata negativa.

## Baterías habituales

| Batería | Tensión | Para qué |
|---|---|---|
| 4 × AA | 6 V (4,8 V recargables) | Robots pequeños, servos |
| Pila de 9 V | 9 V | Arduino solo (dura poco con motores) |
| LiPo 2S | 7,4 V | Robots con motores DC |
| LiPo 3S | 11,1 V | Drones, motores potentes |

:::caution[Baterías LiPo]
Las LiPo dan muchísima corriente. Cárgalas con un cargador específico, guárdalas a media carga y desconéctalas al terminar. Si una se hincha, retírala.
:::
