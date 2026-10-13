---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es un pulsador?

Un **pulsador** es un interruptor que conecta dos puntos de un circuito **mientras lo mantienes pulsado**. Al soltarlo, un muelle lo devuelve a su posición y el circuito se abre otra vez.

Es la forma más directa de que una persona le diga algo a un robot: arrancar, parar, cambiar de modo.

<img src="/img/guias/sensores/pulsadores/anatomia.svg" alt="Pulsador táctil de 4 patas y su conexión interna" />

## El pulsador táctil de 4 patas

El más común en electrónica es el **pulsador táctil** de 6 × 6 o 12 × 12 mm, el que viene en todos los kits. Tiene **4 patas**, pero funciona como un interruptor de dos contactos:

- Las patas están **unidas de dos en dos** por dentro (1 con 2, 3 con 4)
- Al pulsar, el botón une las dos parejas

:::tip
Para no equivocarte, usa siempre dos patas **en diagonal**. Así seguro que quedan una a cada lado del interruptor, sin importar cómo hayas girado el pulsador.
:::

## Pulsador o interruptor

| | Pulsador | Interruptor |
|---|---|---|
| Al soltarlo | vuelve solo a su posición | se queda donde lo dejas |
| Ejemplo | timbre, teclado | luz de casa |
| En un robot | botón de inicio, menú | encendido general |

## En robótica

- **Botón de inicio**: el robot espera a que lo pulses antes de moverse
- **Parachoques** (*bumpers*): un pulsador en el frontal detecta un choque
- **Menús**: varios botones para elegir un modo o ajustar un valor

Un pariente cercano es el [final de carrera](/guias/sensores/finales-de-carrera), un pulsador pensado para que lo active una pieza de la máquina.

En las siguientes secciones verás [cómo leerlo sin errores](./como-funciona), [cómo se conecta](./conexion) y [el código](./codigo-basico).
