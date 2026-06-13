---
sidebar_position: 1
title: Core
---

# rover_core

Workspace que contiene mensajes, servicios y acciones personalizadas para el rover.

## Paquetes

### rover_msgs
Mensajes personalizados para el rover:
- Encoders
- Estado de motores
- Información de batería
- Diagnóstico de hardware

### rover_interfaces
Servicios y acciones:
- Calibración
- Reinicio de controladores
- Control de modo de operación

## Compilación

```bash
cd rover_core
colcon build --symlink-install
source install/setup.bash
```

## Dependencias

Este workspace no depende de otros workspaces del rover. Es la base para todos los demás.

