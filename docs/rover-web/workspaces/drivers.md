---
sidebar_position: 2
title: Drivers
---

# rover_drivers

Workspace con drivers de hardware para el rover.

## Paquetes

### roboclaw_driver
Driver para los controladores de motor RoboClaw 2x15A.

**Características:**
- Control de velocidad de motores
- Lectura de encoders
- Monitoreo de corriente y voltaje
- Soporte para 2 RoboClaw (4 motores total)

**Topics:**
- `/cmd_vel` (sub): Comandos de velocidad
- `/odom` (pub): Odometría de encoders
- `/motor_status` (pub): Estado de motores

**Parámetros:**
- `left_port`: Puerto del RoboClaw izquierdo (/dev/ttyACM1)
- `right_port`: Puerto del RoboClaw derecho (/dev/ttyACM0)
- `wheel_radius`: 0.075m
- `track_width`: 0.250m
- `encoder_cpr`: 4096

### ibus_driver
Driver para receptor FrSky con protocolo IBUS.

**Características:**
- Lectura de 6 canales
- Publicación como Joy messages
- Failsafe detection

**Topics:**
- `/joy` (pub): Datos del control remoto

**Parámetros:**
- `port`: Puerto serial
- `channels`: Número de canales

### px4_bridge
Bridge para comunicación con PX4 via uXRCE-DDS.

**Características:**
- IMU data
- GPS data
- Integración con sistema de localización

**Topics:**
- `/px4/imu` (pub): Datos IMU
- `/px4/gps` (pub): Datos GPS

## Compilación

```bash
cd rover_drivers
colcon build --symlink-install
source install/setup.bash
```

## Dependencias

- rover_core
- pyserial
- Python 3

## Hardware Setup

Ver [hardware-setup.md](../docs/getting-started/hardware-setup.md) para conexiones.

