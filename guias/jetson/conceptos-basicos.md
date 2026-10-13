---
sidebar_position: 5
title: Conceptos básicos
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Conceptos básicos

## Modos de energía

La Jetson puede trabajar con distintos límites de consumo. Con menos consumo, la batería dura más; con más, rinde más.

```bash
sudo nvpmodel -q          # muestra el modo actual
```

El modo se cambia desde el **icono de NVIDIA** de la barra superior del escritorio, o con `sudo nvpmodel -m` seguido del número del modo (la lista de tu modelo está en `/etc/nvpmodel.conf`). En el Orin Nano Super, el modo de máxima potencia se llama **MAXN SUPER**.

Para sacar todo el rendimiento dentro del modo actual, fija las frecuencias al máximo:

```bash
sudo jetson_clocks
```

:::tip
Con `jtop` ves el modo, la temperatura y el consumo en vatios en todo momento. Si la temperatura sube mucho, revisa que el ventilador gira y que la placa tiene aire alrededor.
:::

## CUDA, cuDNN y TensorRT

| Nombre | Qué es | Cuándo lo usas |
|---|---|---|
| **CUDA** | la forma de programar la GPU | a través de librerías como PyTorch u OpenCV |
| **cuDNN** | funciones optimizadas para redes neuronales | lo usa PyTorch por debajo |
| **TensorRT** | optimiza una red ya entrenada para que vaya lo más rápido posible en esa GPU | para el programa final del robot |

El camino habitual: entrenas o descargas un modelo, lo pruebas con PyTorch y, para el robot, lo conviertes a TensorRT para ganar velocidad.

## Los 40 pines

La cabecera de la Jetson tiene **la misma disposición física** que la de la [Raspberry Pi](/guias/raspberry/conceptos-basicos#los-40-pines): alimentación, GND, I2C, SPI y UART en las mismas posiciones, y GPIO a **3,3 V**. Muchos módulos pensados para Raspberry funcionan también aquí.

Se programan con la librería **Jetson.GPIO**, que funciona igual que `RPi.GPIO`:

```python
import time
import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)       # numeración física de los pines
GPIO.setup(12, GPIO.OUT)

while True:
    GPIO.output(12, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12, GPIO.LOW)
    time.sleep(1)
```

Las funciones especiales de algunos pines (PWM, otro bus I2C o SPI) se activan con la herramienta `sudo /opt/nvidia/jetson-io/jetson-io.py`.

:::caution
En un robot, la Jetson trabaja mejor como cerebro, sin conectarle directamente motores ni sensores sencillos. Para eso, un [Arduino por USB](/guias/raspberry/raspberry-y-arduino) es más robusto: el mismo programa de la Raspberry funciona en la Jetson.
:::

## Cámaras

| Tipo | Conexión | Ventaja |
|---|---|---|
| **USB (webcam)** | USB | la más sencilla, funciona con `cv2.VideoCapture(0)` |
| **CSI** (como la Raspberry Pi Camera v2) | conector plano | menos retardo, la procesa el hardware de la Jetson |
| **Profundidad** (Intel RealSense, OAK-D) | USB 3 | da la distancia de cada píxel, ideal para esquivar obstáculos |

## Alimentación en el robot

El kit de desarrollo trae una fuente de **19 V**. En un robot se alimenta desde la batería con un regulador que dé la tensión y la corriente que pide tu placa. Así lo hace el [Rover](/proyectos/rover-web/guides/getting-started/hardware-setup): batería, regulador y Jetson, con fusibles en las líneas principales.

## ROS 2 en la Jetson

JetPack 6 es Ubuntu 22.04, así que [ROS 2 Humble](/guias/ros2/instalacion) se instala igual que en un ordenador. NVIDIA publica además **Isaac ROS**: paquetes de ROS 2 que usan la GPU para visión, detección de objetos y localización con cámaras.
