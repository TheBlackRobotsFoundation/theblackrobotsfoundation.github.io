---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para leer un encoder

Con **A** en el pin 2 y **B** en el pin 3.

## 1. Contar pulsos con sentido

```cpp
#define ENC_A 2
#define ENC_B 3

volatile long pulsos = 0;

void alSubirA() {
  // si B está en LOW cuando A sube, gira en un sentido; si no, en el otro
  if (digitalRead(ENC_B) == LOW) {
    pulsos++;
  } else {
    pulsos--;
  }
}

void setup() {
  pinMode(ENC_A, INPUT_PULLUP);
  pinMode(ENC_B, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(ENC_A), alSubirA, RISING);
  Serial.begin(115200);
}

void loop() {
  noInterrupts();
  long copia = pulsos;   // copia segura del contador
  interrupts();

  Serial.println(copia);
  delay(100);
}
```

Gira la rueda a mano: el número sube en un sentido y baja en el otro. Pon el Monitor Serie a **115200** baudios.

- `volatile` avisa al compilador de que la variable cambia "por sorpresa" dentro de una interrupción
- `attachInterrupt(..., RISING)` llama a `alSubirA()` cada vez que A pasa de LOW a HIGH
- `noInterrupts()` / `interrupts()` evitan leer el contador justo mientras se está modificando

:::tip
Si el número sube cuando esperabas que bajara, intercambia los cables A y B (o los pines en el código).
:::

## 2. Velocidad en rpm

Contamos cuántos pulsos llegan en un intervalo fijo y lo pasamos a vueltas por minuto. Añade esto al código anterior en lugar de su `loop()`:

```cpp
const float PULSOS_POR_VUELTA = 330.0;   // PPR × reducción de tu motor
const unsigned long INTERVALO = 100;     // ms

long anterior = 0;
unsigned long t0 = 0;

void loop() {
  if (millis() - t0 >= INTERVALO) {
    t0 += INTERVALO;

    noInterrupts();
    long ahora = pulsos;
    interrupts();

    long diferencia = ahora - anterior;
    anterior = ahora;

    float vueltasPorSegundo = diferencia / PULSOS_POR_VUELTA * (1000.0 / INTERVALO);
    float rpm = vueltasPorSegundo * 60.0;
    Serial.println(rpm);
  }
}
```

El signo indica el sentido de giro.

## 3. Distancia recorrida

```cpp
const float DIAMETRO_MM = 65.0;

float distanciaMM(long cuenta) {
  return cuenta / PULSOS_POR_VUELTA * PI * DIAMETRO_MM;
}
```

Con dos ruedas, su media es lo que ha avanzado el robot y su diferencia, lo que ha girado.

## 4. Más resolución con una librería

La librería **Encoder** (de Paul Stoffregen, en Administrar Bibliotecas) cuenta todas las subidas y bajadas de A y B (decodificación ×4) y usa interrupciones en los dos pines:

```cpp
#include <Encoder.h>

Encoder rueda(2, 3);

void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.println(rueda.read());
  delay(100);
}
```

Recuerda que así obtienes **4 veces más cuentas por vuelta**: ajusta `PULSOS_POR_VUELTA` a 4 × 330 = 1320.

## ¿Y ahora qué?

Los encoders dicen cuánto han girado las ruedas, pero no si el robot ha patinado o hacia dónde mira. Para eso se combinan con una [IMU](/guias/sensores/imu), como hace el Rover.
