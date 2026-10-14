---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

Dentro del chip hay estructuras microscópicas de silicio (tecnología **MEMS**) que se deforman un poquito al acelerar o girar. El chip mide esa deformación y la convierte en números.

## Los tres ejes y los tres giros

<img src="/img/guias/sensores/imu/ejes.svg" alt="Ejes X, Y y Z del sensor y los giros roll, pitch y yaw" />

Cada sensor mide en los tres ejes. Para los giros se usan los nombres de la aviación:

| Giro | Alrededor de | Ejemplo |
|---|---|---|
| **Roll** (alabeo) | X | un avión que inclina las alas |
| **Pitch** (cabeceo) | Y | un avión que sube o baja el morro |
| **Yaw** (guiñada) | Z | un coche que gira en una curva |

## El acelerómetro: dónde está "abajo"

Quieto sobre una mesa, el acelerómetro mide **1 g en el eje Z**: la gravedad. Si lo inclinas, esa gravedad se reparte entre los ejes, y con un poco de trigonometría sabes el ángulo:

```
roll  = atan2(ay, az)
pitch = atan2(−ax, √(ay² + az²))
```

- **Ventaja**: el ángulo es correcto a largo plazo
- **Problema**: es muy **ruidoso**. Cualquier vibración o movimiento brusco se suma a la gravedad y falsea la medida
- **Límite**: el yaw es invisible para él. Girar sobre Z no cambia hacia dónde apunta la gravedad

## El giroscopio: cuánto gira

El giroscopio mide **velocidad de giro**, en grados por segundo. Para saber el ángulo, se va sumando: `ángulo += velocidad × tiempo`.

- **Ventaja**: es muy **suave** y responde al instante
- **Problema**: tiene **deriva**. Cada medida lleva un error pequeñísimo y, al ir sumando, el ángulo se aleja poco a poco del real

## La fusión: lo mejor de cada uno

<img src="/img/guias/sensores/imu/fusion.svg" alt="Con el sensor quieto, el acelerómetro da ruido, el giroscopio deriva y la fusión se mantiene estable" />

Combinándolos se obtiene una medida suave **y** estable. La forma más sencilla es el **filtro complementario**:

```
ángulo = 0,98 × (ángulo + giro × dt) + 0,02 × ángulo_del_acelerómetro
```

En cada ciclo, el 98 % viene del giroscopio (suavidad) y el 2 % del acelerómetro, que corrige la deriva poco a poco. Lo tienes funcionando en el [código básico](./codigo-basico#3-ángulo-estable-con-filtro-complementario).

Hay filtros más avanzados, como el **filtro de Kalman** o los de **Madgwick** y **Mahony**, que usan los drones y robots profesionales. Siguen la misma idea.

:::tip
El giroscopio tiene un pequeño **offset**: aunque esté quieto, marca algo distinto de cero. Al arrancar, deja el sensor inmóvil un par de segundos, haz la media de lo que mide y réstala siempre después.
:::
