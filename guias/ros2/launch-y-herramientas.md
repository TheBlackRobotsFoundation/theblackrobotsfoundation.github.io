---
sidebar_position: 6
title: Launch y herramientas
sidebar_custom_props:
  icon: /img/guias/iconos/requisitos.svg
---

# Launch y herramientas

Un robot real tiene decenas de nodos. Abrir una terminal para cada uno no es práctico: para eso están los **archivos de launch**. Y para entender lo que pasa dentro, ROS 2 trae herramientas para ver, grabar y reproducir datos.

## Archivos de launch

Un archivo de launch arranca varios nodos a la vez, cada uno con sus parámetros. Crea la carpeta `launch` en tu paquete y dentro el archivo `~/ros2_ws/src/mi_robot/launch/dibujo.launch.py`:

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='turtlesim', executable='turtlesim_node'),
        Node(
            package='mi_robot',
            executable='dibujante',
            parameters=[{'velocidad': 2.0, 'giro': 1.0}],
        ),
        Node(package='mi_robot', executable='vigilante', output='screen'),
    ])
```

Para que `colcon` lo instale, añade la carpeta en `setup.py`. Arriba del todo, importa `glob`:

```python
from glob import glob
```

Y en `data_files`, una línea más:

```python
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
```

Compila y lánzalo:

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
ros2 launch mi_robot dibujo.launch.py
```

Los tres nodos arrancan con un solo comando, y **Ctrl+C** los para todos. El [Rover](/proyectos/rover-web) arranca así todo el robot.

## Grabar y reproducir: rosbag

`ros2 bag` graba los mensajes de los topics que elijas y los reproduce después, exactamente igual. Sirve para probar algoritmos sin tener el robot delante, o para repetir siempre la misma situación.

```bash
ros2 bag record /turtle1/cmd_vel -o paseo
```

Mueve la tortuga con el teclado unos segundos y para con **Ctrl+C**. Mira lo que has grabado:

```bash
ros2 bag info paseo
```

```
Duration:          5.945096849s
Messages:          140
Topic information: Topic: /turtle1/cmd_vel | Type: geometry_msgs/msg/Twist | Count: 140
```

Borra el dibujo y reprodúcelo:

```bash
ros2 service call /clear std_srvs/srv/Empty
ros2 bag play paseo
```

La tortuga repite exactamente el mismo recorrido.

## rqt: herramientas gráficas

```bash
rqt
```

Abre una ventana en la que añades complementos desde el menú **Plugins**:

| Complemento | Para qué |
|---|---|
| **Node Graph** | el grafo de nodos y topics, como `rqt_graph` |
| **Plot** | gráficas en directo de cualquier número, por ejemplo `/turtle1/pose/x` |
| **Topic Monitor** | todos los topics con su frecuencia y su último mensaje |
| **Console** | los mensajes de log de todos los nodos, filtrables |

## RViz: el robot en 3D

**RViz** muestra en 3D lo que "ve" el robot: el modelo del robot, las medidas del [LiDAR](/guias/sensores/lidar/codigo-basico), el mapa, la ruta planificada...

```bash
rviz2
```

Con **Add** se añaden visualizaciones. En la guía de [URDF](/guias/urdf) lo usarás para ver el modelo de tu propio robot.

## Varios ordenadores en la misma red

Los nodos de ROS 2 se encuentran solos en la red local: si el robot y tu portátil están en la misma Wi-Fi, desde el portátil ves los topics del robot con `ros2 topic list` y abres RViz con sus datos.

Para separar varios robots en la misma red, cada uno usa un número distinto:

```bash
export ROS_DOMAIN_ID=7
```

Solo se ven entre sí los ordenadores con el mismo `ROS_DOMAIN_ID` (de 0 a 101). Añádelo a tu `~/.bashrc` para que sea permanente.

:::tip
Si el portátil no ve los topics del robot, revisa que los dos tienen el mismo `ROS_DOMAIN_ID` y que el router no bloquea el tráfico entre dispositivos (algunas redes de invitados lo hacen).
:::
