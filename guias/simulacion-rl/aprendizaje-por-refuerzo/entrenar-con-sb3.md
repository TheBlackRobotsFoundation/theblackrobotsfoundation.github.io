---
sidebar_position: 3
title: Tu primer agente con Stable-Baselines3
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Tu primer agente con Stable-Baselines3

Ya sabes cómo aprende un agente en un laberinto. Para robots con física continua, en vez de programar el algoritmo a mano usamos **Stable-Baselines3** (SB3): una librería con los mejores algoritmos de RL ya implementados y probados.

Vamos a entrenar un agente **de verdad** en el entorno más sencillo: el péndulo invertido.

## El objetivo

`InvertedPendulum-v5` es un carrito con un palo encima. El agente controla una sola cosa —empujar a izquierda o derecha— y gana recompensa por cada instante que mantiene el palo **vertical**. El máximo posible es 1000.

<img src="/img/guias/simulacion-rl/env-pendulo.png" alt="Captura del entorno InvertedPendulum-v5: un carrito amarillo sobre un raíl con un palo vertical encima" width="480" />

*El entorno `InvertedPendulum-v5`: el carrito se mueve por el raíl para mantener el palo en pie.*

## Entrenar en cuatro líneas

Con SB3, entrenar es crear el modelo y llamar a `learn`:

```python
import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("InvertedPendulum-v5")

model = PPO("MlpPolicy", env, verbose=1, seed=0)   # el agente (red neuronal)
model.learn(total_timesteps=50_000)                # entrenar 50.000 pasos
model.save("ppo_pendulo")                          # guardar lo aprendido
```

- `PPO` — el algoritmo (*Proximal Policy Optimization*), robusto y de los más usados
- `"MlpPolicy"` — la política es una red neuronal sencilla (un perceptrón multicapa)
- `learn(50_000)` — deja que juegue 50.000 pasos aprendiendo de cada uno

En pocos segundos, el agente pasa de tirar el palo al instante a mantenerlo firme.

## Comprobar si ha aprendido

SB3 trae una función para medir el rendimiento medio en varios episodios:

```python
from stable_baselines3.common.evaluation import evaluate_policy

media, desv = evaluate_policy(model, env, n_eval_episodes=10)
print(f"Recompensa media: {media:.0f} +/- {desv:.0f} (máximo 1000)")
```

Un agente bien entrenado se acerca a los 1000: el palo ya casi no se cae.

## Ver al agente en acción

Cargamos el modelo guardado y lo dejamos jugar con la ventana abierta. Fíjate: es el mismo bucle `reset` / `step` de siempre, pero ahora la acción la decide el **modelo**, no el azar:

```python
env = gym.make("InvertedPendulum-v5", render_mode="human")

obs, _ = env.reset()
done = False
while not done:
    action, _ = model.predict(obs, deterministic=True)   # el agente decide
    obs, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated
env.close()
```

`model.predict(obs)` es la **política** ya entrenada: le das lo que ve el robot y te devuelve la mejor acción. Con `deterministic=True` le pedimos su mejor jugada, sin exploración.

:::tip
PPO funciona igual de bien en el humanoide: solo cambia `"InvertedPendulum-v5"` por `"Humanoid-v5"`. La diferencia es la **paciencia**: el péndulo aprende en 50.000 pasos; un humanoide necesita millones y bastantes horas de cómputo.
:::
