---
sidebar_position: 3
title: Nodos y topics
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Nodos y topics en la práctica

La mejor forma de entender ROS 2 es tocarlo. **turtlesim** es un simulador mínimo: una tortuga que se mueve por una ventana y que se controla exactamente igual que un robot de verdad, con mensajes de velocidad.

## 1. Arrancar la tortuga

```bash
ros2 run turtlesim turtlesim_node
```

`ros2 run` arranca un nodo: primero el **paquete** (`turtlesim`) y luego el **ejecutable** (`turtlesim_node`). Se abre una ventana con la tortuga en el centro.

## 2. Moverla con el teclado

En otra terminal:

```bash
ros2 run turtlesim turtle_teleop_key
```

Con esa terminal seleccionada, las **flechas** mueven la tortuga. Hay dos nodos en marcha: uno lee el teclado y publica velocidades; el otro las recibe y mueve la tortuga.

## 3. Ver qué está pasando

Abre una tercera terminal y pregunta a ROS 2:

```bash
ros2 node list
```

```
/teleop_turtle
/turtlesim
```

```bash
ros2 topic list
```

```
/parameter_events
/rosout
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```

- `/turtle1/cmd_vel`: las velocidades que manda el teclado
- `/turtle1/pose`: la posición de la tortuga, que publica el simulador

## 4. Escuchar un topic

```bash
ros2 topic echo /turtle1/pose
```

```
x: 5.544444561004639
y: 5.544444561004639
theta: 0.0
linear_velocity: 0.0
angular_velocity: 0.0
---
```

Mueve la tortuga y verás cambiar los números. **Ctrl+C** para parar.

## 5. El tipo de mensaje

Cada topic transporta un tipo de mensaje concreto:

```bash
ros2 topic info /turtle1/cmd_vel
ros2 interface show geometry_msgs/msg/Twist
```

```
Vector3  linear
	float64 x
	float64 y
	float64 z
Vector3  angular
	float64 x
	float64 y
	float64 z
```

`Twist` es **el** mensaje de velocidad de ROS 2: `linear.x` es la velocidad hacia delante y `angular.z`, la velocidad de giro. Es el mismo que usan el Rover, los TurtleBot y casi cualquier robot con ruedas.

## 6. Publicar tú mismo

Sin teclado, escribiendo el mensaje a mano:

```bash
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}"
```

La tortuga describe círculos: recibe un mensaje por segundo (`--rate 1`). Con `--once` en lugar de `--rate 1`, envía uno solo.

## 7. Ver el grafo

```bash
rqt_graph
```

Dibuja los nodos y los topics que los unen. Es la forma más rápida de entender un sistema que no conoces. Con tus propios nodos, el de la siguiente sección, se ve así:

<img src="/img/guias/ros2/grafo-turtlesim.svg" alt="Grafo: el nodo dibujante publica /turtle1/cmd_vel, turtlesim lo recibe y publica /turtle1/pose, que escucha el vigilante" />

## Los comandos de un vistazo

| Comando | Qué hace |
|---|---|
| `ros2 run paquete ejecutable` | arranca un nodo |
| `ros2 node list` | lista los nodos en marcha |
| `ros2 topic list` | lista los topics |
| `ros2 topic echo /topic` | muestra los mensajes de un topic |
| `ros2 topic hz /topic` | cuántos mensajes por segundo llegan |
| `ros2 topic pub /topic tipo "datos"` | publica un mensaje |
| `ros2 interface show tipo` | muestra los campos de un mensaje |

Ahora que sabes usarlos, toca escribir [tus propios nodos](./primer-paquete).
