---
id: plotter-montaje-shield
title: Montaje de la CNC Shield
sidebar_label: Montaje de la Shield
sidebar_position: 4
---

# Montaje de la CNC Shield V3

Una vez cargado el firmware, ya podemos montar la shield encima del Arduino y configurarla. La CNC Shield aloja los tres drivers, y antes de cablear los motores hay que prepararla: clonar el eje y ajustar el microstepping.

![CNC Shield V3 con los 3 drivers](/img/plotter/cnc-shield.jpg)

## 1. Clonado del eje Y (slot A)

La CNC Shield V3 tiene cuatro ranuras de driver: **X, Y, Z y A**. En este plotter el slot **A** se usa para clonar el eje **Y**, de forma que dos motores mueven el puente de manera sincronizada.

Para activarlo, coloca un **puente (jumper)** en los pines de clonado correspondientes al eje Y, que están junto a la ranura del driver A.

![Jumper de clonado del eje A](/img/plotter/clonado-eje.jpg)

## 2. Jumpers de microstepping

El **microstepping** divide cada paso del motor en fracciones más pequeñas, de modo que el movimiento es más fino y silencioso. Debajo de cada driver hay tres jumpers (M0, M1, M2): poniendo los **tres** se obtiene microstepping de **1/16 de paso** con los A4988.

Pon la **misma** configuración en X, Y y A: como Y y A mueven el mismo puente, deben comportarse igual.

![Jumpers de microstepping](/img/plotter/microstepping.jpg)

:::tip
Esto es solo un resumen. Para entender bien qué es el microstepping y cómo funciona un motor paso a paso por dentro, lee la guía de [Motores paso a paso](/guias/actuadores/motores-paso-a-paso/que-son).
:::

## 3. Cableado de los motores

Cada motor se enchufa al **conector de su eje** en la shield. En este plotter el reparto es:

| Motor | Ranura | Notas |
|---|---|---|
| Eje **X** | `X` | Un único motor |
| Eje **Y** (lado 1) | `Y` | — |
| Eje **Y** (lado 2) | `A` | **Clonado** de Y: los dos motores mueven el puente sincronizados |

El **eje Z** (subida y bajada del lápiz) todavía está **pendiente**, así que de momento su ranura no se usa.

Cada motor es un **paso a paso bipolar de 4 cables**, es decir **2 bobinas**. El conector ya viene emparejado de fábrica: solo tienes que enchufarlo en los pines del eje correspondiente, respetando el sentido. Si quieres entender qué cables forman cada bobina, lo tienes en la [guía de conexión de motores](/guias/actuadores/motores-paso-a-paso/conexion).

![Cableado de los motores](/img/plotter/cableado-motores.svg)

:::tip[Si un motor gira al revés]
Gira su conector **180°** y vuelve a enchufarlo: eso invierte el sentido de esa bobina y, con ello, el giro del motor.
:::

:::caution
Nunca conectes o desconectes un driver o un motor con la placa alimentada, y comprueba la orientación del driver antes de dar corriente: montarlo al revés lo destruye.
:::
