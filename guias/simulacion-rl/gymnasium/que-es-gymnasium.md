---
sidebar_position: 1
title: ¿Qué es Gymnasium?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es Gymnasium?

**Gymnasium** es una librería de Python que define una **interfaz estándar** para entornos de aprendizaje por refuerzo. Es el idioma común entre el mundo (el robot en su simulación) y el agente (el que aprende a controlarlo).

Es la continuación del conocido *OpenAI Gym*, ahora mantenida por la fundación **Farama**. Gracias a ella, un mismo algoritmo puede entrenar un péndulo, un humanoide o un videojuego sin cambiar una línea: todos hablan Gymnasium.

## El trato: un entorno, cuatro preguntas

Todo entorno de Gymnasium responde siempre a lo mismo:

- **¿Qué veo?** — la **observación**: el estado del mundo (posiciones, velocidades…)
- **¿Qué puedo hacer?** — la **acción**: lo que el agente puede decidir (fuerzas, movimientos)
- **¿Qué tal lo hice?** — la **recompensa**: un número que premia o castiga
- **¿He terminado?** — si el episodio se acabó (el robot se cayó, o llegó a la meta)

Con solo esas cuatro cosas, cualquier algoritmo de RL puede aprender.

<img src="/img/guias/simulacion-rl/gym-cuatro-preguntas.svg" alt="Las cuatro preguntas que responde todo entorno: qué veo (observación), qué puedo hacer (acción), qué tal lo hice (recompensa) y he terminado (done)" width="620" />

## Dos métodos que lo son todo

Un entorno de Gymnasium se maneja con dos funciones:

```python
import gymnasium as gym

env = gym.make("Humanoid-v5")

obs, info = env.reset()              # empieza un episodio
obs, reward, terminated, truncated, info = env.step(action)   # da un paso
```

- `reset()` — arranca un episodio nuevo y te da la primera observación
- `step(action)` — aplicas una acción y el entorno te devuelve qué pasó

Ese par `reset` / `step` es el corazón de **todo** el aprendizaje por refuerzo. Lo desmontamos en la [siguiente página](anatomia-de-un-entorno).

<img src="/img/guias/simulacion-rl/env-humanoide.png" alt="Captura del entorno Humanoid-v5: un robot humanoide de pie sobre el suelo de la simulación en MuJoCo" width="520" />

*El entorno `Humanoid-v5` que controla el código de arriba: un humanoide simulado, listo para recibir acciones y devolver observaciones.*

:::tip
Gymnasium no simula nada por sí mismo: es la **interfaz**. Por debajo, un entorno de robot usa MuJoCo para la física. Gymnasium solo pone las reglas del juego para que agente y mundo se entiendan.
:::
