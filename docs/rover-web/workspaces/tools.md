---
sidebar_position: 7
title: Tools
---

# rover_tools

Workspace con herramientas de diagnóstico, calibración y testing.

## Paquetes

### rover_diagnostics
Herramientas de diagnóstico del sistema.

**Scripts:**
- `check_hardware.py`: Verifica conexiones de hardware
- `monitor_health.py`: Monitor en tiempo real del sistema
- `test_roboclaw.py`: Test de controladores RoboClaw
- `test_ibus.py`: Test de receptor IBUS
- `test_encoders.py`: Test de encoders
- `diagnostics_node.py`: Nodo de diagnóstico continuo

**Uso:**
```bash
# Verificar hardware
ros2 run rover_diagnostics check_hardware.py

# Monitor continuo
ros2 run rover_diagnostics monitor_health.py

# Test driver específico
ros2 run rover_diagnostics test_roboclaw.py
```

### rover_calibration
Herramientas de calibración.

**Scripts:**
- `calibrate_imu.py`: Calibración de IMU
- `calibrate_encoders.py`: Calibración de encoders
- `calibrate_odometry.py`: Calibración de odometría
- `measure_wheelbase.py`: Medición de parámetros físicos

**Uso:**
```bash
# Calibrar IMU
ros2 run rover_calibration calibrate_imu.py

# Calibrar odometría
ros2 run rover_calibration calibrate_odometry.py --distance 5.0
```

## Compilación

```bash
cd rover_tools
colcon build --symlink-install
source install/setup.bash
```

## Dependencias

- rover_core
- rover_drivers
- pyserial

## Diagnóstico Completo

```bash
# 1. Verificar puertos disponibles
ls -l /dev/tty{ACM,USB}*

# 2. Verificar permisos
groups | grep dialout

# 3. Test de hardware
ros2 launch rover_diagnostics full_diagnostics.launch.py

# 4. Ver reporte
cat ~/rover_diagnostics_report.txt
```

## Scripts de Testing

Similar a los del Rover_old, pero integrados con ROS2:
- Todos los scripts ahora son nodos ROS2
- Pueden ejecutarse individualmente o desde launch files
- Reportan estado via topics de diagnóstico
- Logs centralizados

## Herramientas CLI

```bash
# Ver estado de nodos
ros2 run rover_diagnostics node_status.py

# Ver tópicos activos
ros2 run rover_diagnostics topic_monitor.py

# Verificar frecuencia de publicación
ros2 run rover_diagnostics frequency_check.py /odom
```

