---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es un LiDAR?

Un **LiDAR** (*Light Detection and Ranging*, detección y medida por luz) mide distancias con un **láser**. El que se usa en robótica móvil va montado sobre una cabeza que **gira 360°**, así que en cada vuelta mide la distancia a todo lo que hay alrededor del robot.

El resultado es un "mapa" plano del entorno, actualizado varias veces por segundo. Es el sensor con el que los robots aspiradora, los robots de almacén y el [Rover](/proyectos/rover-web/guides/getting-started/hardware-setup) saben dónde están las paredes y los obstáculos.

<img src="/img/guias/sensores/lidar/anatomia.svg" alt="RPLIDAR A1 visto desde arriba, con su cabeza giratoria, el motor, la base y el conector" />

## El RPLIDAR A1

El **RPLIDAR A1** de Slamtec es el LiDAR 2D más popular para empezar, y el que monta el Rover:

| | RPLIDAR A1 |
|---|---|
| Alcance | 0,15 – 12 m |
| Barrido | 360° |
| Medidas por segundo | hasta 8000 |
| Frecuencia de giro | 5 – 10 vueltas por segundo |
| Resolución angular | ~1° |
| Conexión | UART, con adaptador USB incluido |
| Alimentación | 5 V (por el propio USB) |

## Sus partes

- **Cabeza giratoria**: lleva el emisor láser y el receptor
- **Motor y correa**: hacen girar la cabeza a velocidad constante
- **Base**: con agujeros para atornillarlo al robot
- **Conector**: sale hacia un pequeño adaptador que lo convierte en un puerto USB

## Del ultrasonido al LiDAR

Comparte la idea del [sensor de ultrasonidos](/guias/sensores/ultrasonidos): enviar algo y ver cómo vuelve. La diferencia está en la escala:

| | HC-SR04 | RPLIDAR A1 |
|---|---|---|
| Qué emite | sonido | luz láser |
| Dirección | un cono fijo de 15° | 360° girando |
| Medidas por segundo | ~20 | ~8000 |
| Resultado | una distancia | el contorno de la habitación |

## En robótica

- **Mapas (SLAM)**: el robot construye un plano de un sitio desconocido mientras averigua dónde está dentro de él
- **Navegación**: planificar rutas y esquivar obstáculos con margen
- **Localización**: comparar lo que ve con un mapa ya hecho para saber su posición exacta

:::note[Láser de clase 1]
El RPLIDAR A1 usa un láser infrarrojo de **clase 1**, seguro para los ojos en uso normal. Aun así, no mires fijamente la cabeza de cerca mientras gira.
:::
