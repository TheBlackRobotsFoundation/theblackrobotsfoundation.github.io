---
sidebar_position: 1
title: ¿Qué es una Jetson?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es una NVIDIA Jetson?

Una **Jetson** es un ordenador pequeño de NVIDIA con una **GPU** integrada: el mismo tipo de procesador gráfico que usan los ordenadores para entrenar inteligencia artificial, en una placa que cabe en la mano y consume como una bombilla.

Es la placa de los robots que **ven y entienden** lo que tienen delante: detectar personas y objetos en tiempo real, seguir caminos con una cámara, procesar nubes de puntos de un [LiDAR](/guias/sensores/lidar) o ejecutar redes neuronales sin depender de internet. El [Rover](/proyectos/rover-web) usa una **Jetson Orin** como cerebro.

<img src="/img/guias/jetson/placa.svg" alt="Jetson Orin Nano Developer Kit con su módulo, la cabecera de 40 pines, los puertos y los conectores de cámara" />

## Módulo y kit de desarrollo

Una Jetson tiene dos partes:

- **El módulo**: la placa pequeña con el procesador, la GPU y la memoria. Va debajo del disipador
- **La placa base** (*carrier board*): la que trae los conectores (USB, red, cámaras, pines)

Para empezar se compra un **kit de desarrollo** (*Developer Kit*), que trae las dos montadas y listas para usar.

## Por qué una GPU

<img src="/img/guias/jetson/cpu-gpu.svg" alt="Una CPU con pocos núcleos muy capaces frente a una GPU con cientos de núcleos sencillos" />

- La **CPU** tiene pocos núcleos muy listos: resuelve tareas complejas una tras otra
- La **GPU** tiene cientos o miles de núcleos sencillos: hace la misma operación sobre miles de datos **a la vez**

Una imagen tiene cientos de miles de píxeles, y una red neuronal hace millones de multiplicaciones. Las dos cosas son justo el tipo de trabajo en el que una GPU va decenas de veces más rápido que una CPU.

## Modelos

| Modelo | IA (TOPS) | Memoria | Consumo | Para qué |
|---|---|---|---|---|
| **Jetson Orin Nano Super** (kit) | hasta 67 | 8 GB | 7 – 25 W | empezar: visión, ROS 2, robots móviles |
| **Jetson Orin NX** | hasta 157 | 8 – 16 GB | 10 – 40 W | robots con varias cámaras |
| **Jetson AGX Orin** | hasta 275 | 32 – 64 GB | 15 – 60 W | robots autónomos complejos |

Los **TOPS** (billones de operaciones por segundo) miden su capacidad para inteligencia artificial. Para empezar, el **Orin Nano Super Developer Kit** es la opción natural: es el más asequible y tiene potencia de sobra para aprender.

## Raspberry Pi o Jetson

| | Raspberry Pi 5 | Jetson Orin Nano |
|---|---|---|
| CPU | 4 núcleos Arm | 6 núcleos Arm |
| GPU para IA | — | 1024 núcleos CUDA |
| Visión e IA en tiempo real | básica | su punto fuerte |
| Sistema | Raspberry Pi OS o Ubuntu | Ubuntu (Jetson Linux) |
| ROS 2 | sí | sí |
| Precio aproximado | 60 – 120 € | 250 – 300 € |

Si tu robot necesita **ver**, la Jetson. Si tiene que coordinar sensores y motores, navegar con ROS 2 o conectarse a la red, una [Raspberry Pi](/guias/raspberry) lo hace perfectamente y cuesta mucho menos.

:::tip
En estas guías usaremos el **Jetson Orin Nano Developer Kit**. Todo funciona igual en las demás Jetson Orin.
:::
