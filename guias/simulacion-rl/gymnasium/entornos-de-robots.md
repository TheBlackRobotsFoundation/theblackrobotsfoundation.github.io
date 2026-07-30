---
sidebar_position: 3
title: Entornos de robots
sidebar_custom_props:
  icon: /img/guias/iconos/ejemplos.svg
---

# Entornos de robots

Gymnasium trae un catálogo de robots ya montados sobre MuJoCo, listos para entrenar. Van de lo más simple a lo más complejo, y es el orden ideal para aprender.

## De menos a más articulaciones

| Entorno | Robot | Acciones | Reto |
|---|---|---|---|
| `InvertedPendulum-v5` | Un carro con un palo | 1 | Mantener el palo vertical |
| `Hopper-v5` | Una pata que salta | 3 | Avanzar a saltos sin caer |
| `Walker2d-v5` | Un bípedo plano | 6 | Caminar hacia delante |
| `HalfCheetah-v5` | Un cuadrúpedo plano | 6 | Correr lo más rápido posible |
| `Humanoid-v5` | Un humanoide completo | 17 | Andar sin desplomarse |

Cuantas más articulaciones, más difícil el problema: el humanoide, con 17, es de los más exigentes.

<img src="/img/guias/simulacion-rl/entornos-robots.png" alt="Los cinco robots de Gymnasium renderizados en MuJoCo: péndulo invertido, Hopper, Walker2d, HalfCheetah y Humanoid" width="720" />

*Los cinco entornos, del más simple (1 acción) al más complejo (17). Renders hechos con MuJoCo.*

## Probar cualquiera de ellos

Cambiar de robot es cambiar una sola cadena de texto. Este código sirve para todos:

```python
import gymnasium as gym

ENV_ID = "Walker2d-v5"      # prueba también "Hopper-v5" o "Humanoid-v5"

env = gym.make(ENV_ID, render_mode="human")
obs, _ = env.reset()
done = False
while not done:
    action = env.action_space.sample()
    obs, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated
env.close()
```

Con acciones aleatorias, todos fracasan de forma cómica. Darles inteligencia es el trabajo del agente de RL.

## Empezar por el péndulo

Antes de pelearte con el humanoide, conviene empezar por `InvertedPendulum-v5`: una sola acción, entrena en segundos y es facilísimo de entender. Es justo el que usaremos para [tu primer agente](/guias/simulacion-rl/aprendizaje-por-refuerzo/entrenar-con-sb3).

:::tip
La regla al aprender RL: valida tu código con el entorno **más simple** que puedas. Si tu agente aprende el péndulo, el mismo código (con más paciencia) aprenderá el humanoide.
:::
