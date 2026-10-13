---
sidebar_position: 4
title: Conceptos básicos
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Conceptos básicos

## La terminal

En la Raspberry casi todo se hace desde la **terminal**: una ventana donde escribes órdenes. Con estas te mueves sin problema:

| Comando | Qué hace |
|---|---|
| `pwd` | dice en qué carpeta estás |
| `ls` | lista los archivos de la carpeta |
| `cd carpeta` | entra en una carpeta (`cd ..` sube una) |
| `mkdir nombre` | crea una carpeta |
| `nano archivo` | abre un archivo para editarlo |
| `cp`, `mv`, `rm` | copia, mueve y borra |
| `sudo comando` | ejecuta como administrador |
| `sudo apt install programa` | instala un programa |
| `python3 archivo.py` | ejecuta un programa de Python |
| `Ctrl+C` | para el programa que está en marcha |

:::tip
La tecla **Tab** completa nombres de archivos y comandos, y la **flecha arriba** repite los anteriores. Te ahorran muchísimo tiempo.
:::

## Los 40 pines

<img src="/img/guias/raspberry/pinout.svg" alt="Pinout de los 40 pines de la Raspberry Pi con alimentación, GND, GPIO, I2C, SPI y UART" />

- **5 V y 3,3 V**: alimentación para módulos. Los de 5 V salen directamente de la fuente
- **GND**: masa, varios repartidos
- **GPIO**: entradas y salidas digitales, a **3,3 V**
- Algunos GPIO tienen una segunda función: **I2C**, **SPI**, **UART** y **PWM**, los mismos [protocolos](/guias/electronica/comunicacion) que en Arduino

## Lo que hay que saber de los GPIO

- **Trabajan a 3,3 V.** Un sensor que da 5 V necesita un [divisor de tensión](/guias/electronica/divisor-de-tension) o un convertidor de nivel antes de llegar a un pin
- **Dan poca corriente**: unos 16 mA por pin. Para motores y relés, siempre a través de un [driver](/guias/actuadores/motores-dc) o un módulo
- **Solo son digitales.** Para leer un [potenciómetro](/guias/sensores/potenciometro) o una [LDR](/guias/sensores/ldr) hace falta un conversor analógico (como el ADS1115, por I2C) o un Arduino al lado

## Activar I2C, SPI y el puerto serie

En Raspberry Pi OS vienen desactivados. Se activan con:

```bash
sudo raspi-config
```

En **Interface Options** elige I2C, SPI o Serial Port y reinicia. Para ver los dispositivos I2C conectados (como hace el [escáner I2C](/guias/sensores/imu/codigo-basico#escáner-i2c) de Arduino):

```bash
sudo apt install i2c-tools
i2cdetect -y 1
```

## Programas que arrancan solos

En un robot, el programa debe ponerse en marcha al encender, sin conectarse por SSH. Linux lo hace con un **servicio** de *systemd*. Crea el archivo:

```bash
sudo nano /etc/systemd/system/robot.service
```

Con este contenido (cambia `usuario` y la ruta por los tuyos):

```ini
[Unit]
Description=Programa del robot
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/usuario/parpadeo.py
Restart=always
User=usuario

[Install]
WantedBy=multi-user.target
```

Y actívalo:

```bash
sudo systemctl enable --now robot.service
systemctl status robot.service      # comprueba que está en marcha
```

`Restart=always` lo vuelve a arrancar si falla. Para pararlo: `sudo systemctl stop robot.service`.

## Instalar librerías de Python

Raspberry Pi OS y Ubuntu prefieren que las librerías se instalen con `apt` cuando existen:

```bash
sudo apt install python3-serial python3-opencv
```

Para las que no están en `apt`, crea un **entorno virtual**: una carpeta con su propio Python donde instalar lo que quieras con `pip`:

```bash
python3 -m venv --system-site-packages ~/entorno
source ~/entorno/bin/activate
pip install nombre-de-la-libreria
```

`--system-site-packages` le permite usar también las librerías del sistema, como `gpiozero`.

## Editores para programar

| Editor | Cuándo |
|---|---|
| **Thonny** | con pantalla. Viene instalado, ejecuta con un botón y muestra las variables |
| **Visual Studio Code** | con pantalla (se instala con `sudo apt install code`) o desde tu ordenador con la extensión **Remote - SSH**, que abre las carpetas de la Raspberry como si fueran tuyas |
| **nano** | por SSH, para cambios rápidos en la terminal |

## Ver su escritorio desde tu ordenador

Con **Raspberry Pi Connect** ves y controlas el escritorio de la Raspberry desde el navegador de tu ordenador, sin pantalla conectada a ella. Viene con Raspberry Pi OS: actívalo desde el icono de la barra superior e inicia sesión con una cuenta de Raspberry Pi.

## ¿Y ahora qué?

Con esto ya puedes usar la Raspberry como cerebro de un robot. El siguiente paso es [conectarla con un Arduino](./raspberry-y-arduino), y después, [ROS 2](/guias/ros2).
