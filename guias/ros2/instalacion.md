---
sidebar_position: 2
title: Instalación
sidebar_custom_props:
  icon: /img/guias/iconos/instalacion.svg
---

# Instalación de ROS 2 Humble

ROS 2 Humble se instala en **Ubuntu 22.04**, en un ordenador, una [Raspberry Pi](/guias/raspberry/instalacion) o una [Jetson](/guias/jetson/instalacion). Los pasos son los mismos en los tres.

:::tip
¿Usas Windows o Mac? Lo más cómodo es instalar Ubuntu 22.04 en una máquina virtual o, en Windows, usar **WSL** (Ubuntu dentro de Windows). Todo lo de estas guías funciona así.
:::

## 1. Preparar el sistema

Comprueba que el idioma del sistema usa UTF-8 (en una instalación normal de Ubuntu, ya es así):

```bash
locale
```

Activa el repositorio *universe* de Ubuntu e instala `curl`:

```bash
sudo apt install -y software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install -y curl
```

## 2. Añadir el repositorio de ROS 2

El paquete `ros2-apt-source` configura el repositorio oficial y su clave:

```bash
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo $VERSION_CODENAME)_all.deb"
sudo dpkg -i /tmp/ros2-apt-source.deb
```

## 3. Instalar ROS 2

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y ros-humble-desktop ros-dev-tools
```

| Paquete | Qué trae |
|---|---|
| `ros-humble-desktop` | ROS 2 completo, con RViz, rqt y turtlesim. Para tu ordenador |
| `ros-humble-ros-base` | solo lo esencial, sin herramientas gráficas. Para el robot (Raspberry o Jetson sin pantalla) |
| `ros-dev-tools` | `colcon` y las herramientas para compilar tus paquetes |

La descarga ocupa unos 2 – 3 GB y tarda un rato.

## 4. Cargar ROS 2 en la terminal

Cada terminal nueva necesita saber dónde está ROS 2:

```bash
source /opt/ros/humble/setup.bash
```

Para no escribirlo siempre, añádelo al final de tu `~/.bashrc`, que se ejecuta al abrir cada terminal:

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

## 5. Comprobar que funciona

Abre **dos terminales**. En la primera, un nodo que publica mensajes:

```bash
ros2 run demo_nodes_cpp talker
```

En la segunda, un nodo que los escucha:

```bash
ros2 run demo_nodes_py listener
```

Si en la segunda aparece `I heard: [Hello World: 1]`, `2`, `3`... ROS 2 funciona. Un nodo en C++ y otro en Python se están hablando. Para pararlos, **Ctrl+C** en cada terminal.

:::note
Estas instrucciones siguen la [guía oficial de instalación](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html). Si algún paso cambia, la referencia es esa página.
:::

## Jazzy en Ubuntu 24.04

En una **Raspberry Pi 5** se usa Ubuntu 24.04 con **ROS 2 Jazzy**. Los pasos son idénticos cambiando `humble` por `jazzy` en los comandos: `ros-jazzy-desktop`, `/opt/ros/jazzy/setup.bash`...
