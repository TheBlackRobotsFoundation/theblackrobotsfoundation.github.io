---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es una IMU?

Una **IMU** (*Inertial Measurement Unit*, unidad de medida inercial) es un sensor que mide cómo se **mueve y se orienta** un objeto. Es el oído interno de un robot: le dice si está inclinado, si está girando y hacia dónde acelera.

El **MPU6050** es la IMU más popular para empezar. Junta dos sensores en un solo chip:

- Un **acelerómetro** de 3 ejes: mide aceleraciones, incluida la de la gravedad
- Un **giroscopio** de 3 ejes: mide la velocidad a la que gira

Por eso se le llama IMU de **6 ejes** (o 6 DoF, grados de libertad).

![Módulo GY-521 con el chip MPU6050, los ejes y los pines](/img/guias/sensores/imu/anatomia.svg)

## El módulo GY-521

El chip MPU6050 es diminuto, así que se usa montado en el módulo **GY-521**, que añade:

- Un **regulador** de tensión: el chip trabaja a 3,3 V, pero el módulo se puede alimentar a 5 V
- Las **resistencias pull-up** del bus I2C
- **Ejes serigrafiados**: te dicen hacia dónde apunta cada eje de medida
- **8 pines**, de los que bastan cuatro: VCC, GND, SCL y SDA

Se comunica por [I2C](/guias/electronica/comunicacion#i2c), en la dirección `0x68`.

## Qué mide

| Sensor | Mide | Unidad | Rango por defecto |
|---|---|---|---|
| Acelerómetro | aceleración en X, Y, Z | g (1 g = 9,81 m/s²) | ±2 g |
| Giroscopio | velocidad de giro en X, Y, Z | grados por segundo (°/s) | ±250 °/s |
| Termómetro | temperatura del chip | °C | — |

## En robótica

- **Robots que se equilibran**: un robot de dos ruedas (péndulo invertido) corrige su inclinación cientos de veces por segundo
- **Drones**: la IMU es el sensor principal para mantenerse estable en el aire
- **Orientación**: saber hacia dónde mira un robot móvil. El [Rover](/proyectos/rover-web/guides/getting-started/hardware-setup) combina la IMU de su controladora PX4 con los [encoders](/guias/sensores/encoders) de las ruedas
- **Detectar golpes y caídas**: una aceleración brusca indica un choque

:::note[IMUs de 9 ejes]
Algunas IMUs añaden un **magnetómetro** (una brújula de 3 ejes), como el MPU9250 o el BNO055. Con él, el robot sabe también hacia dónde está el norte.
:::
