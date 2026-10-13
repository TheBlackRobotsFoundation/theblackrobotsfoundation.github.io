---
sidebar_position: 12
title: ROS 2 y Arduino
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# ROS 2 y Arduino

El Arduino lee sensores y mueve motores; ROS 2 corre en la [Raspberry Pi](/guias/raspberry) o la [Jetson](/guias/jetson). Para unirlos se escribe un **nodo puente**: lee el puerto serie y lo publica en topics, y escucha topics y los manda por el puerto serie.

<img src="/img/guias/ros2/arduino-ros.svg" alt="Arduino conectado por USB a un nodo puente de ROS 2 que publica /distancia" />

Este nodo hace dos cosas, como el de cualquier robot con ruedas:

- Publica en **`/distancia`** lo que mide el sensor de ultrasonidos del Arduino
- Escucha **`/cmd_vel`** y lo convierte en la velocidad de cada motor

## El Arduino

Usa el mismo programa de [Raspberry Pi y Arduino](/guias/raspberry/raspberry-y-arduino#el-programa-del-arduino): envía `D 42.5` con la distancia y recibe `M izquierdo derecho` con la velocidad de los motores. Cárgalo y conecta el Arduino por USB.

## El nodo puente

Añade a tu paquete `mi_robot` las dependencias en `package.xml`:

```xml
<depend>sensor_msgs</depend>
<exec_depend>python3-serial</exec_depend>
```

Crea `~/ros2_ws/src/mi_robot/mi_robot/puente_arduino.py`:

```python
import serial
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist


class PuenteArduino(Node):

    def __init__(self):
        super().__init__('puente_arduino')
        self.declare_parameter('puerto', '/dev/ttyACM0')
        self.declare_parameter('baudios', 115200)
        self.declare_parameter('velocidad_max', 0.5)   # m/s que equivalen a PWM 255
        self.declare_parameter('separacion_ruedas', 0.15)   # m

        puerto = self.get_parameter('puerto').value
        baudios = self.get_parameter('baudios').value
        self.serie = serial.Serial(puerto, baudios, timeout=0.05)

        self.pub_distancia = self.create_publisher(Range, 'distancia', 10)
        self.sub_cmd = self.create_subscription(Twist, 'cmd_vel', self.al_recibir_cmd, 10)
        self.timer = self.create_timer(0.02, self.leer_serie)
        self.get_logger().info(f'Conectado a {puerto} a {baudios} baudios')

    def leer_serie(self):
        try:
            while self.serie.in_waiting:
                linea = self.serie.readline().decode(errors='ignore').strip()
                if linea.startswith('D '):
                    try:
                        cm = float(linea[2:])
                    except ValueError:
                        continue
                    self.publicar_distancia(cm / 100.0)   # ROS trabaja en metros
        except (OSError, serial.SerialException):
            self.get_logger().error('Se ha perdido la conexión con el Arduino')
            self.timer.cancel()

    def publicar_distancia(self, metros):
        msg = Range()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'ultrasonidos'
        msg.radiation_type = Range.ULTRASOUND
        msg.field_of_view = 0.26   # unos 15 grados, en radianes
        msg.min_range = 0.02
        msg.max_range = 4.0
        msg.range = metros
        self.pub_distancia.publish(msg)

    def al_recibir_cmd(self, cmd):
        v = cmd.linear.x                     # avance, en m/s
        w = cmd.angular.z                    # giro, en rad/s
        b = self.get_parameter('separacion_ruedas').value
        vmax = self.get_parameter('velocidad_max').value
        izq = (v - w * b / 2) / vmax * 255
        der = (v + w * b / 2) / vmax * 255
        izq = int(max(-255, min(255, izq)))
        der = int(max(-255, min(255, der)))
        try:
            self.serie.write(f'M {izq} {der}\n'.encode())
        except (OSError, serial.SerialException):
            self.get_logger().error('No se puede enviar la orden al Arduino')


def main():
    rclpy.init()
    nodo = PuenteArduino()
    try:
        rclpy.spin(nodo)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        nodo.destroy_node()
        rclpy.try_shutdown()
```

Y regístralo en `setup.py`, junto a los otros:

```python
            'puente_arduino = mi_robot.puente_arduino:main',
```

## Cómo funciona

- **`sensor_msgs/Range`** es el mensaje estándar para sensores de distancia de un solo haz. Además de la distancia, lleva el tipo de sensor, su ángulo y su rango. ROS 2 trabaja siempre en **metros** y **radianes**
- **De `/cmd_vel` a dos motores**: un robot de dos ruedas que avanza a `v` y gira a `w` necesita que la rueda izquierda vaya a `v − w·b/2` y la derecha a `v + w·b/2`, donde `b` es la separación entre ruedas. Es la cinemática de un **robot diferencial**
- **Parámetros**: el puerto, la separación de las ruedas y la velocidad máxima se ajustan sin tocar el código

## Probarlo

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
ros2 run mi_robot puente_arduino --ros-args -p puerto:=/dev/ttyACM0
```

En otra terminal, mira las distancias:

```bash
ros2 topic echo /distancia
```

Y conduce el robot con el teclado (con las **ruedas en el aire** la primera vez):

```bash
sudo apt install ros-humble-teleop-twist-keyboard
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Las teclas `i`, `j`, `l` y `,` mueven el robot y `k` lo para. **Mantén pulsada** la tecla para que siga moviéndose: si dejan de llegar órdenes, el Arduino lo detiene a los 500 ms gracias a su parada de seguridad.

:::tip
Si al pulsar `j` el robot gira a la derecha, el motor izquierdo y el derecho están intercambiados: cambia los cables de OUT1/OUT2 por los de OUT3/OUT4 en el driver. Si va hacia atrás al pulsar `i`, invierte los dos cables de cada motor.
:::

## ¿Y ahora qué?

Con `/cmd_vel` funcionando, tu robot habla el mismo idioma que cualquier robot de ROS 2. El siguiente paso es darle odometría con [encoders](/guias/sensores/encoders), un [LiDAR](/guias/sensores/lidar) y dejar que **Nav2** lo lleve solo por un mapa, como hace el [Rover](/proyectos/rover-web).

:::note[micro-ROS]
Las placas más potentes que el UNO (ESP32, Raspberry Pi Pico, Arduino Portenta) pueden ejecutar **micro-ROS**: el microcontrolador se convierte en un nodo de ROS 2 más, sin puente. Para un Arduino UNO, el puente por puerto serie es la opción adecuada.
:::
