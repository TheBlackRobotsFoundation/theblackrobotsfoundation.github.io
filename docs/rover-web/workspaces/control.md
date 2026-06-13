---
sidebar_position: 3
title: Control
---

# rover_control

Workspace para control de base y teleoperación del rover.

## Paquetes

### rover_base_controller
Controlador principal de la base móvil.

**Características:**
- Cinemática diferencial
- Fusión de odometría (encoders + IMU)
- Control PID de velocidad
- Publicación de TF

**Topics:**
- `/cmd_vel` (sub): Comandos de velocidad
- `/odom` (pub): Odometría fusionada
- `/tf` (pub): Transformaciones

### rover_teleop
Nodos de teleoperación.

**Características:**
- Teleop con PS4 controller
- Teleop con FrSky (IBUS)
- Modos de velocidad (lento/rápido)
- Dead man switch

**Topics:**
- `/joy` (sub): Joystick input
- `/cmd_vel` (pub): Comandos de velocidad

## Compilación

```bash
cd rover_control
colcon build --symlink-install
source install/setup.bash
```

## Dependencias

- rover_core
- rover_drivers
- ros2-control (opcional)

## Uso

```bash
# Teleop con PS4
ros2 launch rover_teleop ps4_teleop.launch.py

# Teleop con FrSky
ros2 launch rover_teleop frsky_teleop.launch.py
```

