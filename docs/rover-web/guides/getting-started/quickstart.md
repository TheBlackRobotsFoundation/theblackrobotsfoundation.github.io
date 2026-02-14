# Quick Start

Guía rápida para empezar a usar el Rover.

## Prerequisitos

- [Instalación](installation.md) completada
- [Hardware](hardware-setup.md) conectado
- ROS2 Humble instalado y sourced

## Primera Vez

### 1. Source del Workspace

```bash
cd ~/Desktop/Rover
source /opt/ros/humble/setup.bash
source rover_bringup/install/setup.bash
```

Añadir a `.bashrc` para automatizar:
```bash
echo "source ~/Desktop/Rover/rover_bringup/install/setup.bash" >> ~/.bashrc
```

### 2. Verificar Hardware

```bash
ros2 run rover_diagnostics check_hardware.py
```

Debe mostrar:
```
✓ RoboClaw Left: /dev/ttyACM1
✓ RoboClaw Right: /dev/ttyACM0
✓ PX4: /dev/ttyACM2
✓ LIDAR: /dev/ttyUSB0
✓ IBUS: /dev/ttyTHS0
```

### 3. Lanzar Rover Mínimo

```bash
ros2 launch rover_launch minimal.launch.py
```

Esto inicia:
- Drivers de RoboClaw
- Controlador base
- Publicación de TF

### 4. Teleoperación

En otra terminal:

```bash
# Con PS4 controller
ros2 launch rover_launch teleop.launch.py controller:=ps4

# O con FrSky
ros2 launch rover_launch teleop.launch.py controller:=frsky
```

## Uso Diario

### Rover Completo

```bash
# Todo el sistema (drivers + sensores + control)
ros2 launch rover_launch rover.launch.py
```

### Solo Teleoperación

```bash
# Terminal 1: Sistema mínimo
ros2 launch rover_launch minimal.launch.py

# Terminal 2: Teleop
ros2 launch rover_launch teleop.launch.py
```

### Con Navegación

```bash
# Con mapa existente
ros2 launch rover_launch navigation.launch.py map:=~/maps/my_map.yaml

# SLAM (crear nuevo mapa)
ros2 launch rover_launch slam.launch.py
```

## Simulación

### Gazebo Básica

```bash
ros2 launch rover_launch simulation.launch.py
```

### Simulación + Navegación

```bash
ros2 launch rover_launch simulation.launch.py navigation:=true
```

### Solo Visualización (RViz)

```bash
ros2 launch rover_description display.launch.py
```

## Verificaciones Comunes

### Ver Topics Activos

```bash
ros2 topic list
```

Deberías ver:
- `/cmd_vel` - Comandos de velocidad
- `/odom` - Odometría
- `/scan` - LIDAR (si conectado)
- `/imu/data` - IMU
- `/joy` - Joystick

### Ver Estado de Nodos

```bash
ros2 node list
```

### Monitorear Odometría

```bash
ros2 topic echo /odom
```

### Visualizar en RViz

```bash
rviz2
```

Añadir displays:
- RobotModel
- TF
- Odometry
- LaserScan (si LIDAR activo)

## Comandos Útiles

### Enviar Comando Manual

```bash
# Mover adelante
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2, y: 0, z: 0}, angular: {x: 0, y: 0, z: 0}}"

# Girar
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0, y: 0, z: 0}, angular: {x: 0, y: 0, z: 0.5}}"

# Detener
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0, y: 0, z: 0}, angular: {x: 0, y: 0, z: 0}}"
```

### Grabar Datos

```bash
# Grabar todos los topics
ros2 bag record -a

# Grabar topics específicos
ros2 bag record /odom /scan /imu/data
```

### Reproducir Datos

```bash
ros2 bag play my_recording.db3
```

## Troubleshooting Rápido

### El rover no se mueve

```bash
# Verificar que cmd_vel se está publicando
ros2 topic hz /cmd_vel

# Verificar estado de motores
ros2 topic echo /motor_status
```

### Odometría no se publica

```bash
# Verificar drivers
ros2 node info /roboclaw_left_node
ros2 node info /roboclaw_right_node

# Ver logs
ros2 run rqt_console rqt_console
```

### Joystick no funciona

```bash
# Verificar que se detecta
ls /dev/input/js*

# Ver datos del joy
ros2 topic echo /joy

# Test de permisos
sudo chmod 666 /dev/input/js0
```

## Crear un Mapa (SLAM)

```bash
# Terminal 1: SLAM
ros2 launch rover_launch slam.launch.py

# Terminal 2: Teleop
ros2 launch rover_launch teleop.launch.py

# Terminal 3: RViz
rviz2 -d ~/Desktop/Rover/rover_navigation/src/rover_nav2_bringup/rviz/slam.rviz

# Cuando termines, guardar mapa
ros2 run nav2_map_server map_saver_cli -f ~/maps/my_map
```

## Navegar Autónomamente

```bash
# Lanzar navegación
ros2 launch rover_launch navigation.launch.py map:=~/maps/my_map.yaml

# En RViz:
# 1. Clic en "2D Pose Estimate"
# 2. Clic en posición inicial en el mapa
# 3. Clic en "Nav2 Goal"
# 4. Clic en destino deseado
```

## Apagar Correctamente

```bash
# Ctrl+C en todas las terminales

# Verificar que no quedan nodos
ros2 node list

# Si quedan procesos colgados
killall -9 roboclaw_driver ibus_driver
```
