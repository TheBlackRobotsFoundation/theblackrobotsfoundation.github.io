---
sidebar_position: 3
title: Visual, colisión e inercia
sidebar_custom_props:
  icon: /img/guias/iconos/configuracion.svg
---

# Visual, colisión e inercia

Para darle cuerpo a un link se usan tres bloques: cómo **se ve**, cómo **choca** y cómo **pesa**. Un link completo lleva los tres.

<img src="/img/guias/urdf/link-capas.svg" alt="Las tres capas de un link: visual (forma y color), colisión (contorno de contacto) e inercial (masa y centro de masa)" width="640" />

```xml
<link name="base_link">
  <visual>
    <origin xyz="0 0 0.05" rpy="0 0 0"/>
    <geometry>
      <box size="2.5 1.5 0.1"/>
    </geometry>
    <material name="green">
      <color rgba="0.2 1 0.2 1"/>
    </material>
  </visual>

  <collision>
    <origin xyz="0 0 0.05" rpy="0 0 0"/>
    <geometry>
      <box size="2.5 1.5 0.1"/>
    </geometry>
  </collision>

  <inertial>
    <origin xyz="0 0 0.05" rpy="0 0 0"/>
    <mass value="12"/>
    <inertia ixx="2.26" ixy="0" ixz="0" iyy="6.26" iyz="0" izz="8.5"/>
  </inertial>
</link>
```

## Visual: cómo se ve

Es la forma que se dibuja en pantalla. Lleva una `<geometry>` y, opcionalmente, un `<material>` con su color (`rgba`, valores de 0 a 1).

Las geometrías básicas son `box` (caja), `cylinder` (cilindro) y `sphere` (esfera). Para formas complejas se usa `<mesh>` con un archivo `.stl` o `.dae`.

## Colisión: cómo choca

Es la forma que el simulador usa para detectar **contactos**. Suele ser idéntica a la visual, pero puedes simplificarla (una caja en vez de una malla con miles de caras) para que la simulación vaya más rápida.

## Inercial: cómo pesa

Le dice al simulador la **masa** y cómo está repartida (el tensor de inercia). Sin este bloque, la física no sabe cómo debe moverse la pieza.

- `<mass>` — la masa en kilogramos
- `<inertia>` — los seis valores del tensor de inercia

:::tip
El `<origin>` de cada bloque se mide **respecto al origen del link**. Truco habitual: subir el visual media altura de la caja (`z = 0.05` para una caja de `0.1`) para que el link "apoye" en su base y no quede medio hundido en el suelo.
:::
