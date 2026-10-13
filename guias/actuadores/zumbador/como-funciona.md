---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

El sonido es aire que vibra. El zumbador lleva dentro una **lámina** que se mueve hacia delante y hacia atrás cuando cambia la tensión, y al moverse empuja el aire.

- En los **piezoeléctricos**, la lámina es de un material que se deforma con la tensión
- En los **magnéticos**, una pequeña bobina atrae y suelta una lámina metálica

## Frecuencia y nota

Cada vez que la señal pasa de LOW a HIGH, la lámina da un empujón. El número de empujones por segundo es la **frecuencia**, en hercios (Hz), y decide la **nota**:

![Ondas cuadradas de distinta frecuencia: más pulsos por segundo dan una nota más aguda](/img/guias/actuadores/zumbador/frecuencia.svg)

- **Pocos pulsos por segundo** → sonido grave
- **Muchos pulsos por segundo** → sonido agudo
- **El doble de frecuencia** → la misma nota, una octava más aguda

| Nota | Frecuencia (octava 4) |
|---|---|
| Do (C4) | 262 Hz |
| Re (D4) | 294 Hz |
| Mi (E4) | 330 Hz |
| Fa (F4) | 349 Hz |
| Sol (G4) | 392 Hz |
| La (A4) | 440 Hz |
| Si (B4) | 494 Hz |

## Activo: el oscilador va dentro

El zumbador activo lleva un pequeño circuito que genera la oscilación por su cuenta. Tú solo lo enciendes y lo apagas: suena siempre a la misma frecuencia (normalmente unos 2,5 kHz).

## Pasivo: la oscilación la pones tú

El pasivo necesita que el Arduino genere la onda. La función `tone(pin, frecuencia)` lo hace por ti: enciende y apaga el pin a la frecuencia exacta que le pidas, sin que tengas que ocuparte de nada más.

:::note
`tone()` usa uno de los temporizadores internos del UNO. Mientras suena, el [PWM](/guias/electronica/pwm) de los pines **3 y 11** deja de funcionar. Si los necesitas para otra cosa, pon el zumbador en otro pin y usa esos dos para algo que no sea `analogWrite()`.
:::

## Resonancia

Cada zumbador suena **más fuerte** cerca de una frecuencia concreta (su frecuencia de resonancia, normalmente entre 2 y 4 kHz). Para una alarma que se oiga bien, usa frecuencias de esa zona.
