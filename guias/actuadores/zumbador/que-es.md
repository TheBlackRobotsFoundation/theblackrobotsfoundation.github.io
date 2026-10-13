---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es un zumbador?

Un **zumbador** (*buzzer*) es un pequeño altavoz que produce sonido cuando recibe una señal eléctrica. Es la forma más sencilla de que un robot **avise**: un pitido al arrancar, una alarma al detectar un obstáculo, una melodía al terminar una tarea.

## Activo o pasivo

Hay dos tipos que por fuera parecen iguales. Se distinguen mirando por debajo:

<img src="/img/guias/actuadores/zumbador/tipos.svg" alt="Zumbador activo, sellado por debajo, y pasivo, con la placa verde visible" />

| | Activo | Pasivo |
|---|---|---|
| Por debajo | sellado en negro | placa verde visible |
| Qué necesita | solo 5 V | una señal que oscile |
| Sonido | un único tono fijo | la nota que tú elijas |
| Código | `digitalWrite()` | `tone()` |
| Para qué | avisos y alarmas | melodías y efectos |

:::tip
¿No sabes cuál tienes? Móntalo como en la [conexión](./conexion) y carga el primer ejemplo del [código](./codigo-basico), que solo pone el pin en HIGH. Si pita, es **activo**. Si solo hace un clic, es **pasivo**.
:::

## Polaridad

Los zumbadores tienen una pata **+**, marcada en la carcasa y normalmente más **larga**. Los pasivos funcionan en cualquier sentido, pero conviene acostumbrarse a respetarla, porque los activos solo suenan bien conectados del derecho.

## En robótica

- **Confirmaciones**: un pitido corto cuando el robot recibe una orden o termina de arrancar
- **Alarmas**: batería baja, obstáculo demasiado cerca, caída detectada
- **Sensor de aparcamiento**: pitidos más rápidos cuanto más cerca está un objeto, con un [sensor de ultrasonidos](/guias/sensores/ultrasonidos)
- **Melodías**: para dar personalidad al robot
