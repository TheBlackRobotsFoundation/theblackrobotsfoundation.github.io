---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para controlar un ESC

Con la señal del ESC en el **pin 9** y el motor **sin hélice y sujeto**.

## 1. Armar y girar despacio

```cpp
#include <Servo.h>

Servo esc;

const int PARADO = 1000;   // µs
const int MAXIMO = 2000;

void setup() {
  esc.attach(9, PARADO, MAXIMO);
  esc.writeMicroseconds(PARADO);   // señal de motor parado
  delay(3000);                     // tiempo para conectar la batería y armar
}

void loop() {
  esc.writeMicroseconds(1150);     // poco acelerador
  delay(3000);
  esc.writeMicroseconds(PARADO);
  delay(3000);
}
```

1. Carga el programa con la **batería desconectada**
2. Conecta la batería: el ESC pitará para indicar que está armado
3. El motor girará despacio 3 segundos, se parará 3, y así sucesivamente

Si el motor no arranca con 1150, prueba 1200: cada ESC tiene su punto de arranque.

## 2. Acelerador con un potenciómetro

Con un [potenciómetro](/guias/sensores/potenciometro/conexion) en A0, controlas la velocidad girando el mando:

```cpp
#include <Servo.h>

Servo esc;

void setup() {
  esc.attach(9, 1000, 2000);
  esc.writeMicroseconds(1000);
  delay(3000);
}

void loop() {
  int valor = analogRead(A0);
  int pulso = map(valor, 0, 1023, 1000, 1400);   // limitado al 40 %
  esc.writeMicroseconds(pulso);
  delay(20);
}
```

:::caution
Gira el potenciómetro **al mínimo antes de conectar la batería**. Si está alto, el ESC no se armará (es su protección) o el motor arrancará de golpe en cuanto lo haga.
:::

El límite de 1400 µs mantiene la prueba en una potencia segura. Súbelo poco a poco solo cuando tengas el motor bien sujeto.

## 3. Calibrar el recorrido del acelerador

Muchos ESC necesitan aprender cuál es el pulso mínimo y el máximo. Se hace una vez:

```cpp
#include <Servo.h>

Servo esc;

void setup() {
  esc.attach(9, 1000, 2000);
  esc.writeMicroseconds(2000);   // 1. máximo, con la batería desconectada
  delay(8000);                   // 2. conecta la batería ahora; espera los pitidos
  esc.writeMicroseconds(1000);   // 3. mínimo: el ESC guarda el recorrido
}

void loop() {}
```

La secuencia exacta de pitidos depende del fabricante: consulta el manual de tu ESC. Mientras calibras, la hélice tampoco debe estar puesta.

## 4. Parada de seguridad

En cualquier programa con motores brushless, conviene una forma rápida de pararlo todo. Por ejemplo, con un [pulsador](/guias/sensores/pulsadores/conexion) en el pin 2:

```cpp
if (digitalRead(2) == LOW) {     // pulsado
  esc.writeMicroseconds(1000);
  while (true) {}                // se queda parado hasta reiniciar
}
```

## ¿Y ahora qué?

Un dron combina cuatro de estos motores con una [IMU](/guias/sensores/imu) que mide su inclinación cientos de veces por segundo y corrige la potencia de cada motor. Si te interesa, sigue el proyecto del [Drone](/proyectos/drone).
