---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es el sensor sigue-líneas?

El **TCRT5000** es un sensor que lanza **luz infrarroja** hacia una superficie y mide cuánta vuelve. Una superficie clara refleja mucha luz; una oscura, muy poca. Con eso, el robot sabe si tiene debajo **una línea negra o el suelo blanco**.

Se vende montado en un pequeño módulo que da la respuesta lista para el Arduino.

![Módulo TCRT5000 con su emisor, su receptor, el potenciómetro y los pines](/img/guias/sensores/infrarrojos/anatomia.svg)

## Sus partes

- **Emisor infrarrojo**: un LED que emite luz a 950 nm, invisible para el ojo (la cámara del móvil sí la ve)
- **Receptor**: un fototransistor que deja pasar más corriente cuanta más luz recibe
- **Potenciómetro**: fija a partir de qué cantidad de luz el módulo dice "blanco"
- **LED indicador**: se enciende cuando detecta reflejo. Muy útil para ajustarlo
- **4 pines**: alimentación, una salida **digital** (DO) y otra **analógica** (AO)

## Características

| | TCRT5000 |
|---|---|
| Distancia de trabajo | 1 – 15 mm (ideal ~2 – 5 mm) |
| Alimentación | 3,3 – 5 V |
| Salidas | digital (DO) y analógica (AO) |

## En robótica

- **Robots sigue-líneas**: dos o más sensores debajo del robot siguen una cinta negra en el suelo. Es una de las competiciones más populares de robótica educativa
- **Detectar bordes**: un robot de sumo detecta el borde blanco del ring para no salirse
- **Contar objetos o vueltas**: una marca blanca en una rueda que pasa delante del sensor

:::note[Sensores de obstáculos IR]
Hay módulos parecidos (como el **FC-51**) con el emisor y el receptor separados, pensados para detectar objetos a unos centímetros. Funcionan con el mismo principio y se programan igual.
:::
