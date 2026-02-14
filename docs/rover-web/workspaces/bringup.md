---
sidebar_position: 6
title: Bringup
---

# rover_bringup

Workspace de integración para lanzar el rover completo.

## Paquetes

### rover_launch
Launch files principales del sistema.

**Launch files:**
- `rover.launch.py`: Lanza el rover completo (hardware real)
- `simulation.launch.py`: Lanza simulación en Gazebo
- `teleop.launch.py`: Solo teleoperación
- `navigation.launch.py`: Navegación autónoma
- `minimal.launch.py`: Sistema mínimo (drivers + control)

**Uso:**
```bash
# Rover físico completo
ros2 launch rover_launch rover.launch.py

# Simulación completa
ros2 launch rover_launch simulation.launch.py

# Teleop con PS4
ros2 launch rover_launch teleop.launch.py controller:=ps4

# Navegación
ros2 launch rover_launch navigation.launch.py map:=my_map.yaml
```

### rover_config
Configuración centralizada del rover.

**Archivos:**
- `rover_params.yaml`: Parámetros principales del rover
  - Dimensiones físicas
  - Puertos de hardware
  - Configuración de sensores
  - Parámetros de navegación

**Parámetros clave:**
```yaml
wheel_radius: 0.075
wheelbase: 0.180
track_width: 0.250
encoder_cpr: 4096
```

## Compilación

```bash
cd rover_bringup
colcon build --symlink-install
source install/setup.bash
```

## Dependencias

Depende de todos los demás workspaces:
- rover_core
- rover_drivers
- rover_control
- rover_navigation
- rover_simulation
- rover_tools

## Estructura de Launch

Los launch files están organizados jerárquicamente:

```
rover.launch.py
├── rover_config (parámetros)
├── rover_drivers
│   ├── roboclaw_driver
│   ├── ibus_driver
│   └── px4_bridge
├── rover_control
│   └── rover_base_controller
├── rover_perception
│   └── rplidar
└── rover_navigation (opcional)
    └── nav2_bringup
```

## Quick Start

```bash
# 1. Source ROS2
source /opt/ros/humble/setup.bash

# 2. Source workspace
source ~/Desktop/Rover/rover_bringup/install/setup.bash

# 3. Verificar hardware
ros2 run rover_tools check_hardware.py

# 4. Lanzar rover
ros2 launch rover_launch rover.launch.py

# 5. En otra terminal - teleop
ros2 launch rover_launch teleop.launch.py
```

## Troubleshooting

Ver [diagnostics](../rover_tools/README.md) para herramientas de diagnóstico.

```bash
# Verificar conexiones
ros2 launch rover_tools diagnostics.launch.py

# Test individual de drivers
ros2 run rover_tools test_roboclaw.py
ros2 run rover_tools test_ibus.py
```

