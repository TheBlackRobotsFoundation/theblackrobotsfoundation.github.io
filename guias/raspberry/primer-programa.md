---
sidebar_position: 3
title: Tu primer programa
sidebar_custom_props:
  icon: /img/guias/iconos/ejemplos.svg
---

# Tu primer programa: un LED y un pulsador

El "Hola Mundo" de la electrónica también funciona en la Raspberry: hacer parpadear un LED. La diferencia con Arduino es que aquí programas en **Python** y el programa corre dentro de Linux.

## El montaje

<img src="/img/guias/raspberry/led-pulsador.svg" alt="LED con resistencia de 220 ohmios en GPIO18 y pulsador en GPIO23, con sus GND" />

| Componente | Conexión |
|---|---|
| LED + resistencia de 220 Ω | **GPIO18** (pin físico 12) y **GND** (pin 14) |
| Pulsador | **GPIO23** (pin físico 16) y **GND** (pin 20), con patas en diagonal |

El LED y el pulsador son los mismos que en las guías de [LED](/guias/actuadores/led) y [pulsadores](/guias/sensores/pulsadores). Cada pin tiene dos nombres: el **número físico** (su posición en la cabecera) y el **número GPIO** (el que usa el código). Los tienes todos en [conceptos básicos](./conceptos-basicos#los-40-pines).

:::caution
Los pines de la Raspberry trabajan a **3,3 V**. Conectarles 5 V los daña. Un LED con su resistencia y un pulsador a GND son totalmente seguros.
:::

## 1. Hacer parpadear el LED

Abre un editor y crea el archivo `parpadeo.py`:

- **Con pantalla**: abre **Thonny** desde el menú de programación
- **Por SSH**: usa el editor de la terminal, con `nano parpadeo.py`

Escribe el programa:

```python
from gpiozero import LED
from time import sleep

led = LED(18)          # GPIO18, el pin físico 12

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

En Thonny, pulsa **Run** (el botón verde). En `nano`, guarda con **Ctrl+O** y **Enter**, sal con **Ctrl+X** y ejecútalo:

```bash
python3 parpadeo.py
```

El LED parpadea cada segundo. Para pararlo, pulsa **Stop** en Thonny o **Ctrl+C** en la terminal.

- `gpiozero` es la librería de Python para los pines de la Raspberry. Viene instalada en Raspberry Pi OS. En Ubuntu se instala con `sudo apt install python3-gpiozero python3-lgpio`
- `LED(18)` prepara el GPIO18 como salida
- `sleep(1)` espera un segundo, como el `delay(1000)` de Arduino

## 2. Encender el LED con el pulsador

```python
from gpiozero import LED, Button
from signal import pause

led = LED(18)
boton = Button(23)     # GPIO23, con su resistencia pull-up interna activada

boton.when_pressed = led.on
boton.when_released = led.off

pause()                # espera a que pase algo, sin gastar CPU
```

Aquí no hay un bucle que pregunte todo el rato por el botón. Le dices a la librería **qué hacer cuando pase algo** (*eventos*), y ella se encarga. `Button` ya activa la [resistencia pull-up](/guias/sensores/pulsadores/como-funciona) interna y filtra los rebotes.

## 3. Brillo con PWM

```python
from gpiozero import PWMLED
from time import sleep

led = PWMLED(18)

while True:
    for i in range(101):          # de 0 a 100 %
        led.value = i / 100
        sleep(0.01)
    for i in range(100, -1, -1):  # y de vuelta
        led.value = i / 100
        sleep(0.01)
```

`PWMLED` usa [PWM](/guias/electronica/pwm), como `analogWrite()` en Arduino, pero el brillo va de **0 a 1** en lugar de 0 a 255.

## ¿Qué ha cambiado respecto a Arduino?

| | Arduino | Raspberry Pi |
|---|---|---|
| Lenguaje | C++ | Python |
| Dónde corre | directamente en el chip | dentro de Linux, como un programa más |
| Subir el programa | compilar y enviar por USB | guardar el archivo y ejecutarlo |
| Parar | desenchufar o subir otro | Stop o Ctrl+C |
| Varios programas a la vez | uno | todos los que quieras |
