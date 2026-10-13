---
sidebar_position: 7
title: Cámara
sidebar_custom_props:
  icon: /img/guias/iconos/ejemplos.svg
---

# Cámara

Una cámara convierte a la Raspberry en un robot que **ve**: puede seguir un objeto de un color, leer códigos QR, detectar caras o grabar lo que encuentra. Las cámaras oficiales se conectan con un cable plano a su propio conector.

<img src="/img/guias/raspberry/camara.svg" alt="Camera Module 3 conectado con un cable plano al conector CAM/DISP de la Raspberry Pi 5" />

## Qué cámara

| Cámara | Notas |
|---|---|
| **Camera Module 3** | 12 MP con enfoque automático. Existe en gran angular y en versión sin filtro infrarrojo (para ver de noche con luz IR) |
| **Webcam USB** | funciona sin más, pero con más retardo y menos control |

:::caution[Cable de la Raspberry Pi 5]
La Pi 5 tiene conectores de cámara **más estrechos** que la Pi 4. Necesitas el cable específico para Pi 5 (de 22 a 15 pines), que se vende aparte. Conecta y desconecta la cámara siempre con la Raspberry **apagada**.
:::

## 1. Conectarla

1. Levanta con cuidado la pestaña del conector **CAM/DISP**
2. Mete el cable con los **contactos dorados** hacia el lado que marca la placa
3. Baja la pestaña. El cable debe quedar firme y recto

## 2. Probarla

En Raspberry Pi OS, las herramientas `rpicam` vienen instaladas:

```bash
rpicam-hello                      # vista previa durante 5 segundos
rpicam-still -o foto.jpg          # hace una foto
rpicam-vid -t 10000 -o video.h264 # graba 10 segundos de vídeo
```

`rpicam-hello` necesita pantalla para mostrar la imagen. Por SSH, usa `rpicam-still` y abre la foto en tu ordenador.

## 3. Hacer fotos desde Python

La librería **Picamera2** viene con Raspberry Pi OS:

```python
from picamera2 import Picamera2
import time

camara = Picamera2()
camara.start()
time.sleep(1)                 # deja que ajuste la exposición
camara.capture_file('foto.jpg')
camara.stop()
```

## 4. Seguir un objeto de un color

Con OpenCV (`sudo apt install python3-opencv`), cada fotograma se convierte en una matriz de píxeles que puedes analizar. Este programa busca el objeto **azul** más grande y te dice dónde está:

```python
import cv2
from picamera2 import Picamera2

camara = Picamera2()
config = camara.create_preview_configuration(main={'format': 'RGB888', 'size': (640, 480)})
camara.configure(config)
camara.start()

while True:
    imagen = camara.capture_array()               # los píxeles, listos para OpenCV
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    mascara = cv2.inRange(hsv, (100, 120, 70), (130, 255, 255))   # tonos azules

    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contornos:
        mayor = max(contornos, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(mayor)
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print('Objeto azul en x =', x + w // 2)

    cv2.imshow('Camara', imagen)
    if cv2.waitKey(1) == ord('q'):                # q para salir
        break
```

- **HSV** separa el color (H, el tono) de la luz (V, el brillo). Así el azul se detecta igual con más o menos luz
- `inRange()` deja en blanco los píxeles cuyo color está entre los dos límites
- `findContours()` agrupa esos píxeles en manchas y nos quedamos con la mayor

La posición `x` del objeto es justo lo que necesita un robot para **seguirlo**: si está a la izquierda del centro (320), gira a la izquierda; si está a la derecha, a la derecha. Con los [motores](./motores-y-servos) de la sección anterior, tienes un robot que persigue una pelota.

:::tip
Para otro color, cambia los límites de `inRange()`. En OpenCV el tono va de 0 a 180: rojo cerca de 0 o de 180, verde alrededor de 60 y azul alrededor de 120.
:::

## ¿Y ahora qué?

Detectar colores funciona muy bien con objetos claros y luz uniforme. Para reconocer **qué** es cada cosa (una persona, una taza, un perro) hacen falta redes neuronales, el terreno de la [Jetson](/guias/jetson/deteccion-de-objetos).
