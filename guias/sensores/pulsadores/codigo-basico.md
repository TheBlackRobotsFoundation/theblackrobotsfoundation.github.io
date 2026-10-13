---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para leer un pulsador

Con el pulsador entre el **pin 2** y **GND**, vamos de lo más simple a lo más útil.

## 1. Leer el estado

Mostramos en el Monitor Serie si está pulsado o suelto.

```cpp
#define BOTON 2

void setup() {
  pinMode(BOTON, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(BOTON) == LOW) {   // LOW = pulsado (pull-up)
    Serial.println("Pulsado");
  } else {
    Serial.println("Suelto");
  }
  delay(100);
}
```

Abre el Monitor Serie (**Herramientas → Monitor Serie**, a 9600 baudios) y pulsa.

## 2. Encender un LED mientras pulsas

El Arduino UNO tiene un LED en la placa conectado al **pin 13**. No hace falta montar nada más.

```cpp
#define BOTON 2
#define LED   13

void setup() {
  pinMode(BOTON, INPUT_PULLUP);
  pinMode(LED, OUTPUT);
}

void loop() {
  bool pulsado = digitalRead(BOTON) == LOW;
  digitalWrite(LED, pulsado ? HIGH : LOW);
}
```

## 3. Contar pulsaciones sin rebotes

Detectamos el **momento** en que se pulsa (el cambio de HIGH a LOW) y esperamos a que la señal se estabilice antes de aceptarlo.

```cpp
#define BOTON 2
const unsigned long ESPERA = 30;   // ms de antirrebote

int contador = 0;
int estadoEstable = HIGH;
int ultimaLectura = HIGH;
unsigned long ultimoCambio = 0;

void setup() {
  pinMode(BOTON, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int lectura = digitalRead(BOTON);

  if (lectura != ultimaLectura) {     // la señal se ha movido
    ultimoCambio = millis();
  }

  if (millis() - ultimoCambio > ESPERA && lectura != estadoEstable) {
    estadoEstable = lectura;          // lleva 30 ms quieta: es real
    if (estadoEstable == LOW) {
      contador++;
      Serial.print("Pulsaciones: ");
      Serial.println(contador);
    }
  }

  ultimaLectura = lectura;
}
```

- `millis()` devuelve los milisegundos desde que arrancó la placa, y permite medir tiempos **sin detener el programa** como haría `delay()`
- Solo se cuenta cuando el estado lleva **30 ms** sin cambiar

## 4. Encender y apagar con cada pulsación

Sobre el código anterior, basta con cambiar lo que pasa al detectar la pulsación:

```cpp
bool ledEncendido = false;

// ...dentro del if (estadoEstable == LOW):
ledEncendido = !ledEncendido;
digitalWrite(13, ledEncendido);
```

:::tip
Si vas a usar varios botones, la librería **Bounce2** (Herramientas → Administrar Bibliotecas) hace el antirrebote por ti con una línea por botón.
:::

## ¿Y ahora qué?

El siguiente paso natural es leer un valor que cambie de forma continua, como el giro de un [potenciómetro](/guias/sensores/potenciometro).
