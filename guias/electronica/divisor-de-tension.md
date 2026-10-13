---
sidebar_position: 4
title: Divisor de tensión
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Divisor de tensión

Dos resistencias en serie reparten la tensión entre ellas. En el punto donde se unen aparece una tensión **proporcional** a sus valores. Es uno de los circuitos más útiles que existen.

![Divisor de tensión con dos resistencias y la fórmula de la salida](/img/guias/electronica/divisor-de-tension.svg)

## La fórmula

```
Vout = Vin × R2 / (R1 + R2)
```

Algunos ejemplos con `Vin = 5 V`:

| R1 | R2 | Vout |
|---|---|---|
| 10 kΩ | 10 kΩ | 2,5 V |
| 10 kΩ | 20 kΩ | 3,3 V |
| 20 kΩ | 10 kΩ | 1,67 V |

## Para qué sirve

### Leer sensores resistivos

Muchos sensores cambian su **resistencia** según lo que miden: una [fotorresistencia (LDR)](/guias/sensores/ldr) con la luz, un termistor con la temperatura. El Arduino mide tensiones, así que se coloca el sensor como R1 o R2 junto a una resistencia fija, y la tensión del punto central cambia con la magnitud. Ese punto va a un pin analógico.

### El potenciómetro

Un [potenciómetro](/guias/sensores/potenciometro) es un divisor de tensión en una sola pieza: al girarlo, mueves el punto central a lo largo de una pista resistiva.

### Bajar un nivel de tensión

Para conectar una señal de 5 V a un componente que trabaja a 3,3 V, un divisor con 10 kΩ y 20 kΩ la deja en unos 3,3 V.

:::caution
El divisor sirve para **señales**, que consumen muy poca corriente. Para alimentar un componente (un motor, un módulo) se usa un **regulador de tensión**.
:::

## Resistencias pull-up y pull-down

Una variante muy habitual: una resistencia que mantiene un pin en un valor conocido (HIGH o LOW) mientras nada lo fuerza al contrario. Es la clave para leer bien un [pulsador](/guias/sensores/pulsadores/como-funciona).
