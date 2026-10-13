---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

## LED RGB

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| LED RGB de cátodo común | 1 |
| Resistencias de 220 Ω (rojo, rojo, marrón) | 3 |
| Protoboard y cables | — |

![Esquema: LED RGB con R al pin 11, G al 10, B al 9 a través de 220 Ω y la pata común a GND](/img/guias/actuadores/led-rgb/conexion-rgb.svg)

| LED RGB | Arduino |
|---|---|
| `R` | pin **11**, a través de 220 Ω |
| Pata común (la larga) | **GND** |
| `G` | pin **10**, a través de 220 Ω |
| `B` | pin **9**, a través de 220 Ω |

:::note[Ánodo común]
Si tu LED es de ánodo común, conecta la pata larga a **5V** en lugar de GND. El resto del montaje es igual.
:::

## Tira WS2812 (NeoPixel)

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Tira, anillo o matriz WS2812 (hasta 8 LEDs con esta conexión) | 1 |
| Resistencia de 330 Ω (naranja, naranja, marrón) | 1 |
| Condensador electrolítico de 1000 µF, 6,3 V o más | recomendado |

![Esquema: tira WS2812 con 5 V, GND y la entrada de datos al pin 6 a través de 330 Ω](/img/guias/actuadores/led-rgb/conexion-tira.svg)

| Tira | Arduino |
|---|---|
| `5V` | **5V** |
| `DIN` | pin **6**, a través de 330 Ω |
| `GND` | **GND** |

- La **resistencia de 330 Ω** en la línea de datos protege el primer LED de picos al conectar
- El **condensador de 1000 µF** entre 5V y GND, junto a la tira, absorbe los picos de consumo al encenderse. Respeta su polaridad: la franja va a GND

:::caution[Más de 8 LEDs]
Alimenta la tira con una **fuente de 5 V** propia, de al menos 60 mA por LED. Une su GND con el GND del Arduino, y conecta el 5V de la fuente a la tira. El Arduino solo aporta el cable de datos y GND.
:::

Con todo conectado, pasa al [código básico](./codigo-basico).
