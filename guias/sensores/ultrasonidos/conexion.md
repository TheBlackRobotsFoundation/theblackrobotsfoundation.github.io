---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

Cuatro cables: dos de alimentación y dos de señal.

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Sensor HC-SR04 | 1 |
| Cables dupont macho-hembra | 4 |

## Esquema de conexión

![Esquema: HC-SR04 conectado a 5 V, pines 10 y 9 y GND](/img/guias/sensores/ultrasonidos/conexion.svg)

| HC-SR04 | Arduino |
|---|---|
| `VCC` | **5V** |
| `Trig` | pin digital **10** |
| `Echo` | pin digital **9** |
| `GND` | **GND** |

Trig y Echo pueden ir a **cualquier pin digital**. Si cambias los pines, cámbialos también en el código.

:::tip
Monta el sensor **lo más recto posible**, mirando al frente y algo elevado del suelo. Si apunta hacia abajo, detectará el propio suelo como un obstáculo.
:::

:::note[Placas de 3,3 V]
El HC-SR04 saca **5 V** por Echo. Con el UNO no hay problema. Si lo usas con una placa de 3,3 V (ESP32, Raspberry Pi), pon un [divisor de tensión](/guias/electronica/divisor-de-tension) en Echo o usa la versión **HC-SR04P**, que funciona a 3,3 V.
:::

Con todo conectado, pasa al [código básico](./codigo-basico).
