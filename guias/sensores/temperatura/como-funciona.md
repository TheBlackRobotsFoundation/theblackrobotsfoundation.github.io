---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona por dentro

Dentro de la carcasa blanca hay tres piezas:

- Un **sensor capacitivo de humedad**: dos placas separadas por un material que absorbe vapor de agua. Cuanta más humedad, más cambia su capacidad
- Un **termistor**: una resistencia que cambia con la temperatura
- Un **microcontrolador** pequeño que mide los dos, aplica la calibración de fábrica y prepara los datos

## Un solo cable para todo

El DHT22 usa un protocolo propio de **un solo cable** (*single-wire*):

1. El Arduino pone la línea a LOW un momento para decirle "mide"
2. El sensor contesta con **40 bits**, codificados según lo largo de cada pulso

<img src="/img/guias/sensores/temperatura/trama.svg" alt="Trama de 40 bits del DHT22: humedad, temperatura y control" />

Los últimos 8 bits son una **suma de comprobación**: si no cuadra con el resto, el dato llegó mal y se descarta. La librería hace todo este trabajo por ti.

## Humedad relativa

La humedad que mide es **relativa**: cuánto vapor de agua tiene el aire comparado con el máximo que podría tener a esa temperatura. Un 100 % significa aire saturado (niebla, condensación).

## Sensación térmica

Con temperatura y humedad se puede calcular el **índice de calor**: la temperatura que *siente* una persona. Con humedad alta, el sudor se evapora peor y 30 °C se perciben como 33 °C o más. La librería trae una función para calcularlo.

:::caution
El DHT22 necesita unos **2 segundos** entre lecturas. Si lo lees más rápido, te devuelve el dato anterior o un error.
:::
