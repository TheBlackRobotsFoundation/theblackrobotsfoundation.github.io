---
sidebar_position: 1
title: ¿Qué es MuJoCo?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es MuJoCo?

**MuJoCo** (*Multi-Joint dynamics with Contact*) es un **motor de física**: un programa que calcula cómo se mueve un robot cuando actúan sobre él la gravedad, los motores y los choques con el suelo.

Le das un robot y unas fuerzas en sus articulaciones, y MuJoCo te dice, paso a paso, dónde acaba cada pieza. Es el escenario donde un robot puede caerse mil veces sin romperse nada.

<img src="/img/guias/simulacion-rl/env-halfcheetah.png" alt="Captura de un robot cuadrúpedo (HalfCheetah) simulado en MuJoCo sobre un suelo de cuadrícula" width="560" />

*Un robot (HalfCheetah) dentro de MuJoCo: la gravedad, el suelo y sus articulaciones, todo simulado.*

## ¿Por qué se usa en robótica e IA?

- **Rápido y preciso** — simula contactos y articulaciones muy bien, ideal para entrenar
- **Gratis y open source** — mantenido por Google DeepMind
- **El estándar en aprendizaje por refuerzo** — la mayoría de entornos de robots (humanoides, cuadrúpedos) corren sobre MuJoCo
- **Se integra con Python** — se controla con unas pocas líneas, como veremos

## Cómo describe un robot: MJCF

MuJoCo usa su propio formato de texto, el **MJCF** (un XML, primo del [URDF](/guias/urdf/que-es-urdf)). Describe lo mismo —piezas, articulaciones, geometría— más detalles de física como la fricción o los motores.

La buena noticia: si ya entiendes URDF, MJCF te resultará familiar. Y MuJoCo puede **importar URDF** directamente, así que puedes reutilizar robots que ya tengas.

## El bucle de simulación

Toda simulación en MuJoCo hace lo mismo, una y otra vez:

1. Lee el **estado** actual (posiciones y velocidades de cada articulación)
2. Aplica las **fuerzas** de los motores
3. Avanza el tiempo un pasito (un `step`) y calcula el nuevo estado

Repitiendo ese paso miles de veces por segundo, el robot cobra vida. En la [primera simulación](humanoide-en-mujoco) lo vemos con un humanoide de verdad.

<img src="/img/guias/simulacion-rl/stack.svg" alt="El stack de simulación: URDF describe el cuerpo, MuJoCo simula la física, Gymnasium lo envuelve como entorno y el RL entrena la política" width="480" />

*Dónde encaja MuJoCo: pone la física dentro de un stack que va del cuerpo del robot hasta el agente que lo controla.*

:::tip
MuJoCo solo se ocupa de la **física**. La inteligencia (qué fuerza aplicar en cada momento) la pone el agente de aprendizaje por refuerzo, que veremos más adelante.
:::
