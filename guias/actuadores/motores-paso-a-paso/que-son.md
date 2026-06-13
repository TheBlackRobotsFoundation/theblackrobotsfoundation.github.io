---
sidebar_position: 1
title: ¿Qué son?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué son los motores paso a paso?

Un motor paso a paso (en inglés *stepper*) es un tipo de motor eléctrico que, en lugar de girar de forma continua como un motor normal, se mueve en **pasos discretos**: pequeños saltos de ángulo exactos y repetibles.

![Foto de un motor paso a paso](/img/guias/motores/motor-foto.jpg)

Piensa en la diferencia entre un grifo y un interruptor de la luz. Un motor normal es como el grifo: lo abres y gira sin más, sin saber exactamente cuánto. Un motor paso a paso es como ir pulsando un botón: cada pulsación lo avanza **un paso concreto**, y tú controlas exactamente cuántos pasos da.

## ¿Por qué son tan útiles en robótica?

La gran ventaja es que puedes saber **con precisión** en qué posición está el eje simplemente **contando los pasos** que le has ordenado, sin necesidad de sensores que midan la posición.

- **Precisión**: cada paso es un ángulo fijo, siempre el mismo
- **Control de posición sin sensores**: sabes dónde estás contando pasos
- **Buen par a baja velocidad**: ideales para mover ejes, correas y mecanismos
- **Mantienen la posición**: cuando están parados, "frenan" en su sitio y aguantan

Por eso son el motor estrella de las **impresoras 3D**, las **máquinas CNC**, los **plotters** y los **brazos robóticos**: en todos ellos hace falta mover algo a una posición exacta una y otra vez.

## El ángulo de paso

La mayoría de motores paso a paso tienen un ángulo de **1.8° por paso**. Como una vuelta completa son 360°:

```
360° / 1.8° = 200 pasos por vuelta
```

Es decir, hacen falta **200 pasos** para que el eje dé una vuelta entera. Esto es clave: si sabes los pasos, sabes el ángulo exacto que ha girado.

## Tipos de motores paso a paso

| Tipo | Cables | Características |
|---|---|---|
| **Bipolar** | 4 | Más par y eficiencia. Necesita un driver tipo puente H (A4988, DRV8825). |
| **Unipolar** | 5 o 6 | Más fáciles de controlar pero con menos par. Llevan una toma central en cada bobina. |

El más habitual en impresoras 3D, CNC y plotters es el **NEMA 17 bipolar**.

:::note[¿Qué significa "NEMA 17"?]
"NEMA 17" indica el **tamaño** del motor: la cara mide **1,7 × 1,7 pulgadas**, que equivalen a unos **42 × 42 mm**.
:::

## Limitaciones

No todo es perfecto. Conviene conocer sus puntos débiles:

- **Pierden par a alta velocidad**: cuanto más rápido giran, menos fuerza tienen
- **Pueden "perder pasos"**: si les pides demasiada velocidad o carga, se saltan posiciones y pierdes la cuenta
- **Consumen aunque estén parados**: para mantener la posición siguen gastando corriente

En las siguientes secciones verás [cómo funcionan por dentro](./como-funcionan), [cómo se conectan](./conexion) y [cómo mover uno con código](./codigo-basico).
