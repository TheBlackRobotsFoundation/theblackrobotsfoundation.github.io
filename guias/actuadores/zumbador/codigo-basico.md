---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para hacer sonar un zumbador

Con el zumbador en el **pin 8**.

## 1. Zumbador activo: pitidos

Se controla como un LED: HIGH suena, LOW calla.

```cpp
#define ZUMBADOR 8

void setup() {
  pinMode(ZUMBADOR, OUTPUT);
}

void loop() {
  digitalWrite(ZUMBADOR, HIGH);   // pita
  delay(200);
  digitalWrite(ZUMBADOR, LOW);    // calla
  delay(800);
}
```

## 2. Zumbador pasivo: una nota

```cpp
#define ZUMBADOR 8

void setup() {
  tone(ZUMBADOR, 440, 500);   // La a 440 Hz durante 500 ms
}

void loop() {}
```

- `tone(pin, frecuencia)` suena hasta que llames a `noTone(pin)`
- `tone(pin, frecuencia, duración)` suena durante esos milisegundos y para solo

## 3. Una melodía

Guardamos las notas y sus duraciones en dos listas y las recorremos:

```cpp
#define ZUMBADOR 8

// Do Re Mi Fa Sol La Si Do
int notas[]     = {262, 294, 330, 349, 392, 440, 494, 523};
int duraciones[] = {250, 250, 250, 250, 250, 250, 250, 500};

void setup() {
  for (int i = 0; i < 8; i++) {
    tone(ZUMBADOR, notas[i], duraciones[i]);
    delay(duraciones[i] * 1.3);   // pequeña pausa entre notas
  }
  noTone(ZUMBADOR);
}

void loop() {}
```

El `delay()` es algo más largo que la nota: así cada una se distingue de la siguiente.

## 4. Sirena

Subimos y bajamos la frecuencia de forma continua:

```cpp
void loop() {
  for (int f = 600; f <= 1600; f += 10) {
    tone(ZUMBADOR, f);
    delay(3);
  }
  for (int f = 1600; f >= 600; f -= 10) {
    tone(ZUMBADOR, f);
    delay(3);
  }
}
```

## 5. Sonidos para tu robot

Unas cuantas funciones cortas dan mucha vida a un robot:

```cpp
void sonidoInicio() {
  tone(ZUMBADOR, 523, 100); delay(130);
  tone(ZUMBADOR, 659, 100); delay(130);
  tone(ZUMBADOR, 784, 150); delay(180);
}

void sonidoError() {
  tone(ZUMBADOR, 200, 300); delay(350);
}

void sonidoOk() {
  tone(ZUMBADOR, 1000, 60); delay(80);
  tone(ZUMBADOR, 1500, 60); delay(80);
}
```

## ¿Y ahora qué?

Combínalo con el [sensor de ultrasonidos](/guias/sensores/ultrasonidos/codigo-basico) para hacer un sensor de aparcamiento: cambia el LED del último ejemplo de esa guía por un `tone()`.
