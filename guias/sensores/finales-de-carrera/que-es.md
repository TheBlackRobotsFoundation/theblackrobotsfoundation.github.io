---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es un final de carrera?

Un **final de carrera** (*limit switch*, o *endstop* en impresoras 3D) es un interruptor pensado para que lo active **una pieza de la máquina** al llegar a un punto. Le dice al controlador: "aquí se acaba el recorrido".

![Microinterruptor con palanca, botón interno y tres terminales](/img/guias/sensores/finales-de-carrera/anatomia.svg)

## Cómo es

El más común es un **microinterruptor** (*microswitch*) con palanca:

- **Palanca**: amplía el recorrido y hace que se active con muy poca fuerza
- **Botón interno**: hace un "clic" claro y preciso, siempre en el mismo punto
- **3 terminales**: COM, NC y NO

## Los tres terminales

| Terminal | Nombre | Conectado a COM |
|---|---|---|
| **COM** | común | — |
| **NC** | *normally closed*, normalmente cerrado | en reposo |
| **NO** | *normally open*, normalmente abierto | al pulsar |

Usando COM y NO funciona como un [pulsador](/guias/sensores/pulsadores). Usando COM y NC funciona al revés: el circuito está cerrado hasta que se pulsa.

## Para qué sirve

- **Homing**: la máquina busca su posición de inicio (el "cero") moviéndose hasta tocar el final de carrera. Lo hacen las impresoras 3D, las CNC y muchos plotters
- **Seguridad**: parar un motor antes de que un eje choque contra su extremo
- **Detectar presencia**: una puerta cerrada, una pieza colocada, un parachoques que toca algo

:::note[Otros tipos]
Además de los mecánicos, hay finales de carrera **ópticos** (una pieza corta un haz de luz) y **magnéticos** (un imán activa un sensor Hall). Al Arduino le llegan igual: HIGH o LOW.
:::
