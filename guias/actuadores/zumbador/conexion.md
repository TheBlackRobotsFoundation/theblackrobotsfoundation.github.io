---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

Dos cables, con una resistencia pequeña en serie para proteger el pin.

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Zumbador (activo o pasivo) | 1 |
| Resistencia de 100 Ω (marrón, negro, marrón) | 1 |
| Protoboard y cables | — |

## Esquema de conexión

![Esquema: zumbador con su + al pin 8 a través de 100 Ω y su − a GND](/img/guias/actuadores/zumbador/conexion.svg)

| Zumbador | Arduino |
|---|---|
| `+` (pata larga) | pin digital **8**, a través de la resistencia de 100 Ω |
| `−` | **GND** |

## ¿Por qué la resistencia?

Los zumbadores piezoeléctricos consumen muy poco, pero los magnéticos pueden pedir más corriente de la que conviene sacar de un pin (unos 20 mA). Con 100 Ω en serie, cualquiera de los dos queda protegido y sigue sonando de sobra.

:::tip[Más volumen]
Para una alarma que se oiga de verdad, se alimenta el zumbador a través de un **transistor** (como un 2N2222 o un BC547): el pin del Arduino solo da la orden y el transistor deja pasar la corriente. Es el mismo principio que usa un [módulo de relé](/guias/actuadores/reles/como-funciona).
:::

Con todo conectado, pasa al [código básico](./codigo-basico).
