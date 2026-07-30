---
sidebar_position: 2
title: Instalación
sidebar_custom_props:
  icon: /img/guias/iconos/instalacion.svg
---

# Instalación

Todo lo de esta sección funciona en Python. Necesitas **Python 3.10 o superior** y `pip`. Lo ideal es trabajar dentro de un **entorno virtual** para no ensuciar el sistema.

## 1. Crear un entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate    # en Windows: venv\Scripts\activate
```

## 2. Instalar MuJoCo (y lo que usaremos después)

```bash
pip install mujoco gymnasium[mujoco] stable-baselines3 imageio
```

- `mujoco` — el motor de física
- `gymnasium[mujoco]` — los entornos de robots listos para usar
- `stable-baselines3` — los algoritmos de aprendizaje por refuerzo
- `imageio` — para guardar vídeos de las simulaciones

## 3. Comprobar que funciona

Este mini-programa carga un robot humanoide de ejemplo y muestra cuántas articulaciones tiene:

```python
import gymnasium as gym

env = gym.make("Humanoid-v5")
print("Entorno cargado:", env.spec.id)
print("Articulaciones a controlar:", env.action_space.shape[0])
env.close()
```

Si imprime `Articulaciones a controlar: 17`, MuJoCo y Gymnasium están listos.

:::tip
¿Ves un error raro al importar, o un "segmentation fault"? Suele ser un choque entre librerías (por ejemplo, tener TensorFlow instalado a la vez). Trabajar en un entorno virtual limpio evita casi todos estos problemas.
:::
