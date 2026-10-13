---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es un potenciómetro?

Un **potenciómetro** es una resistencia variable con un mando giratorio. Es el control de volumen de toda la vida: lo giras y una magnitud sube o baja de forma continua.

Para un Arduino es la manera más directa de **leer una entrada analógica**: un valor que puede estar en cualquier punto entre el mínimo y el máximo.

<img src="/img/guias/sensores/potenciometro/anatomia.svg" alt="Potenciómetro rotativo con su eje y sus tres patas" />

## Sus tres patas

- **Los dos extremos**: van a 5 V y a GND
- **La central (cursor)**: da una tensión que depende de cuánto lo hayas girado

Si conectas los extremos al revés, el potenciómetro funciona igual, solo que **al revés**: el máximo queda donde estaba el mínimo.

## El valor que lleva escrito

Un potenciómetro se identifica por su **resistencia total**, entre los dos extremos. Para leerlo con Arduino, cualquier valor entre **1 kΩ y 100 kΩ** funciona; el de **10 kΩ** es el más habitual. A veces viene escrito como un código: `103` significa 10 × 10³ = 10 kΩ.

## Tipos

| Tipo | Cómo se ve | Uso |
|---|---|---|
| **Rotativo** | eje que gira unos 270° | mandos, ajustes |
| **Deslizante** | barra que se mueve en línea recta | mesas de mezclas |
| **Trimmer** | pequeño, se ajusta con destornillador | calibrar una vez y olvidarse |

El [driver A4988](/proyectos/plotter/plotter-vref) y el [sensor sigue-líneas](/guias/sensores/infrarrojos) llevan un trimmer para ajustar su comportamiento.

## En robótica

- **Mandos**: ajustar la velocidad de un motor o la posición de un [servo](/guias/actuadores/servomotores)
- **Medir ángulos**: unido a una articulación, el potenciómetro dice cuánto ha girado. Es justo lo que lleva un servo por dentro
- **Calibrar**: fijar un umbral, una ganancia o un brillo sin reprogramar
