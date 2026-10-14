---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

Hay dos circuitos separados: el de **control** (Arduino y módulo) y el de **potencia** (fuente, relé y carga).

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Módulo de relé de 5 V (1 canal) | 1 |
| Ventilador, bomba o tira de LEDs de 12 V | 1 |
| Fuente o batería de 12 V | 1 |
| Cables | — |

## Esquema de conexión

<img src="/img/guias/actuadores/reles/conexion.svg" alt="Esquema: módulo de relé al Arduino y ventilador de 12 V conmutado por COM y NO" />

### Control

| Módulo | Arduino |
|---|---|
| `VCC` | **5V** |
| `GND` | **GND** |
| `IN` | pin digital **7** |

### Potencia

1. **+ de la fuente** → borna **COM** del relé
2. Borna **NO** → **+ del ventilador**
3. **− del ventilador** → **− de la fuente**

El relé corta o deja pasar el cable positivo, como un interruptor puesto en ese cable.

:::caution
- Monta y revisa la parte de potencia **con la fuente desconectada**
- Respeta los límites que lleva escritos el relé
- La parte de potencia de estas guías trabaja siempre a **12 V**, lejos de la red eléctrica
:::

## Varios relés

Hay módulos de 2, 4 y 8 canales. Cada canal tiene su pin `IN` (IN1, IN2...) y comparten VCC y GND. Con más de dos relés activos a la vez, aliméntalos con una fuente de 5 V aparte: cada bobina consume unos 80 mA.

Con todo conectado, pasa al [código básico](./codigo-basico).
