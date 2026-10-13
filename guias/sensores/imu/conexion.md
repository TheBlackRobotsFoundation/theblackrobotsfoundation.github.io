---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

Cuatro cables: alimentación y los dos del bus [I2C](/guias/electronica/comunicacion#i2c).

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Módulo MPU6050 (GY-521) | 1 |
| Cables dupont macho-hembra | 4 |

## Esquema de conexión

![Esquema: MPU6050 con VCC a 5 V, GND, SDA a A4 y SCL a A5](/img/guias/sensores/imu/conexion.svg)

| MPU6050 | Arduino UNO |
|---|---|
| `VCC` | **5V** |
| `GND` | **GND** |
| `SCL` | **A5** (o el pin SCL junto a AREF) |
| `SDA` | **A4** (o el pin SDA junto a AREF) |

En el UNO, A4/A5 y los pines SDA/SCL de la fila de arriba son **los mismos**: usa los que te queden más cómodos.

## Los otros pines

| Pin | Para qué sirve |
|---|---|
| `AD0` | cambia la dirección: sin conectar (o a GND) = `0x68`, a 3,3 V = `0x69`. Permite usar dos MPU6050 a la vez |
| `INT` | avisa al Arduino cuando hay datos nuevos (uso avanzado) |
| `XDA`, `XCL` | para conectarle un magnetómetro externo |

## Montaje en el robot

- **Fíjalo bien**: con tornillos o cinta de doble cara. Si baila, medirá sus propias vibraciones
- **Alineado**: con los ejes serigrafiados paralelos a los del robot (X hacia delante, por ejemplo). Así los ángulos coinciden con los del robot sin hacer cuentas
- **Cerca del centro de giro** y lejos de los motores, que vibran y generan campos magnéticos

Con todo conectado, pasa al [código básico](./codigo-basico).
