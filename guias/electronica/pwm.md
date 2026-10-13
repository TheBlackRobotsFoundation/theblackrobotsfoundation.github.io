---
sidebar_position: 3
title: PWM
sidebar_custom_props:
  icon: /img/guias/iconos/configuracion.svg
---

# PWM: valores intermedios con un pin digital

**PWM** (*Pulse Width Modulation*, modulación por ancho de pulso) consiste en encender y apagar un pin cientos de veces por segundo. Variando **cuánto tiempo está encendido** en cada ciclo, el componente recibe de media una tensión intermedia.

![Tres señales PWM con ciclos de trabajo del 25, 50 y 75 por ciento](/img/guias/electronica/pwm.svg)

## El ciclo de trabajo

El porcentaje de tiempo que la señal está en HIGH se llama **ciclo de trabajo** (*duty cycle*):

- **0 %** → siempre apagado (0 V de media)
- **50 %** → la mitad del tiempo encendido (≈ 2,5 V de media)
- **100 %** → siempre encendido (5 V)

Un LED parpadea tan rápido que tu ojo ve un brillo intermedio. Un motor recibe empujones tan seguidos que gira a una velocidad intermedia.

## En Arduino

`analogWrite()` acepta un valor de **0 a 255**, que se corresponde con el ciclo de trabajo:

```cpp
analogWrite(9, 0);     // 0 %
analogWrite(9, 64);    // 25 %
analogWrite(9, 128);   // 50 %
analogWrite(9, 255);   // 100 %
```

Para pasar de porcentaje a valor: `valor = porcentaje × 255 / 100`.

## Qué pines lo admiten

En el UNO, los pines con PWM llevan el símbolo **~**: **3, 5, 6, 9, 10 y 11**.

| Pines | Frecuencia |
|---|---|
| 5 y 6 | ~980 Hz |
| 3, 9, 10 y 11 | ~490 Hz |

## Dónde lo vas a usar

- Regular el brillo de un [LED](/guias/actuadores/led/codigo-basico) o un [LED RGB](/guias/actuadores/led-rgb)
- Controlar la velocidad de un [motor DC](/guias/actuadores/motores-dc)
- Generar sonidos con un [zumbador](/guias/actuadores/zumbador)

:::note[PWM y servos]
Los [servomotores](/guias/actuadores/servomotores) también se controlan con pulsos, pero de una forma concreta: lo que importa es la **duración del pulso** (entre 1 y 2 ms), y de eso se encarga la librería `Servo`.
:::
