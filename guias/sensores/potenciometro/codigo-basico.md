---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para leer un potenciómetro

Con el cursor conectado a **A0**.

## 1. Leer el valor

```cpp
#define POT A0

void setup() {
  Serial.begin(9600);
}

void loop() {
  int valor = analogRead(POT);   // 0 … 1023
  Serial.println(valor);
  delay(50);
}
```

Abre **Herramientas → Serial Plotter** en lugar del Monitor Serie: verás una gráfica que sube y baja mientras giras el mando.

## 2. Pasarlo a voltios o a porcentaje

```cpp
int valor = analogRead(A0);

float voltios = valor * 5.0 / 1023.0;
int porcentaje = map(valor, 0, 1023, 0, 100);
```

`map()` traslada un número de un rango a otro: aquí, de 0 – 1023 a 0 – 100.

## 3. Controlar el brillo de un LED

Conecta un [LED con su resistencia](/guias/actuadores/led/conexion) al **pin 9** (con PWM). El potenciómetro decide el brillo:

```cpp
#define POT A0
#define LED 9

void setup() {
  pinMode(LED, OUTPUT);
}

void loop() {
  int valor = analogRead(POT);            // 0 … 1023
  int brillo = map(valor, 0, 1023, 0, 255);
  analogWrite(LED, brillo);               // 0 … 255
}
```

La lectura va de 0 a 1023 y `analogWrite()` admite de 0 a 255: `map()` hace la traducción. Tienes el porqué en [PWM](/guias/electronica/pwm).

## 4. Lecturas más estables

Es normal que el valor "baile" uno o dos puntos aunque no toques el mando. Para suavizarlo, haz la media de varias lecturas:

```cpp
int leerSuave(int pin) {
  long suma = 0;
  for (int i = 0; i < 16; i++) {
    suma += analogRead(pin);
  }
  return suma / 16;
}
```

## ¿Y ahora qué?

Con el mismo código puedes leer cualquier sensor que dé una tensión. El siguiente, una [fotorresistencia](/guias/sensores/ldr), que mide la luz. Y si quieres mover algo con el mando, prueba a controlar un [servomotor](/guias/actuadores/servomotores/codigo-basico).
