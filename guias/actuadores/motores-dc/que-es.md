---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es un motor DC?

Un **motor DC** (de corriente continua) es el motor más sencillo: le das tensión y gira. Si inviertes los cables, gira al revés. Si le das menos tensión, gira más despacio.

Es el motor de los juguetes, los ventiladores pequeños y las ruedas de la mayoría de robots móviles.

<img src="/img/guias/actuadores/motores-dc/motor.svg" alt="Motor DC con su eje, la carcasa y los dos terminales" />

## Motorreductores

Un motor DC solo gira muy rápido (miles de vueltas por minuto) y con poca fuerza. Para mover un robot se usa casi siempre un **motorreductor**: el motor con una caja de engranajes que **baja la velocidad y multiplica la fuerza**.

| Motor | Velocidad típica | Tensión | Dónde se ve |
|---|---|---|---|
| **TT amarillo** (1:48) | ~200 rpm | 3 – 6 V | kits de coche robot |
| **N20** | 30 – 1000 rpm según reducción | 6 – 12 V | robots pequeños, con encoder |
| **JGA25-370** | 100 – 600 rpm | 6 – 12 V | robots medianos, con encoder |

Muchos traen un [encoder](/guias/sensores/encoders) en la parte trasera para medir cuánto giran.

## Por qué necesita un driver

Un motor pequeño consume entre **200 mA y 1 A**, y al arrancar pide aún más. Un pin del Arduino da unos 20 mA. Además, para cambiar el sentido hay que **invertir la polaridad**, algo que un pin no puede hacer.

La solución es un **driver de motores**: el Arduino le manda órdenes con sus pines y el driver deja pasar la corriente de la batería hacia el motor, en el sentido y con la fuerza que toque.

## El L298N

El **L298N** es el driver de motores más extendido en kits de robótica. Controla **dos motores DC** a la vez, cada uno con su sentido y su velocidad.

<img src="/img/guias/actuadores/motores-dc/l298n.svg" alt="Módulo L298N con su disipador, las bornas de los motores, la alimentación y los pines de control" />

| | L298N |
|---|---|
| Motores | 2 DC (o 1 paso a paso bipolar) |
| Tensión de motores | 5 – 35 V |
| Corriente por motor | 2 A (picos de 3 A) |
| Control | ENA/ENB (velocidad) e IN1 – IN4 (sentido) |
| Extra | regulador que da 5 V |

:::note[Otros drivers]
El L298N es robusto y fácil de encontrar, pero pierde unos **2 V** por el camino en forma de calor. Drivers más modernos como el **TB6612FNG** o el **DRV8833** son más pequeños y eficientes, y se programan de forma muy parecida. Para empezar, cualquiera vale.
:::
