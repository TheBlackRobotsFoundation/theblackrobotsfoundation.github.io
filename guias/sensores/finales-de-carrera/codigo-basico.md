---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para un final de carrera

Con **NO** en el pin 2 y **COM** a GND.

## 1. Detectar el tope

```cpp
#define FINAL 2

void setup() {
  pinMode(FINAL, INPUT_PULLUP);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  bool enTope = digitalRead(FINAL) == LOW;
  digitalWrite(13, enTope);   // el LED de la placa se enciende en el tope
  Serial.println(enTope ? "En el tope" : "Libre");
  delay(100);
}
```

## 2. Homing con un motor paso a paso

Usando el montaje de la guía de [motores paso a paso](/guias/actuadores/motores-paso-a-paso/conexion) (STEP en el pin 12, DIR en el 11) y el final de carrera en el pin 2. El motor gira despacio hacia el tope, se para al tocarlo y se separa un poco:

```cpp
#define STEP_PIN 12
#define DIR_PIN  11
#define FINAL    2

long posicion = 0;   // en pasos

void paso(int pausa) {
  digitalWrite(STEP_PIN, HIGH);
  delayMicroseconds(pausa);
  digitalWrite(STEP_PIN, LOW);
  delayMicroseconds(pausa);
}

void homing() {
  digitalWrite(DIR_PIN, LOW);                 // sentido hacia el final de carrera
  while (digitalRead(FINAL) == HIGH) {        // mientras no lo toque...
    paso(1500);                               // ...avanza despacio
  }
  digitalWrite(DIR_PIN, HIGH);                // se separa 50 pasos
  for (int i = 0; i < 50; i++) paso(1500);
  posicion = 0;                               // este es el cero
}

void setup() {
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
  pinMode(FINAL, INPUT_PULLUP);
  homing();
}

void loop() {
  // a partir de aquí, "posicion" cuenta desde un punto conocido
}
```

:::caution
Comprueba primero con el motor **sin carga** que gira hacia el lado del final de carrera. Si gira al revés, cambia `LOW` por `HIGH` en la primera línea de `homing()` (y al revés en la segunda).
:::

## 3. Parada de seguridad

En cualquier programa que mueva un eje, comprueba el final de carrera **antes de cada paso**:

```cpp
if (digitalRead(FINAL) == LOW) {
  // en el tope: no seguir en este sentido
} else {
  paso(800);
}
```

## ¿Y ahora qué?

GRBL, el firmware que mueve el [Plotter](/proyectos/plotter), trae este mismo homing listo para usar en cuanto le añades finales de carrera. Para saber la posición de un eje que gira sin fin, como una rueda, el sensor adecuado es el [encoder](/guias/sensores/encoders).
