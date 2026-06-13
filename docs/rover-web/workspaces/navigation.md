---
sidebar_position: 4
title: Navigation
---

# rover_navigation

Workspace para navegación autónoma con Nav2 y localización.

## Paquetes

### rover_nav2_bringup
Configuración y launch files para Nav2.

**Contenido:**
- `launch/`: Launch files para Nav2
- `params/`: Parámetros de Nav2 personalizados para el rover
  - `nav2_params.yaml`: Configuración principal
  - `costmap_common.yaml`: Footprint y capas de costmap
  - `planner_server.yaml`: Configuración del planificador
  - `controller_server.yaml`: Configuración del controlador
- `maps/`: Mapas guardados

**Parámetros clave:**
```yaml
robot_radius: 0.15  # Basado en track_width/2
footprint: [[0.15, 0.125], [0.15, -0.125], [-0.15, -0.125], [-0.15, 0.125]]
```

### rover_localization
Fusión de sensores para localización.

**Características:**
- Fusión EKF (encoders + IMU + GPS)
- AMCL para localización con mapa
- Filtro de Kalman extendido

**Nodos:**
- `ekf_localization`: Robot localization EKF
- `gps_fusion`: Integración de GPS

## Compilación

```bash
cd rover_navigation
colcon build --symlink-install
source install/setup.bash
```

## Dependencias

- rover_core
- rover_control
- Nav2
- robot_localization

## Uso

```bash
# Navegación con mapa existente
ros2 launch rover_nav2_bringup navigation.launch.py map:=my_map.yaml

# SLAM (crear mapa)
ros2 launch rover_nav2_bringup slam.launch.py

# Solo localización
ros2 launch rover_localization localization.launch.py
```

## Configuración

La geometría del robot se configura automáticamente desde los parámetros:
- wheel_radius: 0.075m
- wheelbase: 0.180m
- track_width: 0.250m

Esto genera el footprint y radio de colisión para Nav2.

