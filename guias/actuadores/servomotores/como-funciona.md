---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

## Por dentro

Dentro de la carcasa hay cuatro piezas que trabajan juntas:

- Un **motor DC** pequeño, que gira muy rápido
- Una **reductora** de engranajes, que baja la velocidad y multiplica la fuerza
- Un **potenciómetro** unido al eje de salida, que mide su ángulo real (como el [potenciómetro](/guias/sensores/potenciometro/como-funciona) de las guías de sensores)
- Un **circuito de control**, que lo coordina todo

![Bucle de control del servo: la señal, el circuito, el motor, el eje y el potenciómetro que mide el ángulo real](/img/guias/actuadores/servomotores/por-dentro.svg)

El circuito compara constantemente **el ángulo que le pides** con **el que mide el potenciómetro**. Si no coinciden, mueve el motor hacia el lado correcto; cuando coinciden, lo para. Esto se llama **control en lazo cerrado**, y es la misma idea que usan robots mucho más grandes.

Por eso el servo **aguanta su posición**: si empujas el brazo, el potenciómetro detecta que se ha movido y el motor hace fuerza para volver.

## La señal: un pulso cada 20 ms

El servo recibe un pulso cada **20 milisegundos** (50 veces por segundo). Lo que cuenta es **cuánto dura** ese pulso:

![Pulsos de 1, 1,5 y 2 ms y los ángulos de 0, 90 y 180 grados](/img/guias/actuadores/servomotores/pulsos.svg)

| Duración del pulso | Ángulo |
|---|---|
| 1 ms | 0° |
| 1,5 ms | 90° (el centro) |
| 2 ms | 180° |

Los valores exactos cambian un poco entre modelos: muchos servos llegan a sus extremos con pulsos de entre 0,5 y 2,5 ms.

La librería `Servo` de Arduino genera estos pulsos por ti. Tú solo le dices el ángulo.

## El consumo

Un servo consume poco cuando está quieto, pero al moverse o al hacer fuerza pide picos importantes:

| | SG90 | MG996R |
|---|---|---|
| En reposo | ~10 mA | ~10 mA |
| Moviéndose | 100 – 250 mA | 500 – 900 mA |
| Bloqueado (haciendo toda su fuerza) | ~650 mA | hasta 2,5 A |

Un SG90 se puede alimentar del Arduino. Con más servos, o con servos grandes, los picos hacen que la placa se reinicie: necesitan una [fuente aparte](/guias/electronica/alimentacion).
