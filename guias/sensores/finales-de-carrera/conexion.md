---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

Dos cables, igual que un pulsador: **COM** a GND y **NO** a un pin digital.

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Final de carrera (microinterruptor con palanca) | 1 |
| Cables dupont con terminal hembra o soldados | 2 |

## Esquema de conexión

<img src="/img/guias/sensores/finales-de-carrera/conexion.svg" alt="Esquema: final de carrera con COM a GND y NO al pin 2" />

| Final de carrera | Arduino |
|---|---|
| `COM` | **GND** |
| `NO` | pin digital **2** |
| `NC` | sin conectar |

Las letras suelen venir grabadas en el lateral del interruptor, junto a cada terminal.

:::tip[Módulos de impresora 3D]
Los finales de carrera para impresoras 3D vienen montados en una plaquita con 3 cables (VCC, GND y señal) y un LED. Esos se conectan con la señal a un pin, VCC a 5V y GND a GND, y se leen con `INPUT` normal: la placa ya trae su propia resistencia.
:::

Con todo conectado, pasa al [código básico](./codigo-basico).
