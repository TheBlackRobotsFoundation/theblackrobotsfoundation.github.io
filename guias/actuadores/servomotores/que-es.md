---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es un servomotor?

Un **servomotor** (o simplemente **servo**) es un motor al que le dices **un ángulo** y va hasta él. Si algo intenta moverlo, hace fuerza para volver. Dentro lleva todo lo necesario: motor, engranajes, un sensor de posición y la electrónica que lo controla.

Mientras un [motor DC](/guias/actuadores/motores-dc) gira sin parar y un [paso a paso](/guias/actuadores/motores-paso-a-paso) avanza contando pasos, el servo **va directo a una posición**.

<img src="/img/guias/actuadores/servomotores/anatomia.svg" alt="Micro servo SG90 con su brazo, el eje, las orejas y el cable de tres hilos" />

## Sus partes

- **Eje de salida**: gira normalmente entre **0° y 180°**
- **Brazos** (*bocinas*): piezas de plástico que se encajan en el eje. Vienen varias en la bolsa
- **Orejas**: para atornillarlo a la estructura
- **Cable de 3 hilos**:

| Color | Función |
|---|---|
| **Marrón** (o negro) | GND |
| **Rojo** | alimentación (5 V) |
| **Naranja** (o amarillo, o blanco) | señal |

## Tipos más habituales

| Modelo | Tamaño | Par aproximado | Engranajes | Para qué |
|---|---|---|---|---|
| **SG90** | micro (9 g) | 1,8 kg·cm | plástico | aprender, mecanismos ligeros |
| **MG90S** | micro (13 g) | 2,2 kg·cm | metal | lo mismo, más resistente |
| **MG996R** | estándar (55 g) | ~10 kg·cm | metal | brazos robóticos, direcciones |

El **par** dice cuánta fuerza hace: 1,8 kg·cm significa que levanta 1,8 kg colgados a 1 cm del eje, o 0,9 kg a 2 cm.

:::note[Servos de rotación continua]
Algunos servos (como el **FS90R**) giran sin fin, como un motor. En ellos el ángulo que les mandas se convierte en **velocidad y sentido**: 90 para, 0 gira rápido hacia un lado y 180 hacia el otro. Son una forma cómoda de mover las ruedas de un robot pequeño.
:::

## En robótica

- **Brazos robóticos**: un servo por articulación
- **Pinzas**: abrir y cerrar
- **Dirección** de un coche robot
- **Cabeza giratoria**: un servo que mueve un [sensor de ultrasonidos](/guias/sensores/ultrasonidos) de lado a lado para mirar alrededor
- **Robots con patas**: arañas, humanoides pequeños
