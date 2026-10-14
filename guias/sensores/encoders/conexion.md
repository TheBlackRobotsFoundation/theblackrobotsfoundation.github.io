---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

Los cuatro cables del encoder van al Arduino. Los dos del motor van a su driver, como cualquier [motor DC](/guias/actuadores/motores-dc/conexion).

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Motorreductor con encoder Hall (tipo JGA25-370 o N20) | 1 |
| Cables dupont | 4 |
| Driver de motor (para hacerlo girar) | opcional |

## Esquema de conexión

<img src="/img/guias/sensores/encoders/conexion.svg" alt="Esquema: encoder con VCC a 5 V, GND, A al pin 2 y B al pin 3" />

| Encoder | Arduino |
|---|---|
| `VCC` | **5V** |
| `GND` | **GND** |
| `A` (C1) | pin digital **2** |
| `B` (C2) | pin digital **3** |
| `M1` y `M2` | al driver del motor |

:::caution
**M1 y M2 son los cables del motor.** Conéctalos únicamente al driver, nunca a un pin del Arduino.
:::

Los colores cambian entre fabricantes. Uno muy habitual es: **rojo** M1, **negro** GND, **amarillo** A, **verde** B, **azul** VCC y **blanco** M2. Comprueba la serigrafía de la placa del encoder.

:::tip
Para probar el encoder no hace falta mover el motor: gira la rueda **a mano** y verás los pulsos en el Monitor Serie.
:::

## Con un encoder de mando (KY-040)

Si usas un encoder rotativo de los de mando: `CLK` → pin 2, `DT` → pin 3, `+` → 5V, `GND` → GND. Su pin `SW` es un pulsador al apretar el eje, y se lee como un [pulsador](/guias/sensores/pulsadores).

Con todo conectado, pasa al [código básico](./codigo-basico).
