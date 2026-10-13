---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

Con el módulo de 3 pines, la conexión es directa: alimentación, datos y GND.

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Módulo DHT22 (o DHT11) de 3 pines | 1 |
| Cables dupont macho-hembra | 3 |

## Esquema de conexión

![Esquema: módulo DHT22 conectado a 5 V, pin 2 y GND](/img/guias/sensores/temperatura/conexion.svg)

| DHT22 | Arduino |
|---|---|
| `+` (VCC) | **5V** |
| `OUT` (DATA) | pin digital **2** |
| `−` (GND) | **GND** |

:::caution
El orden de los pines **cambia entre fabricantes**. Antes de conectar, lee lo que pone serigrafiado en tu placa: `+`, `OUT` y `−` (o `VCC`, `DATA`, `GND`).
:::

## Si usas el sensor suelto (4 patas)

Mirándolo de frente, con la rejilla hacia ti, las patas de izquierda a derecha son:

1. **VCC** → 5V
2. **DATA** → pin 2, y una resistencia de **10 kΩ** entre este pin y 5V
3. Sin conexión
4. **GND** → GND

Con todo conectado, pasa al [código básico](./codigo-basico).
