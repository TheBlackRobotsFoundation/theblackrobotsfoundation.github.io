---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es el DHT22?

El **DHT22** (también llamado **AM2302**) es un sensor que mide **temperatura** y **humedad relativa** del aire, y envía las dos medidas ya calculadas al Arduino por **un solo cable de datos**.

Es tu primer sensor "inteligente": lleva un pequeño chip dentro que hace las medidas y te las entrega como números. Tú solo tienes que pedírselas.

<img src="/img/guias/sensores/temperatura/anatomia.svg" alt="Módulo DHT22 con su rejilla, su placa y sus tres pines" />

## Sensor suelto o módulo

El DHT22 se vende de dos formas:

- **Sensor suelto** (4 patas): necesita una resistencia pull-up de 10 kΩ en la línea de datos
- **Módulo** (3 pines, sobre una placa pequeña): ya trae la resistencia. Es el que usaremos

## Qué mide y con qué precisión

| | DHT22 | DHT11 |
|---|---|---|
| Temperatura | −40 a 80 °C | 0 a 50 °C |
| Precisión temperatura | ±0,5 °C | ±2 °C |
| Humedad | 0 – 100 % | 20 – 80 % |
| Precisión humedad | ±2 – 5 % | ±5 % |
| Lecturas | 1 cada 2 s | 1 por segundo |
| Color habitual | blanco | azul |

El **DHT11** es su hermano pequeño: más barato y menos preciso. Se conecta y se programa exactamente igual, cambiando una sola palabra en el código.

## En robótica y proyectos

- **Estación meteorológica**: el proyecto clásico con este sensor
- **Invernaderos y terrarios**: encender un ventilador o un riego con un [relé](/guias/actuadores/reles) cuando sube la temperatura
- **Robots de exterior**: vigilar la temperatura de la electrónica y de las baterías

:::note[Otros sensores de temperatura]
Si solo necesitas temperatura, hay alternativas: el **DS18B20** (también digital, existe en versión sumergible) o el **LM35** (analógico, se lee con `analogRead()`). La forma de trabajar que verás aquí te sirve para ambos.
:::
