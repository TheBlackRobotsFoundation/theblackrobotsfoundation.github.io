---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

## Por dentro: bobinas fijas, imanes que giran

En un motor DC las bobinas giran y unas escobillas cambian su corriente en cada vuelta. En un brushless es al revés: las **bobinas están fijas** en el estator y los **imanes giran** con la campana. La corriente de las bobinas se cambia **electrónicamente**, sin piezas que rocen.

![Estator con las bobinas de las tres fases y la campana con los imanes alrededor](/img/guias/actuadores/brushless/por-dentro.svg)

Las bobinas se agrupan en **tres fases** (A, B y C), una por cada cable. El ESC activa las fases por turnos, de dos en dos: A-B, A-C, B-C, B-A, C-A, C-B... Cada combinación crea un campo magnético en una dirección distinta, y los imanes de la campana lo persiguen. Al ir rotando la secuencia, la campana gira.

Es la misma idea que un [motor paso a paso](/guias/actuadores/motores-paso-a-paso/como-funcionan), pero con la secuencia generada miles de veces por segundo por el ESC.

## El ESC: un controlador completo

El ESC lleva un pequeño microcontrolador y seis transistores de potencia. Hace tres cosas:

1. **Detecta la posición** de la campana midiendo la tensión que se induce en la fase que no está activa en cada momento
2. **Conmuta las fases** en el instante justo para que el motor siga girando
3. **Regula la velocidad** según la señal que recibe

## La señal: igual que un servo

Un ESC normal entiende la misma señal que un [servomotor](/guias/actuadores/servomotores/como-funciona): un pulso cada 20 ms. Lo que cambia es el significado:

| Pulso | Servo | ESC |
|---|---|---|
| 1 ms (1000 µs) | 0° | motor parado |
| 1,5 ms (1500 µs) | 90° | media potencia |
| 2 ms (2000 µs) | 180° | potencia máxima |

Por eso un Arduino controla un ESC con la librería `Servo`, mandando microsegundos en lugar de ángulos.

:::note
Los drones de carreras usan protocolos digitales más rápidos (**OneShot**, **DShot**), que envían la orden cientos de veces por segundo. Para aprender, el pulso clásico de servo funciona con cualquier ESC.
:::

## El armado

Por seguridad, un ESC **no hace girar el motor** al encenderse hasta que recibe una señal de **motor parado** (1000 µs) durante un par de segundos. Lo confirma con unos pitidos. Este paso se llama **armar** el ESC, y evita que el motor arranque solo si el mando o el programa empiezan con el acelerador alto.

## Cambiar el sentido de giro

Basta con **intercambiar dos de los tres cables** del motor, cualesquiera. En un dron, la mitad de los motores giran en un sentido y la otra mitad en el contrario, para compensar el giro de todo el aparato.
