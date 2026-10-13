---
sidebar_position: 3
title: Código
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código

## La lógica

El robot repite una y otra vez una decisión muy sencilla:

![Diagrama de flujo: medir la distancia; si es menor de 25 cm, parar, retroceder y girar; si no, avanzar](/img/guias/proyecto-esquiva-obstaculos/logica.svg)

El giro se hace hacia un lado **al azar** y durante un tiempo variable. Así el robot no se queda atascado repitiendo siempre el mismo movimiento en una esquina.

## El programa completo

```cpp
// Robot esquiva-obstáculos · Black Robots

// --- Pines ---------------------------------------------------------
#define TRIG A5
#define ECHO A4

#define ENA 11   // velocidad motor izquierdo
#define IN1 10
#define IN2 9
#define IN3 8
#define IN4 7
#define ENB 6    // velocidad motor derecho

// --- Ajustes -------------------------------------------------------
const int DISTANCIA_MINIMA = 25;   // cm: más cerca de esto, esquiva
const int VELOCIDAD = 170;         // 0 – 255
const int VEL_GIRO  = 160;

// --- Motores -------------------------------------------------------
void motores(int izq, int der) {   // de -255 a 255 cada uno
  izq = constrain(izq, -255, 255);
  der = constrain(der, -255, 255);
  digitalWrite(IN1, izq > 0);
  digitalWrite(IN2, izq < 0);
  analogWrite(ENA, abs(izq));
  digitalWrite(IN3, der > 0);
  digitalWrite(IN4, der < 0);
  analogWrite(ENB, abs(der));
}

void avanzar()  { motores(VELOCIDAD, VELOCIDAD); }
void parar()    { motores(0, 0); }

// --- Sensor --------------------------------------------------------
float medirDistancia() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  long tiempo = pulseIn(ECHO, HIGH, 30000);
  if (tiempo == 0) return 999;      // sin eco: camino libre
  return tiempo * 0.0343 / 2;
}

// --- Maniobra de esquivar ------------------------------------------
void esquivar() {
  parar();
  delay(150);

  motores(-VELOCIDAD, -VELOCIDAD);  // un poco hacia atrás
  delay(350);

  if (random(2) == 0) {
    motores(-VEL_GIRO, VEL_GIRO);   // gira a la izquierda
  } else {
    motores(VEL_GIRO, -VEL_GIRO);   // gira a la derecha
  }
  delay(random(300, 700));          // durante un tiempo al azar

  parar();
  delay(100);
}

// --- Programa ------------------------------------------------------
void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  int pines[] = {ENA, IN1, IN2, IN3, IN4, ENB};
  for (int p : pines) pinMode(p, OUTPUT);

  parar();
  randomSeed(analogRead(A0));       // azar distinto en cada arranque
  delay(2000);                      // 2 s para dejarlo en el suelo
}

void loop() {
  float distancia = medirDistancia();

  if (distancia < DISTANCIA_MINIMA) {
    esquivar();
  } else {
    avanzar();
  }

  delay(30);
}
```

## Cómo funciona

- **`motores(izq, der)`**: la función de la [guía de motores DC](/guias/actuadores/motores-dc/codigo-basico). Valores positivos, hacia delante; negativos, hacia atrás
- **`medirDistancia()`**: la de la [guía de ultrasonidos](/guias/sensores/ultrasonidos/codigo-basico). Si no llega eco, devuelve 999 para que el robot lo trate como camino libre
- **`esquivar()`**: la maniobra completa: parar, retroceder y girar
- **`random(2)`** da 0 o 1 al azar: elige el lado del giro
- **`randomSeed(analogRead(A0))`**: A0 está sin conectar y su lectura es ruido, así que cada arranque el azar empieza en un punto distinto

## Primera prueba

1. Con el robot **en el aire**, sube el programa y conecta la batería
2. Las dos ruedas deben girar **hacia delante**
3. Pon la mano delante del sensor: deben parar, ir hacia atrás y girar

| Lo que ves | Solución |
|---|---|
| Una rueda gira hacia atrás | intercambia los dos cables de ese motor en el L298N |
| Las dos giran hacia atrás | intercambia los cables de los dos motores |
| Al girar, se va hacia el lado contrario | intercambia los motores: el izquierdo a OUT3/OUT4 y el derecho a OUT1/OUT2 |
| No se mueve | revisa el GND común y que los puentes de ENA/ENB estén quitados |
| Esquiva sin nada delante | el sensor ve el suelo: levántalo o inclínalo un poco hacia arriba |

## Ajustes

- **`DISTANCIA_MINIMA`**: súbela si el robot llega a tocar los obstáculos; bájala si esquiva demasiado pronto
- **`VELOCIDAD`**: empieza en 150 – 170. Si los motores zumban sin moverse, súbela
- **Tiempos de `esquivar()`**: ajusta los `delay()` hasta que gire lo justo en tu suelo

:::tip
Si el robot se desvía al ir recto, un motor es algo más rápido que el otro. Compénsalo bajando su velocidad: por ejemplo, `motores(VELOCIDAD, VELOCIDAD - 15)` en `avanzar()`.
:::

¿Funciona? Pasa a las [mejoras](./mejoras).
