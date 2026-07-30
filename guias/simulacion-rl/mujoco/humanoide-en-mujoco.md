---
sidebar_position: 3
title: Un humanoide en MuJoCo
sidebar_custom_props:
  icon: /img/guias/iconos/ejemplos.svg
---

# Un humanoide en MuJoCo

Vamos a cargar un **robot humanoide completo** —torso, brazos y piernas, 17 articulaciones— y verlo moverse. Este es el resultado que buscamos:

{/* Pega el ID de tu vídeo de YouTube en TU_VIDEO_ID (la parte final de la URL, p. ej. youtu.be/XXXXXXXXXXX) */}
<iframe width="720" height="405" src="https://www.youtube.com/embed/TU_VIDEO_ID" title="Humanoide en MuJoCo" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>

Ese humanoide está controlado por un agente entrenado con aprendizaje por refuerzo. Aquí lo cargamos ya listo; en la sección de [RL](/guias/simulacion-rl/aprendizaje-por-refuerzo/que-es-el-rl) veremos cómo aprende.

## El bucle de simulación en código

Con Gymnasium por encima de MuJoCo, mover el humanoide un episodio completo es este bucle:

```python
import gymnasium as gym

# Cargamos el humanoide con ventana en pantalla
env = gym.make("Humanoid-v5", render_mode="human")

obs, _ = env.reset()          # estado inicial del robot
done = False
while not done:
    # Aquí decidiría el agente; de momento, acción aleatoria
    action = env.action_space.sample()
    obs, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated

env.close()
```

Si lo ejecutas verás al humanoide... desplomarse. Es normal: con acciones **aleatorias** no sabe andar. Ese es justo el problema que resuelve el aprendizaje por refuerzo.

## Grabar la simulación en vídeo

Para guardar un MP4 en vez de abrir una ventana, se cambia el `render_mode` y se acumulan los fotogramas:

```python
import gymnasium as gym
import imageio

env = gym.make("Humanoid-v5", render_mode="rgb_array", width=1280, height=720)

obs, _ = env.reset()
frames, done = [], False
while not done:
    action = env.action_space.sample()
    obs, reward, terminated, truncated, _ = env.step(action)
    frames.append(env.render())      # capturamos cada fotograma
    done = terminated or truncated
env.close()

imageio.mimsave("humanoide.mp4", frames, fps=50, quality=8)
```

## Las tres piezas del bucle

- `reset()` — coloca el robot en su posición de partida y devuelve la primera **observación**
- `step(action)` — aplica una acción (las fuerzas en las articulaciones) y avanza la física un paso
- `render()` — dibuja el estado actual, para verlo o grabarlo

:::tip
`Humanoid-v5` es un entorno de **Gymnasium**, la capa que envuelve a MuJoCo y le da esta interfaz tan limpia de `reset` / `step`. Es lo que vemos en la [siguiente sección](/guias/simulacion-rl/gymnasium/que-es-gymnasium).
:::
