---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

Puedes usar solo la salida digital, solo la analógica o las dos. En el esquema conectamos las dos para probarlas.

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Módulo TCRT5000 | 1 |
| Cables dupont macho-hembra | 4 |
| Cinta aislante negra y un folio blanco | para probar |

## Esquema de conexión

![Esquema: TCRT5000 conectado a 5 V, GND, pin 2 y A0](/img/guias/sensores/infrarrojos/conexion.svg)

| TCRT5000 | Arduino |
|---|---|
| `VCC` | **5V** |
| `GND` | **GND** |
| `DO` | pin digital **2** |
| `AO` | **A0** |

:::tip
Para probar, pega una tira de cinta aislante negra sobre un folio blanco y pasa el sensor por encima, a unos milímetros.
:::

## Para un robot sigue-líneas

Se usan dos sensores (o más), uno a cada lado de la línea, separados algo más que el ancho de la cinta. Cada uno a su propio pin: por ejemplo **DO izquierdo → pin 2** y **DO derecho → pin 3**.

Con todo conectado, pasa al [código básico](./codigo-basico).
