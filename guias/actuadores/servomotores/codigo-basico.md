---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para mover un servo

La librería **Servo** viene incluida con el Arduino IDE.

## 1. Ir a un ángulo

```cpp
#include <Servo.h>

Servo miServo;

void setup() {
  miServo.attach(9);    // señal en el pin 9
  miServo.write(90);    // al centro
}

void loop() {}
```

Úsalo para **centrar el servo** antes de montar el brazo.

## 2. Barrido de 0° a 180°

```cpp
#include <Servo.h>

Servo miServo;

void setup() {
  miServo.attach(9);
}

void loop() {
  for (int angulo = 0; angulo <= 180; angulo++) {
    miServo.write(angulo);
    delay(15);
  }
  for (int angulo = 180; angulo >= 0; angulo--) {
    miServo.write(angulo);
    delay(15);
  }
}
```

El `delay(15)` controla la velocidad: el servo va al ángulo pedido lo más rápido que puede, así que para un movimiento suave se le piden ángulos poco a poco.

## 3. Controlarlo con un potenciómetro

Con un [potenciómetro](/guias/sensores/potenciometro/conexion) en A0, el servo copia el giro del mando:

```cpp
#include <Servo.h>

Servo miServo;

void setup() {
  miServo.attach(9);
}

void loop() {
  int valor = analogRead(A0);              // 0 … 1023
  int angulo = map(valor, 0, 1023, 0, 180);
  miServo.write(angulo);
  delay(15);
}
```

## 4. Ajustar el recorrido

Si tu servo no llega a 0° o 180°, o zumba en los extremos, dale los límites de pulso al hacer `attach()`:

```cpp
miServo.attach(9, 500, 2400);   // pulso mínimo y máximo, en microsegundos
```

Prueba con valores entre 500 y 1000 para el mínimo y entre 2000 y 2500 para el máximo, hasta que recorra todo sin forzar. También puedes mandar el pulso directamente con `miServo.writeMicroseconds(1500);`.

:::caution
Si el servo **zumba y se calienta** quieto en un extremo, está intentando ir más allá de su tope mecánico. Reduce el recorrido: forzarlo así acaba rompiendo los engranajes.
:::

## 5. Mirar a los lados

Un servo que mueve un [sensor de ultrasonidos](/guias/sensores/ultrasonidos) permite al robot comparar izquierda, centro y derecha antes de decidir:

```cpp
int mirar(int angulo) {
  miServo.write(angulo);
  delay(300);                 // tiempo para llegar y dejar de vibrar
  return medirDistancia();    // función de la guía de ultrasonidos
}

// en loop():
int izquierda = mirar(150);
int centro    = mirar(90);
int derecha   = mirar(30);
```

Es una mejora muy habitual del [robot esquiva-obstáculos](/guias/proyecto-esquiva-obstaculos/mejoras).

## ¿Y ahora qué?

Para mover ruedas, que giran sin fin, el motor adecuado es el [motor DC](/guias/actuadores/motores-dc) con un driver.
