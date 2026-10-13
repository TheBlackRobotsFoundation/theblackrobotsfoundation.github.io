---
sidebar_position: 7
title: Mensajes propios
sidebar_custom_props:
  icon: /img/guias/iconos/documentacion.svg
---

# Mensajes y servicios propios

ROS 2 trae cientos de tipos de mensaje (`Twist`, `Range`, `Image`, `LaserScan`...). Cuando ninguno encaja con lo que quieres enviar, creas el tuyo. Se definen en un **paquete de interfaces**, separado de los nodos, para que cualquier otro paquete pueda usarlos.

Vamos a crear:

- Un mensaje `Obstaculo` con la distancia y el ángulo de lo más cercano y si es peligroso
- Un servicio `CambiarUmbral` para ajustar a qué distancia se considera peligro

## 1. El paquete de interfaces

Las interfaces se compilan con CMake, así que el paquete es de tipo `ament_cmake`:

```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_cmake mi_robot_interfaces
cd mi_robot_interfaces
rm -rf include src
mkdir msg srv
```

## 2. Definir el mensaje y el servicio

`msg/Obstaculo.msg`:

```
# Lo más cercano que ve el robot
float32 distancia    # en metros
float32 angulo       # en radianes: 0 es delante, positivo a la izquierda
bool peligro         # true si está más cerca que el umbral
```

`srv/CambiarUmbral.srv`:

```
# Petición
float32 umbral       # nueva distancia de peligro, en metros
---
# Respuesta
bool aceptado
string mensaje
```

Cada línea es un campo: **tipo** y **nombre**. Los tipos básicos son `bool`, `int32`, `float32`, `float64`, `string`, y también otros mensajes (`geometry_msgs/Point`) o listas (`float32[]`). En un servicio, `---` separa la petición de la respuesta.

## 3. Generarlos

Sustituye `CMakeLists.txt` por:

```cmake
cmake_minimum_required(VERSION 3.8)
project(mi_robot_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Obstaculo.msg"
  "srv/CambiarUmbral.srv"
)

ament_package()
```

Y añade en `package.xml`, después de la línea de `ament_cmake`:

```xml
<buildtool_depend>rosidl_default_generators</buildtool_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```

Compila:

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
ros2 interface show mi_robot_interfaces/msg/Obstaculo
```

ROS 2 genera el código para Python y C++ a partir de esos archivos de texto.

:::note
Las **acciones** propias se definen igual, en una carpeta `action/` con archivos `.action` de tres bloques: objetivo, resultado y progreso, como el `RotateAbsolute` de la [sección anterior](./acciones).
:::

## 4. Usarlos en un nodo

En el paquete `mi_robot`, añade la dependencia en `package.xml`:

```xml
<depend>mi_robot_interfaces</depend>
```

Este nodo calcula la pared más cercana a la tortuga, publica un `Obstaculo` y ofrece el servicio para cambiar el umbral. Crea `mi_robot/detector.py`:

```python
import math
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from turtlesim.msg import Pose
from mi_robot_interfaces.msg import Obstaculo
from mi_robot_interfaces.srv import CambiarUmbral


class Detector(Node):

    def __init__(self):
        super().__init__('detector')
        self.umbral = 1.0
        self.pub = self.create_publisher(Obstaculo, 'obstaculo', 10)
        self.sub = self.create_subscription(Pose, '/turtle1/pose', self.al_recibir, 10)
        self.srv = self.create_service(CambiarUmbral, 'cambiar_umbral', self.al_cambiar)

    def al_recibir(self, pose):
        # distancia a cada pared de la ventana (11 x 11) y su dirección en el mundo
        paredes = [(pose.x, math.pi), (11.0 - pose.x, 0.0),
                   (pose.y, -math.pi / 2), (11.0 - pose.y, math.pi / 2)]
        distancia, direccion = min(paredes)
        angulo = math.atan2(math.sin(direccion - pose.theta), math.cos(direccion - pose.theta))

        msg = Obstaculo()
        msg.distancia = distancia
        msg.angulo = angulo
        msg.peligro = distancia < self.umbral
        self.pub.publish(msg)

    def al_cambiar(self, peticion, respuesta):
        if peticion.umbral <= 0.0:
            respuesta.aceptado = False
            respuesta.mensaje = 'El umbral tiene que ser positivo'
        else:
            self.umbral = peticion.umbral
            respuesta.aceptado = True
            respuesta.mensaje = f'Umbral cambiado a {self.umbral:.2f} m'
        return respuesta


def main():
    rclpy.init()
    nodo = Detector()
    try:
        rclpy.spin(nodo)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        nodo.destroy_node()
        rclpy.try_shutdown()
```

Se importan exactamente igual que los estándar: `from mi_robot_interfaces.msg import Obstaculo`. Regístralo en `setup.py` (`'detector = mi_robot.detector:main',`) y compila.

## 5. Probarlo

Con turtlesim y el detector en marcha:

```bash
ros2 topic echo --once /obstaculo
```

```
distancia: 5.455555438995361
angulo: -1.5520000457763672
peligro: false
---
```

Y cambia el umbral:

```bash
ros2 service call /cambiar_umbral mi_robot_interfaces/srv/CambiarUmbral "{umbral: 2.5}"
```

```
response:
mi_robot_interfaces.srv.CambiarUmbral_Response(aceptado=True, mensaje='Umbral cambiado a 2.50 m')
```

Con un valor negativo, el servidor lo rechaza y lo explica en `mensaje`: una respuesta bien diseñada dice **por qué**.

:::tip
Antes de crear un mensaje, busca si ya existe uno estándar: `sensor_msgs`, `geometry_msgs` y `nav_msgs` cubren casi todo lo de un robot móvil. Usar los estándar permite que tu nodo hable con RViz, Nav2 y cualquier otro paquete sin adaptadores.
:::
