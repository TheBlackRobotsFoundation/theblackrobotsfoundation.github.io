---
sidebar_position: 1
title: ¿Qué es ROS 2?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es ROS 2?

**ROS** (*Robot Operating System*) es el conjunto de herramientas y librerías con el que se programan la mayoría de robots de investigación y muchos industriales. Su nombre engaña un poco: funciona **sobre** Linux, como una capa que organiza todos los programas de un robot y los hace hablar entre sí.

**ROS 2** es su versión actual, más rápida, segura y preparada para robots reales. Es open source y gratuita.

## La idea: piezas pequeñas que se hablan

Un robot hace muchas cosas a la vez: leer el LiDAR, calcular dónde está, decidir por dónde ir, mover los motores. En ROS 2, cada una es un programa pequeño e independiente llamado **nodo**, y los nodos se pasan información mediante **mensajes**.

<img src="/img/guias/ros2/grafo-robot.svg" alt="Grafo de un robot móvil: el LiDAR publica /scan, los motores publican /odom, la navegación publica /cmd_vel" />

- El nodo del **LiDAR** publica las distancias en `/scan`
- El nodo de los **motores** publica cuánto han girado las ruedas en `/odom`
- El nodo de **navegación** escucha los dos, decide y publica la velocidad en `/cmd_vel`
- El nodo de los motores escucha `/cmd_vel` y mueve las ruedas. Un **mando** puede publicar también en `/cmd_vel` para conducirlo a mano

Así funciona el [Rover](/proyectos/rover-web): cada pieza es un nodo, y cambiar el LiDAR o los motores solo implica cambiar su nodo.

## Por qué se usa tanto

- **No reinventas nada**: hay paquetes listos para cientos de sensores, para hacer mapas, navegar o mover brazos robóticos
- **Herramientas**: ver los datos en 3D, grabarlos y reproducirlos, dibujar gráficas, simular el robot
- **Python o C++**: cada nodo en el lenguaje que prefieras, y se entienden entre ellos
- **Red**: los nodos pueden estar en ordenadores distintos. El robot ejecuta los suyos y tú ves sus datos desde tu portátil, por Wi-Fi

## Las palabras que vas a oír

| Concepto | Qué es |
|---|---|
| **Nodo** | un programa que hace una tarea concreta |
| **Topic** | un canal con nombre por el que circulan mensajes, como `/cmd_vel` |
| **Mensaje** | el tipo de dato que viaja: una velocidad, una imagen, una distancia |
| **Servicio** | una pregunta con respuesta entre dos nodos |
| **Acción** | una tarea larga con progreso, como "navega hasta la cocina" |
| **Parámetro** | un ajuste de un nodo que se cambia sin tocar el código |
| **Paquete** | una carpeta con nodos relacionados, lista para compartir |
| **Workspace** | la carpeta donde guardas y compilas tus paquetes |

## Versiones (distribuciones)

Cada versión de ROS 2 va ligada a una versión de Ubuntu:

| Distribución | Ubuntu | Soporte hasta |
|---|---|---|
| **Humble Hawksbill** | 22.04 | mayo de 2027 |
| **Jazzy Jalisco** | 24.04 | mayo de 2029 |

Estas guías usan **Humble**, la versión del Rover y la que trae una Jetson con JetPack 6. Todo el código funciona igual en Jazzy, cambiando `humble` por `jazzy` en los comandos.

En las siguientes secciones verás [cómo instalarlo](./instalacion), [nodos y topics en la práctica](./nodos-y-topics) y [tu primer paquete](./primer-paquete).
