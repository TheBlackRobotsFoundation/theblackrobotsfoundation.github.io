---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

Tres cables: alimentación, GND y señal.

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Micro servo SG90 | 1 |
| Cables dupont macho-macho | 3 |

## Esquema de conexión

<img src="/img/guias/actuadores/servomotores/conexion.svg" alt="Esquema: servo SG90 con marrón a GND, rojo a 5 V y naranja al pin 9" />

| Servo | Arduino |
|---|---|
| Marrón (GND) | **GND** |
| Rojo (5 V) | **5V** |
| Naranja (señal) | pin digital **9** |

La señal puede ir a **cualquier pin digital**, tenga o no el símbolo `~`: la librería `Servo` genera los pulsos por su cuenta.

:::note
La librería `Servo` usa un temporizador del UNO que también se ocupa del PWM de los pines **9 y 10**. Mientras haya un servo funcionando, `analogWrite()` en esos dos pines deja de funcionar. Si usas LEDs o motores con PWM, ponlos en otros pines.
:::

## Varios servos o servos grandes

Con dos o más servos, o con un MG996R, aliméntalos aparte:

1. Una **fuente de 5 – 6 V** (un portapilas de 4 × AA va perfecto) alimenta el cable **rojo** de todos los servos
2. El **marrón** de los servos va al negativo de esa fuente **y** al GND del Arduino ([GND común](/guias/electronica/alimentacion))
3. Cada cable **naranja** va a su pin del Arduino

:::tip
Un condensador de **470 – 1000 µF** entre el + y el − de la alimentación de los servos suaviza los picos al arrancar y evita temblores.
:::

## Montar el brazo

Antes de atornillar el brazo, carga el código de la siguiente sección para dejar el servo en **90°**. Así colocas el brazo centrado y tendrás el mismo recorrido hacia cada lado.

Con todo conectado, pasa al [código básico](./codigo-basico).
