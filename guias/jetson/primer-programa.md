---
sidebar_position: 3
title: Tu primer programa
sidebar_custom_props:
  icon: /img/guias/iconos/ejemplos.svg
---

# Tu primer programa: hola, GPU

Vamos a ver la GPU trabajando: primero vigilarla, luego usar una cámara y, por último, hacer un cálculo en la GPU y compararlo con la CPU.

## 1. Ver la Jetson por dentro con jtop

**jtop** es un monitor que muestra en tiempo real el uso de la CPU y la GPU, la memoria, la temperatura y el consumo. Instálalo:

```bash
sudo apt install -y python3-pip
sudo pip3 install -U jetson-stats
sudo reboot
```

Y ábrelo:

```bash
jtop
```

Déjalo abierto en una terminal mientras pruebas los siguientes ejemplos: verás subir el uso de la GPU. Se cierra con **q**.

## 2. Una cámara con OpenCV

OpenCV viene instalado con JetPack. Conecta una **webcam USB** y crea `camara.py`:

```python
import cv2

camara = cv2.VideoCapture(0)       # la primera cámara USB

while True:
    ok, imagen = camara.read()
    if not ok:
        break

    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    bordes = cv2.Canny(gris, 80, 160)   # detecta los contornos

    cv2.imshow('Camara', imagen)
    cv2.imshow('Bordes', bordes)
    if cv2.waitKey(1) & 0xFF == ord('q'):   # q para salir
        break

camara.release()
cv2.destroyAllWindows()
```

```bash
python3 camara.py
```

Se abren dos ventanas: la imagen de la cámara y sus contornos, calculados en cada fotograma. Es la base de cualquier programa de visión.

:::note
Las ventanas necesitan el escritorio de la Jetson. Si estás conectado por SSH, ejecútalo desde una terminal del propio escritorio.
:::

## 3. Un cálculo en la GPU

Las librerías de IA, como **PyTorch**, usan la GPU a través de CUDA. NVIDIA publica una versión de PyTorch preparada para cada JetPack: instálala siguiendo su guía [PyTorch for Jetson](https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/index.html).

Con PyTorch instalado, este programa multiplica dos matrices enormes en la CPU y en la GPU:

```python
import time
import torch

print('GPU disponible:', torch.cuda.is_available())
print('GPU:', torch.cuda.get_device_name(0))

a = torch.rand(4000, 4000)
b = torch.rand(4000, 4000)

t = time.time()
a @ b
print(f'CPU: {time.time() - t:.2f} s')

a, b = a.cuda(), b.cuda()       # los datos pasan a la GPU
a @ b
torch.cuda.synchronize()        # primera vez: la GPU se "despierta"

t = time.time()
a @ b
torch.cuda.synchronize()        # espera a que la GPU termine
print(f'GPU: {time.time() - t:.3f} s')
```

Son 64 000 millones de operaciones. La GPU lo resuelve muchas veces más rápido que la CPU: esa diferencia es la que permite detectar objetos en vídeo en tiempo real.

- `torch.cuda.is_available()` debe decir `True`. Si dice `False`, la versión de PyTorch instalada no es la de NVIDIA para Jetson
- `.cuda()` mueve los datos a la memoria de la GPU
- `synchronize()` espera a que la GPU acabe, para medir el tiempo de verdad

## ¿Y ahora qué?

El siguiente paso natural es **detectar objetos** con una red neuronal ya entrenada. La librería **Ultralytics** (modelos YOLO) tiene una [guía específica para Jetson](https://docs.ultralytics.com/guides/nvidia-jetson/) y con unas pocas líneas detecta personas, coches o tazas en la imagen de tu cámara.
