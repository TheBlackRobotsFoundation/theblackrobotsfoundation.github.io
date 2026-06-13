---
sidebar_position: 4
title: Conceptos básicos
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Conceptos básicos

## Funciones esenciales

| Función | Para qué sirve |
|---|---|
| `setup()` | Se ejecuta una vez al arrancar. Configura pines y comunicaciones. |
| `loop()` | Se repite infinitamente. Aquí va la lógica del programa. |
| `pinMode(pin, modo)` | Define si un pin es `INPUT` o `OUTPUT`. |
| `digitalWrite(pin, valor)` | Pone un pin digital a `HIGH` (5V) o `LOW` (0V). |
| `digitalRead(pin)` | Lee el estado de un pin digital. |
| `analogRead(pin)` | Lee un pin analógico (valor entre 0 y 1023). |
| `analogWrite(pin, valor)` | Salida PWM en pines compatibles (0–255). |
| `delay(ms)` | Pausa el programa X milisegundos. |
| `Serial.begin(9600)` | Inicia la comunicación con el ordenador. |
| `Serial.println(x)` | Imprime un valor en el Monitor Serie. |

## Pines: digitales vs analógicos

- **Pines digitales** (0–13): solo entienden `HIGH` o `LOW`
- **Pines analógicos** (A0–A5): leen valores entre 0 y 5V (0–1023)
- **Pines PWM** (marcados con `~`): simulan una salida analógica

## Librerías

Las librerías añaden funcionalidades extra. Para instalar una:

1. Ve a **Herramientas → Administrar Bibliotecas**
2. Busca la librería por nombre
3. Pulsa **Instalar**

Librerías útiles para empezar:

- `Servo.h` — control de servomotores
- `Wire.h` — comunicación I2C
- `SPI.h` — comunicación SPI
- `EEPROM.h` — guardar datos en la memoria de la placa

## ¿Y ahora qué?

Con esto ya tienes la base. Los siguientes pasos naturales son aprender a leer sensores, controlar motores y comunicar el Arduino con el ordenador. Todo eso lo verás aplicado en los proyectos de Black Robots.
