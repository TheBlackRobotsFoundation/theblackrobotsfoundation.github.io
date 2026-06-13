---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para mover un motor

Vamos a mover un motor paso a paso con un driver A4988, usando solo los pines **STEP** y **DIR**.

## Opción 1: sin librerías (pulsos manuales)

Cada pulso en el pin STEP hace avanzar el motor un paso. El pin DIR decide el sentido.

```cpp
#define STEP_PIN 12
#define DIR_PIN  11

void setup() {
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);

  digitalWrite(DIR_PIN, HIGH);  // sentido de giro
}

void loop() {
  // Una vuelta completa = 200 pasos (motor de 1.8°)
  for (int i = 0; i < 200; i++) {
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(800);      // velocidad: menos = más rápido
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(800);
  }

  delay(1000);  // pausa de 1 segundo entre vueltas
}
```

### ¿Qué hace?

- `DIR_PIN` en `HIGH` o `LOW` cambia el sentido de giro
- Cada par de pulsos `HIGH`/`LOW` en `STEP_PIN` es **un paso**
- El `delayMicroseconds()` controla la **velocidad**: cuanto más corto, más rápido (pero si te pasas, el motor pierde pasos)
- 200 pasos = una vuelta completa

## Opción 2: con la librería AccelStepper

La librería **AccelStepper** facilita el control con aceleración y velocidad suave. Instálala desde **Herramientas → Administrar Bibliotecas → AccelStepper**.

```cpp
#include <AccelStepper.h>

// Modo DRIVER = control por STEP y DIR
AccelStepper motor(AccelStepper::DRIVER, 12, 11);  // STEP=12, DIR=11

void setup() {
  motor.setMaxSpeed(1000);      // pasos por segundo
  motor.setAcceleration(500);   // aceleración
  motor.moveTo(200);            // mover 200 pasos (una vuelta)
}

void loop() {
  // Cuando llega, vuelve al inicio (movimiento de ida y vuelta)
  if (motor.distanceToGo() == 0) {
    motor.moveTo(-motor.currentPosition());
  }
  motor.run();   // hay que llamarlo continuamente
}
```

:::tip
Usa **AccelStepper** siempre que puedas: maneja la aceleración por ti y evita que el motor pierda pasos al arrancar y frenar.
:::

## ¿Y ahora qué?

Con esto ya sabes mover un motor. El siguiente paso es coordinar varios a la vez para mover un mecanismo completo, justo como hace el firmware GRBL en el [Plotter](/proyectos/plotter).
