---
sidebar_position: 5
title: Motores y servos
sidebar_custom_props:
  icon: /img/guias/iconos/configuracion.svg
---

# Motores y servos

La Raspberry puede mover motores directamente con sus pines, a través de un driver, igual que el Arduino. `gpiozero` trae clases ya preparadas para servos, motores e incluso robots completos de dos ruedas.

## Un servo

<img src="/img/guias/raspberry/servo.svg" alt="Servo SG90 con la señal en GPIO18, 5 V en el pin 4 y GND en el pin 6" />

| Servo | Raspberry Pi |
|---|---|
| Marrón (GND) | **GND** (pin 6) |
| Rojo (5 V) | **5V** (pin 4) |
| Naranja (señal) | **GPIO18** (pin 12) |

```python
from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_angle=0, max_angle=180,
                     min_pulse_width=0.0005, max_pulse_width=0.0025)

while True:
    for angulo in (0, 90, 180, 90):
        servo.angle = angulo
        sleep(1)
```

- `AngularServo` traduce el ángulo al pulso que espera el servo (lo tienes explicado en la guía de [servomotores](/guias/actuadores/servomotores/como-funciona))
- `min_pulse_width` y `max_pulse_width` son los pulsos de 0° y 180°: 0,5 y 2,5 ms valen para la mayoría de micro servos. Si el tuyo no llega a los extremos o zumba en ellos, ajústalos

:::note[Un poco de temblor]
La Raspberry genera estos pulsos con Linux funcionando a la vez, y a veces se retrasan unos microsegundos: el servo puede temblar un poco. Para un brazo con varios servos, la solución es una placa **PCA9685** (16 servos por I2C) o dejar los servos en un [Arduino](./raspberry-y-arduino), que genera los pulsos con precisión.
:::

Un SG90 se puede alimentar del pin de 5 V. Con más servos, o servos grandes, aliméntalos con una [fuente aparte](/guias/actuadores/servomotores/conexion) y une su GND con el de la Raspberry.

## Un motor DC con el L298N

<img src="/img/guias/raspberry/motor.svg" alt="Motor DC con un driver L298N: ENA a GPIO12, IN1 a GPIO16, IN2 a GPIO20 y GND común con la batería" />

El montaje es el de la guía de [motores DC](/guias/actuadores/motores-dc/conexion), cambiando el Arduino por la Raspberry:

| L298N | Raspberry Pi |
|---|---|
| `ENA` | **GPIO12** (pin 32) |
| `IN1` | **GPIO16** (pin 36) |
| `IN2` | **GPIO20** (pin 38) |
| `GND` | **GND** (pin 30), y al − de la batería |

```python
from gpiozero import Motor
from time import sleep

motor = Motor(forward=16, backward=20, enable=12)   # IN1, IN2 y ENA

motor.forward(0.6)     # 60 % hacia delante
sleep(2)
motor.stop()
sleep(1)
motor.backward(0.6)    # 60 % hacia atrás
sleep(2)
motor.stop()
```

La velocidad va de **0 a 1**. `Motor` aplica PWM al pin IN que corresponde a cada sentido y mantiene ENA activado.

:::caution
El L298N recibe órdenes de 3,3 V de la Raspberry y las entiende bien. Lo que **nunca** debe llegar a un pin de la Raspberry es la tensión de la batería: revisa que ningún cable de la batería toca la cabecera.
:::

## Un robot de dos ruedas

Con un segundo motor en OUT3/OUT4 (por ejemplo IN3 a **GPIO5**, IN4 a **GPIO6** y ENB a **GPIO13**), la clase `Robot` los maneja juntos:

```python
from gpiozero import Robot, Motor
from time import sleep

robot = Robot(left=Motor(16, 20, enable=12),
              right=Motor(5, 6, enable=13))

robot.forward(0.5)
sleep(2)
robot.left(0.5)        # gira sobre sí mismo
sleep(0.6)
robot.stop()
```

`Robot` tiene `forward()`, `backward()`, `left()`, `right()` y `stop()`, y `robot.value = (izquierdo, derecho)` para dar a cada rueda su velocidad, de −1 a 1.

## ¿Raspberry o Arduino para los motores?

Las dos opciones funcionan. Para empezar, conectar el driver directamente a la Raspberry es lo más sencillo. Cuando el robot crece, se suele pasar los motores a un [Arduino](./raspberry-y-arduino): sus pulsos son más precisos, aguanta mejor el ruido eléctrico de los motores y, si el programa de la Raspberry falla, el Arduino puede parar el robot por su cuenta.
