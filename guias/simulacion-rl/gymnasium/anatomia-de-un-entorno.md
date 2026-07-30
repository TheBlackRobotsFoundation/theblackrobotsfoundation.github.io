---
sidebar_position: 2
title: Anatomía de un entorno
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Anatomía de un entorno

Un entorno de Gymnasium se resume en un **bucle**: observar, actuar, recibir recompensa, repetir. Aquí lo tienes entero, con un agente que juega al azar:

```python
import gymnasium as gym

env = gym.make("Humanoid-v5")

obs, info = env.reset()               # 1. estado inicial
total = 0.0
done = False

while not done:
    action = env.action_space.sample()          # 2. elegir acción
    obs, reward, terminated, truncated, info = env.step(action)   # 3. actuar
    total += reward                             # 4. sumar recompensa
    done = terminated or truncated              # 5. ¿episodio terminado?

print(f"Recompensa total del episodio: {total:.0f}")
env.close()
```

Ese es el patrón que veremos una y otra vez. Vamos pieza a pieza.

<img src="/img/guias/simulacion-rl/bucle-reset-step.svg" alt="El bucle de un entorno: reset inicia el episodio, y luego se repite elegir acción, step y comprobar si done hasta que el episodio termina" width="480" />

## Observación y acción: los espacios

Cada entorno declara qué forma tienen sus observaciones y sus acciones, en los **espacios** `observation_space` y `action_space`:

```python
print(env.observation_space)   # Box(-inf, inf, (348,), float64)
print(env.action_space)        # Box(-0.4, 0.4, (17,), float32)
```

- La **observación** del humanoide son 348 números (ángulos, velocidades, contactos…)
- La **acción** son 17 números: la fuerza en cada una de sus articulaciones

Un `Box` es un espacio **continuo** (valores con decimales dentro de un rango). Otros entornos usan `Discrete` (un número entero: 0, 1, 2…), típico de rejillas y laberintos.

## Lo que devuelve `step`

Cada `step(action)` devuelve cinco cosas:

| Valor | Qué es |
|---|---|
| `obs` | La nueva observación tras actuar |
| `reward` | La recompensa de este paso |
| `terminated` | `True` si el episodio acabó por la tarea (el robot se cayó) |
| `truncated` | `True` si se acabó por tiempo (límite de pasos) |
| `info` | Datos extra para depurar |

## La recompensa: qué queremos que aprenda

La **recompensa** es la señal que guía al agente. En el humanoide, se le premia por **avanzar** y por **mantenerse en pie**, y se le penaliza por gastar demasiada fuerza. El agente no sabe "andar": solo busca acumular la mayor recompensa posible, y andar resulta ser la mejor forma de lograrlo.

:::tip
Diseñar bien la recompensa es el 80% del trabajo en RL. Si un robot aprende algo raro (avanzar arrastrándose en vez de andar), casi siempre es porque la recompensa premiaba eso sin querer.
:::
