---
sidebar_position: 4
title: Mejoras
sidebar_custom_props:
  icon: /img/guias/iconos/ejemplos.svg
---

# Mejoras

El robot básico ya esquiva. Estas mejoras lo hacen más listo, y cada una te lleva a una guía nueva.

## 1. Frenar al acercarse

En vez de ir siempre a la misma velocidad, el robot reduce al acercarse a un obstáculo. Cambia `avanzar()` en `loop()` por:

```cpp
int v = map(constrain(distancia, DISTANCIA_MINIMA, 80), DISTANCIA_MINIMA, 80, 110, 200);
motores(v, v);
```

A 80 cm o más va a 200; cerca del límite, a 110. Sus maniobras son más suaves y precisas.

## 2. Mirar antes de girar

Con el sensor sobre un [servomotor](/guias/actuadores/servomotores), el robot mira a los dos lados y gira hacia el que tiene **más espacio**, en lugar de al azar.

Conecta el servo con su señal en el **pin 5** (su alimentación, como en la [guía de servos](/guias/actuadores/servomotores/conexion)) y sustituye el bloque del giro en `esquivar()`:

```cpp
#include <Servo.h>
Servo cuello;   // en setup(): cuello.attach(5); cuello.write(90);

float mirar(int angulo) {
  cuello.write(angulo);
  delay(350);
  return medirDistancia();
}

// dentro de esquivar(), después de retroceder:
float izquierda = mirar(160);
float derecha   = mirar(20);
cuello.write(90);

if (izquierda > derecha) {
  motores(-VEL_GIRO, VEL_GIRO);
} else {
  motores(VEL_GIRO, -VEL_GIRO);
}
delay(450);
```

:::note
La librería `Servo` desactiva el PWM de los pines 9 y 10. En este robot esos pines son IN1 e IN2, que solo usan `digitalWrite()`, así que todo sigue funcionando. Por eso la velocidad va en los pines 11 y 6.
:::

## 3. Avisar con sonido

Un [zumbador activo](/guias/actuadores/zumbador) en el **pin 4** da un pitido corto cada vez que esquiva:

```cpp
// al principio de esquivar():
digitalWrite(4, HIGH);
delay(80);
digitalWrite(4, LOW);
```

Recuerda `pinMode(4, OUTPUT);` en `setup()`. Usa uno **activo**: la función `tone()` de los pasivos desactivaría el PWM del pin 11.

## 4. Ir recto de verdad

Con motores con [encoder](/guias/sensores/encoders), el robot cuenta las vueltas de cada rueda y corrige la que va más rápida. Conecta la señal **A** de cada encoder a los pines **2** y **3** (los que tienen interrupción) y la **B** a **A1** y **A2**. Es el primer paso hacia la **odometría**: saber cuánto ha avanzado y girado el robot.

## 5. Convertirlo en sigue-líneas

Cambia el HC-SR04 por dos [sensores infrarrojos](/guias/sensores/infrarrojos) mirando al suelo y usa la lógica de su [código básico](/guias/sensores/infrarrojos/codigo-basico): ya tienes las funciones de los motores escritas.

## 6. Más allá

Con el mismo esqueleto, cambiando sensores y lógica:

- Un robot que **sigue la luz** con dos [LDR](/guias/sensores/ldr)
- Un robot que **mantiene la distancia** a una pared, para recorrer pasillos
- Un robot que **mapea** una habitación con un [LiDAR](/guias/sensores/lidar), como hace el [Rover](/proyectos/rover-web)
