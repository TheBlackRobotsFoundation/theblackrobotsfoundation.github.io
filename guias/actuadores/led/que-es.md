---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es un LED?

Un **LED** (del inglés *Light Emitting Diode*, "diodo emisor de luz") es un pequeño componente electrónico que **emite luz cuando pasa corriente por él**. Es barato, dura muchísimo, consume muy poco y es el primer componente que monta casi todo el mundo al empezar con electrónica.

![Foto de un LED](/img/guias/led/led-foto.jpg)

## Es un diodo: tiene polaridad

Lo más importante de un LED es que es un **diodo**, y un diodo solo deja pasar la corriente **en un sentido**. Por eso un LED tiene **polaridad**: hay que conectarlo del derecho o no lucirá.

Para distinguir sus dos patas:

- **Pata larga → ánodo (+)**: va hacia el lado positivo
- **Pata corta → cátodo (−)**: va hacia masa (GND)

:::tip
Si te cuesta recordarlo: la pata **larga** es la del **+** (tiene "más" pata). Otra pista: el LED suele tener un **lado plano** en el borde, y ese lado es el **cátodo (−)**.
:::

## ¿Por qué son tan útiles?

- **Indicadores**: avisan de si algo está encendido, conectado o funcionando
- **Señalización**: semáforos, luces de aviso, efectos
- **Aprender**: son la forma perfecta de comprobar que tu código y tus conexiones funcionan

De hecho, el primer programa de casi cualquier placa (el famoso *Blink*) consiste en **hacer parpadear un LED**.

## Lo que nunca debes olvidar

Un LED **siempre necesita una resistencia** que limite la corriente. Si lo conectas directamente a 5V, le entra demasiada corriente y **se quema** (a veces al instante). Verás el porqué en la siguiente sección.
