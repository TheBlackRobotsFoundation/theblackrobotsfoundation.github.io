---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

Todo se basa en una idea: el sonido viaja a una **velocidad conocida**. Si mides cuánto tarda en ir y volver, sabes la distancia.

![El sensor emite un pulso, el objeto lo refleja y el pin Echo marca la duración del viaje](/img/guias/sensores/ultrasonidos/eco.svg)

## Paso a paso

1. El Arduino pone el pin **Trig** en HIGH durante **10 µs**: es la orden de "mide"
2. El sensor emite 8 pulsos de ultrasonido a 40 kHz
3. El pin **Echo** se pone en HIGH y se queda así hasta que llega el eco
4. La **duración** del pulso en Echo es el tiempo de ida y vuelta del sonido

## La cuenta

El sonido viaja a unos **343 m/s** a 20 °C, que son **0,0343 cm por microsegundo**. Como el tiempo medido incluye la ida y la vuelta, se divide entre dos:

```
distancia (cm) = tiempo (µs) × 0,0343 / 2
```

Por ejemplo, si Echo dura **1166 µs**:

```
1166 × 0,0343 / 2 ≈ 20 cm
```

Una forma equivalente y muy usada: `distancia = tiempo / 58`.

## Medir el pulso con Arduino

La función `pulseIn()` espera a que un pin cambie y mide cuánto dura el pulso:

```cpp
long tiempo = pulseIn(ECHO, HIGH, 30000);
```

El último número es un **tiempo máximo** de espera en microsegundos. 30 000 µs equivalen a unos 5 m de ida y vuelta: si no llega eco antes, devuelve 0 y el programa sigue.

## Límites a tener en cuenta

- **Zona ciega**: por debajo de unos 2 cm, el eco llega antes de que el sensor esté escuchando
- **Cono de 15°**: detecta lo que tiene delante, y algo a los lados. Dos objetos dentro del cono dan la distancia del más cercano
- **Ecos perdidos**: superficies blandas o inclinadas pueden dar 0 o un valor máximo. Por eso conviene descartar lecturas raras
- **Varios sensores a la vez**: si disparan juntos, cada uno puede escuchar el eco del otro. Dispáralos uno detrás de otro

:::tip
La velocidad del sonido cambia un poco con la temperatura (unos 0,6 m/s por grado). Para medidas de precisión, combínalo con un [DHT22](/guias/sensores/temperatura) y corrige el cálculo.
:::
