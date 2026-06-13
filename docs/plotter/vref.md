---
id: plotter-vref
title: Ajuste de los drivers (Vref)
sidebar_label: Ajuste de drivers (Vref)
sidebar_position: 6
---

# Ajuste de los drivers (Vref)

Cada driver A4988 decide **cuánta corriente** le llega al motor. Ese límite se ajusta con un **potenciómetro** diminuto que lleva el propio driver, y al voltaje de referencia que marca se le llama **Vref**.

¿Por qué importa?

- **Poca corriente** → el motor va flojo, pierde pasos y el dibujo sale mal
- **Demasiada corriente** → el motor y el driver se **calientan** en exceso y se pueden dañar

El objetivo es darle al motor la corriente justa.

:::info
Este paso necesita un **multímetro** y un destornillador muy fino. Si nunca lo has hecho, ve con calma: es delicado pero no difícil.
:::

## ¿De dónde saco la corriente del motor?

La corriente **no la eliges tú: es un dato de tu motor**. La encuentras en:

- La **etiqueta pegada en el propio motor**, o
- Su **datasheet** (hoja de características)

Búscala como **"Rated Current"** o **"Current/Phase"** (corriente por fase), expresada en amperios. En motores estilo NEMA 17 suele estar entre **1.2 A y 2.0 A**.

## Calcular el Vref objetivo

Una vez sabes la corriente de tu motor, para los A4988 la fórmula es:

```
Vref = corriente_del_motor × 8 × Rsense
```

El `Rsense` depende de la versión del driver (suele venir impreso en las resistencias de la placa). El valor más común es **0.100 Ω**, que simplifica la fórmula a:

```
Vref = corriente_del_motor × 0.8
```

:::tip
En un plotter el cabezal pesa poco, así que **no hace falta exprimir el motor**. Ajusta la corriente a un **70-80%** de la nominal del motor: tendrás fuerza de sobra y todo irá más fresco.
:::

## Cómo ajustarlo, paso a paso

El tornillo que hay que girar es el **potenciómetro** del propio driver: una pieza metálica diminuta que asoma sobre la placa del A4988.

<img src="/img/plotter/vref-tornillo.jpg" alt="Medición del Vref con el multímetro sobre la CNC Shield" width="440" />

1. Alimenta la placa (fuente de 12V **y** USB conectados)
2. Pon el multímetro en modo **voltaje continuo (DC)**
3. Conecta la punta **negra** a un pin de **GND** de la shield
4. Apoya la punta **roja** sobre el **tornillo del potenciómetro** del driver
5. Gira el tornillo **muy despacio** con el destornillador hasta leer el Vref que calculaste
6. Repite en cada driver (X, Y y A con el mismo valor, ya que Y y A mueven el mismo puente)

:::caution
- Gira el potenciómetro con suavidad: es frágil.
- No dejes que la punta del destornillador toque otros componentes mientras la placa está encendida.
:::

## Comprobación

Después de ajustar, haz mover los motores un rato y **toca con cuidado** los motores y los drivers:

- Si se calientan demasiado para mantener el dedo encima → baja un poco el Vref
- Si pierden pasos o van sin fuerza → súbelo un poco
