---
sidebar_position: 2
title: Q-learning y SARSA
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Q-learning y SARSA

Para entender **cómo** aprende un agente, lo mejor es el caso más simple: un robot en un **laberinto** de casillas. Aquí no hace falta MuJoCo ni redes neuronales, solo una tabla de números. Son los algoritmos **Q-learning** y **SARSA**.

<img src="/img/guias/simulacion-rl/laberinto-tablaq.svg" alt="Un laberinto de casillas con inicio S y meta G, junto a la tabla Q que guarda, para cada estado y acción, cómo de buena es" width="660" />

## La tabla Q

La idea es guardar, para cada **casilla** (estado) y cada **movimiento** (acción), un número que estima "cómo de bueno es". Eso es la **tabla Q**: una fila por estado, una columna por acción.

```python
import numpy as np

# Tabla Q vacía: tantas filas como estados, tantas columnas como acciones
Q = np.zeros([env.observation_space.n, env.action_space.n])
```

Al principio está toda a cero: el agente no sabe nada. El entrenamiento va rellenando esos números con la experiencia.

## El algoritmo Q-learning

El agente recorre el laberinto muchas veces (**episodios**). En cada paso: mira su casilla, elige la acción que más promete, la ejecuta y **actualiza la tabla** con lo que ha aprendido.

```python
eta = 0.628      # tasa de aprendizaje: cuánto pesa cada nueva experiencia
gamma = 0.9      # cuánto valoramos las recompensas futuras
episodios = 300

for i in range(episodios):
    s, _ = env.reset()
    done = False
    while not done:
        # Elegir acción: la mejor conocida, con algo de azar para explorar
        a = np.argmax(Q[s, :] + np.random.randn(1, env.action_space.n) * (1.0 / (i + 1)))

        # Ejecutarla y ver qué pasa
        s1, r, done, _, _ = env.step(a)

        # La fórmula del Q-learning: corregimos nuestra estimación
        Q[s, a] = Q[s, a] + eta * (r + gamma * np.max(Q[s1, :]) - Q[s, a])

        s = s1
```

Esa línea de `Q[s, a] = ...` es el corazón del algoritmo. En palabras: *acerca tu estimación actual a lo que acabas de ganar, más lo mejor que puedas conseguir desde la casilla siguiente*.

- `eta` (tasa de aprendizaje) — cuánto haces caso a cada nueva experiencia
- `gamma` (factor de descuento) — cuánto te importan las recompensas futuras frente a las inmediatas
- El ruido `np.random.randn(...)` decreciente hace que el agente **explore mucho al principio** y se fíe más de la tabla según avanza

## SARSA: el primo prudente

**SARSA** es casi idéntico, con una diferencia clave en la actualización. En vez de suponer que en la casilla siguiente tomará la **mejor** acción posible, usa la acción que **realmente** va a tomar:

```python
# Q-learning: asume la MEJOR acción futura (optimista)
Q[s, a] += eta * (r + gamma * np.max(Q[s1, :]) - Q[s, a])

# SARSA: usa la acción que REALMENTE tomará (realista)
Q[s, a] += eta * (r + gamma * Q[s1, a1] - Q[s, a])
```

- **Q-learning** aprende la ruta óptima aunque durante el entrenamiento se arriesgue: es *optimista*
- **SARSA** tiene en cuenta sus propios errores de exploración: es más *prudente*, tiende a rutas seguras

## Del laberinto al humanoide

Estos algoritmos tabulares funcionan cuando hay pocos estados y acciones. El humanoide tiene 348 observaciones **continuas**: una tabla no cabe ni en el universo. Ahí entran las **redes neuronales**, que sustituyen la tabla por una función que aprende. De eso se encargan algoritmos como PPO y SAC, que veremos [con Stable-Baselines3](entrenar-con-sb3).

:::tip
Q-learning en un laberinto es el "hola mundo" del RL: pequeño, visual y sin cajas negras. Si entiendes esa línea de actualización, ya entiendes la idea que hay detrás de entrenar un humanoide.
:::
