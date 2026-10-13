---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para controlar un relé

Con **IN** en el pin 7.

## 1. Encender y apagar

```cpp
#define RELE 7

// Cambia a LOW si tu módulo es activo en bajo
#define ENCENDIDO HIGH
#define APAGADO   !ENCENDIDO

void setup() {
  digitalWrite(RELE, APAGADO);   // primero el estado, luego el modo:
  pinMode(RELE, OUTPUT);         // así no hace un clic al arrancar
}

void loop() {
  digitalWrite(RELE, ENCENDIDO);
  delay(3000);
  digitalWrite(RELE, APAGADO);
  delay(3000);
}
```

Oirás el clic y verás el LED del módulo cada 3 segundos. Si el ventilador funciona al revés (apagado cuando debería estar encendido), cambia `HIGH` por `LOW` en la línea de `ENCENDIDO`.

## 2. Termostato

Con un [DHT22](/guias/sensores/temperatura/conexion) en el pin 2, el ventilador se enciende con calor. Usamos dos umbrales (histéresis) para que el relé no esté conmutando todo el rato:

```cpp
#include <DHT.h>

#define RELE 7
#define ENCENDIDO HIGH
#define APAGADO   !ENCENDIDO

DHT dht(2, DHT22);

const float ENCENDER_A = 27.0;   // °C
const float APAGAR_A   = 25.5;
bool ventilador = false;

void setup() {
  digitalWrite(RELE, APAGADO);
  pinMode(RELE, OUTPUT);
  dht.begin();
}

void loop() {
  delay(2000);
  float t = dht.readTemperature();
  if (isnan(t)) return;

  if (!ventilador && t > ENCENDER_A) ventilador = true;
  if (ventilador && t < APAGAR_A)    ventilador = false;

  digitalWrite(RELE, ventilador ? ENCENDIDO : APAGADO);
}
```

## 3. Temporizador sin bloquear el programa

Un riego que se activa 10 segundos cada hora, usando `millis()` para que el Arduino pueda hacer otras cosas mientras tanto:

```cpp
const unsigned long CADA    = 3600000UL;   // 1 hora en ms
const unsigned long DURANTE = 10000UL;     // 10 s

unsigned long inicio = 0;

void loop() {
  unsigned long t = millis() - inicio;

  if (t >= CADA) {
    inicio = millis();        // empieza un ciclo nuevo
  }
  digitalWrite(RELE, t < DURANTE ? ENCENDIDO : APAGADO);

  // ...aquí puede ir el resto del programa
}
```

:::tip
La `UL` al final de los números indica que son `unsigned long`. Sin ella, `3600000` puede no caber en un `int` del Arduino UNO, y el cálculo sale mal.
:::

## ¿Y ahora qué?

Con relés, sensores y un poco de lógica tienes la base de cualquier automatismo: invernaderos, acuarios, alarmas. Para un robot, el siguiente actuador es el más potente de todos: el [motor brushless](/guias/actuadores/brushless).
