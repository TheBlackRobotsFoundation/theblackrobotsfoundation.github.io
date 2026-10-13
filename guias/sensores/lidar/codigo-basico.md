---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para leer el LiDAR

Dos caminos: **Python**, para entender los datos y hacer pruebas rápidas, y **ROS 2**, para usarlo dentro de un robot como el Rover.

## Con Python

### Instalar la librería

```bash
pip install rplidar-roboticia matplotlib
```

### 1. Leer una vuelta

```python
from rplidar import RPLidar

lidar = RPLidar('/dev/ttyUSB0')

print(lidar.get_info())     # modelo, firmware y número de serie
print(lidar.get_health())   # ('Good', 0) si todo va bien

try:
    for i, vuelta in enumerate(lidar.iter_scans()):
        print(f'Vuelta {i}: {len(vuelta)} puntos')
        for calidad, angulo, distancia in vuelta[:5]:
            print(f'  {angulo:6.1f}°  {distancia:7.1f} mm')
        if i >= 4:
            break
finally:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
```

- `iter_scans()` va devolviendo vueltas completas, cada una como una lista de `(calidad, ángulo, distancia)`
- El bloque `finally` para el motor y libera el puerto aunque el programa falle

### 2. Ver el entorno en directo

```python
import math
import matplotlib.pyplot as plt
from rplidar import RPLidar

lidar = RPLidar('/dev/ttyUSB0')

plt.ion()
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

try:
    for vuelta in lidar.iter_scans():
        angulos = [math.radians(a) for _, a, _ in vuelta]
        distancias = [d / 1000 for _, _, d in vuelta]   # a metros

        ax.clear()
        ax.scatter(angulos, distancias, s=2)
        ax.set_rmax(4)
        plt.pause(0.01)
finally:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
```

Verás el contorno de la habitación desde el punto de vista del LiDAR. Muévete a su alrededor y aparecerás como un pequeño arco que se desplaza.

### 3. ¿Hay algo cerca?

```python
for vuelta in lidar.iter_scans():
    delante = [d for _, a, d in vuelta if (a < 20 or a > 340) and d > 0]
    if delante and min(delante) < 400:
        print(f'Obstáculo delante a {min(delante):.0f} mm')
```

Filtra los puntos de los ±20° de delante y mira el más cercano: es el [robot esquiva-obstáculos](/guias/proyecto-esquiva-obstaculos), en versión LiDAR.

## Con ROS 2

En ROS 2, un **nodo** se encarga del LiDAR y publica cada vuelta en el topic `/scan` (mensaje `sensor_msgs/LaserScan`). Cualquier otro nodo del robot (mapas, navegación) la recibe de ahí.

### Instalar el driver

```bash
sudo apt install ros-humble-rplidar-ros
```

### Lanzarlo y verlo

```bash
ros2 launch rplidar_ros view_rplidar_a1_launch.py serial_port:=/dev/ttyUSB0
```

Se abre **RViz** con los puntos del LiDAR. Para lanzar solo el nodo, sin RViz, usa `rplidar_a1_launch.py`.

### Comprobar el topic

```bash
ros2 topic hz /scan     # vueltas por segundo
ros2 topic echo /scan --once
```

El mensaje trae los ángulos de inicio y fin, el incremento entre medidas y la lista `ranges` con las distancias en metros.

## ¿Y ahora qué?

Así es como el [Rover](/proyectos/rover-web) lee su LiDAR. Con el topic `/scan` funcionando, el siguiente paso en ROS 2 es construir un mapa con **slam_toolbox** y navegar por él con **Nav2**.
