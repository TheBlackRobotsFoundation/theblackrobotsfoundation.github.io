---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

Conectar un LED a un Arduino es muy sencillo si respetas dos cosas: la **polaridad** (pata larga al +, pata corta al −) y la **resistencia** en serie.

## Lista de componentes

| Componente | Cantidad |
|---|---|
| LED (cualquier color) | 1 |
| Resistencia de 220 Ω | 1 |
| Protoboard | 1 |
| Cables dupont macho-macho | 2 |

## Esquema de conexión

![Esquema: LED con resistencia en una protoboard](/img/guias/led/conexion.png)

El recorrido de la corriente es:

1. Sale por un **pin digital** del Arduino (por ejemplo el pin 8)
2. Pasa por la **resistencia de 220 Ω**
3. Entra por la **pata larga (ánodo, +)** del LED
4. Sale por la **pata corta (cátodo, −)**
5. Vuelve al Arduino por **GND**

:::tip
La resistencia puede ir **antes o después** del LED, da igual el orden: lo que importa es que esté **en serie** (en el mismo camino de la corriente).
:::

## Identificar las patas

- **Pata larga = ánodo (+)** → hacia el pin (a través de la resistencia)
- **Pata corta = cátodo (−)** → hacia GND
- Si las patas están cortadas iguales, busca el **lado plano** del LED: ese borde es el **cátodo (−)**

:::caution
Si el LED no enciende, lo más probable es que esté **del revés**. Dale la vuelta: al ser un diodo, conectado al contrario simplemente no luce (no se rompe por eso, pero no funciona).
:::
