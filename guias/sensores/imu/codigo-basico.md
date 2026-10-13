---
sidebar_position: 4
title: Código básico
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Código básico para leer la IMU

Con SDA en A4 y SCL en A5. Usaremos la librería **Wire**, que viene con el Arduino IDE, para ver qué pasa por dentro.

## Escáner I2C

Antes de nada, comprueba que el Arduino ve el sensor. Este programa recorre todas las direcciones del bus y muestra las que responden:

```cpp
#include <Wire.h>

void setup() {
  Wire.begin();
  Serial.begin(115200);
  Serial.println("Buscando dispositivos I2C...");

  for (byte dir = 1; dir < 127; dir++) {
    Wire.beginTransmission(dir);
    if (Wire.endTransmission() == 0) {
      Serial.print("Encontrado en 0x");
      Serial.println(dir, HEX);
    }
  }
  Serial.println("Fin");
}

void loop() {}
```

Con el MPU6050 conectado debe aparecer **0x68**. Si no aparece nada, revisa SDA y SCL (es muy fácil intercambiarlos).

## 1. Leer los datos en bruto

```cpp
#include <Wire.h>

const int MPU = 0x68;

int16_t leer16() {
  int16_t alto = Wire.read();
  int16_t bajo = Wire.read();
  return (alto << 8) | bajo;
}

void setup() {
  Wire.begin();
  Wire.beginTransmission(MPU);
  Wire.write(0x6B);   // registro de energía
  Wire.write(0);      // lo despertamos (arranca dormido)
  Wire.endTransmission();
  Serial.begin(115200);
}

void loop() {
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);              // primer registro de datos
  Wire.endTransmission(false);
  Wire.requestFrom(MPU, 14);     // 14 bytes: acel, temperatura y giro

  float ax = leer16() / 16384.0;   // en g
  float ay = leer16() / 16384.0;
  float az = leer16() / 16384.0;
  float temp = leer16() / 340.0 + 36.53;   // en °C
  float gx = leer16() / 131.0;     // en °/s
  float gy = leer16() / 131.0;
  float gz = leer16() / 131.0;

  Serial.print(ax); Serial.print("\t");
  Serial.print(ay); Serial.print("\t");
  Serial.print(az); Serial.print("\t");
  Serial.print(gx); Serial.print("\t");
  Serial.print(gy); Serial.print("\t");
  Serial.println(gz);
  delay(50);
}
```

- Cada medida ocupa **2 bytes** (16 bits). `leer16()` los junta en un número
- **16384** y **131** convierten los números del chip a g y a °/s en los rangos por defecto (±2 g y ±250 °/s)

Con el sensor plano y quieto, `az` debe marcar cerca de **1** y el resto cerca de **0**. Abre el Serial Plotter y muévelo.

## 2. Inclinación con el acelerómetro

Sustituye las líneas de `Serial.print` del ejemplo anterior por:

```cpp
float roll  = atan2(ay, az) * 180.0 / PI;
float pitch = atan2(-ax, sqrt(ay * ay + az * az)) * 180.0 / PI;

Serial.print(roll);
Serial.print("\t");
Serial.println(pitch);
```

Inclínalo despacio: los ángulos son correctos. Dale golpecitos a la mesa: verás el ruido.

## 3. Ángulo estable con filtro complementario

Combinamos acelerómetro y giroscopio. Añade estas variables globales al ejemplo 1:

```cpp
float anguloRoll = 0, anguloPitch = 0;
unsigned long tAnterior = 0;
```

Y, en `loop()`, después de leer los datos:

```cpp
unsigned long ahora = micros();
float dt = (ahora - tAnterior) / 1000000.0;   // segundos desde la última vuelta
tAnterior = ahora;

float accRoll  = atan2(ay, az) * 180.0 / PI;
float accPitch = atan2(-ax, sqrt(ay * ay + az * az)) * 180.0 / PI;

anguloRoll  = 0.98 * (anguloRoll  + gx * dt) + 0.02 * accRoll;
anguloPitch = 0.98 * (anguloPitch + gy * dt) + 0.02 * accPitch;

Serial.print(anguloRoll);
Serial.print("\t");
Serial.println(anguloPitch);
```

Ahora el ángulo es suave, responde rápido y no deriva. Baja el `delay()` a 10 ms: el filtro funciona mejor cuanto más a menudo se ejecuta.

:::tip
Si el ángulo se va despacio hacia un lado, es el offset del giroscopio. Mide `gx` y `gy` con el sensor quieto, apunta su valor medio y réstalo en cada lectura.
:::

## Con una librería

Cuando quieras ir más rápido, la librería **Adafruit MPU6050** (Administrar Bibliotecas) te da las medidas ya convertidas a unidades y permite cambiar los rangos con una línea. Para orientación en 3D sin deriva, mira las librerías basadas en el procesador interno del chip (DMP), como **MPU6050** de Electronic Cats.

## ¿Y ahora qué?

Con la IMU sabes hacia dónde mira el robot; con los [encoders](/guias/sensores/encoders), cuánto avanza. El último paso para que un robot entienda su entorno es verlo entero: el [LiDAR](/guias/sensores/lidar).
