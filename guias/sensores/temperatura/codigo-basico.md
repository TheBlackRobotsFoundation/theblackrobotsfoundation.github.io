---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para leer el DHT22

## Instalar la librería

En el Arduino IDE, abre **Herramientas → Administrar Bibliotecas**, busca **DHT sensor library** (de Adafruit) e instálala. Si te pregunta por sus dependencias (**Adafruit Unified Sensor**), acepta instalarlas también.

## 1. Leer temperatura y humedad

```cpp
#include <DHT.h>

#define PIN_DHT 2
#define TIPO    DHT22    // cambia a DHT11 si usas ese modelo

DHT dht(PIN_DHT, TIPO);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  delay(2000);   // el DHT22 necesita 2 s entre lecturas

  float humedad = dht.readHumidity();
  float temperatura = dht.readTemperature();   // en °C

  if (isnan(humedad) || isnan(temperatura)) {
    Serial.println("Error al leer el sensor");
    return;
  }

  Serial.print("Temperatura: ");
  Serial.print(temperatura, 1);
  Serial.print(" °C   Humedad: ");
  Serial.print(humedad, 1);
  Serial.println(" %");
}
```

- `isnan()` comprueba si la lectura ha fallado (*not a number*). Si aparece siempre, revisa el cable de datos y el tipo de sensor
- `return` salta al siguiente `loop()` sin imprimir nada

## 2. Sensación térmica

Añade estas líneas después de comprobar la lectura:

```cpp
float sensacion = dht.computeHeatIndex(temperatura, humedad, false);
Serial.print("Sensación térmica: ");
Serial.println(sensacion, 1);
```

El último parámetro (`false`) indica que trabajamos en grados Celsius.

## 3. Avisar si hace demasiado calor

Usamos el LED de la placa como aviso:

```cpp
const float LIMITE = 28.0;

// en setup():
pinMode(13, OUTPUT);

// en loop(), tras leer:
digitalWrite(13, temperatura > LIMITE ? HIGH : LOW);
```

Cambia el LED por un [relé](/guias/actuadores/reles) y tendrás un termostato que enciende un ventilador.

## ¿Y ahora qué?

Hasta aquí, sensores que miden el entorno. El siguiente paso es que el robot sepa **a qué distancia** están las cosas: [sensor de ultrasonidos](/guias/sensores/ultrasonidos).
