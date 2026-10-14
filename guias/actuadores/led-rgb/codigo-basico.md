---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico

## LED RGB

### 1. Elegir un color

Una función que recibe los tres valores y los aplica a la vez:

```cpp
#define PIN_R 11
#define PIN_G 10
#define PIN_B 9

void color(int r, int g, int b) {
  analogWrite(PIN_R, r);
  analogWrite(PIN_G, g);
  analogWrite(PIN_B, b);
}

void setup() {
  pinMode(PIN_R, OUTPUT);
  pinMode(PIN_G, OUTPUT);
  pinMode(PIN_B, OUTPUT);
}

void loop() {
  color(255, 0, 0);     delay(1000);   // rojo
  color(0, 255, 0);     delay(1000);   // verde
  color(0, 0, 255);     delay(1000);   // azul
  color(255, 160, 0);   delay(1000);   // ámbar
  color(255, 255, 255); delay(1000);   // blanco
}
```

Si es de **ánodo común**, cambia cada `analogWrite(pin, v)` por `analogWrite(pin, 255 - v)`.

### 2. Transición suave

Pasa del rojo al azul poco a poco:

```cpp
void loop() {
  for (int i = 0; i <= 255; i++) {
    color(255 - i, 0, i);   // el rojo baja mientras el azul sube
    delay(8);
  }
  for (int i = 255; i >= 0; i--) {
    color(255 - i, 0, i);
    delay(8);
  }
}
```

### 3. Indicador de estado

```cpp
void estadoOk()      { color(0, 255, 0); }
void estadoAviso()   { color(255, 120, 0); }
void estadoError()   { color(255, 0, 0); }
```

Llámalas desde tu programa según lo que pase: batería, distancia, conexión.

## Tira WS2812

### Instalar la librería

En **Herramientas → Administrar Bibliotecas**, busca e instala **Adafruit NeoPixel**.

### 4. Encender los LEDs uno a uno

```cpp
#include <Adafruit_NeoPixel.h>

#define PIN_TIRA 6
#define NUM_LEDS 8

Adafruit_NeoPixel tira(NUM_LEDS, PIN_TIRA, NEO_GRB + NEO_KHZ800);

void setup() {
  tira.begin();
  tira.setBrightness(50);   // 0 – 255: limita el brillo (y el consumo)
  tira.show();              // empieza todo apagado
}

void loop() {
  for (int i = 0; i < NUM_LEDS; i++) {
    tira.setPixelColor(i, tira.Color(0, 150, 255));   // LED i en azul claro
    tira.show();
    delay(80);
  }
  tira.clear();
  tira.show();
  delay(300);
}
```

- `setPixelColor(i, color)` prepara el color del LED `i` (el primero es el 0)
- `show()` envía todos los colores a la tira. Hasta que no lo llamas, no cambia nada

### 5. Arcoíris

La librería trae funciones para trabajar con el **tono** del color, que da arcoíris en pocas líneas:

```cpp
void loop() {
  for (long tono = 0; tono < 65536; tono += 256) {
    for (int i = 0; i < NUM_LEDS; i++) {
      long t = tono + i * 65536L / NUM_LEDS;
      tira.setPixelColor(i, tira.gamma32(tira.ColorHSV(t)));
    }
    tira.show();
    delay(10);
  }
}
```

:::tip
Si los colores salen cambiados (pides rojo y sale verde), tu tira usa otro orden de colores. Cambia `NEO_GRB` por `NEO_RGB`.
:::

## ¿Y ahora qué?

Usa la tira como "barra" que crece con la distancia de un [sensor de ultrasonidos](/guias/sensores/ultrasonidos), o como indicador de inclinación con una [IMU](/guias/sensores/imu).
