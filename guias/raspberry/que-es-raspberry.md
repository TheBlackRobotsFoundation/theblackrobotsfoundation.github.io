---
sidebar_position: 1
title: ¿Qué es Raspberry Pi?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es Raspberry Pi?

Raspberry Pi es un **ordenador completo en una sola placa**: tiene procesador, memoria, USB, red, Wi-Fi, salida de vídeo y un sistema operativo Linux. Le conectas un teclado y una pantalla y funciona como cualquier PC. Y además tiene **40 pines** para conectar electrónica, como un Arduino.

La fabrica la **Raspberry Pi Foundation**, una organización británica creada para acercar la informática a todo el mundo.

<img src="/img/guias/raspberry/placa.svg" alt="Raspberry Pi 5 con sus pines GPIO, procesador, puertos USB, Ethernet, USB-C, micro-HDMI y conectores de cámara" />

## Arduino, Raspberry Pi y Jetson

Las tres aparecen en casi cualquier robot, y cada una tiene su papel:

<img src="/img/guias/raspberry/tres-cerebros.svg" alt="Arduino como microcontrolador, Raspberry Pi como ordenador con Linux y Jetson como ordenador con GPU" />

| | Arduino UNO | Raspberry Pi 5 | Jetson Orin Nano |
|---|---|---|---|
| Qué es | microcontrolador | ordenador | ordenador con GPU |
| Sistema | tu programa, y nada más | Linux | Linux |
| Lenguaje habitual | C++ | Python, C++ | Python, C++ |
| Memoria | 2 KB | 2 – 16 GB | 8 GB |
| Pines | 5 V, con entradas analógicas | 3,3 V, solo digitales | 3,3 V, solo digitales |
| Arranque | instantáneo | unos 20 segundos | unos 30 segundos |
| Su fuerte | tiempo real, sensores y motores | cálculo, red, ROS 2, cámaras | visión e inteligencia artificial |

En un robot es muy habitual usar **dos**: la Raspberry Pi (o la Jetson) piensa y el Arduino mueve los motores y lee los sensores. Lo verás en [Raspberry Pi y Arduino](./raspberry-y-arduino).

## Modelos

| Modelo | Procesador | Memoria | Para qué |
|---|---|---|---|
| **Raspberry Pi 5** | 4 núcleos a 2,4 GHz | 2 – 16 GB | el más potente: ROS 2, visión |
| **Raspberry Pi 4** | 4 núcleos a 1,5 – 1,8 GHz | 1 – 8 GB | sigue siendo muy capaz y fácil de encontrar |
| **Raspberry Pi Zero 2 W** | 4 núcleos a 1 GHz | 512 MB | robots muy pequeños y ligeros |

Para empezar con robótica y ROS 2, la **Raspberry Pi 5 de 4 u 8 GB** es la opción más equilibrada. Todo lo de estas guías funciona también en una Pi 4.

## En robótica

- **El cerebro del robot**: ejecuta [ROS 2](/guias/ros2), decide hacia dónde ir y coordina todas las piezas
- **Visión**: con una cámara, detecta colores, caras, códigos QR o líneas
- **Conexión**: Wi-Fi para controlarlo desde el móvil o el ordenador
- **Sensores avanzados**: un [LiDAR](/guias/sensores/lidar) o una cámara de profundidad se conectan directamente por USB

:::tip
En estas guías usaremos una **Raspberry Pi 5**. Si tienes una Pi 4, todo funciona igual.
:::
