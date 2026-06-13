---
sidebar_position: 3
title: Cómo se conectan
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conectan

Para mover un motor paso a paso bipolar con Arduino necesitas un **driver** intermedio. El Arduino no puede dar la corriente que necesita el motor directamente: el driver se encarga de eso.

Usaremos el **A4988**, el driver más común para motores NEMA 17.

## Qué necesitas

- Arduino UNO
- Driver A4988
- Motor NEMA 17 (bipolar, 4 cables)
- Fuente de alimentación de 12V
- Un condensador de 100µF entre VMOT y GND (protege el driver)

## Esquema de conexiones

![Esquema: Arduino + A4988 + motor](/img/guias/motores/esquema-conexion.svg)

## Conexiones del A4988

| Pin A4988 | Se conecta a |
|---|---|
| `VMOT` | + de la fuente 12V |
| `GND` (junto a VMOT) | – de la fuente 12V |
| `VDD` | 5V del Arduino |
| `GND` (junto a VDD) | GND del Arduino |
| `STEP` | pin digital **12** (amarillo) |
| `DIR` | pin digital **11** (verde) |
| `1A 1B 2A 2B` | las 4 fases del motor |
| `EN` | (opcional) habilitar/deshabilitar |

:::caution[Muy importante]
- Pon el **condensador** entre VMOT y GND **antes** de alimentar. Sin él, los picos de tensión pueden destruir el driver.
- **Nunca** conectes o desconectes el motor con el driver alimentado.
- Ajusta la corriente con el **potenciómetro** del A4988 (Vref) según tu motor.
:::

## Las bobinas del motor

El motor bipolar tiene 2 bobinas (4 cables). Cada bobina va a un par:

- Bobina 1 → `1A` y `1B`
- Bobina 2 → `2A` y `2B`

:::tip
¿No sabes qué cables forman cada bobina? Junta dos cables: si al hacerlo notas resistencia al girar el eje a mano, esos dos son de la misma bobina.
:::

Con todo conectado, ya puedes pasar al [código básico](./codigo-basico) para moverlo.
