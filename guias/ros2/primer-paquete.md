---
sidebar_position: 4
title: Tu primer paquete
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Tu primer paquete

Vamos a escribir dos nodos en Python:

- **dibujante**: publica velocidades para que la tortuga dibuje círculos
- **vigilante**: escucha la posición de la tortuga y avisa cuando se acerca a una pared

## 1. Crear el workspace

Un **workspace** es la carpeta donde viven tus paquetes:

<img src="/img/guias/ros2/workspace.svg" alt="Estructura de un workspace de ROS 2: src con los paquetes y las carpetas build, install y log" />

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

## 2. Crear el paquete

```bash
ros2 pkg create --build-type ament_python mi_robot --dependencies rclpy geometry_msgs turtlesim
```

- `ament_python`: un paquete con nodos en Python
- `--dependencies`: lo que va a usar. `rclpy` es la librería de ROS 2 para Python; `geometry_msgs` trae el mensaje `Twist`; `turtlesim`, el mensaje `Pose`

## 3. El nodo dibujante

Crea el archivo `~/ros2_ws/src/mi_robot/mi_robot/dibujante.py`:

```python
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Dibujante(Node):

    def __init__(self):
        super().__init__('dibujante')
        self.publicador = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.publicar)   # 10 veces por segundo
        self.get_logger().info('Dibujante en marcha')

    def publicar(self):
        msg = Twist()
        msg.linear.x = 2.0     # avanza
        msg.angular.z = 1.0    # y gira a la vez: un círculo
        self.publicador.publish(msg)


def main():
    rclpy.init()
    nodo = Dibujante()
    try:
        rclpy.spin(nodo)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        nodo.destroy_node()
        rclpy.try_shutdown()
```

- Un nodo es una **clase** que hereda de `Node`. Su nombre en ROS 2 es el que le das a `super().__init__()`
- `create_publisher(tipo, topic, 10)` crea el publicador. El 10 es cuántos mensajes guarda si el receptor va con retraso
- `create_timer(0.1, función)` llama a `publicar()` cada 0,1 segundos
- `rclpy.spin(nodo)` mantiene el nodo vivo, atendiendo a sus timers y suscripciones, hasta que pulsas Ctrl+C

## 4. El nodo vigilante

Crea `~/ros2_ws/src/mi_robot/mi_robot/vigilante.py`:

```python
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from turtlesim.msg import Pose


class Vigilante(Node):

    def __init__(self):
        super().__init__('vigilante')
        self.suscriptor = self.create_subscription(Pose, '/turtle1/pose', self.al_recibir, 10)

    def al_recibir(self, pose):
        # la ventana de turtlesim mide 11 x 11
        distancia = min(pose.x, pose.y, 11.0 - pose.x, 11.0 - pose.y)
        if distancia < 1.0:
            self.get_logger().warn(f'¡Cerca de la pared! ({distancia:.2f})')


def main():
    rclpy.init()
    nodo = Vigilante()
    try:
        rclpy.spin(nodo)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        nodo.destroy_node()
        rclpy.try_shutdown()
```

`create_subscription()` llama a `al_recibir()` **cada vez que llega un mensaje**, con el mensaje como argumento. No hay que preguntar: ROS 2 avisa.

## 5. Registrar los nodos

Abre `~/ros2_ws/src/mi_robot/setup.py` y añade los dos nodos en `entry_points`:

```python
    entry_points={
        'console_scripts': [
            'dibujante = mi_robot.dibujante:main',
            'vigilante = mi_robot.vigilante:main',
        ],
    },
```

Cada línea dice: el ejecutable `dibujante` es la función `main` del archivo `mi_robot/dibujante.py`.

## 6. Compilar

Siempre desde la raíz del workspace:

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

- `colcon build` compila e instala todos los paquetes de `src/`
- `--symlink-install` enlaza tus archivos de Python en lugar de copiarlos: si cambias el código, no hace falta volver a compilar (solo al añadir archivos o tocar `setup.py`)
- `source install/setup.bash` le dice a esta terminal dónde están tus paquetes. Hazlo en **cada terminal nueva**

## 7. Probarlo

Tres terminales (en las dos últimas, `source ~/ros2_ws/install/setup.bash` primero):

```bash
ros2 run turtlesim turtlesim_node
```

```bash
ros2 run mi_robot dibujante
```

```bash
ros2 run mi_robot vigilante
```

La tortuga dibuja un círculo. Si la mueves con el teclado hacia una pared, el vigilante empieza a avisar:

```
[WARN] [vigilante]: ¡Cerca de la pared! (0.97)
```

<img src="/img/guias/ros2/turtlesim.png" alt="Ventana de turtlesim con la tortuga dibujando dos círculos" />

:::tip
Si `ros2 run` dice que no encuentra el paquete, te falta `source install/setup.bash` en esa terminal. Es el despiste más habitual en ROS 2.
:::

## ¿Y ahora qué?

Ahora la velocidad está escrita en el código. En [servicios y parámetros](./servicios-y-parametros) la harás ajustable y añadirás un botón de pausa.
