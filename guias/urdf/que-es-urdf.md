---
sidebar_position: 1
title: ¿Qué es un URDF?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es un URDF?

Un **URDF** (*Unified Robot Description Format*) es un archivo de texto en formato **XML** que describe un robot: de qué piezas está hecho, cómo se conectan entre sí y cómo se mueven.

Es la forma estándar de decirle a un ordenador "así es mi robot" sin que el robot exista físicamente. Con ese archivo, un programa puede dibujarlo, simularlo o planificar sus movimientos.

## ¿Para qué sirve?

- **Visualizarlo** en herramientas como RViz antes de construirlo
- **Simularlo** en Gazebo, MuJoCo o Isaac para probar sin arriesgar hardware
- **Controlarlo** con ROS, que usa el URDF para saber dónde está cada articulación
- **Compartirlo**: al ser un archivo de texto, cualquiera puede leerlo y reutilizarlo

## Las dos piezas de todo URDF

Un robot en URDF se construye con solo dos tipos de elementos:

- **Links** — las piezas rígidas: un brazo, una rueda, el torso, un dedo
- **Joints** — las uniones entre piezas: definen cómo se mueve un link respecto a otro

Un robot no es más que una cadena de **links** enlazados por **joints**. Empezamos por ahí en la siguiente página.

<img src="/img/guias/urdf/arbol-robot.svg" alt="Árbol de un robot: un torso raíz del que cuelgan links (cabeza, brazo, pierna...) unidos por joints" width="620" />

*Un robot en URDF es un árbol: un link raíz del que cuelgan los demás, cada uno unido por un joint.*

:::tip
El URDF describe **la forma y la estructura** del robot, no su comportamiento. La lógica (qué hace el robot) va aparte, en tu código de control.
:::
