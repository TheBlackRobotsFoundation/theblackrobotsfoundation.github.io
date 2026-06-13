---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para controlar un LED

Suponiendo que el LED está conectado al **pin 8** (a través de su resistencia), vamos a ver tres cosas: encenderlo, hacerlo parpadear y atenuarlo.

## 1. Encenderlo

Lo más simple: ponemos el pin como salida y lo dejamos en `HIGH` (5V).

```cpp
#define LED_PIN 8

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);  // LED encendido
}

void loop() {
  // nada: el LED se queda encendido
}
```

## 2. Hacerlo parpadear (Blink)

Encendemos, esperamos, apagamos y esperamos, en bucle.

```cpp
#define LED_PIN 8

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH);  // enciende
  delay(500);                   // espera 0,5 s
  digitalWrite(LED_PIN, LOW);   // apaga
  delay(500);                   // espera 0,5 s
}
```

- `digitalWrite(LED_PIN, HIGH)` saca 5V por el pin → el LED enciende
- `digitalWrite(LED_PIN, LOW)` saca 0V → el LED apaga
- `delay(500)` pausa medio segundo

## 3. Atenuarlo (efecto fade con PWM)

Algunos pines (los marcados con `~` en la placa) permiten **PWM**, que simula voltajes intermedios. Con `analogWrite()` controlamos el **brillo** de 0 (apagado) a 255 (máximo).

```cpp
#define LED_PIN 9   // el pin 9 admite PWM (~)

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // Sube el brillo poco a poco
  for (int brillo = 0; brillo <= 255; brillo++) {
    analogWrite(LED_PIN, brillo);
    delay(5);
  }
  // Y lo baja
  for (int brillo = 255; brillo >= 0; brillo--) {
    analogWrite(LED_PIN, brillo);
    delay(5);
  }
}
```

:::tip
Para usar `analogWrite()` el LED debe estar en un pin **con PWM** (los que llevan el símbolo `~` al lado del número: 3, 5, 6, 9, 10 y 11 en el Arduino UNO).
:::
