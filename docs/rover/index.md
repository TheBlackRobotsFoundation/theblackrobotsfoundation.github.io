---
sidebar_position: 1
---

# Rover

Plataforma robótica móvil de tracción diferencial basada en ROS2 para aprendizaje y experimentación en robótica móvil, navegación autónoma y fusión de sensores.

## Características

- **Arquitectura**: Componentes independientes y reutilizables (ROS2 Humble)
- **Hardware**: Jetson Orin, RoboClaw 2x15A, PX4, RPLiDAR
- **Navegación**: Integración con Nav2
- **Simulación**: Modelo en Gazebo

## Repositorio

**Todo el código y documentación completa:**  
[github.com/TheBlackRobotsFoundation/Rover](https://github.com/TheBlackRobotsFoundation/Rover)

## Documentación

### Primeros Pasos
- [Instalación](getting-started/installation.md) - Setup inicial y dependencias
- [Hardware Setup](getting-started/hardware-setup.md) - Conexiones y configuración
- [Quick Start](getting-started/quickstart.md) - Primer uso

### Arquitectura
- [Visión General](architecture/overview.md) - Diseño del sistema

## Especificaciones Técnicas

| Componente | Especificación |
|-----------|----------------|
| Radio de rueda | 0.075 m |
| Wheelbase | 0.180 m |
| Track width | 0.250 m |
| Encoders | 4096 CPR |
| Computadora | NVIDIA Jetson Orin |
| Controladores | RoboClaw 2x15A |
| Sensores | PX4 (IMU, GPS), RPLiDAR |

## Licencia

GPL v3 - Ver [LICENSE](https://github.com/TheBlackRobotsFoundation/Rover/blob/main/LICENSE)
- **Sensores**: PX4 (IMU/GPS), RPLiDAR
- **Control**: PS4 Controller, FrSky FR6

## Enlaces

- [GitHub](https://github.com/TheBlackRobotsFoundation/Rover)
- [Web](https://theblackrobotsfoundation.github.io)
- [Proyecto](https://theblackrobotsfoundation.github.io/proyectos/rover/)
