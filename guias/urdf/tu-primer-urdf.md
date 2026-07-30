---
sidebar_position: 4
title: Tu primer URDF
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Tu primer URDF

Vamos a construir un robot completo desde cero: una **base fija** con un **brazo que gira**. Solo dos links y un joint, pero es un URDF válido y funcional.

## El robot que vamos a describir

- Un `base_link`: una caja plana que hace de soporte
- Un `brazo`: un cilindro vertical
- Un joint `revolute` que deja al brazo girar sobre la base

## El archivo completo

Guárdalo como `mi_robot.urdf`:

```xml
<?xml version="1.0"?>
<robot name="mi_robot">

  <!-- Pieza 1: la base, una caja plana -->
  <link name="base_link">
    <visual>
      <origin xyz="0 0 0.05"/>
      <geometry>
        <box size="0.4 0.4 0.1"/>
      </geometry>
      <material name="gris">
        <color rgba="0.5 0.5 0.53 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 0.05"/>
      <geometry>
        <box size="0.4 0.4 0.1"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="2"/>
      <inertia ixx="0.03" ixy="0" ixz="0" iyy="0.03" iyz="0" izz="0.05"/>
    </inertial>
  </link>

  <!-- Pieza 2: el brazo, un cilindro vertical -->
  <link name="brazo">
    <visual>
      <origin xyz="0 0 0.25"/>
      <geometry>
        <cylinder radius="0.03" length="0.5"/>
      </geometry>
      <material name="azul">
        <color rgba="0.42 0.55 0.7 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 0.25"/>
      <geometry>
        <cylinder radius="0.03" length="0.5"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="0.5"/>
      <inertia ixx="0.01" ixy="0" ixz="0" iyy="0.01" iyz="0" izz="0.001"/>
    </inertial>
  </link>

  <!-- La articulación: el brazo gira sobre la base -->
  <joint name="base_a_brazo" type="revolute">
    <parent link="base_link"/>
    <child link="brazo"/>
    <origin xyz="0 0 0.1"/>
    <axis xyz="0 0 1"/>
    <limit lower="-3.14" upper="3.14" effort="5" velocity="1.0"/>
  </joint>

</robot>
```

## Leyéndolo de arriba abajo

1. `<robot name="mi_robot">` abre la descripción y le pone nombre
2. El `base_link` es una caja de 40×40×10 cm, gris, apoyada en el suelo
3. El `brazo` es un cilindro de 3 cm de radio y 50 cm de alto, azul
4. El joint `base_a_brazo` cuelga el brazo de la base, 10 cm por encima (`origin z=0.1`), y le deja **girar sobre el eje Z** (`axis 0 0 1`) media vuelta a cada lado (`limit ±3.14`)

## Comprobar que es válido

La herramienta `check_urdf` te dice si el árbol está bien formado:

```bash
check_urdf mi_robot.urdf
```

Si todo va bien, imprime la jerarquía: `base_link` → `brazo`.

## Así se ve

Al cargar el robot en un visor 3D, la base gris y el brazo azul aparecen tal cual los describimos:

<img src="/img/guias/urdf/mi-robot-render.png" alt="El robot base + brazo renderizado en 3D: una base gris plana y un brazo cilíndrico azul vertical" width="560" />

*El mismo robot del código, renderizado en 3D: la base y el brazo que acabamos de describir.*

:::tip
¿El brazo aparece medio hundido en la base? Ajusta el `origin` del joint (la altura a la que cuelga) o el `origin` del visual del brazo. En URDF, colocar bien los orígenes es la mitad del trabajo.
:::
