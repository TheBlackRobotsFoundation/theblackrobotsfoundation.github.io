---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es un motor brushless?

Un **motor brushless** (sin escobillas) es un motor eléctrico muy eficiente y potente para su tamaño. Gira a miles de revoluciones por minuto y apenas se desgasta, por eso es el que mueve los **drones**, los aviones de radiocontrol, los patinetes eléctricos y los discos duros.

Para funcionar necesita un **ESC** (*Electronic Speed Controller*, variador electrónico de velocidad), que convierte la corriente de la batería en la secuencia de pulsos que hace girar el motor.

![Motor brushless con su campana, el eje y los tres cables, y un ESC con sus conexiones](/img/guias/actuadores/brushless/anatomia.svg)

## El motor

- **Campana**: la parte exterior, que **gira** con el eje. En los motores de dron (*outrunner*), los imanes van pegados por dentro de ella
- **Estator**: la parte fija del centro, con las bobinas
- **3 cables**: uno por cada fase del motor

## El ESC

- **2 cables gruesos** (rojo y negro): a la batería
- **3 cables** hacia el motor
- **Cable de servo** de 3 hilos: **señal** (blanco o amarillo), **GND** (marrón o negro) y **BEC** (rojo)

El **BEC** (*Battery Eliminator Circuit*) es una salida de 5 V que trae el ESC para alimentar un receptor de radio o un servo. Si el Arduino ya tiene su alimentación, ese cable se deja sin conectar.

## Cómo se leen sus datos

Un motor brushless se identifica con unos números del tipo **2212 920KV**:

| Dato | Qué significa | En el ejemplo |
|---|---|---|
| **2212** | tamaño del estator: diámetro y altura en mm | 22 mm × 12 mm |
| **KV** | vueltas por minuto por cada voltio, sin carga | 920 rpm por voltio |

Con una batería de 11,1 V, un motor de 920 KV gira a unas `920 × 11,1 ≈ 10 200 rpm` sin hélice. Con hélice, algo menos.

- **KV alto**: más velocidad, para hélices pequeñas
- **KV bajo**: más par, para hélices grandes

## Brushless frente a motor DC

| | Motor DC | Brushless |
|---|---|---|
| Escobillas | sí: se desgastan | no |
| Eficiencia | 75 – 80 % | 85 – 90 % |
| Control | un [driver con puente H](/guias/actuadores/motores-dc) | un ESC |
| Cables | 2 | 3 |
| Uso típico | ruedas de robots | drones, hélices, vehículos rápidos |

:::danger[Seguridad]
Un motor brushless con hélice puede causar **cortes graves** en un instante. Haz todas las pruebas **sin hélice**, con el motor **sujeto** a algo firme, y desconecta la batería antes de tocar nada.
:::
