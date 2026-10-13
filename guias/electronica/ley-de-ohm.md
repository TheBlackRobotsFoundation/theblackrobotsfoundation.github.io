---
sidebar_position: 1
sidebar_label: Tensión y corriente
title: Tensión, corriente y resistencia
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# Tensión, corriente y resistencia

Tres magnitudes explican casi todo lo que pasa en un circuito. Entenderlas bien te ahorra muchos componentes quemados.

| Magnitud | Qué mide | Unidad | Símil con el agua |
|---|---|---|---|
| **Tensión** (V) | La "presión" que empuja a los electrones | voltio (V) | La altura del depósito |
| **Corriente** (I) | Cuántos electrones pasan por segundo | amperio (A) | El caudal de la tubería |
| **Resistencia** (R) | Cuánto se opone un componente al paso de corriente | ohmio (Ω) | Un estrechamiento en la tubería |

## La Ley de Ohm

Las tres se relacionan con una sola fórmula:

![Ley de Ohm: una pila, una resistencia y la corriente que circula](/img/guias/electronica/ley-de-ohm.svg)

Despejando, obtienes la que necesites en cada momento:

```
V = I × R        I = V / R        R = V / I
```

### Un ejemplo

Conectas una resistencia de **1 kΩ** (1000 Ω) a los **5 V** del Arduino. ¿Cuánta corriente circula?

```
I = 5 V / 1000 Ω = 0,005 A = 5 mA
```

Es exactamente el cálculo que se hace para elegir la resistencia de un [LED](/guias/actuadores/led/como-funciona).

## La potencia

Cuando la corriente atraviesa una resistencia, parte de la energía se convierte en **calor**. Esa potencia se calcula así:

```
P = V × I        (en vatios, W)
```

Las resistencias comunes aguantan **0,25 W**. En los circuitos de las guías trabajarás muy por debajo, pero es el motivo por el que un componente "pequeño" se calienta si le pides demasiada corriente.

## Prefijos que verás a todas horas

| Prefijo | Valor | Ejemplo |
|---|---|---|
| **k** (kilo) | × 1000 | 10 kΩ = 10 000 Ω |
| **M** (mega) | × 1 000 000 | 1 MΩ |
| **m** (mili) | ÷ 1000 | 20 mA = 0,020 A |
| **µ** (micro) | ÷ 1 000 000 | 100 µF, 10 µs |

:::tip
El Arduino UNO trabaja a **5 V** y cada pin entrega con comodidad unos **20 mA**. Con esos dos números en la cabeza ya puedes saber si un componente se puede conectar directamente o necesita algo intermedio. Lo verás en [cómo alimentar un robot](./alimentacion).
:::
