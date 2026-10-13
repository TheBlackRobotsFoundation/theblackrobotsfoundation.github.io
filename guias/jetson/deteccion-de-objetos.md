---
sidebar_position: 4
title: Detección de objetos
sidebar_custom_props:
  icon: /img/guias/iconos/ejemplos.svg
---

# Detección de objetos

Aquí es donde la Jetson brilla: una **red neuronal** mira cada fotograma de la cámara y dice qué hay, dónde y con qué seguridad. Con eso, el robot puede seguir a una persona, esquivar a un perro o buscar una taza.

<img src="/img/guias/jetson/deteccion.svg" alt="Fotograma con cajas alrededor de una persona, una taza y un perro, cada una con su nombre y su confianza" />

Usaremos **YOLO** (*You Only Look Once*), la familia de modelos de detección más popular, a través de la librería **Ultralytics**. Viene entrenado para reconocer 80 tipos de objetos: personas, coches, bicicletas, perros, gatos, tazas, sillas, móviles...

## 1. Instalar Ultralytics

En la Jetson, Ultralytics necesita la versión de PyTorch preparada para su GPU. Su [guía para Jetson](https://docs.ultralytics.com/guides/nvidia-jetson/) explica los dos caminos:

- **Con Docker**: una imagen ya preparada con todo instalado, la forma más rápida
- **Con pip**: instalando `ultralytics` y después las versiones de PyTorch y torchvision para tu JetPack que indica la guía

Comprueba al final que PyTorch ve la GPU, como en el [primer programa](./primer-programa#3-un-cálculo-en-la-gpu).

## 2. Detectar objetos en una imagen

```python
from ultralytics import YOLO

modelo = YOLO('yolo11n.pt')                 # la primera vez se descarga (6 MB)
resultados = modelo('https://ultralytics.com/images/bus.jpg')

for caja in resultados[0].boxes:
    nombre = modelo.names[int(caja.cls)]
    confianza = float(caja.conf)
    x1, y1, x2, y2 = caja.xyxy[0].tolist()
    print(f'{nombre:10s} {confianza:.2f}   x={x1:.0f}..{x2:.0f}')

resultados[0].save('resultado.jpg')         # la imagen con las cajas dibujadas
```

```
bus        0.94   x=4..796
person     0.89   x=671..810
person     0.88   x=47..239
person     0.86   x=223..344
person     0.62   x=0..69
```

- `yolo11n` es el modelo **nano**, el más pequeño y rápido. Hay versiones más grandes (`s`, `m`, `l`, `x`) que aciertan más pero van más despacio
- Cada caja trae su **clase** (`cls`), su **confianza** (`conf`, de 0 a 1) y sus **coordenadas** en píxeles (`xyxy`: esquina superior izquierda e inferior derecha)
- Los nombres de las clases están en inglés: `person`, `dog`, `cup`...

## 3. En directo con la cámara

```python
import cv2
from ultralytics import YOLO

modelo = YOLO('yolo11n.pt')
camara = cv2.VideoCapture(0)

while True:
    ok, imagen = camara.read()
    if not ok:
        break

    resultado = modelo(imagen, verbose=False)[0]
    cv2.imshow('Detecciones', resultado.plot())   # el fotograma con las cajas

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()
```

Abre `jtop` en otra terminal: verás la GPU trabajando en cada fotograma.

## 4. Del dibujo a una decisión

Para un robot, lo útil es convertir la detección en un número que pueda usar para moverse. Este fragmento busca la **persona más grande** (la más cercana) y calcula cuánto está desviada del centro de la imagen:

```python
ancho = imagen.shape[1]
personas = [c for c in resultado.boxes if modelo.names[int(c.cls)] == 'person']


def area(caja):
    x1, y1, x2, y2 = caja.xyxy[0].tolist()
    return (x2 - x1) * (y2 - y1)


if personas:
    mayor = max(personas, key=area)
    x1, y1, x2, y2 = mayor.xyxy[0].tolist()
    centro = (x1 + x2) / 2
    error = (centro - ancho / 2) / (ancho / 2)    # de -1 (izquierda) a 1 (derecha)
    print(f'persona en x={centro:.0f}, error {error:+.2f}')
```

Con ese `error`, girar es inmediato: velocidad de giro proporcional al error, y el robot mantiene a la persona en el centro. Es el mismo control que usarías para seguir un color con la [Raspberry Pi](/guias/raspberry/camara), con un detector mucho más listo.

## 5. Más velocidad con TensorRT

Para el programa final del robot, convierte el modelo a **TensorRT**: se optimiza para la GPU exacta de tu Jetson y va bastante más rápido.

```python
from ultralytics import YOLO

YOLO('yolo11n.pt').export(format='engine')   # crea yolo11n.engine (tarda unos minutos)
```

Y después úsalo igual, cargando el nuevo archivo:

```python
modelo = YOLO('yolo11n.engine')
```

:::note[Licencia]
Ultralytics y sus modelos YOLO se distribuyen con licencia **AGPL-3.0**: puedes usarlos libremente en proyectos abiertos como los de esta web. Si algún día los integras en un producto cerrado, revisa sus condiciones.
:::

## ¿Y ahora qué?

Con el `error` en la mano, publícalo en un topic de [ROS 2](/guias/ros2) y deja que otro nodo mueva los motores: la misma estructura que el [puente con Arduino](/guias/ros2/ros2-y-arduino).
