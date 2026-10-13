---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

## Medir una distancia: triangulación

El RPLIDAR A1 mide por **triangulación láser**. El emisor lanza un punto de luz; un pequeño sensor de imagen, colocado a unos centímetros, lo ve rebotar en el objeto. Según lo lejos que esté, la luz vuelve con un **ángulo distinto** y cae en un punto distinto del sensor:

![El ángulo con el que vuelve la luz cambia con la distancia al objeto](/img/guias/sensores/lidar/triangulacion.svg)

El chip del LiDAR convierte esa posición en una distancia. Lo hace miles de veces por segundo.

:::note
Los LiDAR de más alcance (como los RPLIDAR de la serie S) miden por **tiempo de vuelo** (*ToF*): cronometran lo que tarda la luz en ir y volver, igual que el ultrasonido con el sonido.
:::

## Medir todo el entorno: el barrido

Mientras la cabeza gira, el LiDAR toma medidas continuamente. Cada una es una pareja **(ángulo, distancia)**. Al terminar una vuelta tienes unos cientos de puntos que dibujan el contorno de todo lo que rodea al robot:

![Habitación vista desde arriba con los puntos que mide el LiDAR en una vuelta](/img/guias/sensores/lidar/barrido.svg)

Fíjate en la **sombra** detrás de la caja: el láser no atraviesa objetos, así que lo que queda detrás de un obstáculo no aparece en esa vuelta. El robot lo descubrirá cuando se mueva.

## De ángulo y distancia a coordenadas

Para dibujar los puntos o trabajar con ellos, se pasan de coordenadas polares a cartesianas (con el LiDAR en el origen):

```
x = distancia × cos(ángulo)
y = distancia × sin(ángulo)
```

## Cómo envía los datos

El LiDAR habla por **UART** a 115200 baudios. El adaptador incluido lo convierte en un puerto USB, que en Linux aparece como `/dev/ttyUSB0`. Cada medida llega con tres valores:

| Dato | Qué es |
|---|---|
| **Calidad** | cuánta luz ha vuelto (0 = medida no válida) |
| **Ángulo** | en grados, de 0 a 360 |
| **Distancia** | en milímetros |

Son unos **8000 datos por segundo**: demasiados para un Arduino UNO, que tiene 2 KB de RAM. Por eso el LiDAR se conecta a un ordenador o una **Raspberry Pi**, y ahí se procesa con Python o con ROS 2.

## Lo que más le cuesta

- **Cristales y espejos**: la luz los atraviesa o rebota hacia otro lado
- **Superficies negras mate**: absorben el láser y devuelven poca luz
- **Objetos por encima o por debajo del plano**: un LiDAR 2D mide solo a su altura. Una mesa puede "desaparecer" si el láser pasa entre sus patas
