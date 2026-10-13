---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

Tres cables: los extremos a la alimentación y el cursor a un pin analógico.

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Potenciómetro lineal de 10 kΩ | 1 |
| Protoboard | 1 |
| Cables dupont macho-macho | 3 |

## Esquema de conexión

![Esquema: potenciómetro conectado a 5 V, A0 y GND](/img/guias/sensores/potenciometro/conexion.svg)

| Potenciómetro | Arduino |
|---|---|
| Extremo | **GND** |
| Cursor (central) | **A0** |
| Otro extremo | **5V** |

:::tip
Si al girar a la derecha el valor baja en vez de subir, intercambia los dos cables de los extremos.
:::

Con todo conectado, pasa al [código básico](./codigo-basico).
