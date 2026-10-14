---
sidebar_position: 6
title: Acciones
sidebar_custom_props:
  icon: /img/guias/iconos/ejemplos.svg
---

# Acciones

Una **acción** es la forma de pedirle a un nodo una **tarea larga**: girar hasta un ángulo, llevar el brazo a una posición, navegar hasta la cocina. A diferencia de un [servicio](./servicios-y-parametros), quien la pide recibe **avisos de progreso** mientras se ejecuta y puede **cancelarla** a medias.

| Parte | Sentido | Ejemplo |
|---|---|---|
| **Objetivo** (*goal*) | cliente → servidor | "mira hacia 90°" |
| **Progreso** (*feedback*) | servidor → cliente, varias veces | "faltan 40°" |
| **Resultado** (*result*) | servidor → cliente, al final | "he girado 90°" |

La navegación de Nav2 es una acción: le das un punto del mapa y te va diciendo cuánto le queda.

## Probarla desde la terminal

turtlesim trae una acción para girar la tortuga hasta un ángulo. Con `turtlesim_node` en marcha:

```bash
ros2 action list
```

```
/turtle1/rotate_absolute
```

Su tipo se ve igual que el de un mensaje:

```bash
ros2 interface show turtlesim/action/RotateAbsolute
```

```
# The desired heading in radians
float32 theta
---
# The angular displacement in radians to the starting position
float32 delta
---
# The remaining rotation in radians
float32 remaining
```

Tres bloques separados por `---`: el **objetivo**, el **resultado** y el **progreso**. Envía un objetivo:

```bash
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 3.14}" --feedback
```

```
Goal accepted with ID: 1eb307449799463a9feb5affdc1d38d7

Feedback:
    remaining: 3.140000104904175

Feedback:
    remaining: 3.124000072479248
...
```

La tortuga gira despacio y la terminal va mostrando cuánto le falta.

## Un cliente en Python

Crea `~/ros2_ws/src/mi_robot/mi_robot/girador.py`:

```python
import math
import rclpy
from rclpy.action import ActionClient
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from turtlesim.action import RotateAbsolute


class Girador(Node):

    def __init__(self):
        super().__init__('girador')
        self.cliente = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')

    def girar(self, angulo):
        self.get_logger().info('Esperando al servidor de la acción...')
        self.cliente.wait_for_server()

        objetivo = RotateAbsolute.Goal()
        objetivo.theta = angulo
        self.get_logger().info(f'Objetivo: mirar a {math.degrees(angulo):.0f}°')

        envio = self.cliente.send_goal_async(objetivo, feedback_callback=self.al_progresar)
        envio.add_done_callback(self.al_aceptar)

    def al_progresar(self, mensaje):
        restante = mensaje.feedback.remaining
        self.get_logger().info(f'Faltan {math.degrees(restante):.0f}°')

    def al_aceptar(self, futuro):
        manejador = futuro.result()
        if not manejador.accepted:
            self.get_logger().warn('El servidor ha rechazado el objetivo')
            rclpy.shutdown()
            return
        manejador.get_result_async().add_done_callback(self.al_terminar)

    def al_terminar(self, futuro):
        resultado = futuro.result().result
        self.get_logger().info(f'Hecho: ha girado {abs(math.degrees(resultado.delta)):.0f}°')
        rclpy.shutdown()


def main():
    rclpy.init()
    nodo = Girador()
    nodo.girar(math.pi / 2)        # mirar hacia arriba (90°)
    try:
        rclpy.spin(nodo)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        nodo.destroy_node()
        rclpy.try_shutdown()
```

Regístralo en `setup.py` (`'girador = mi_robot.girador:main',`), compila y pruébalo con turtlesim en marcha:

```bash
ros2 run mi_robot girador
```

```
[INFO] [girador]: Objetivo: mirar a 90°
[INFO] [girador]: Faltan 90°
[INFO] [girador]: Faltan 89°
...
[INFO] [girador]: Faltan 1°
[INFO] [girador]: Hecho: ha girado 90°
```

## Cómo funciona

Todo es **asíncrono**: el nodo no se queda esperando, sino que le dice a ROS 2 qué hacer cuando pase cada cosa.

1. `send_goal_async()` envía el objetivo y le pasa `al_progresar` para cada aviso de progreso
2. Cuando el servidor contesta si **acepta** el objetivo, se llama a `al_aceptar`
3. `al_aceptar` pide el resultado, y cuando llega se llama a `al_terminar`
4. `al_terminar` muestra el resultado y cierra el nodo

Los ángulos van en **radianes**, como en todo ROS 2: `math.pi / 2` son 90°.

:::tip
Mientras gira, pulsa **Ctrl+C** en la terminal del `ros2 action send_goal`: el objetivo se cancela y la tortuga se para donde esté. Poder cancelar es justo lo que distingue una acción de un servicio.
:::
