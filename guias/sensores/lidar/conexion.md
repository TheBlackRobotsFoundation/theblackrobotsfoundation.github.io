---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

El RPLIDAR A1 viene con todo lo necesario: el cable y un adaptador UART-USB. Se conecta a un **ordenador o una Raspberry Pi** por USB, y por ese mismo cable recibe la alimentación.

## Qué necesitas

| Componente | Cantidad |
|---|---|
| RPLIDAR A1 (con su adaptador) | 1 |
| Cable micro-USB de datos | 1 |
| Ordenador con Linux o Raspberry Pi | 1 |

## Esquema de conexión

![Esquema: RPLIDAR A1, adaptador UART-USB y ordenador](/img/guias/sensores/lidar/conexion.svg)

1. Conecta el cable del LiDAR al **adaptador**
2. Conecta el adaptador al **ordenador** con el cable micro-USB
3. El LiDAR empieza a girar

## Comprobar que el ordenador lo ve

En Linux, el adaptador aparece como un puerto serie:

```bash
ls /dev/ttyUSB*
```

Debe salir `/dev/ttyUSB0`. Para poder usarlo sin `sudo`, añade tu usuario al grupo `dialout` y vuelve a iniciar sesión:

```bash
sudo usermod -aG dialout $USER
```

:::tip[Nombre fijo para el puerto]
Si conectas varios dispositivos USB, el número puede cambiar (`ttyUSB0`, `ttyUSB1`...). El Rover usa una **regla udev** para que el LiDAR aparezca siempre como `/dev/rplidar`. Tienes la regla en su [guía de hardware](/proyectos/rover-web/guides/getting-started/hardware-setup).
:::

## En Windows y macOS

Instala el driver **CP210x** de Silicon Labs (es el chip del adaptador). El puerto aparecerá como `COM3`, `COM4`... en Windows, o como `/dev/tty.SLAB_USBtoUART` en macOS.

:::caution[Alimentación]
El motor del LiDAR arranca con un pico de corriente. Algunos puertos USB de portátil o hubs sin alimentación se quedan cortos y el LiDAR gira a tirones o se reinicia. Si te pasa, conéctalo directamente al ordenador o usa un hub con alimentación propia.
:::

## En el robot

- Móntalo en la **parte más alta** del robot, con vista libre en los 360°
- **Horizontal**: si está inclinado, verá el suelo por un lado y el techo por el otro
- Comprueba hacia dónde mira su **ángulo 0°**: pon un objeto justo delante del robot y mira con qué ángulo aparece en el [código](./codigo-basico). Gira el LiDAR hasta que coincida con 0°, o ten en cuenta la diferencia en el programa

Con todo conectado, pasa al [código básico](./codigo-basico).
