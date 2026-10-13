---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para mover motores DC

Con **ENA** en el pin 11, **IN1** en el 10 e **IN2** en el 9.

:::tip
Para las primeras pruebas, deja el robot **con las ruedas en el aire** (sobre una caja, por ejemplo). Así no sale disparado si algo no va como esperas.
:::

## 1. Adelante, parar y atrás

```cpp
#define ENA 11
#define IN1 10
#define IN2 9

void setup() {
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}

void loop() {
  // adelante
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 200);
  delay(2000);

  // parar
  analogWrite(ENA, 0);
  delay(1000);

  // atrás
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  analogWrite(ENA, 200);
  delay(2000);

  analogWrite(ENA, 0);
  delay(1000);
}
```

## 2. Una función para el motor

Una sola función que recibe la velocidad **con signo**: positiva hacia delante, negativa hacia atrás.

```cpp
void motorA(int velocidad) {           // de -255 a 255
  velocidad = constrain(velocidad, -255, 255);
  digitalWrite(IN1, velocidad > 0);
  digitalWrite(IN2, velocidad < 0);
  analogWrite(ENA, abs(velocidad));
}
```

`motorA(150)` avanza, `motorA(-150)` retrocede y `motorA(0)` para.

## 3. Arranque suave

Acelerar de golpe hace patinar las ruedas y pide un pico de corriente a la batería. Mejor subir poco a poco:

```cpp
void loop() {
  for (int v = 0; v <= 255; v += 5) {
    motorA(v);
    delay(20);
  }
  delay(1000);
  for (int v = 255; v >= 0; v -= 5) {
    motorA(v);
    delay(20);
  }
  delay(1000);
}
```

## 4. Dos motores: las funciones de un robot

Con el segundo motor conectado (ENB en el 6, IN3 en el 8, IN4 en el 7), estas funciones mueven un robot de dos ruedas. Son las que usan el [sigue-líneas](/guias/sensores/infrarrojos/codigo-basico):

```cpp
#define ENA 11
#define IN1 10
#define IN2 9
#define IN3 8
#define IN4 7
#define ENB 6

int velocidad = 180;

void motores(int izq, int der) {        // de -255 a 255 cada uno
  izq = constrain(izq, -255, 255);
  der = constrain(der, -255, 255);
  digitalWrite(IN1, izq > 0);
  digitalWrite(IN2, izq < 0);
  analogWrite(ENA, abs(izq));
  digitalWrite(IN3, der > 0);
  digitalWrite(IN4, der < 0);
  analogWrite(ENB, abs(der));
}

void avanzar()        { motores(velocidad, velocidad); }
void retroceder()     { motores(-velocidad, -velocidad); }
void girarIzquierda() { motores(-velocidad, velocidad); }
void girarDerecha()   { motores(velocidad, -velocidad); }
void parar()          { motores(0, 0); }

void setup() {
  int pines[] = {ENA, IN1, IN2, IN3, IN4, ENB};
  for (int p : pines) pinMode(p, OUTPUT);
}

void loop() {
  avanzar();         delay(1500);
  girarDerecha();    delay(500);
  avanzar();         delay(1500);
  parar();           delay(2000);
}
```

Los giros hacen rodar una rueda hacia delante y la otra hacia atrás: el robot gira **sobre sí mismo**. Para curvas más abiertas, frena una rueda en lugar de invertirla: `motores(velocidad, velocidad / 3)`.

:::tip
Si el robot va hacia atrás cuando le dices `avanzar()`, o gira al revés, intercambia los cables del motor que va mal en sus bornas OUT. Es más fácil que tocar el código.
:::

## ¿Y ahora qué?

Con un [sensor de ultrasonidos](/guias/sensores/ultrasonidos) delante y estas funciones, ya tienes la base de un robot móvil que esquiva obstáculos.
