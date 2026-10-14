---
sidebar_position: 6
title: Sensores por I2C
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Sensores por I2C

Muchos sensores avanzados se conectan por [I2C](/guias/electronica/comunicacion#i2c): IMUs, sensores de distancia láser, de temperatura, pantallas... La Raspberry tiene un bus I2C en los pines **3 (SDA)** y **5 (SCL)**. Como ejemplo, conectamos la misma IMU de la guía de [Arduino](/guias/sensores/imu).

## 1. Activar I2C

En Raspberry Pi OS:

```bash
sudo raspi-config
```

**Interface Options → I2C → Yes** y reinicia. En Ubuntu viene activado. Instala después las herramientas y la librería de Python:

```bash
sudo apt install i2c-tools python3-smbus2
```

## 2. Conectar la IMU

<img src="/img/guias/raspberry/imu.svg" alt="MPU6050 conectado a la Raspberry: VCC a 3,3 V, GND, SDA al pin 3 y SCL al pin 5" />

| MPU6050 | Raspberry Pi |
|---|---|
| `VCC` | **3,3 V** (pin 17) |
| `GND` | **GND** (pin 9) |
| `SDA` | **SDA**, GPIO2 (pin 3) |
| `SCL` | **SCL**, GPIO3 (pin 5) |

:::tip
Aliméntalo con **3,3 V**. Así todo el bus I2C trabaja a la tensión de la Raspberry y sus pines quedan protegidos.
:::

## 3. Comprobar que aparece

```bash
i2cdetect -y 1
```

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
...
60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

El `68` es la dirección del MPU6050, igual que en el [escáner I2C](/guias/sensores/imu/codigo-basico#escáner-i2c) de Arduino. Si no aparece, revisa SDA y SCL.

## 4. Leer la inclinación

Los registros son los mismos que en Arduino: se despierta el sensor escribiendo un 0 en el registro `0x6B` y se leen 14 bytes a partir del `0x3B`.

```python
import math
import time
from smbus2 import SMBus

MPU = 0x68
bus = SMBus(1)                         # el bus I2C de los pines 3 y 5
bus.write_byte_data(MPU, 0x6B, 0)      # despierta el sensor


def con_signo(alto, bajo):
    valor = (alto << 8) | bajo
    return valor - 65536 if valor >= 32768 else valor


while True:
    d = bus.read_i2c_block_data(MPU, 0x3B, 14)   # 14 bytes desde el registro 0x3B
    ax = con_signo(d[0], d[1]) / 16384.0          # en g
    ay = con_signo(d[2], d[3]) / 16384.0
    az = con_signo(d[4], d[5]) / 16384.0
    gz = con_signo(d[12], d[13]) / 131.0          # en °/s

    roll = math.degrees(math.atan2(ay, az))
    pitch = math.degrees(math.atan2(-ax, math.sqrt(ay * ay + az * az)))
    print(f'roll {roll:6.1f}°   pitch {pitch:6.1f}°   giro Z {gz:6.1f} °/s')
    time.sleep(0.1)
```

```
roll   30.0°   pitch    0.4°   giro Z    0.3 °/s
```

- `SMBus(1)` abre el bus I2C número 1, el de la cabecera
- `read_i2c_block_data(dirección, registro, n)` lee `n` bytes seguidos
- `con_signo()` junta los dos bytes de cada medida en un número con signo, lo que en Arduino hacía el tipo `int16_t`

Para un ángulo estable, añade el [filtro complementario](/guias/sensores/imu/como-funciona#la-fusión-lo-mejor-de-cada-uno): funciona exactamente igual en Python.

## Otros sensores I2C

La forma de trabajar es siempre la misma: comprobar la dirección con `i2cdetect` y leer sus registros, o usar la librería que ofrece el fabricante. Muchos módulos tienen librería de Python en el proyecto **Adafruit Blinka / CircuitPython**, que funciona en la Raspberry:

| Sensor | Mide |
|---|---|
| VL53L0X | distancia con láser, hasta 2 m |
| BME280 | temperatura, humedad y presión |
| ADS1115 | 4 entradas analógicas: lo que le falta a la Raspberry |
| SSD1306 | pantalla OLED pequeña |
