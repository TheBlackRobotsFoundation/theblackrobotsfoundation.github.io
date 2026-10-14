---
sidebar_position: 2
title: Instalación
sidebar_custom_props:
  icon: /img/guias/iconos/instalacion.svg
---

# Instalación

La Raspberry Pi arranca desde una **tarjeta microSD**. Instalarla consiste en grabar el sistema operativo en esa tarjeta desde tu ordenador. Después la puedes usar de dos formas: **como un ordenador**, con pantalla, teclado y ratón, o **a distancia**, desde tu ordenador por SSH.

<img src="/img/guias/raspberry/instalacion.svg" alt="Proceso de instalación: Raspberry Pi Imager, la microSD, el primer arranque y las dos formas de usarla, con pantalla o por SSH" />

## Qué necesitas

| Componente | Notas |
|---|---|
| Raspberry Pi 5 | o Pi 4 |
| Tarjeta microSD de 32 GB o más | clase A2: arranca y responde más rápido |
| Fuente USB-C oficial | **5 V y 5 A** para la Pi 5 (5 V y 3 A para la Pi 4) |
| Lector de tarjetas | para grabarla desde el ordenador |
| Disipador o caja con ventilador | recomendado en la Pi 5 |
| Pantalla, teclado y ratón | para usarla como ordenador |
| Cable **micro-HDMI a HDMI** | la Raspberry Pi 4 y la 5 tienen salidas micro-HDMI |

:::caution
Una fuente que se queda corta provoca reinicios y errores difíciles de entender. Usa la oficial o una de la misma potencia: el cargador de un móvil no suele bastar.
:::

## Qué sistema operativo elegir

| Sistema | Cuándo elegirlo |
|---|---|
| **Raspberry Pi OS (64 bits)** | para aprender Linux, Python y electrónica. Es el sistema oficial, trae escritorio y todo preparado |
| **Ubuntu 24.04** | para usar [ROS 2](/guias/ros2) en una Pi 5 (con ROS 2 Jazzy) |
| **Ubuntu 22.04** | para usar ROS 2 Humble en una Pi 4, la misma versión que usa el [Rover](/proyectos/rover-web) |

De Ubuntu hay dos versiones: **Desktop**, con escritorio, para usarla con pantalla; y **Server**, más ligera y sin escritorio, para un robot que controlas a distancia.

## 1. Grabar la tarjeta con Raspberry Pi Imager

1. Descarga **Raspberry Pi Imager** desde [raspberrypi.com/software](https://www.raspberrypi.com/software/) e instálalo
2. Elige el **modelo** de tu placa, el **sistema operativo** y la **tarjeta** donde grabarlo
3. Cuando te ofrezca **personalizar** el sistema, acepta y rellena:
   - **Nombre del equipo** (*hostname*), por ejemplo `robot`
   - **Usuario y contraseña**
   - **Wi-Fi**: el nombre de tu red, la contraseña y el país
   - **Activar SSH**, si quieres poder usarla también a distancia
4. Graba la tarjeta. Tarda unos minutos

## 2. Primer arranque

Mete la tarjeta en la Raspberry y conecta la alimentación **lo último**. El primer arranque tarda un par de minutos porque el sistema se termina de configurar. El LED verde parpadea mientras lee la tarjeta.

## 3. Usarla con pantalla, teclado y ratón

La forma más directa: la Raspberry se convierte en un ordenador de escritorio.

<img src="/img/guias/raspberry/escritorio.svg" alt="Raspberry Pi conectada a una pantalla por micro-HDMI, a un teclado y un ratón por USB y a su fuente por USB-C" />

| Cable | De la Raspberry a |
|---|---|
| micro-HDMI a HDMI | la pantalla. Usa el puerto **HDMI 0**, el más cercano al USB-C |
| USB | el teclado y el ratón |
| USB-C | la fuente de alimentación |

Al arrancar aparece el escritorio. Para escribir órdenes, abre la **Terminal** desde el menú o con **Ctrl+Alt+T**. Raspberry Pi OS trae además **Thonny**, un editor de Python muy sencillo con un botón para ejecutar el programa: ideal para empezar.

## 4. Usarla a distancia por SSH

En un robot no hay pantalla. **SSH** abre una terminal de la Raspberry en tu ordenador, a través de la red. Necesitas haber activado SSH al grabar la tarjeta. Desde la terminal de tu ordenador (en Windows, PowerShell):

```bash
ssh usuario@robot.local
```

Cambia `usuario` y `robot` por los que elegiste. La primera vez te pregunta si confías en el equipo: escribe `yes` y luego la contraseña.

:::tip
Si `robot.local` no responde, mira la IP de la Raspberry: con pantalla, ejecuta `hostname -I` en su terminal; sin pantalla, búscala en la configuración de tu router. Luego conéctate con ella: `ssh usuario@192.168.1.42`.
:::

Las dos formas se pueden combinar: aprende con pantalla y, cuando la montes en el robot, sigue trabajando por SSH.

## 5. Actualizar el sistema

Ya sea en la terminal de su escritorio o por SSH, lo primero es poner todo al día:

```bash
sudo apt update
sudo apt full-upgrade -y
sudo reboot
```

- `sudo` ejecuta el comando como administrador
- `apt` es el gestor de programas: instala, actualiza y desinstala

Ya tienes tu Raspberry lista para [el primer programa](./primer-programa).
