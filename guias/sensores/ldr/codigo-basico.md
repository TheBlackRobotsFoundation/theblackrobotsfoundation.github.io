---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para leer la luz

Con el divisor conectado a **A0**.

## 1. Leer la luz

```cpp
#define LDR A0

void setup() {
  Serial.begin(9600);
}

void loop() {
  int luz = analogRead(LDR);   // más luz = valor más alto
  Serial.println(luz);
  delay(100);
}
```

Tapa la LDR con el dedo y acércale una linterna mientras miras el **Serial Plotter**. Apunta los valores que salen con luz y a oscuras: los necesitas para el siguiente paso.

## 2. Encender un LED al oscurecer

Usamos el LED de la placa (pin 13). Cuando la luz baja de un umbral, se enciende.

```cpp
#define LDR A0
#define LED 13
const int UMBRAL = 300;   // ajústalo con tus lecturas

void setup() {
  pinMode(LED, OUTPUT);
}

void loop() {
  int luz = analogRead(LDR);
  digitalWrite(LED, luz < UMBRAL ? HIGH : LOW);
  delay(50);
}
```

## 3. Sin parpadeos en el límite

Si la luz está justo en el umbral, el LED tiembla entre encendido y apagado. Se evita con **dos umbrales** (histéresis): uno para encender y otro, algo más alto, para apagar.

```cpp
const int ENCENDER = 280;
const int APAGAR   = 340;
bool encendido = false;

void loop() {
  int luz = analogRead(A0);

  if (!encendido && luz < ENCENDER) encendido = true;
  if (encendido  && luz > APAGAR)   encendido = false;

  digitalWrite(13, encendido);
  delay(50);
}
```

La histéresis es un truco que usarás con muchos sensores: temperatura, distancia, nivel de batería.

## ¿Y ahora qué?

Con dos LDR y dos [motores](/guias/actuadores/motores-dc) puedes montar un robot que persigue la luz: compara las dos lecturas y gira hacia la mayor.
