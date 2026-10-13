---
sidebar_position: 2
title: Montaje
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Montaje

## 1. El chasis

1. Atornilla los **dos motores** a la placa del chasis, con los ejes hacia fuera
2. Monta la **rueda loca** en la parte trasera (o delantera, según el kit)
3. Encaja las **ruedas** en los ejes de los motores
4. Si los motores no traen cables soldados, suelda dos a cada uno

:::tip
Antes de cerrar nada, comprueba que cada motor gira tocando sus cables con los de una pila. Así descartas un motor defectuoso antes de cablearlo todo.
:::

## 2. Colocar los módulos

- **HC-SR04** en el frontal, recto y algo elevado. Si apunta hacia abajo, detectará el suelo
- **L298N** en el centro, cerca de los motores
- **Arduino** donde quede accesible el puerto USB, para reprogramarlo sin desmontar
- **Baterías** abajo y centradas: así el robot no vuelca

Sujétalo todo con tornillos, bridas o cinta de doble cara.

## 3. Las conexiones

![Esquema completo del robot: HC-SR04, Arduino, L298N, batería y dos motores](/img/guias/proyecto-esquiva-obstaculos/conexion.svg)

### Sensor HC-SR04

| HC-SR04 | Arduino |
|---|---|
| `VCC` | **5V** |
| `Trig` | **A5** (el pin marcado como SCL también vale: es el mismo) |
| `Echo` | **A4** (o el pin SDA) |
| `GND` | **GND** |

Los pines analógicos funcionan también como **digitales**. Usando A4 y A5 para el sensor, todos los pines digitales del 6 al 11 quedan juntos para el driver.

### Driver L298N

| L298N | Arduino |
|---|---|
| `ENA` | pin **11** |
| `IN1` | pin **10** |
| `IN2` | pin **9** |
| `IN3` | pin **8** |
| `IN4` | pin **7** |
| `ENB` | pin **6** |

Quita los puentes de **ENA** y **ENB** antes de conectar sus cables (lo tienes explicado en la [guía de motores DC](/guias/actuadores/motores-dc/conexion)).

### Motores

| Motor | L298N |
|---|---|
| Izquierdo | `OUT1` y `OUT2` |
| Derecho | `OUT3` y `OUT4` |

### Alimentación

| De | A |
|---|---|
| Batería + (a través del interruptor) | `12V` del L298N |
| Batería − | `GND` del L298N **y** GND del Arduino |
| Power bank o pila de 9 V | puerto USB o jack del Arduino |

:::caution[GND común]
El cable que une el **− de la batería** con el **GND del Arduino** es imprescindible. Sin él, el driver no entiende las órdenes y los motores no se mueven o hacen cosas raras. Lo tienes explicado en [cómo alimentar un robot](/guias/electronica/alimentacion).
:::

## 4. Comprobaciones antes de encender

- [ ] Ningún cable de la batería toca un pin del Arduino
- [ ] Los puentes de ENA y ENB están quitados
- [ ] El GND de la batería, el del L298N y el del Arduino están unidos
- [ ] El robot está **con las ruedas en el aire** para la primera prueba

Todo listo: pasa al [código](./codigo).
