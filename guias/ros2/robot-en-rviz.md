---
sidebar_position: 11
title: Tu robot en RViz
sidebar_custom_props:
  icon: /img/guias/iconos/ejemplos.svg
---

# Tu robot en RViz

En la guía de [URDF](/guias/urdf/tu-primer-urdf) describiste un robot con una base y un brazo. Ahora lo vas a ver en **RViz** y a mover su brazo desde un nodo de ROS 2.

<img src="/img/guias/ros2/rviz-robot.png" alt="RViz mostrando el robot del URDF: la base gris, el brazo azul, la mano blanca y los ejes de TF" />

Hacen falta tres piezas:

| Pieza | Qué hace |
|---|---|
| **robot_state_publisher** | lee el URDF y publica la TF de cada pieza según el ángulo de los joints |
| **Un nodo que publica `/joint_states`** | dice en qué ángulo está cada joint |
| **RViz** | dibuja el modelo y sus frames |

## 1. El URDF, con una mano

El brazo del URDF es un cilindro que gira sobre sí mismo: al girar se ve igual. Para notar el movimiento, añade una **mano** en lo alto del brazo. Copia `mi_robot.urdf` a `~/ros2_ws/src/mi_robot/urdf/` y, justo antes de `</robot>`, añade:

```xml
<!-- Pieza 3: una mano en lo alto del brazo, para ver cómo gira -->
<link name="mano">
  <visual>
    <origin xyz="0.06 0 0"/>
    <geometry>
      <box size="0.12 0.04 0.04"/>
    </geometry>
    <material name="blanco">
      <color rgba="0.9 0.9 0.9 1"/>
    </material>
  </visual>
</link>

<joint name="brazo_a_mano" type="fixed">
  <parent link="brazo"/>
  <child link="mano"/>
  <origin xyz="0 0 0.5"/>
</joint>
```

Un joint `fixed` une la mano al brazo, a 50 cm de su base. Comprueba el árbol:

```bash
check_urdf mi_robot.urdf
```

```
root Link: base_link has 1 child(ren)
    child(1):  brazo
        child(1):  mano
```

## 2. Un nodo que mueve el brazo

Crea `mi_robot/mover_brazo.py`:

```python
import math
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from sensor_msgs.msg import JointState


class MoverBrazo(Node):

    def __init__(self):
        super().__init__('mover_brazo')
        self.pub = self.create_publisher(JointState, 'joint_states', 10)
        self.t = 0.0
        self.timer = self.create_timer(0.05, self.publicar)   # 20 veces por segundo

    def publicar(self):
        self.t += 0.05
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['base_a_brazo']                  # el joint del URDF
        msg.position = [1.5 * math.sin(self.t)]      # va y viene, en radianes
        self.pub.publish(msg)


def main():
    rclpy.init()
    nodo = MoverBrazo()
    try:
        rclpy.spin(nodo)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        nodo.destroy_node()
        rclpy.try_shutdown()
```

Publica en `/joint_states` el ángulo del joint `base_a_brazo`, oscilando entre −1,5 y 1,5 radianes. El nombre tiene que coincidir **exactamente** con el del URDF.

## 3. La configuración de RViz

Crea `~/ros2_ws/src/mi_robot/rviz/ver_robot.rviz`:

```yaml
Panels:
  - Class: rviz_common/Displays
    Name: Displays
Visualization Manager:
  Class: ""
  Displays:
    - Class: rviz_default_plugins/Grid
      Name: Grid
      Enabled: true
      Cell Size: 0.1
      Plane Cell Count: 20
      Color: 70; 70; 70
      Value: true
    - Class: rviz_default_plugins/RobotModel
      Name: RobotModel
      Enabled: true
      Description Source: Topic
      Description Topic:
        Value: /robot_description
      Value: true
    - Class: rviz_default_plugins/TF
      Name: TF
      Enabled: true
      Marker Scale: 0.6
      Show Names: false
      Value: true
  Enabled: true
  Global Options:
    Background Color: 12; 12; 12
    Fixed Frame: base_link
    Frame Rate: 30
  Name: root
  Tools:
    - Class: rviz_default_plugins/MoveCamera
  Value: true
  Views:
    Current:
      Class: rviz_default_plugins/Orbit
      Distance: 1.15
      Focal Point:
        X: 0
        Y: 0
        Z: 0.3
      Pitch: 0.45
      Yaw: 0.9
      Name: Current View
      Target Frame: <Fixed Frame>
      Value: Orbit (rviz)
Window Geometry:
  Width: 1280
  Height: 760
  X: 0
  Y: 0
```

Dice qué mostrar (la cuadrícula, el modelo del robot y TF), desde qué frame (`base_link`) y desde dónde mirar. No hace falta escribirlo a mano: cualquier configuración que montes en RViz se guarda con **File → Save Config As**.

## 4. Un launch para todo

Crea `launch/ver_robot.launch.py`:

```python
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    carpeta = get_package_share_directory('mi_robot')
    with open(os.path.join(carpeta, 'urdf', 'mi_robot.urdf')) as f:
        urdf = f.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': urdf}],
        ),
        Node(package='mi_robot', executable='mover_brazo'),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', os.path.join(carpeta, 'rviz', 'ver_robot.rviz')],
        ),
    ])
```

- `get_package_share_directory()` encuentra la carpeta donde se instaló el paquete
- El URDF se lee como texto y se le pasa a `robot_state_publisher` como el parámetro `robot_description`
- `-d` le dice a RViz qué configuración abrir

## 5. Instalar los archivos

En `setup.py`, añade las carpetas `urdf` y `rviz` a `data_files`, junto a la de `launch`:

```python
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/urdf', glob('urdf/*')),
        ('share/' + package_name + '/rviz', glob('rviz/*')),
```

Registra el nodo en `entry_points` (`'mover_brazo = mi_robot.mover_brazo:main',`) y añade en `package.xml`:

```xml
<exec_depend>robot_state_publisher</exec_depend>
<exec_depend>rviz2</exec_depend>
```

## 6. Lanzarlo

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
ros2 launch mi_robot ver_robot.launch.py
```

Se abre RViz con el robot, y el brazo gira a un lado y a otro con su mano. Los ejes de colores son los frames de TF de cada pieza.

:::note
`robot_state_publisher` puede avisar de que *el link raíz tiene inercia y KDL no lo admite*. Es solo un aviso: el robot se ve y se mueve igual. Si quieres quitarlo, añade un link vacío `base_footprint` como raíz, unido a `base_link` con un joint `fixed`.
:::

:::tip[Mover los joints con el ratón]
El paquete `joint_state_publisher_gui` abre una ventana con un control deslizante por joint: `sudo apt install ros-humble-joint-state-publisher-gui` y úsalo en lugar de `mover_brazo`. Es la forma más rápida de comprobar que todos los joints de un URDF giran hacia donde deben.
:::

## ¿Y ahora qué?

Con el URDF, TF y RViz funcionando, tienes la base de cualquier robot en ROS 2. El siguiente paso es simularlo con física (Gazebo o [MuJoCo](/guias/simulacion-rl/mujoco)) y, en un robot real, cambiar `mover_brazo` por el nodo que lee los encoders de sus motores, como hace el [Rover](/proyectos/rover-web).
