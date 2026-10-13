---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es un encoder?

Un **encoder** es un sensor que mide **cuánto gira un eje y en qué sentido**. Va unido al eje de un motor o de una rueda y genera pulsos al girar: contándolos, sabes el ángulo recorrido, la velocidad y, si es una rueda, la distancia avanzada.

Es lo que convierte un motor "a ciegas" en uno que sabe exactamente lo que está haciendo.

![Motorreductor con encoder magnético en la parte trasera](/img/guias/sensores/encoders/anatomia.svg)

## Un motor con encoder

El formato más habitual en robots pequeños es un **motorreductor con encoder** integrado:

- **Motor DC**: el que da el giro
- **Reductora**: unos engranajes que bajan la velocidad y aumentan la fuerza
- **Disco magnético**: un imán con varios polos, montado en el eje del motor
- **Placa del encoder**: dos sensores Hall (detectan campos magnéticos), llamados **A** y **B**
- **6 cables**: dos para el motor y cuatro para el encoder

## Tipos

| Tipo | Cómo detecta | Dónde se ve |
|---|---|---|
| **Magnético** | sensores Hall y un disco imantado | motorreductores, robots |
| **Óptico** | un disco con ranuras que corta un haz de luz | impresoras, ratones antiguos |
| **Rotativo de mando** (KY-040) | contactos mecánicos | mandos de volumen, menús |

Todos ellos dan el mismo tipo de señal, así que el código es igual para cualquiera.

## Incremental o absoluto

- **Incremental**: da pulsos al girar. Sabes cuánto has girado **desde que empezaste a contar**. Es el que veremos
- **Absoluto**: da directamente la posición del eje, incluso recién encendido. Es más caro y se usa en brazos robóticos industriales

## En robótica

- **Odometría**: calcular cuánto ha avanzado y girado el robot a partir de lo que han girado sus ruedas
- **Control de velocidad**: mantener una velocidad constante aunque cambie la carga o la batería
- **Ir recto**: comparar las dos ruedas y corregir la que va más rápida

El [Rover](/proyectos/rover-web/guides/getting-started/hardware-setup) usa encoders de cuadratura de **4096 cuentas por vuelta** (CPR) en sus motores, y los combina con una [IMU](/guias/sensores/imu) para saber dónde está.
