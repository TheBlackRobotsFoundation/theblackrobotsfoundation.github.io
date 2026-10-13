---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

El montaje tiene tres partes: el **motor** al driver, la **batería** al driver y el **Arduino** al driver, con un GND compartido.

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Módulo L298N | 1 |
| Motor DC o motorreductor (6 – 12 V) | 1 o 2 |
| Batería de 7 – 12 V (LiPo 2S, 6 × AA o similar) | 1 |
| Cables dupont y destornillador pequeño | — |

## Esquema de conexión

![Esquema: motor en OUT1 y OUT2, batería en 12V y GND, y ENA, IN1 e IN2 a los pines 11, 10 y 9](/img/guias/actuadores/motores-dc/conexion.svg)

### Motor

| Motor | L298N |
|---|---|
| un terminal | `OUT1` |
| el otro terminal | `OUT2` |

### Alimentación

| De | A |
|---|---|
| Batería + | `12V` del L298N |
| Batería − | `GND` del L298N |
| `GND` del L298N | **GND** del Arduino |

### Control

| L298N | Arduino |
|---|---|
| `ENA` | pin **11** (PWM) |
| `IN1` | pin **10** |
| `IN2` | pin **9** |

## Los puentes (*jumpers*) del módulo

El L298N trae unos puentes de plástico que conviene revisar antes de alimentar:

- **ENA y ENB**: con el puente puesto, el motor va siempre a tope. **Quítalo** para controlar la velocidad desde el Arduino. De los dos pines que quedan al aire, uno es la señal ENA y el otro da 5 V: conecta el cable del Arduino al que está serigrafiado como **ENA**. Si dudas, mide con un polímetro con la batería conectada; el que marca 5 V es el que hay que dejar libre
- **5V-EN** (junto a las bornas de alimentación): con el puente puesto y la batería a **12 V o menos**, el regulador del módulo da 5 V por la borna `5V`. Por encima de 12 V hay que quitarlo

:::caution
- **Une siempre los GND** de la batería, el L298N y el Arduino. Sin ese cable, el motor no responde o hace cosas raras
- Conecta y desconecta los motores con la **batería desconectada**
- Si un motor gira al revés de lo que esperabas, **intercambia sus dos cables** en OUT1 y OUT2
:::

## Un segundo motor

Igual que el primero, en el otro lado del módulo:

| L298N | Conecta a |
|---|---|
| `OUT3` y `OUT4` | el motor B |
| `ENB` | pin **6** (PWM) |
| `IN3` | pin **8** |
| `IN4` | pin **7** |

Es justo el montaje del [robot esquiva-obstáculos](/guias/proyecto-esquiva-obstaculos).

Con todo conectado, pasa al [código básico](./codigo-basico).
