---
sidebar_position: 1
id: rover-intro
title: Rover
---

# Rover

## ¿Qué es este proyecto?

El Rover es una plataforma robótica móvil de tracción diferencial diseñada para **aprender y experimentar** con:
- **Robótica móvil**: Cinemática, odometría, control de motores
- **ROS2**
- **Navegación autónoma**: Uso de Nav2 para planificación de rutas y esquivar obstáculos
- **Fusión de sensores**: Combinación de encoders, IMU y GPS para localización
- **Hardware real**: Integración completa con controladores de motor, sensores y computadora embebida

Este proyecto está diseñado con fines **educativos** y de **investigación**, permitiéndote desde controlar el rover manualmente hasta implementar navegación autónoma completa.

## ¿Qué aprenderás?

- Estructura de un proyecto ROS2
- Comunicación entre nodos mediante topics, services y actions
- Control de motores DC con encoders
- Odometría por ruedas y fusión con IMU
- Configuración y uso de Nav2 para navegación
- Integración de sensores (LIDAR, IMU, GPS)
- Launch files y gestión de parámetros
- Debugging y diagnóstico de sistemas robóticos

## Características del Sistema

- **Arquitectura modular**: Componentes independientes adaptables a tu hardware
- **Hardware configurable**: No requiere componentes específicos
- **Navegación autónoma**: Integración con Nav2
- **Simulación**: Modelo en Gazebo

### Hardware de Esta Implementación

Desarrollado y probado con:
- **Computadora**: Jetson Orin
- **Motores**: RoboClaw 2x15A
- **Sensores**: PX4, RPLiDAR
- **Control**: Teclado, PS4, FrSky

El sistema es modular: cambia componentes en `rover_bringup/rover_config/`

## Arquitectura del Sistema

El rover está organizado en **capas funcionales** que se comunican mediante ROS2:

```
┌─────────────────────────────────────────────────────────────┐
│                    APLICACIÓN / USUARIO                      │
│  (Teleop manual, Navegación autónoma, Scripts de prueba)   │
└────────────────────────┬────────────────────────────────────┘
                         │ /cmd_vel (Twist)
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   CAPA DE CONTROL                            │
│  - Base Controller: Convierte cmd_vel a velocidades ruedas  │
│  - Odometría: Fusiona encoders + IMU → publica /odom        │
│  - TF: Publica transformaciones (odom → base_link)          │
└────────────┬───────────────────────────┬────────────────────┘
             │ Motor commands            │ Sensor data
             ▼                           ▼
┌─────────────────────────┐  ┌──────────────────────────────┐
│   CAPA DE DRIVERS       │  │   CAPA DE PERCEPCIÓN         │
│  - RoboClaw (motores)   │  │  - LIDAR (/scan)             │
│  - IBUS (radio)         │  │  - PX4 (IMU, GPS)            │
└────────────┬────────────┘  └──────────────┬───────────────┘
             │                               │
             ▼                               ▼
┌─────────────────────────────────────────────────────────────┐
│                      HARDWARE FÍSICO                         │
│  Motores DC | Encoders | LIDAR | IMU | GPS | Radio RC       │
└─────────────────────────────────────────────────────────────┘
```

### Flujo de Datos Principal

1. **Entrada de control**: Usuario o Nav2 publica comandos en `/cmd_vel`
2. **Control**: Base controller convierte velocidades lineales/angulares a velocidades de ruedas
3. **Actuación**: Drivers de motor envían comandos a los controladores
4. **Sensado**: Encoders y sensores publican datos constantemente
5. **Odometría**: Los datos se fusionan para estimar posición en `/odom`
6. **Localización**: Nav2 usa `/odom` y `/scan` para navegación

## Especificaciones del Robot (Ejemplo)

**Nota**: Estos valores son del ejemplo de implementación. 
Configura los tuyos en `rover_bringup/rover_config/config/rover_params.yaml`

| Parámetro | Valor |
|-----------|-------|
| Radio de rueda | 0.075 m |
| Wheelbase | 0.180 m |
| Track width | 0.250 m |
| Encoders | 4096 CPR |
| Controlador | Jetson Orin |

## Quick Start

### Prerequisitos

- **Ubuntu 22.04** en Jetson Orin u otra computadora ARM64/x86_64
- **ROS2 Humble** instalado
- Conocimientos básicos de terminal Linux y ROS2

### Paso 1: Clonar e Instalar

```bash
# Clonar el repositorio
git clone https://github.com/TheBlackRobotsFoundation/Rover.git
cd Rover

# Instalar todas las dependencias automáticamente
./scripts/setup.sh
```

**¿Qué hace `setup.sh`?**
- Instala herramientas de compilación de ROS2 (colcon, vcstool)
- Instala paquetes de ROS2 necesarios (Nav2, Gazebo, joy, etc.)
- Instala dependencias Python (pyserial, pyyaml)
- Configura permisos de puertos seriales (grupo dialout)
- Crea reglas udev para identificar dispositivos USB

### Paso 2: Compilar el Proyecto

```bash
# Compilar todos los paquetes
./scripts/build_all.sh

# Source del workspace (añadir a ~/.bashrc para hacerlo automático)
source install/setup.bash
```

**¿Qué hace `build_all.sh`?**
- Compila los 15 paquetes ROS2 del proyecto en orden correcto
- Genera archivos de instalación en `install/`
- Crea symlinks para desarrollo rápido (no necesitas recompilar al editar Python)

### Paso 3: Verificar la Instalación

```bash
# Verificar que los paquetes estén disponibles
ros2 pkg list | grep rover

# Deberías ver:
# rover_base_controller
# rover_calibration
# rover_config
# rover_description
# ... (15 paquetes total)
```

### Paso 4: Primer Uso

**Opción A: Simulación (sin hardware)**
```bash
# Lanzar simulación en Gazebo
ros2 launch rover_simulation gazebo.launch.py

# En otra terminal: teleop con teclado
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

**Opción B: Hardware Real**
```bash
# 1. Conectar hardware (ver docs/getting-started/hardware-setup.md)
# 2. Verificar conexiones
ros2 run rover_diagnostics check_hardware.py

# 3. Lanzar drivers y control
ros2 launch rover_bringup rover.launch.py

# 4. En otra terminal: teleop (elige tu método)
# Con teclado:
ros2 run teleop_twist_keyboard teleop_twist_keyboard
# Con joystick (ejemplo PS4, ver docs para otros):
ros2 launch rover_control ps4_teleop.launch.py
```

### Paso 5: Explorar

```bash
# Ver topics activos
ros2 topic list

# Monitorear odometría
ros2 topic echo /odom

# Ver transformaciones
ros2 run tf2_tools view_frames

# Visualizar en RViz
rviz2
```

## Cómo Funciona: Conceptos Clave

### Topics y Nodos

En ROS2, los programas se organizan en **nodos** que se comunican mediante **topics**:

```
┌──────────────┐    /cmd_vel     ┌──────────────────┐
│ Teleop Node  │─────────────────▶│ Base Controller  │
│ (joystick)   │   (Twist msg)   │ Node             │
└──────────────┘                 └────────┬─────────┘
                                          │ /wheel_speeds
                                          ▼
                                 ┌──────────────────┐
                                 │ RoboClaw Driver  │
                                 │ Node             │
                                 └────────┬─────────┘
                                          │ Serial commands
                                          ▼
                                    [Hardware]
```

**Topics principales del Rover:**
- `/cmd_vel`: Comandos de velocidad (linear.x, angular.z)
- `/odom`: Odometría del robot (posición, orientación, velocidades)
- `/scan`: Datos del LIDAR (LaserScan)
- `/imu/data`: Datos del IMU (aceleración, velocidad angular)
- `/joy`: Estado del joystick (botones, ejes)

### Control Diferencial

El rover usa **tracción diferencial**: las ruedas izquierda y derecha pueden girar a velocidades diferentes.

```python
# Conversión de cmd_vel a velocidades de ruedas
v = cmd_vel.linear.x   # Velocidad lineal (m/s)
w = cmd_vel.angular.z  # Velocidad angular (rad/s)

# Cinemática diferencial
v_left = v - (w * track_width / 2)
v_right = v + (w * track_width / 2)
```

- Para **avanzar recto**: v > 0, w = 0 → ambas ruedas igual velocidad
- Para **girar en su lugar**: v = 0, w > 0 → ruedas a velocidades opuestas
- Para **curva**: v > 0, w > 0 → una rueda más rápida que la otra

### Odometría

La odometría calcula la posición del robot integrando el movimiento de las ruedas:

```
1. Leer encoders → obtener pulsos desde última lectura
2. Convertir pulsos a distancia: d = pulsos / CPR * 2π * radio_rueda
3. Calcular desplazamiento: Δx, Δy, Δθ usando cinemática diferencial
4. Integrar: x += Δx, y += Δy, θ += Δθ
5. Publicar en /odom y actualizar TF (odom → base_link)
```

### Transformaciones (TF)

TF es el sistema de coordenadas de ROS2. Define cómo se relacionan los frames:

```
map                     (Frame del mapa, fijo en el mundo)
 └─ odom                (Frame de odometría, puede derivar)
     └─ base_footprint  (Proyección del robot en el suelo)
         └─ base_link   (Centro del chasis)
             ├─ lidar_link    (Posición del LIDAR)
             ├─ imu_link      (Posición del IMU)
             ├─ wheel_fl_link (Rueda frontal izq)
             └─ ...
```

- **Static TF**: Enlaces fijos (base_link → sensores) definidos en URDF
- **Dynamic TF**: Cambia con movimiento (odom → base_link) publicado por odometría

## Estructura del Proyecto

```
Rover/
├── rover_core/          # Mensajes e interfaces personalizadas
│   ├── rover_msgs/      # Definiciones de mensajes custom
│   └── rover_interfaces/# Servicios y acciones
│
├── rover_drivers/       # Drivers para comunicación con hardware
│   ├── roboclaw_driver/ # Control de motores DC
│   ├── ibus_driver/     # Receptor de radio FrSky
│   └── px4_bridge/      # Bridge para IMU y GPS de PX4
│
├── rover_control/       # Lógica de control del robot
│   ├── rover_base_controller/  # Cinemática y odometría
│   └── rover_teleop/           # Nodos de teleoperación
│
├── rover_navigation/    # Navegación autónoma con Nav2
│   ├── rover_nav2_bringup/    # Configuración de Nav2
│   └── rover_localization/     # Fusión de sensores (EKF)
│
├── rover_perception/    # Procesamiento de sensores
│   └── (en desarrollo)
│
├── rover_simulation/    # Simulación en Gazebo
│   ├── rover_description/      # Modelo URDF del robot
│   └── rover_gazebo/           # Mundos y plugins
│
├── rover_bringup/       # Integración del sistema completo
│   ├── rover_launch/    # Launch files principales
│   └── rover_config/    # Parámetros centralizados
│
├── rover_tools/         # Herramientas de desarrollo
│   ├── rover_diagnostics/      # Verificación de hardware
│   └── rover_calibration/      # Calibración de sensores
│
├── docs/                # Documentación detallada
│   ├── getting-started/ # Guías de instalación y primer uso
│   ├── architecture/    # Diagramas y explicaciones técnicas
│   ├── guides/          # Tutoriales paso a paso
│   └── troubleshooting/ # Solución de problemas
│
└── scripts/             # Scripts de automatización
    ├── setup.sh         # Instalación de dependencias
    ├── build_all.sh     # Compilación completa
    └── sync_docs.sh     # Sincronización con web
```

### ¿Dónde está cada cosa?

| Si quieres... | Mira en... |
|--------------|-----------|
| Añadir un nuevo mensaje | `rover_core/rover_msgs/msg/` |
| Modificar control de motores | `rover_drivers/roboclaw_driver/` |
| Cambiar comportamiento de teleop | `rover_control/rover_teleop/` |
| Ajustar parámetros de Nav2 | `rover_navigation/rover_nav2_bringup/params/` |
| Modificar modelo 3D del robot | `rover_simulation/rover_description/urdf/` |
| Cambiar configuración de hardware | `rover_bringup/rover_config/config/rover_params.yaml` |
| Crear un nuevo launch file | `rover_bringup/rover_launch/launch/` |

## Documentación Completa

Toda la documentación está en este repositorio, en la carpeta [docs/](/proyectos/rover-web/guides):

- **[Getting Started](/proyectos/rover-web/guides/getting-started/installation)**: Instalación, configuración y primeros pasos
- **[Arquitectura](/proyectos/rover-web/guides/architecture/overview)**: Diseño del sistema

## Componentes del Proyecto

Cada workspace es independiente y puede compilarse por separado:

| Workspace | Descripción | Dependencias |
|-----------|-------------|--------------|
| rover_core | Mensajes e interfaces base | - |
| rover_drivers | Drivers de hardware | rover_core |
| rover_control | Control y teleoperación | rover_core, rover_drivers |
| rover_navigation | Nav2 y localización | rover_core, rover_control |
| rover_perception | Sensores | rover_core |
| rover_simulation | Simulación Gazebo | rover_core, rover_control |
| rover_bringup | Integración completa | Todos |
| rover_tools | Diagnóstico | rover_core, rover_drivers |

## Desarrollo

### Compilar un workspace específico
```bash
cd rover_drivers
colcon build --symlink-install
source install/setup.bash
```

### Compilar todo
```bash
./scripts/build_all.sh
```

### Testing
```bash
./scripts/test_all.sh
```

### Diagnóstico
```bash
ros2 launch rover_tools diagnostics.launch.py
```

## Hardware Setup

Ver documentación detallada en [docs/getting-started/hardware-setup.md](/proyectos/rover-web/guides/getting-started/hardware-setup)

### Ejemplo de Configuración
**Controladores de motor**: Depende de tu hardware (RoboClaw, ODrive, etc.)
**Sensores**: LIDAR, IMU, GPS (opcionales según tu setup)
**Control**: Teclado, joystick, radio RC (configurable)

**¿Dónde configurar?**
- Puertos y dispositivos: `rover_bringup/rover_config/config/rover_params.yaml`
- Parámetros del robot: mismo archivo
- Launch files: `rover_bringup/rover_launch/launch/`

## Contribuir

1. Fork el proyecto
2. Crea tu feature branch: `git checkout -b feature/amazing-feature`
3. Commit tus cambios: `git commit -m 'Add amazing feature'`
4. Push a la branch: `git push origin feature/amazing-feature`
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo GPL v3. Ver [LICENSE](https://github.com/TheBlackRobotsFoundation/Rover/blob/main/LICENSE) para más detalles.

## Contacto

The Black Robots Foundation - [@TheBlackRobots](https://github.com/TheBlackRobotsFoundation)

Proyecto: [https://github.com/TheBlackRobotsFoundation/Rover](https://github.com/TheBlackRobotsFoundation/Rover)

