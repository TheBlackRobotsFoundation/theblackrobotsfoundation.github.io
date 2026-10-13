---
sidebar_position: 10
sidebar_label: TF (coordenadas)
title: TF y sistemas de coordenadas
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# TF: los sistemas de coordenadas

Un robot está lleno de "puntos de vista". El LiDAR mide distancias **desde el LiDAR**; la cámara ve **desde la cámara**; las ruedas cuentan **desde el centro del robot**; el mapa está **en coordenadas del mundo**. Para juntarlo todo, ROS 2 necesita saber dónde está cada pieza respecto a las demás. De eso se encarga **TF**.

<img src="/img/guias/ros2/tf.svg" alt="Un robot visto desde arriba con sus ejes base_link y laser, y el árbol de TF: map, odom, base_link y los sensores" />

## Frames y transformaciones

- Cada pieza tiene su **frame**: un sistema de coordenadas con su origen y sus ejes. Por convenio, **X** apunta hacia delante (rojo), **Y** a la izquierda (verde) y **Z** hacia arriba (azul)
- Una **transformación** dice dónde está un frame respecto a otro: una **traslación** (x, y, z) y una **rotación**
- Los frames forman un **árbol**: cada uno tiene un único padre

Los nombres habituales en un robot móvil:

| Frame | Qué es | Quién lo publica |
|---|---|---|
| `map` | el mapa | la localización (AMCL, SLAM) |
| `odom` | donde empezó a moverse | la odometría ([encoders](/guias/sensores/encoders), IMU) |
| `base_link` | el centro del robot | — |
| `laser`, `imu`, `camara` | cada sensor | fijos: el URDF o `static_transform_publisher` |

Con este árbol, TF responde a preguntas como "¿dónde está, en el mapa, el punto que el LiDAR ve a 2 metros?" sin que tú hagas ninguna cuenta.

## Transformaciones fijas

Un sensor atornillado al robot no se mueve respecto a él. Su transformación es **estática** y se publica una sola vez:

```bash
ros2 run tf2_ros static_transform_publisher --x 0.2 --z 0.1 --frame-id base_link --child-frame-id laser
```

"El `laser` está 20 cm por delante y 10 cm por encima de `base_link`". Los valores que no indicas valen 0. Para girarlo, añade `--yaw`, `--pitch` o `--roll` en radianes.

## Transformaciones que se mueven

La posición del robot en el mundo cambia continuamente: su transformación se publica muchas veces por segundo. Este nodo convierte la posición de la tortuga en una transformación de `mundo` a `tortuga`. Crea `mi_robot/tf_tortuga.py`:

```python
import math
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose


class TfTortuga(Node):

    def __init__(self):
        super().__init__('tf_tortuga')
        self.difusor = TransformBroadcaster(self)
        self.sub = self.create_subscription(Pose, '/turtle1/pose', self.al_recibir, 10)

    def al_recibir(self, pose):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'mundo'         # el sistema "padre"
        t.child_frame_id = 'tortuga'        # el que se mueve
        t.transform.translation.x = pose.x
        t.transform.translation.y = pose.y
        # el giro alrededor de Z, escrito como cuaternión
        t.transform.rotation.z = math.sin(pose.theta / 2)
        t.transform.rotation.w = math.cos(pose.theta / 2)
        self.difusor.sendTransform(t)


def main():
    rclpy.init()
    nodo = TfTortuga()
    try:
        rclpy.spin(nodo)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        nodo.destroy_node()
        rclpy.try_shutdown()
```

Añade `<depend>tf2_ros</depend>` en `package.xml`, regístralo en `setup.py` (`'tf_tortuga = mi_robot.tf_tortuga:main',`) y compila.

### La rotación como cuaternión

TF guarda las rotaciones como **cuaterniones**: cuatro números (x, y, z, w) que evitan los problemas de los ángulos en 3D. Para un giro de θ alrededor de Z, la fórmula es sencilla: `z = sin(θ/2)` y `w = cos(θ/2)`. No hace falta entenderlos a fondo: las herramientas los traducen a grados.

## Consultar una transformación

Con turtlesim, el dibujante y `tf_tortuga` en marcha, y una cámara imaginaria montada sobre la tortuga:

```bash
ros2 run tf2_ros static_transform_publisher --x 0.2 --z 0.1 --frame-id tortuga --child-frame-id camara
```

Pregunta dónde está la cámara en el mundo:

```bash
ros2 run tf2_ros tf2_echo mundo camara
```

```
- Translation: [4.033, 7.517, 0.100]
- Rotation: in RPY (degree) [0.000, -0.000, 159.787]
```

TF ha encadenado `mundo → tortuga → camara` y te da la posición de la cámara en el mundo, actualizada mientras la tortuga se mueve.

## Ver el árbol

```bash
ros2 run tf2_tools view_frames
```

Escucha unos segundos y genera un PDF con el árbol de frames, quién publica cada uno y a qué frecuencia. Y en [RViz](./robot-en-rviz), la visualización **TF** dibuja los ejes de cada frame en 3D.

:::tip
La mayoría de errores de "no encuentro la transformación" vienen de un frame mal escrito o de un eslabón que nadie publica. `view_frames` te enseña en un vistazo qué falta.
:::
