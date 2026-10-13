---
sidebar_position: 5
sidebar_label: Comunicación
title: Comunicación (UART, I2C, SPI)
sidebar_custom_props:
  icon: /img/guias/iconos/documentacion.svg
---

# Comunicación: UART, I2C y SPI

Los sensores sencillos dan una tensión o un HIGH/LOW. Los más avanzados (una IMU, un LiDAR, una pantalla) **envían datos** en forma de bytes. Para eso usan un **protocolo de comunicación**: unas reglas comunes para hablar por unos pocos cables.

## UART (puerto serie)

Dos cables cruzados: lo que uno transmite (**TX**) llega a lo que el otro recibe (**RX**).

```
Arduino TX  ──→  RX dispositivo
Arduino RX  ←──  TX dispositivo
        GND ───  GND
```

- Comunica **dos** dispositivos
- Ambos deben usar la misma **velocidad** (*baud rate*), por ejemplo 9600 o 115200
- Es lo que usa el **Monitor Serie** del Arduino IDE a través del USB

```cpp
Serial.begin(9600);
Serial.println("Hola");
```

Un ejemplo real: el [LiDAR](/guias/sensores/lidar) del Rover envía sus medidas por UART, a través de un adaptador USB.

## I2C

Dos cables compartidos por **muchos dispositivos** a la vez:

- **SDA**: los datos
- **SCL**: el reloj que marca el ritmo

![Bus I2C con un Arduino y tres dispositivos conectados a SDA y SCL](/img/guias/electronica/bus-i2c.svg)

Cada dispositivo tiene una **dirección** (un número como `0x68`) y solo responde cuando le llaman por ella. En el UNO, SDA es **A4** y SCL es **A5** (también están duplicados junto al pin AREF).

```cpp
#include <Wire.h>

void setup() {
  Wire.begin();   // el Arduino controla el bus
}
```

Lo usarás con la [IMU MPU6050](/guias/sensores/imu).

:::tip
¿No sabes qué dirección tiene un módulo? Un **escáner I2C** recorre el bus y te muestra las direcciones que responden. Tienes uno listo en la [guía de la IMU](/guias/sensores/imu/codigo-basico#escáner-i2c).
:::

## SPI

Cuatro cables y mucha velocidad. Se usa con tarjetas SD, pantallas y algunos sensores rápidos.

| Señal | Función | Pin UNO |
|---|---|---|
| **MOSI** | datos del Arduino al dispositivo | 11 |
| **MISO** | datos del dispositivo al Arduino | 12 |
| **SCK** | reloj | 13 |
| **CS** | elige con qué dispositivo se habla | cualquiera (normalmente 10) |

## Cuál es cuál

| | UART | I2C | SPI |
|---|---|---|---|
| Cables | 2 (+ GND) | 2 (+ GND) | 4 (+ GND) |
| Dispositivos | 2 | hasta ~100 | varios, un CS por cada uno |
| Velocidad | media | media | alta |
| Ejemplo | GPS, LiDAR | IMU, pantallas OLED | tarjeta SD |

En la práctica, la librería de cada módulo se encarga del protocolo. Lo que te toca a ti es **conectar bien los cables**, y para eso basta con saber cuál usa.
