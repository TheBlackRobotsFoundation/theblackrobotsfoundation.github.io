---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para medir distancias

Con **Trig** en el pin 10 y **Echo** en el pin 9.

## 1. Medir y mostrar la distancia

```cpp
#define TRIG 10
#define ECHO 9

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  Serial.begin(9600);
}

void loop() {
  // pulso de 10 µs en Trig
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  // duración del eco (máximo 30 ms)
  long tiempo = pulseIn(ECHO, HIGH, 30000);
  float distancia = tiempo * 0.0343 / 2;

  if (tiempo == 0) {
    Serial.println("Sin eco (fuera de alcance)");
  } else {
    Serial.print(distancia, 1);
    Serial.println(" cm");
  }

  delay(60);   // deja que se apaguen los ecos antes de medir otra vez
}
```

Mueve la mano delante del sensor y mira el Monitor Serie.

## 2. Una función reutilizable

Para usarlo dentro de un programa más grande, encapsula la medida:

```cpp
float medirDistancia() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  long tiempo = pulseIn(ECHO, HIGH, 30000);
  if (tiempo == 0) return 999;   // sin eco: lo tratamos como "muy lejos"
  return tiempo * 0.0343 / 2;
}
```

Devolver un valor grande cuando no hay eco hace que el resto del programa lo trate como "camino libre".

## 3. Lecturas fiables: la mediana

Una lectura suelta puede salir mal por un eco perdido. Tomar **5 medidas y quedarse con la del medio** descarta los valores raros:

```cpp
float distanciaFiable() {
  float m[5];
  for (int i = 0; i < 5; i++) {
    m[i] = medirDistancia();
    delay(10);
  }
  // ordenamos (5 valores: basta con un método sencillo)
  for (int i = 0; i < 4; i++)
    for (int j = i + 1; j < 5; j++)
      if (m[j] < m[i]) { float t = m[i]; m[i] = m[j]; m[j] = t; }
  return m[2];   // la mediana
}
```

## 4. Alarma de proximidad

El LED de la placa parpadea más rápido cuanto más cerca está el objeto, como un sensor de aparcamiento:

```cpp
void loop() {
  float d = medirDistancia();

  if (d < 50) {
    int pausa = map(d, 0, 50, 30, 400);   // cerca = pausa corta
    digitalWrite(13, HIGH);
    delay(30);
    digitalWrite(13, LOW);
    delay(pausa);
  } else {
    digitalWrite(13, LOW);
    delay(60);
  }
}
```

Recuerda añadir `pinMode(13, OUTPUT);` en `setup()`. Con un [zumbador](/guias/actuadores/zumbador) en lugar del LED, suena como el de un coche.

:::tip
La librería **NewPing** (Administrar Bibliotecas) simplifica todo esto a una línea, `sonar.ping_cm()`, y gestiona varios sensores a la vez.
:::

## ¿Y ahora qué?

Con este sensor, dos [motores DC](/guias/actuadores/motores-dc) y un driver ya tienes lo necesario para el [robot esquiva-obstáculos](/guias/proyecto-esquiva-obstaculos).
