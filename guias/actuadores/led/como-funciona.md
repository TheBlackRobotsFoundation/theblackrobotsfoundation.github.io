---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona por dentro

Un LED es una **unión de dos materiales semiconductores**. Cuando la corriente cruza esa unión en el sentido correcto, la energía se libera en forma de **luz**. El color depende del material, no de "pintar" el LED: hay materiales que emiten en rojo, otros en verde, azul, etc.

## La caída de tensión

Cada LED "consume" una parte del voltaje al encenderse, lo que se llama **caída de tensión** (o *Vf*, voltaje directo). Es aproximada y depende del color:

| Color | Caída de tensión (aprox.) |
|---|---|
| Rojo | ~1.8 V |
| Amarillo / verde | ~2.0 – 2.2 V |
| Azul / blanco | ~3.0 – 3.4 V |

## La corriente: el dato que importa

Un LED no se controla por voltaje, sino por **corriente**. La mayoría funcionan bien con unos **10–20 mA** (miliamperios). Pasarse de ahí lo va quemando.

El problema es que un LED **no limita la corriente por sí mismo**: si le das de más, la acepta toda hasta destruirse. Por eso hace falta una **resistencia en serie** que haga de "freno".

## ¿Cuánta resistencia? La fórmula

Se calcula con la **Ley de Ohm**, restando primero la caída del LED al voltaje de tu fuente:

```
R = (V_fuente − V_led) / I_led
```

Por ejemplo, para un LED rojo en un Arduino (5 V), buscando unos 15 mA:

```
R = (5 V − 1.8 V) / 0.015 A ≈ 213 Ω
```

Como 213 Ω no es un valor comercial, se usa el más cercano hacia arriba: una resistencia de **220 Ω** es la elección típica y segura.

:::tip
Para empezar no hace falta calcular nada: una resistencia de **220 Ω o 330 Ω** va perfecta para casi cualquier LED a 5 V. La de 330 Ω lo deja un poco menos brillante, pero más protegido.
:::

:::caution
Sin resistencia, el LED (o incluso el pin del Arduino) se puede dañar. **Nunca** conectes un LED directamente entre un pin y GND.
:::
