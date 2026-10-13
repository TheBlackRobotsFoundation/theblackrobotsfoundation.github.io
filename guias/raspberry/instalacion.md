---
sidebar_position: 2
title: Instalación
sidebar_custom_props:
  icon: /img/guias/iconos/instalacion.svg
---

# Instalación

La Raspberry Pi arranca desde una **tarjeta microSD**. Instalarla consiste en grabar el sistema operativo en esa tarjeta desde tu ordenador, con todo configurado para poder controlarla después a distancia.

<img src="/img/guias/raspberry/instalacion.svg" alt="Proceso de instalación: Raspberry Pi Imager en el ordenador, la microSD, el primer arranque y la conexión por SSH" />

## Qué necesitas

| Componente | Notas |
|---|---|
| Raspberry Pi 5 | o Pi 4 |
| Tarjeta microSD de 32 GB o más | clase A2: arranca y responde más rápido |
| Fuente USB-C oficial | **5 V y 5 A** para la Pi 5 (5 V y 3 A para la Pi 4) |
| Lector de tarjetas | para grabarla desde el ordenador |
| Disipador o caja con ventilador | recomendado en la Pi 5 |

:::caution
Una fuente que se queda corta provoca reinicios y errores difíciles de entender. Usa la oficial o una de la misma potencia: el cargador de un móvil no suele bastar.
:::

## Qué sistema operativo elegir

| Sistema | Cuándo elegirlo |
|---|---|
| **Raspberry Pi OS (64 bits)** | para aprender Linux, Python y electrónica. Es el sistema oficial y trae todo preparado |
| **Ubuntu Server 24.04** | para usar [ROS 2](/guias/ros2) en una Pi 5 (con ROS 2 Jazzy) |
| **Ubuntu Server 22.04** | para usar ROS 2 Humble en una Pi 4, la misma versión que usa el [Rover](/proyectos/rover-web) |

ROS 2 se instala con un par de comandos en Ubuntu, que es el sistema para el que se publica. Si vas a usar ROS 2, empieza directamente con Ubuntu.

## 1. Grabar la tarjeta con Raspberry Pi Imager

1. Descarga **Raspberry Pi Imager** desde [raspberrypi.com/software](https://www.raspberrypi.com/software/) e instálalo
2. Elige el **modelo** de tu placa, el **sistema operativo** y la **tarjeta** donde grabarlo
3. Cuando te ofrezca **personalizar** el sistema, acepta y rellena:
   - **Nombre del equipo** (*hostname*), por ejemplo `robot`
   - **Usuario y contraseña**
   - **Wi-Fi**: el nombre de tu red, la contraseña y el país
   - **Activar SSH**, con usuario y contraseña
4. Graba la tarjeta. Tarda unos minutos

Con esto, la Raspberry se conectará sola a tu Wi-Fi en el primer arranque y podrás controlarla desde el ordenador, sin pantalla ni teclado.

## 2. Primer arranque

Mete la tarjeta en la Raspberry y conecta la alimentación. El primer arranque tarda un par de minutos porque el sistema se termina de configurar. El LED verde parpadea mientras lee la tarjeta.

## 3. Conectarte por SSH

**SSH** abre una terminal de la Raspberry en tu ordenador, a través de la red. Desde la terminal de tu ordenador (en Windows, PowerShell):

```bash
ssh usuario@robot.local
```

Cambia `usuario` y `robot` por los que elegiste. La primera vez te pregunta si confías en el equipo: escribe `yes` y luego la contraseña.

:::tip
Si `robot.local` no responde, busca la IP de la Raspberry en la página de configuración de tu router y conéctate con ella: `ssh usuario@192.168.1.42`.
:::

## 4. Actualizar el sistema

Ya dentro, lo primero es poner todo al día:

```bash
sudo apt update
sudo apt full-upgrade -y
sudo reboot
```

- `sudo` ejecuta el comando como administrador
- `apt` es el gestor de programas: instala, actualiza y desinstala

Tras el reinicio, vuelve a conectarte por SSH. Ya tienes tu Raspberry lista para [el primer programa](./primer-programa).

:::note[Con pantalla y teclado]
Si prefieres usarla como un ordenador normal, elige **Raspberry Pi OS** con escritorio, conecta una pantalla por micro-HDMI, un teclado y un ratón. Todo lo de estas guías se hace igual desde su terminal.
:::
