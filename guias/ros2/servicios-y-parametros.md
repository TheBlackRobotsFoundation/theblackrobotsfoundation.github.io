---
sidebar_position: 5
title: Servicios y parámetros
sidebar_custom_props:
  icon: /img/guias/iconos/configuracion.svg
---

# Servicios y parámetros

Los topics son un flujo continuo de mensajes. Para lo demás, ROS 2 tiene otras dos herramientas: **servicios** para preguntar y recibir respuesta, y **parámetros** para ajustar un nodo sin tocar su código.

<img src="/img/guias/ros2/comunicacion.svg" alt="Topic, servicio y acción: un flujo continuo, una pregunta con respuesta y una tarea larga con progreso" />

| | Topic | Servicio | Acción |
|---|---|---|---|
| Cómo funciona | uno publica, cualquiera escucha | pregunta y respuesta | objetivo, progreso y resultado |
| Cuándo | datos continuos: sensores, velocidades | órdenes puntuales: pausar, reiniciar | tareas largas: navegar a un punto |
| Ejemplo | `/scan`, `/cmd_vel` | `/pausa` | `navigate_to_pose` de Nav2 |

## Probar servicios de turtlesim

Con `turtlesim_node` en marcha:

```bash
ros2 service list
```

Entre otros, verás `/clear`, `/reset`, `/spawn` y `/turtle1/teleport_absolute`. Llámalos:

```bash
ros2 service call /clear std_srvs/srv/Empty
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2.0, y: 2.0, theta: 0.0, name: 'tortuga2'}"
```

El primero borra el dibujo; el segundo crea una segunda tortuga.

## El dibujante con parámetros y pausa

Vamos a mejorar el nodo de la [sección anterior](./primer-paquete) con:

- Dos **parámetros**, `velocidad` y `giro`, para cambiar el dibujo en marcha
- Un **servicio** `/pausa`: le pides `true` y se para; `false`, y continúa

Primero, añade la dependencia en `package.xml`, junto a las otras líneas `<depend>`:

```xml
<depend>std_srvs</depend>
```

Y sustituye `dibujante.py` por esta versión:

```python
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import SetBool


class Dibujante(Node):

    def __init__(self):
        super().__init__('dibujante')
        self.declare_parameter('velocidad', 2.0)
        self.declare_parameter('giro', 1.0)
        self.pausado = False

        self.publicador = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.servicio = self.create_service(SetBool, 'pausa', self.al_pedir_pausa)
        self.timer = self.create_timer(0.1, self.publicar)   # 10 veces por segundo
        self.get_logger().info('Dibujante en marcha')

    def publicar(self):
        msg = Twist()
        if not self.pausado:
            msg.linear.x = self.get_parameter('velocidad').value
            msg.angular.z = self.get_parameter('giro').value
        self.publicador.publish(msg)

    def al_pedir_pausa(self, peticion, respuesta):
        self.pausado = peticion.data
        respuesta.success = True
        respuesta.message = 'En pausa' if self.pausado else 'Dibujando'
        self.get_logger().info(respuesta.message)
        return respuesta


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

- `declare_parameter(nombre, valor)` crea el parámetro con su valor por defecto, y `get_parameter(nombre).value` lo lee. Como se lee en cada mensaje, un cambio se nota al instante
- `create_service(tipo, nombre, función)` crea el servicio. La función recibe la **petición**, rellena la **respuesta** y la devuelve
- `SetBool` es un tipo de servicio estándar: la petición lleva un `data` (verdadero o falso) y la respuesta, `success` y `message`

Como has tocado `package.xml`, vuelve a compilar:

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

## Usarlo

Con `turtlesim_node` y el nuevo `dibujante` en marcha, desde otra terminal:

```bash
ros2 param list /dibujante
ros2 param set /dibujante giro 2.0
```

La tortuga empieza a dibujar un círculo más pequeño: con más giro y la misma velocidad, la curva se cierra. Y para pausarla:

```bash
ros2 service call /pausa std_srvs/srv/SetBool "{data: true}"
```

```
response:
std_srvs.srv.SetBool_Response(success=True, message='En pausa')
```

Con `{data: false}` vuelve a dibujar.

:::tip
Los parámetros también se pueden dar al arrancar el nodo: `ros2 run mi_robot dibujante --ros-args -p velocidad:=1.0 -p giro:=0.5`. Y en un archivo de launch, como verás en la [siguiente sección](./launch-y-herramientas).
:::
