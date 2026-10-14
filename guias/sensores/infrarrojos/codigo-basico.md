---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para detectar la línea

Con **DO** en el pin 2 y **AO** en A0.

## 1. Blanco o negro (salida digital)

```cpp
#define SENSOR_DO 2

void setup() {
  pinMode(SENSOR_DO, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(SENSOR_DO) == HIGH) {
    Serial.println("Negro (línea)");
  } else {
    Serial.println("Blanco");
  }
  delay(100);
}
```

## 2. Cuánta luz vuelve (salida analógica)

```cpp
#define SENSOR_AO A0

void setup() {
  Serial.begin(9600);
}

void loop() {
  int valor = analogRead(SENSOR_AO);
  Serial.println(valor);
  delay(50);
}
```

Abre el **Serial Plotter** y pasa el sensor del blanco al negro. Apunta los dos valores: el punto medio entre ambos es un buen umbral si prefieres decidir tú en el código en vez de con el potenciómetro.

## 3. La lógica de un sigue-líneas

Con dos sensores, uno a cada lado de la línea, el robot decide así:

| Izquierdo | Derecho | Qué significa | Qué hacer |
|---|---|---|---|
| blanco | blanco | la línea está en medio | recto |
| negro | blanco | la línea se va a la izquierda | girar a la izquierda |
| blanco | negro | la línea se va a la derecha | girar a la derecha |
| negro | negro | cruce o final | parar |

```cpp
#define IZQ 2
#define DER 3

// Motores (montaje de la guía de motores DC)
#define ENA 11
#define IN1 10
#define IN2 9
#define IN3 8
#define IN4 7
#define ENB 6
const int VELOCIDAD = 140;

void motores(int izq, int der) {
  digitalWrite(IN1, izq > 0);  digitalWrite(IN2, izq < 0);  analogWrite(ENA, abs(izq));
  digitalWrite(IN3, der > 0);  digitalWrite(IN4, der < 0);  analogWrite(ENB, abs(der));
}
void avanzar()        { motores(VELOCIDAD, VELOCIDAD); }
void girarIzquierda() { motores(-VELOCIDAD, VELOCIDAD); }
void girarDerecha()   { motores(VELOCIDAD, -VELOCIDAD); }
void parar()          { motores(0, 0); }

void setup() {
  pinMode(IZQ, INPUT);
  pinMode(DER, INPUT);
  int pines[] = {ENA, IN1, IN2, IN3, IN4, ENB};
  for (int p : pines) pinMode(p, OUTPUT);
}

void loop() {
  bool izqNegro = digitalRead(IZQ) == HIGH;
  bool derNegro = digitalRead(DER) == HIGH;

  if (!izqNegro && !derNegro) {
    avanzar();
  } else if (izqNegro && !derNegro) {
    girarIzquierda();
  } else if (!izqNegro && derNegro) {
    girarDerecha();
  } else {
    parar();
  }
}
```

Las funciones de los motores son las de la guía de [motores DC](/guias/actuadores/motores-dc/codigo-basico), donde tienes explicado cómo funcionan y cómo conectar el L298N.

:::tip
Empieza con los motores **despacio**. Un sigue-líneas rápido necesita reaccionar muy deprisa; cuando funcione bien lento, ve subiendo la velocidad.
:::

## ¿Y ahora qué?

Para que un robot sepa **cuánto** han girado sus ruedas, y con ello cuánto ha avanzado, necesitas [encoders](/guias/sensores/encoders).
