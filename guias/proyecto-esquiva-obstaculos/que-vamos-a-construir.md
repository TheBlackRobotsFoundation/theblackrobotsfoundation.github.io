---
sidebar_position: 1
sidebar_label: El proyecto
title: Qué vamos a construir
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# Qué vamos a construir

Un robot de dos ruedas que **avanza solo y esquiva lo que se encuentra**. Mide la distancia con un sensor de ultrasonidos; cuando algo está demasiado cerca, se para, retrocede, gira y sigue su camino.

Es el proyecto clásico para empezar en robótica móvil porque reúne las tres partes de cualquier robot:

![Diagrama de bloques: el HC-SR04 mide, el Arduino decide y el L298N mueve los motores con la batería](/img/guias/proyecto-esquiva-obstaculos/bloques.svg)

- **Percibir**: el [sensor de ultrasonidos](/guias/sensores/ultrasonidos) mide la distancia a lo que tiene delante
- **Decidir**: el [Arduino](/guias/arduino/que-es-arduino) compara esa distancia con un límite y elige qué hacer
- **Actuar**: el [driver L298N](/guias/actuadores/motores-dc) mueve los dos [motores DC](/guias/actuadores/motores-dc) con la energía de la batería

## Lo que necesitas saber

Cada pieza tiene su guía. Puedes empezar ya y consultarlas a medida que las necesites:

| Guía | Para qué |
|---|---|
| [Primer programa](/guias/arduino/primer-programa) | subir código al Arduino |
| [Cómo alimentar un robot](/guias/electronica/alimentacion) | baterías y GND común |
| [Ultrasonidos](/guias/sensores/ultrasonidos) | medir la distancia |
| [Motores DC y puente H](/guias/actuadores/motores-dc) | mover las ruedas |

## Materiales

| Componente | Cantidad | Notas |
|---|---|---|
| Chasis 2WD con dos motores TT y rueda loca | 1 | el kit más común; trae ruedas y tornillería |
| Arduino UNO | 1 | |
| Módulo L298N | 1 | |
| Sensor HC-SR04 | 1 | mejor con un soporte que lo mantenga recto |
| Portapilas de 6 × AA o batería LiPo 2S (7,4 V) | 1 | para los motores |
| Power bank USB o pila de 9 V con conector | 1 | para el Arduino |
| Interruptor | 1 | recomendado, en el cable + de la batería |
| Cables dupont macho-hembra y macho-macho | ~15 | |
| Bridas, cinta de doble cara | — | para sujetar los módulos |

:::tip
Los kits de "coche robot 2WD" traen chasis, motores, ruedas, portapilas e interruptor por muy poco dinero. Cualquiera sirve: las medidas exactas dan igual.
:::

## Cómo está organizado

1. [Montaje](./montaje): el chasis y todas las conexiones
2. [Código](./codigo): el programa completo, explicado
3. [Mejoras](./mejoras): ideas para hacerlo más listo
