---
sidebar_position: 2
title: Links y joints
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Links y joints

Todo robot en URDF se construye con **links** (piezas) unidos por **joints** (articulaciones). Vamos a ver cada uno.

## Links: las piezas

Un **link** es una pieza rígida del robot. Se declara con un nombre:

```xml
<link name="base_link"></link>
```

Un link puede estar vacío (solo un punto de referencia) o llevar geometría. En la página de [visual, colisión e inercia](visual-colision-inercia) veremos cómo darle forma.

## Joints: las uniones

Un **joint** conecta dos links: un `parent` (padre) y un `child` (hijo). Define **cómo** se mueve el hijo respecto al padre.

```xml
<joint name="hombro" type="revolute">
  <parent link="torso"/>
  <child link="brazo"/>
  <origin xyz="0 0 0.5" rpy="0 0 0"/>
  <axis xyz="0 1 0"/>
  <limit lower="-1.57" upper="1.57" effort="10" velocity="1.0"/>
</joint>
```

- `<parent>` / `<child>` — qué dos links une
- `<origin>` — dónde se coloca la articulación: `xyz` es la posición y `rpy` la rotación (roll, pitch, yaw) en radianes
- `<axis>` — el eje sobre el que gira o se desliza
- `<limit>` — hasta dónde puede moverse (`lower`/`upper`), su fuerza y velocidad máximas

## Tipos de joint más usados

| Tipo | Movimiento |
|---|---|
| `fixed` | Ninguno: pega dos links de forma rígida |
| `revolute` | Gira sobre un eje, con límites (un codo) |
| `continuous` | Gira sin límites (una rueda) |
| `prismatic` | Se desliza en línea recta (un cajón, un pistón) |

<img src="/img/guias/urdf/tipos-joint.svg" alt="Los cuatro tipos de joint: fixed (sin movimiento), revolute (gira con límites), continuous (gira sin fin) y prismatic (se desliza)" width="600" />

## El árbol del robot

Los joints encadenan links formando un **árbol**: un link raíz, y cada joint cuelga un nuevo hijo. Un humanoide, por ejemplo, parte del `torso` y va colgando brazos, piernas y cabeza.

:::tip
La regla de oro: cada link (salvo la raíz) tiene **un único joint padre**. Si dos joints apuntan al mismo hijo, el URDF no es válido.
:::
