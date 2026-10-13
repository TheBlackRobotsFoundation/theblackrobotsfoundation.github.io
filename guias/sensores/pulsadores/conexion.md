---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

Gracias a la pull-up interna del Arduino, un pulsador necesita solo **dos cables**.

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Pulsador táctil | 1 |
| Protoboard | 1 |
| Cables dupont macho-macho | 2 |

## Esquema de conexión

![Esquema: pulsador conectado al pin 2 y a GND del Arduino](/img/guias/sensores/pulsadores/conexion.svg)

| Pulsador | Arduino |
|---|---|
| Una pata | pin digital **2** |
| La pata en diagonal | **GND** |

Coloca el pulsador **sobre la ranura central** de la protoboard, con dos patas a cada lado. Así cada pareja de patas queda en columnas distintas.

:::tip
Si el pulsador "siempre está pulsado", las dos patas que usas están unidas por dentro. Gíralo 90° o cambia a la pata en diagonal.
:::

Con todo conectado, pasa al [código básico](./codigo-basico).
