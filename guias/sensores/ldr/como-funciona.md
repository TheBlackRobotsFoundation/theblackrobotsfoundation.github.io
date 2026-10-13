---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

El material de la pista libera más electrones cuanta más luz recibe. Más electrones libres significa que la corriente pasa con más facilidad, es decir, **menos resistencia**.

<img src="/img/guias/sensores/ldr/como-funciona.svg" alt="Curva de resistencia de la LDR según la luz y divisor de tensión para leerla" />

## De resistencia a tensión

El Arduino mide **tensiones**. Para leer una resistencia que cambia, se monta un [divisor de tensión](/guias/electronica/divisor-de-tension): la LDR arriba, una resistencia fija de **10 kΩ** abajo y el punto central a un pin analógico.

```
A0 = 5 V × 10 kΩ / (R_LDR + 10 kΩ)
```

| Luz | R_LDR | Tensión en A0 | `analogRead()` |
|---|---|---|---|
| Oscuridad | 1 MΩ | ~0,05 V | ~10 |
| Habitación | 10 kΩ | 2,5 V | ~512 |
| Luz directa | 1 kΩ | ~4,5 V | ~930 |

Con la LDR arriba, **más luz = número más alto**. Si la pones abajo, el comportamiento se invierte.

## Qué resistencia fija elegir

El divisor es más sensible cuando la resistencia fija se parece a la de la LDR en las condiciones que te interesan. **10 kΩ** va bien para luz de interior. Para detectar cambios en penumbra, prueba con 47 kΩ o 100 kΩ.

:::note
La LDR reacciona en unas decenas de milisegundos. Para detectar si es de día o de noche, de sobra; para detectar parpadeos rápidos, se usa un fotodiodo o un fototransistor.
:::
