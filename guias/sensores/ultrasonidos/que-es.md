---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es el sensor de ultrasonidos?

El **HC-SR04** mide la **distancia** hasta un objeto usando sonido. Emite un pitido tan agudo que el oído humano no lo percibe (un **ultrasonido**, a 40 kHz), escucha el eco y calcula a qué distancia está lo que lo ha reflejado.

Es el mismo principio que usan los murciélagos y los sensores de aparcamiento de los coches.

![Sensor HC-SR04 con su emisor, su receptor y sus cuatro pines](/img/guias/sensores/ultrasonidos/anatomia.svg)

## Sus partes

- **Emisor (T, *transmitter*)**: el "altavoz" que lanza el pulso de ultrasonido
- **Receptor (R, *receiver*)**: el "micrófono" que escucha el eco
- **Electrónica**: genera el pulso y te avisa de cuánto ha tardado el eco
- **4 pines**: VCC, Trig, Echo y GND

## Características

| | HC-SR04 |
|---|---|
| Alcance | 2 cm a 4 m |
| Resolución | ~3 mm |
| Ángulo de detección | ~15° (un cono estrecho) |
| Alimentación | 5 V |
| Consumo | ~15 mA |

## En robótica

- **Esquivar obstáculos**: el uso estrella. El robot mide qué tiene delante y gira antes de chocar. Lo montarás en el [proyecto del robot esquiva-obstáculos](/guias/proyecto-esquiva-obstaculos)
- **Mantener una distancia**: seguir a una persona o una pared a 20 cm
- **Medir niveles**: el nivel de agua de un depósito, mirando desde arriba

## Lo que mejor detecta

El sonido rebota bien en superficies **duras, planas y de frente**: paredes, cajas, puertas. Las superficies blandas (cojines, ropa) absorben parte del sonido, y las muy inclinadas lo desvían hacia otro lado. Tenlo en cuenta al interpretar las medidas.

:::note[Su hermano mayor]
Cuando un robot necesita ver **todo lo que le rodea** con precisión, se usa un [LiDAR](/guias/sensores/lidar): el mismo principio de "medir lo que tarda en volver", con un láser que gira 360°.
:::
