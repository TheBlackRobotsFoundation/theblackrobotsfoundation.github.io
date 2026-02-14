# Instalación

Guía completa para instalar el Rover desde cero.

## Requisitos

### Sistema Operativo
- Ubuntu 22.04 LTS
- ROS2 Humble

### Hardware Mínimo
- CPU: Quad-core ARM64 o x86_64
- RAM: 4GB mínimo, 8GB recomendado
- Almacenamiento: 32GB
- Puerto USB: 3+ disponibles

## Instalación de ROS2

Si aún no tienes ROS2 Humble instalado:

```bash
# Configurar repositorios
sudo apt update && sudo apt install curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Instalar ROS2 Humble
sudo apt update
sudo apt install ros-humble-desktop

# Source
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## Clonar el Repositorio

```bash
cd ~/Desktop
git clone https://github.com/TheBlackRobotsFoundation/Rover.git
cd Rover
```

## Instalación Automática

El script de setup instalará todas las dependencias automáticamente:

```bash
./scripts/setup.sh
```

Este script:
1. Verifica que ROS2 esté instalado
2. Instala herramientas de compilación (colcon, vcstool)
3. Instala dependencias de ROS2 (Nav2, Gazebo, etc.)
4. Instala dependencias Python (pyserial, pyyaml)
5. Configura permisos de puertos seriales
6. Configura udev rules para dispositivos

## Instalación Manual

Si prefieres instalar manualmente:

### Dependencias de Sistema

```bash
sudo apt update
sudo apt install -y \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    python3-pip \
    python3-serial \
    python3-yaml
```

### Dependencias de ROS2

```bash
sudo apt install -y \
    ros-humble-nav2-bringup \
    ros-humble-navigation2 \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-joint-state-publisher \
    ros-humble-robot-state-publisher \
    ros-humble-xacro \
    ros-humble-joy \
    ros-humble-teleop-twist-joy \
    ros-humble-rplidar-ros
```

### Dependencias Python

```bash
pip3 install --user pyserial pyyaml
```

### Rosdep

```bash
# Inicializar rosdep
sudo rosdep init
rosdep update

# Instalar dependencias del workspace
cd ~/Desktop/Rover
rosdep install --from-paths . --ignore-src -r -y
```

## Permisos de Puertos Seriales

```bash
# Agregar usuario al grupo dialout
sudo usermod -a -G dialout $USER

# IMPORTANTE: Cerrar sesión y volver a entrar
```

## Compilar

```bash
cd ~/Desktop/Rover
./scripts/build_all.sh
```

## Verificar Instalación

```bash
# Source del workspace
source ~/Desktop/Rover/rover_bringup/install/setup.bash

# Verificar que los paquetes estén disponibles
ros2 pkg list | grep rover

# Deberías ver:
# rover_msgs
# rover_interfaces
# roboclaw_driver
# ibus_driver
# ...
```

## Troubleshooting

### Error: ROS2 no encontrado

```bash
source /opt/ros/humble/setup.bash
```

### Error: Permisos denegados en puerto serial

```bash
sudo usermod -a -G dialout $USER
# Cerrar sesión y volver a entrar
```

### Error: Dependencias faltantes

```bash
rosdep install --from-paths . --ignore-src -r -y
```

## Próximos Pasos

- [Hardware Setup](hardware-setup.md): Conectar el hardware
- [Quick Start](quickstart.md): Primer uso del rover
