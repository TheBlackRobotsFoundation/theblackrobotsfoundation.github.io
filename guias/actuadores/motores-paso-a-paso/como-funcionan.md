---
sidebar_position: 2
title: Cómo funcionan
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funcionan por dentro

Dentro de un motor paso a paso hay dos piezas clave:

- El **estátor**: la parte fija, con varias **bobinas** (electroimanes) repartidas alrededor
- El **rotor**: la parte que gira, que es un imán

Cuando haces pasar corriente por una bobina, esta se convierte en un imán y **atrae al rotor**, que se alinea con ella. Si vas activando las bobinas en orden, el rotor va "persiguiendo" al campo magnético y gira **un paso cada vez**. Si activas las bobinas en orden inverso, gira al revés.

Así de simple: encender bobinas en secuencia = movimiento controlado, paso a paso.

## El driver hace el trabajo sucio

Tú no activas las bobinas a mano. De eso se encarga el **driver** (por ejemplo el A4988): tú solo le das dos señales y él se ocupa de energizar las bobinas en el orden correcto.

- **STEP**: cada pulso que recibe = un paso (o micropaso)
- **DIR**: el nivel de esta señal (alto o bajo) decide el sentido de giro

Esto lo verás en la práctica en [cómo se conectan](./conexion) y en el [código básico](./codigo-basico).

## Pasos por vuelta

Como vimos, un motor típico de 1.8° necesita **200 pasos** para dar una vuelta completa:

```
360° / 1.8° = 200 pasos por vuelta
```

## Microstepping (micropasos)

Aquí viene una de las partes más importantes. El driver puede **dividir cada paso** en fracciones más pequeñas: medios pasos, cuartos, octavos, dieciseisavos... Esto se llama **microstepping**.

En vez de saltar de golpe de un paso al siguiente, el driver ajusta la corriente de las bobinas de forma gradual para dejar el rotor en **posiciones intermedias**.

### ¿Para qué sirve?

- **Movimiento más suave**: el motor no da "tirones", se desliza
- **Menos ruido y vibración**
- **Más resolución**: puedes posicionar el eje con mucho más detalle

### Un ejemplo

Con un A4988 configurado a **1/16 de paso**, cada paso completo se divide en 16:

```
200 pasos × 16 micropasos = 3200 micropasos por vuelta
```

Pasas de 200 a **3200 posiciones** por vuelta. Muchísima más finura.

### El compromiso

El microstepping no es gratis. Cuanto más lo subes:

- **Más suavidad y resolución** (bueno)
- **Menos par por micropaso** (el motor "empuja" con menos fuerza en cada micropaso)

Por eso no siempre se usa el máximo. Un valor de **1/16** es un equilibrio muy habitual para impresoras 3D, CNC y plotters.

### Cómo se configura en el A4988

El microstepping se elige con tres pines del driver — **MS1, MS2 y MS3** — que en una CNC Shield son los **jumpers M0, M1 y M2** que hay debajo de cada driver. Según cuáles pongas, obtienes una resolución distinta:

| MS1 (M0) | MS2 (M1) | MS3 (M2) | Resolución | Pasos por vuelta |
|:---:|:---:|:---:|---|:---:|
| ○ | ○ | ○ | Paso completo | 200 |
| ● | ○ | ○ | 1/2 paso | 400 |
| ○ | ● | ○ | 1/4 paso | 800 |
| ● | ● | ○ | 1/8 paso | 1600 |
| ● | ● | ● | **1/16 paso** | **3200** |

**●** = jumper puesto · **○** = sin jumper

![Jumpers de microstepping en la CNC Shield](/img/plotter/microstepping.jpg)

:::tip
En la práctica, el microstepping se elige con esos **jumpers** debajo de cada driver. Lo ves aplicado en el montaje del [Plotter](/proyectos/plotter/plotter-montaje-shield).
:::

## El par y la pérdida de pasos

Los motores paso a paso tienen **mucha fuerza (par) a baja velocidad**, que es justo lo que se necesita para mover ejes con precisión. Pero a medida que giran más rápido, **pierden par**.

Si les pides más velocidad o más carga de la que pueden, ocurre lo peor: **pierden pasos**. El motor se salta posiciones, pero el driver sigue contando como si nada, así que **pierdes la referencia** de dónde está el eje. En un plotter esto se traduce en un dibujo torcido o descuadrado.

La solución es no exigirles de más: velocidades y aceleraciones razonables, y la corriente bien ajustada (el [Vref](/proyectos/plotter/plotter-vref) en el caso del plotter).
