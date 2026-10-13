---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

Leer un pulsador parece tan simple como conectarlo entre un pin y GND. Hay dos detalles que marcan la diferencia entre una lectura limpia y una que da saltos sin sentido: la **resistencia pull-up** y el **rebote**.

## El pin "al aire"

Cuando el pulsador está suelto, el pin se queda **desconectado de todo**. Un pin así está *flotando*: capta ruido eléctrico del ambiente y lee HIGH y LOW al azar, aunque nadie toque el botón.

La solución es una resistencia que lleve el pin a un valor conocido mientras el pulsador está suelto.

<img src="/img/guias/sensores/pulsadores/pull-up-pull-down.svg" alt="Circuitos pull-up y pull-down" />

### Pull-up

Una resistencia une el pin con **5 V**. Suelto, el pin lee **HIGH**. Al pulsar, el botón conecta el pin directamente a GND y lee **LOW**.

### Pull-down

La resistencia une el pin con **GND**. Suelto, lee **LOW**. Al pulsar, lee **HIGH**.

### La pull-up interna

El Arduino lleva dentro una resistencia pull-up en cada pin (de unos 20 – 50 kΩ). Se activa con una línea de código:

```cpp
pinMode(2, INPUT_PULLUP);
```

Con ella te ahorras la resistencia externa: el pulsador va directamente entre el pin y GND. Es la forma que usaremos.

:::note[Lógica invertida]
Con `INPUT_PULLUP`, **pulsado = LOW** y **suelto = HIGH**. Al principio despista; en cuanto lo tienes en cuenta en el código, deja de importar.
:::

## El rebote

Los contactos de un pulsador son dos láminas de metal. Al cerrarse, **rebotan** unas cuantas veces durante unos milisegundos antes de quedarse quietas:

<img src="/img/guias/sensores/pulsadores/rebote.svg" alt="Señal de un pulsador con rebotes al pulsar" />

El Arduino es tan rápido que ve cada rebote como una pulsación distinta. Si cuentas pulsaciones, una sola puede sumar 3 o 4.

La solución se llama **antirrebote** (*debounce*): después de detectar un cambio, esperas unos **20 – 50 ms** y solo lo das por bueno si sigue igual. Lo tienes resuelto en el [código básico](./codigo-basico#3-contar-pulsaciones-sin-rebotes).
