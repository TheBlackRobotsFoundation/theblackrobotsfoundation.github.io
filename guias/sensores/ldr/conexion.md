---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

La LDR y una resistencia de 10 kΩ forman un divisor de tensión. El punto donde se unen va a **A0**.

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Fotorresistencia (LDR) | 1 |
| Resistencia de 10 kΩ (marrón, negro, naranja) | 1 |
| Protoboard | 1 |
| Cables dupont macho-macho | 3 |

## Esquema de conexión

![Esquema: LDR y resistencia de 10 kΩ formando un divisor conectado a A0](/img/guias/sensores/ldr/conexion.svg)

El recorrido es:

1. **5V** del Arduino → una pata de la LDR
2. La otra pata de la LDR → **A0** y, en ese mismo punto, la resistencia de 10 kΩ
3. El otro extremo de la resistencia → **GND**

:::tip
En la protoboard, el "punto de unión" es simplemente una columna donde coinciden la pata de la LDR, la de la resistencia y el cable que va a A0.
:::

Con todo conectado, pasa al [código básico](./codigo-basico).
