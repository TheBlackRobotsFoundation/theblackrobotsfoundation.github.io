---
sidebar_position: 4
title: Un humanoide que aprende a andar
sidebar_custom_props:
  icon: /img/guias/iconos/ejemplos.svg
---

# Un humanoide que aprende a andar

Juntamos todo lo de esta sección: [MuJoCo](/guias/simulacion-rl/mujoco/que-es-mujoco) pone la física, [Gymnasium](/guias/simulacion-rl/gymnasium/que-es-gymnasium) pone las reglas y el [aprendizaje por refuerzo](que-es-el-rl) pone la inteligencia. El resultado es un humanoide de 17 articulaciones que aprende a caminar solo.

## Entrenar un humanoide desde cero

El código es el mismo que el del péndulo, cambiando el entorno y el algoritmo. Para robots complejos, **SAC** (*Soft Actor-Critic*) suele aprender mejor que PPO:

```python
import gymnasium as gym
from stable_baselines3 import SAC

env = gym.make("Humanoid-v5")

model = SAC("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=2_000_000)    # millones de pasos: horas de cómputo
model.save("sac_humanoide")
```

La única diferencia real con el péndulo es la **escala**: donde el péndulo necesitaba 50.000 pasos, el humanoide necesita millones. Entrenarlo entero lleva horas, incluso con una buena GPU.

## Aprovechar un modelo ya entrenado

Como entrenar desde cero es caro, la comunidad **Farama** publica agentes expertos ya entrenados. Podemos descargar uno y verlo andar al instante, sin esperar horas:

```python
import gymnasium as gym
from huggingface_sb3 import load_from_hub
from stable_baselines3 import SAC

# Descargamos un humanoide experto ya entrenado
ruta = load_from_hub("farama-minari/Humanoid-v5-SAC-expert",
                     "humanoid-v5-sac-expert.zip")
model = SAC.load(ruta)

# Y lo dejamos correr
env = gym.make("Humanoid-v5", render_mode="human")
obs, _ = env.reset()
done = False
while not done:
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated
env.close()
```

Este es justo el humanoide del vídeo del principio: la política ya sabe qué fuerza aplicar en cada articulación para avanzar sin caerse.

{/* Pega el ID de tu vídeo de YouTube en TU_VIDEO_ID (la parte final de la URL, p. ej. youtu.be/XXXXXXXXXXX) */}
<iframe width="720" height="405" src="https://www.youtube.com/embed/TU_VIDEO_ID" title="Humanoide que aprende a andar" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>

## El camino completo, de un vistazo

Recorriendo estas guías has visto las cuatro piezas encajar:

1. **URDF / MJCF** describe el cuerpo del robot
2. **MuJoCo** simula su física paso a paso
3. **Gymnasium** lo convierte en un entorno con `reset` y `step`
4. **RL** (Q-learning para entender, SB3 para la práctica) entrena la política que lo controla

<img src="/img/guias/simulacion-rl/stack.svg" alt="El camino completo: del URDF que describe el cuerpo, a MuJoCo que lo simula, a Gymnasium que lo envuelve, al RL que lo entrena" width="480" />

Ese mismo camino sirve para un péndulo, un cuadrúpedo o un humanoide: solo cambia la escala del problema.

:::tip
¿El siguiente paso? Coge un [URDF propio](/guias/urdf/tu-primer-urdf), impórtalo en MuJoCo, envuélvelo como entorno de Gymnasium y entrénalo con SB3. Ahí es donde la simulación deja de ser un ejemplo y pasa a ser **tu** robot.
:::
