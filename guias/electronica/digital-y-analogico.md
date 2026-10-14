---
sidebar_position: 2
sidebar_label: Digital y analógico
title: Señales digitales y analógicas
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Señales digitales y analógicas

Todo lo que entra y sale de un Arduino es una **señal eléctrica**: una tensión que cambia con el tiempo. Hay dos formas de leerla o generarla.

<img src="/img/guias/electronica/digital-analogico.svg" alt="Comparación entre una señal digital y una analógica" />

## Digital: encendido o apagado

Una señal digital tiene **dos estados**:

- **HIGH** (1): unos 5 V
- **LOW** (0): unos 0 V

Es perfecta para todo lo que funciona "a dos niveles": un pulsador pulsado o suelto, un LED encendido o apagado, un sensor que detecta o deja de detectar.

```cpp
pinMode(2, INPUT);            // el pin 2 lee
int estado = digitalRead(2);  // HIGH o LOW

pinMode(8, OUTPUT);           // el pin 8 escribe
digitalWrite(8, HIGH);        // saca 5 V
```

Los pines digitales del UNO son del **0 al 13**. Los analógicos (A0 a A5) también funcionan como digitales si los necesitas.

:::caution
Los pines **0 (RX) y 1 (TX)** los usa el USB para subir programas y para el Monitor Serie. Déjalos libres mientras estés aprendiendo.
:::

## Analógica: todos los valores intermedios

Una señal analógica puede tomar **cualquier valor** entre 0 y 5 V. Así se comportan muchos sensores: un potenciómetro, una fotorresistencia o un sensor de temperatura dan una tensión que sube y baja de forma continua.

El Arduino la lee con los pines **A0 a A5** y un conversor interno (ADC) de **10 bits**, que la traduce a un número entre **0 y 1023**:

<img src="/img/guias/electronica/conversion-adc.svg" alt="El conversor analógico-digital traduce de 0 a 5 V en un número de 0 a 1023" />

```cpp
int valor = analogRead(A0);              // 0 … 1023
float voltios = valor * 5.0 / 1023.0;    // lo pasamos a voltios
```

Cada "escalón" equivale a unos **4,9 mV** (5 V / 1024).

## ¿Y para sacar una tensión intermedia?

El UNO genera valores intermedios con un truco llamado **PWM**: enciende y apaga un pin muy deprisa. Lo tienes explicado en la [siguiente sección](./pwm).

## Resumen

| | Digital | Analógica |
|---|---|---|
| Valores | 0 o 1 | 0 a 1023 (lectura) |
| Pines (UNO) | 0 a 13 | A0 a A5 |
| Leer | `digitalRead()` | `analogRead()` |
| Escribir | `digitalWrite()` | `analogWrite()` (PWM) |
