---
sidebar_position: 5
title: Simulation
---

# rover_simulation

Workspace para simulación del rover en Gazebo.

## Paquetes

### rover_description
URDF y modelo del rover.

**Contenido:**
- `urdf/rover.urdf.xacro`: Descripción completa del robot
- `meshes/`: Modelos 3D (STL/DAE)
- `config/`: Configuración de joint_state_publisher, etc.
- `launch/`: Launch para visualización en RViz

**Parámetros del robot:**
```xml
<xacro:property name="wheel_radius" value="0.075"/>
<xacro:property name="wheelbase" value="0.180"/>
<xacro:property name="track_width" value="0.250"/>
<xacro:property name="chassis_length" value="0.300"/>
<xacro:property name="chassis_width" value="0.250"/>
<xacro:property name="chassis_height" value="0.100"/>
```

### rover_gazebo
Configuración de Gazebo.

**Contenido:**
- `launch/`: Launch files para simulación
- `worlds/`: Mundos de Gazebo
- `models/`: Modelos de entorno

**Plugins incluidos:**
- Differential drive controller
- LIDAR sensor
- IMU sensor
- Camera
- GPS

## Compilación

```bash
cd rover_simulation
colcon build --symlink-install
source install/setup.bash
```

## Dependencias

- rover_core
- gazebo_ros
- xacro
- urdf

## Uso

```bash
# Visualizar en RViz
ros2 launch rover_description display.launch.py

# Simulación en Gazebo (vacío)
ros2 launch rover_gazebo gazebo.launch.py

# Simulación con mundo
ros2 launch rover_gazebo gazebo.launch.py world:=warehouse

# Gazebo + Nav2
ros2 launch rover_gazebo navigation_sim.launch.py
```

## Estructura URDF

El robot está modelado con:
- `base_link`: Centro del chasis
- `base_footprint`: Proyección en el suelo
- 4x `wheel_link`: Ruedas (FL, FR, RL, RR)
- `lidar_link`: Sensor LIDAR
- `imu_link`: IMU
- `camera_link`: Cámara (opcional)

