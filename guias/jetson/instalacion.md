---
sidebar_position: 2
title: Instalación
sidebar_custom_props:
  icon: /img/guias/iconos/instalacion.svg
---

# Instalación

El sistema de la Jetson se llama **JetPack**: Ubuntu con todo el software de NVIDIA ya preparado para usar la GPU.

<img src="/img/guias/jetson/jetpack.svg" alt="Capas de JetPack: Jetson Linux sobre el módulo, CUDA, TensorRT y cuDNN, y tus programas encima" />

| Capa | Qué hace |
|---|---|
| **Jetson Linux** | Ubuntu 22.04 con los drivers de NVIDIA (en JetPack 6) |
| **CUDA** | permite programar la GPU |
| **cuDNN, TensorRT** | aceleran las redes neuronales |
| **VPI, Multimedia** | aceleran visión por ordenador y cámaras |

Como es Ubuntu 22.04, puedes instalar **ROS 2 Humble** exactamente igual que en un ordenador: la misma versión que usa el [Rover](/proyectos/rover-web).

## Qué necesitas

| Componente | Notas |
|---|---|
| Jetson Orin Nano Developer Kit | trae su fuente de alimentación |
| Tarjeta microSD de 64 GB o más | clase A2 |
| Pantalla DisplayPort, teclado y ratón | para el primer arranque |
| SSD NVMe M.2 | opcional, pero mucho más rápido que la microSD |

## 1. Grabar la tarjeta

1. Descarga la **imagen de JetPack para microSD** del Orin Nano Developer Kit desde la [página oficial de NVIDIA](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit)
2. Grábala en la tarjeta con **Balena Etcher** (o con Raspberry Pi Imager, eligiendo "usar imagen personalizada")
3. Mete la tarjeta en la ranura que hay **debajo del módulo**, junto al disipador

:::caution[Firmware]
Los kits fabricados antes de JetPack 6 traen un firmware antiguo que no arranca directamente con la imagen nueva. Si al encender la pantalla se queda en negro o en el menú de la placa, sigue el paso de **actualización del firmware** de la guía oficial de NVIDIA: se hace una sola vez.
:::

## 2. Primer arranque

Conecta la pantalla, el teclado, el ratón y, por último, la alimentación. El asistente de Ubuntu te pide:

- Aceptar la licencia
- Idioma, teclado y zona horaria
- **Usuario y contraseña**
- Conectarte a la red Wi-Fi o por cable

Al terminar, tendrás un escritorio de Ubuntu normal.

## 3. Actualizar y completar JetPack

Abre una terminal y ejecuta:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y nvidia-jetpack
sudo reboot
```

`nvidia-jetpack` instala (o completa) CUDA, cuDNN, TensorRT y el resto de componentes. Ocupa varios GB.

## 4. Controlarla a distancia

SSH viene activado. Desde tu ordenador:

```bash
ssh usuario@IP-de-la-jetson
```

Puedes ver la IP con `hostname -I` en la propia Jetson. Desde aquí, todo se trabaja igual que en la [Raspberry Pi](/guias/raspberry/conceptos-basicos): la terminal, los servicios que arrancan solos y Visual Studio Code por SSH.

## Arrancar desde un SSD

Un SSD NVMe es varias veces más rápido que la microSD: el sistema arranca antes y los programas cargan mejor. Para instalar JetPack directamente en el SSD se usa **SDK Manager**, el programa de NVIDIA que se ejecuta en un ordenador con Ubuntu y graba la Jetson por USB. La [documentación de NVIDIA](https://developer.nvidia.com/sdk-manager) lo explica paso a paso.

:::note[Otras Jetson]
Los módulos Orin NX y AGX Orin se instalan con **SDK Manager** o con la imagen que da el fabricante de su placa base.
:::
