---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

Dentro del microinterruptor hay una lámina metálica con un muelle que conecta COM con uno de los otros dos terminales. Al empujar la palanca, la lámina salta de golpe al otro lado.

<img src="/img/guias/sensores/finales-de-carrera/estados.svg" alt="Estados del final de carrera: en reposo COM con NC, pulsado COM con NO" />

Ese salto brusco es lo que le da su **precisión**: se activa siempre en el mismo punto, con un margen de décimas de milímetro.

## Leerlo con Arduino

Se lee exactamente igual que un [pulsador](/guias/sensores/pulsadores/como-funciona), con la pull-up interna:

- **COM** → GND
- **NO** → un pin con `INPUT_PULLUP`

| Estado | Pin |
|---|---|
| Libre | HIGH |
| Pulsado (en el tope) | LOW |

## NO o NC: cuál usar

Las máquinas profesionales suelen cablear los finales de carrera en **NC**. El motivo es la seguridad: si un cable se suelta o se rompe, el circuito se abre y el controlador lo ve **igual que si el final de carrera estuviera pulsado**. La máquina se para en vez de seguir moviéndose a ciegas.

Para empezar, **NO** es más intuitivo. Cuando montes una máquina de verdad, piensa en pasarte a NC.

## Homing: encontrar el cero

Una máquina con [motores paso a paso](/guias/actuadores/motores-paso-a-paso) cuenta pasos para saber dónde está, pero al encenderse no sabe dónde empieza. El final de carrera le da esa referencia:

<img src="/img/guias/sensores/finales-de-carrera/homing.svg" alt="El carro avanza despacio hasta tocar el final de carrera y esa posición pasa a ser el cero" />

1. El eje se mueve **despacio** hacia el final de carrera
2. Al pulsarse, se para
3. Esa posición pasa a ser **el cero**, y desde ahí se cuentan los pasos

Muchas máquinas lo hacen dos veces: una rápida para acercarse y otra lenta para afinar.

:::tip
También rebota como un pulsador. Para homing no suele importar (te paras al primer contacto), pero si cuentas activaciones, aplica el mismo [antirrebote](/guias/sensores/pulsadores/codigo-basico#3-contar-pulsaciones-sin-rebotes).
:::
