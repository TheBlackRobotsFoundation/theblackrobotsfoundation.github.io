---
sidebar_position: 5
title: Raspberry Pi y Arduino
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Raspberry Pi y Arduino

La combinación más habitual en robótica: la **Raspberry Pi piensa** y el **Arduino actúa**. Se conectan con un simple cable USB y se hablan por el [puerto serie](/guias/electronica/comunicacion#uart-puerto-serie).

<img src="/img/guias/raspberry/arduino-usb.svg" alt="Raspberry Pi conectada por USB a un Arduino, con los mensajes que se intercambian" />

## Por qué los dos

- El **Arduino** responde en microsegundos, tiene entradas analógicas, trabaja a 5 V y aguanta mejor los golpes de la electrónica. Es perfecto para leer sensores y mover motores
- La **Raspberry** tiene la potencia para decidir, ver con una cámara, conectarse a la red y ejecutar [ROS 2](/guias/ros2)
- El cable USB lleva los datos y además **alimenta** el Arduino

## El idioma entre los dos

Se ponen de acuerdo en unos mensajes de texto sencillos, uno por línea:

| Mensaje | Quién lo envía | Significa |
|---|---|---|
| `D 42.5` | Arduino | la distancia medida es 42,5 cm |
| `M 150 150` | Raspberry | motor izquierdo a 150, derecho a 150 |
| `M -150 150` | Raspberry | gira sobre sí mismo |

## El programa del Arduino

Usa el sensor de la guía de [ultrasonidos](/guias/sensores/ultrasonidos) y el driver de la guía de [motores DC](/guias/actuadores/motores-dc). El sensor va en **A5 (Trig)** y **A4 (Echo)**, porque los pines 6 a 11 los usa el driver: los pines analógicos funcionan también como digitales.

```cpp
// Arduino conectado a una Raspberry Pi o una Jetson:
// envía la distancia y recibe la velocidad de cada motor.

#define TRIG A5   // sensor HC-SR04 (A5 y A4 funcionan como pines digitales)
#define ECHO A4

#define ENA 11    // driver L298N, montaje de la guía de motores DC
#define IN1 10
#define IN2 9
#define IN3 8
#define IN4 7
#define ENB 6

unsigned long ultimoEnvio = 0;
unsigned long ultimaOrden = 0;

void motores(int izq, int der) {
  izq = constrain(izq, -255, 255);
  der = constrain(der, -255, 255);
  digitalWrite(IN1, izq > 0);  digitalWrite(IN2, izq < 0);  analogWrite(ENA, abs(izq));
  digitalWrite(IN3, der > 0);  digitalWrite(IN4, der < 0);  analogWrite(ENB, abs(der));
}

float medirDistancia() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  long tiempo = pulseIn(ECHO, HIGH, 30000);
  if (tiempo == 0) return 400;   // sin eco: lo tratamos como lejos
  return tiempo * 0.0343 / 2;
}

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(20);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  int pines[] = {ENA, IN1, IN2, IN3, IN4, ENB};
  for (int p : pines) pinMode(p, OUTPUT);
  motores(0, 0);
}

void loop() {
  // 1. Órdenes de la Raspberry: "M izquierdo derecho"
  if (Serial.available() && Serial.read() == 'M') {
    int izq = Serial.parseInt();
    int der = Serial.parseInt();
    motores(izq, der);
    ultimaOrden = millis();
  }

  // 2. Seguridad: si dejan de llegar órdenes, para
  if (millis() - ultimaOrden > 500) {
    motores(0, 0);
  }

  // 3. Diez veces por segundo, envía la distancia: "D 42.5"
  if (millis() - ultimoEnvio >= 100) {
    ultimoEnvio = millis();
    Serial.print("D ");
    Serial.println(medirDistancia(), 1);
  }
}
```

La parada de seguridad es importante: si el programa de la Raspberry se cuelga o se desconecta el cable, el robot se detiene en medio segundo.

## El programa de la Raspberry

Conecta el Arduino a un USB de la Raspberry y comprueba en qué puerto aparece:

```bash
ls /dev/ttyACM* /dev/ttyUSB*
```

Los Arduino originales salen como `/dev/ttyACM0`; muchos clónicos, como `/dev/ttyUSB0`. Instala la librería para el puerto serie y da permiso a tu usuario para usarlo (después, cierra la sesión y vuelve a entrar):

```bash
sudo apt install python3-serial
sudo usermod -aG dialout $USER
```

Este programa lee las distancias y decide: si hay algo cerca, gira; si no, avanza.

```python
import time
import serial

arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
time.sleep(2)   # el Arduino se reinicia al abrir el puerto: le damos tiempo

while True:
    linea = arduino.readline().decode(errors='ignore').strip()
    if not linea.startswith('D '):
        continue

    distancia = float(linea[2:])
    print(f'Distancia: {distancia:.1f} cm')

    if distancia < 25:
        arduino.write(b'M -150 150\n')   # algo delante: gira
    else:
        arduino.write(b'M 150 150\n')    # camino libre: avanza
```

:::tip
Prueba primero con las **ruedas en el aire**. Si quieres ver solo las distancias, comenta las dos líneas de `arduino.write` con un `#` delante.
:::

## Alimentación del conjunto

- La **Raspberry** necesita su propia fuente estable de 5 V: un power bank potente o un regulador de 5 V y 5 A desde la batería del robot
- El **Arduino** se alimenta por el USB de la Raspberry
- Los **motores**, con su batería a través del driver, y con [GND común](/guias/electronica/alimentacion)

## ¿Y ahora qué?

Este "idioma" casero funciona muy bien para un robot pequeño. Cuando el robot crece (más sensores, mapas, navegación), lo habitual es pasar a [ROS 2](/guias/ros2), que organiza todo esto por ti. Tienes este mismo Arduino conectado a ROS 2 en [ROS 2 y Arduino](/guias/ros2/ros2-y-arduino).
