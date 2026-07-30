---
sidebar_position: 1
title: ¿Qué es el aprendizaje por refuerzo?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es el aprendizaje por refuerzo?

El **aprendizaje por refuerzo** (o **RL**, de *Reinforcement Learning*) es enseñar a un agente a base de **premios y castigos**, sin decirle nunca cómo hacer la tarea. Prueba, se equivoca, y poco a poco descubre solo qué le conviene.

Es la misma idea con la que se adiestra a un animal: no le explicas la teoría, le das una recompensa cuando acierta y repite lo que le funciona.

## Las tres piezas

Todo problema de RL tiene los mismos tres actores:

- **Agente** — el que aprende y decide (el "cerebro" del robot)
- **Entorno** — el mundo donde actúa (el humanoide y su física en MuJoCo)
- **Recompensa** — el número que le dice si va bien o mal

## El ciclo de aprendizaje

El agente y el entorno se pasan la pelota en un bucle:

1. El agente **observa** el estado del entorno
2. Elige una **acción**
3. El entorno cambia y le devuelve una **recompensa**
4. El agente ajusta su estrategia para ganar más recompensa la próxima vez

Repitiendo esto millones de veces, el agente afina una **política**: su forma de decidir qué hacer en cada situación.

<img src="/img/guias/simulacion-rl/ciclo-rl-simple.svg" alt="El ciclo del aprendizaje por refuerzo: el agente envía una acción al entorno, y el entorno le devuelve una observación y una recompensa" width="560" />

## La política: lo que de verdad aprende

La **política** es el resultado del entrenamiento: una función que, dada una observación, devuelve la mejor acción. Cuando decimos que "el humanoide aprendió a andar", queremos decir que su política ya sabe qué fuerza aplicar en cada articulación para avanzar sin caerse.

## El gran dilema: explorar o explotar

Un agente vive una tensión constante:

- **Explotar** — repetir lo que ya sabe que da recompensa
- **Explorar** — probar cosas nuevas por si hay algo aún mejor

Si solo explota, se queda con la primera estrategia mediocre que encuentra. Si solo explora, nunca aprovecha lo aprendido. Todo algoritmo de RL es, en el fondo, una forma de equilibrar estas dos.

## El ciclo completo

Con todas las piezas sobre la mesa, así funciona el ciclo por dentro: la **política** elige la acción y el **aprendizaje** la ajusta con la recompensa que calcula el entorno.

<img src="/img/guias/simulacion-rl/ciclo-rl.svg" alt="El ciclo del aprendizaje por refuerzo en detalle: dentro del agente, la política elige la acción y el aprendizaje la actualiza; dentro del entorno, la física aplica la acción y calcula la recompensa. Abajo, los pasos en orden: observar, decidir, actuar, recompensa, aprender" width="700" />

:::tip
En RL no programas **cómo** se hace la tarea, sino **qué** quieres conseguir (la recompensa). El "cómo" lo descubre el agente. Ese cambio de mentalidad es lo que hace el RL tan potente... y a veces tan sorprendente.
:::
