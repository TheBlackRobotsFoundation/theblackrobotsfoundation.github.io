# Hardware Setup

Guía para conectar y configurar el hardware del Rover.

## Diagrama de Conexiones

```
Jetson Orin
├── USB (ttyACM0) ──> RoboClaw Right (Motores derechos)
├── USB (ttyACM1) ──> RoboClaw Left (Motores izquierdos)
├── USB (ttyACM2) ──> PX4 (IMU, GPS)
├── USB (ttyUSB0) ──> RPLiDAR
└── UART (ttyTHS0) ──> FrSky FR6 Receiver
```

## Controladores de Motor - RoboClaw

### Conexión

**RoboClaw Right** (Ruedas derechas):
- Puerto USB: `/dev/ttyACM0`
- Dirección I2C: 128 (0x80)
- M1: Rueda delantera derecha
- M2: Rueda trasera derecha

**RoboClaw Left** (Ruedas izquierdas):
- Puerto USB: `/dev/ttyACM1`
- Dirección I2C: 128 (0x80)
- M1: Rueda delantera izquierda
- M2: Rueda trasera izquierda

### Configuración

1. Descargar e instalar Ion Motion Studio
2. Conectar cada RoboClaw via USB
3. Configurar:
   - Baud rate: 115200
   - Address: 128
   - Encoder mode: Quadrature
   - Max current: 15A

### PID Tuning

Valores iniciales en Motion Studio:
- P: 1.0
- I: 0.5
- D: 0.25
- QPPS: 3300 (ajustar según velocidad máxima de encoders)

## Encoders

- Tipo: Quadrature
- CPR: 4096 (counts per revolution)
- Conexión: Direct a RoboClaw (encoder inputs)

## PX4 Flight Controller

### Conexión

- Puerto USB: `/dev/ttyACM2`
- Firmware: PX4 v1.14+
- Protocolo: uXRCE-DDS

### Configuración

1. Instalar QGroundControl
2. Flashear firmware PX4
3. Habilitar uXRCE-DDS:
   ```
   UXRCE_DDS_CFG = 102 (TELEM 2)
   SER_TEL2_BAUD = 921600
   ```

### Sensores Disponibles

- IMU: Datos de aceleración y giroscopio
- Magnetómetro: Orientación
- GPS: Posición global (conectar módulo GPS externo)

## RPLiDAR

### Conexión

- Puerto USB: `/dev/ttyUSB0`
- Modelo: A1 (puede ser A2)
- Alimentación: 5V desde USB

### Montaje

- Posición: Centro del chasis, parte superior
- Frame: `lidar_link`
- Orientación: 0° apuntando hacia adelante

## Receptor FrSky FR6

### Conexión

- Protocolo: IBUS
- Puerto: UART Jetson (ttyTHS0)
- Baud rate: 115200
- Pines:
  - RX: GPIO TX
  - TX: GPIO RX
  - GND: GND
  - VCC: 5V

### Bindeado

1. Encender transmisor en modo bind
2. Conectar FR6 con botón bind presionado
3. LED debe parpadear y luego quedarse fijo

### Canales

1. Throttle (adelante/atrás)
2. Steering (izquierda/derecha)
3. Mode switch
4. Unused
5. Unused
6. Unused

## Verificación de Hardware

### Verificar Puertos

```bash
# Listar dispositivos USB
ls -l /dev/tty{ACM,USB}*

# Deberías ver:
# /dev/ttyACM0 -> RoboClaw Right
# /dev/ttyACM1 -> RoboClaw Left
# /dev/ttyACM2 -> PX4
# /dev/ttyUSB0 -> RPLiDAR
```

### Test de Comunicación

```bash
# Source workspace
source ~/Desktop/Rover/rover_bringup/install/setup.bash

# Test RoboClaw
ros2 run rover_diagnostics test_roboclaw.py

# Test IBUS
ros2 run rover_diagnostics test_ibus.py

# Test LIDAR
ros2 run rover_diagnostics test_lidar.py
```

## Udev Rules

Para nombres consistentes de dispositivos:

```bash
# Ver vendor/product IDs
lsusb

# Crear udev rules (ya incluido en setup.sh)
sudo nano /etc/udev/rules.d/99-rover.rules
```

Contenido:
```
# RoboClaw
SUBSYSTEM=="tty", ATTRS{idVendor}=="03eb", SYMLINK+="roboclaw%n"

# PX4
SUBSYSTEM=="tty", ATTRS{idVendor}=="26ac", SYMLINK+="px4"

# RPLiDAR
SUBSYSTEM=="tty", ATTRS{idVendor}=="10c4", SYMLINK+="rplidar"
```

Recargar:
```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

## Alimentación

### Baterías

- Tipo: LiPo 3S o 4S
- Capacidad: 5000mAh mínimo
- Conector: XT60

### Distribución de Poder

1. Batería -> Switch -> Regulador 12V
2. 12V -> RoboClaw x2 (power input)
3. 12V -> Regulador 5V -> Jetson Orin
4. 5V -> PX4, FR6, Sensores

### Safety

- Incluir fusibles en líneas principales
- Voltage monitor en batería
- Emergency stop switch

## Dimensiones y Montaje

### Chasis

- Largo: 300mm
- Ancho: 250mm
- Alto: 100mm

### Ruedas

- Diámetro: 150mm
- Radio: 75mm
- Ancho: ~40mm

### Mediciones para Calibración

```bash
# Medir wheelbase (distancia entre ejes)
ros2 run rover_calibration measure_wheelbase.py

# Medir track width (distancia entre ruedas)
ros2 run rover_calibration measure_track_width.py
```

## Troubleshooting

### No se detectan dispositivos USB

```bash
# Verificar permisos
ls -l /dev/ttyACM0
sudo chmod 666 /dev/ttyACM0

# O agregar usuario a dialout
sudo usermod -a -G dialout $USER
```

### RoboClaw no responde

- Verificar baud rate (115200)
- Verificar dirección I2C (128)
- Revisar conexión USB
- Reiniciar RoboClaw (desconectar/conectar)

### PX4 no publica datos

- Verificar uXRCE-DDS habilitado
- Verificar puerto correcto en QGroundControl
- Revisar baudrate

### LIDAR no gira

- Verificar alimentación 5V
- Revisar conexión USB
- Test con: `ros2 run rplidar_ros rplidar_node`

## Próximos Pasos

- [Quick Start](quickstart.md): Primer arranque del rover
