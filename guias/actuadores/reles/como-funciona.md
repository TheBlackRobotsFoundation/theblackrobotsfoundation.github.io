---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

Dentro del relé hay una **bobina**: un hilo enrollado alrededor de un núcleo de hierro. Al pasar corriente, la bobina se convierte en un **electroimán** que atrae una palanca metálica. La palanca está unida a **COM** y salta de un contacto a otro.

<img src="/img/guias/actuadores/reles/por-dentro.svg" alt="Relé en reposo, con COM unido a NC, y activado, con COM unido a NO" />

- **Bobina sin corriente**: un muelle mantiene la palanca arriba, tocando **NC**
- **Bobina con corriente**: el electroimán baja la palanca, que pasa a tocar **NO**

Al cambiar se oye un **clic**: es la palanca chocando con el contacto.

## Por qué el módulo lleva un transistor

La bobina de un relé de 5 V consume unos **70 – 90 mA**, más de lo que debe dar un pin (unos 20 mA). El transistor del módulo hace de intermediario: el pin solo le da una orden con muy poca corriente y el transistor deja pasar la corriente de la bobina desde el pin VCC.

## El diodo de protección

Una bobina guarda energía en forma de campo magnético. Al cortar la corriente, esa energía se libera de golpe como un **pico de tensión** que puede llegar a cientos de voltios y dañar el transistor. El **diodo** colocado en paralelo con la bobina le da un camino para descargarse sin peligro. El módulo ya lo trae; si algún día montas un relé suelto, no te olvides de él.

## Activo en alto o en bajo

Hay módulos que se activan con **IN en HIGH** y otros con **IN en LOW** (muchos de los más baratos funcionan así). Algunos traen un puente para elegir.

| Módulo | Relé activado con |
|---|---|
| Activo en alto (*high level trigger*) | `digitalWrite(IN, HIGH)` |
| Activo en bajo (*low level trigger*) | `digitalWrite(IN, LOW)` |

Si al arrancar el relé se activa solo, o funciona al revés de lo que esperas, tu módulo es activo en bajo. Lo tienes resuelto en el [código básico](./codigo-basico).

## Límites

- **Corriente y tensión máximas**: las que lleva escritas el relé. Quédate siempre por debajo
- **Velocidad**: un relé tarda unos 10 ms en conmutar y se desgasta con el uso (unos 100 000 ciclos). Sirve para encender y apagar cosas, y para regular velocidad o brillo con PWM se usa un transistor o un [driver de motores](/guias/actuadores/motores-dc)
