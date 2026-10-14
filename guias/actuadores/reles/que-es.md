---
sidebar_position: 1
title: ¿Qué es?
sidebar_custom_props:
  icon: /img/guias/iconos/inicio.svg
---

# ¿Qué es un relé?

Un **relé** es un **interruptor que se acciona con electricidad**. Una señal pequeña (los 5 V de un pin del Arduino) mueve un contacto metálico que enciende o apaga otro circuito, que puede tener su propia alimentación y consumir mucha más corriente.

Los dos circuitos quedan **separados**: el Arduino solo controla el interruptor; la corriente de la carga pasa por los contactos del relé.

<img src="/img/guias/actuadores/reles/anatomia.svg" alt="Módulo de relé con el relé, el LED, las bornas de potencia y los pines de control" />

## El módulo de relé

El relé suelto necesita algunos componentes para conectarse al Arduino. El **módulo** los trae todos montados:

- **El relé**: la caja azul. Lleva escritos sus límites (por ejemplo `10A 250VAC`, `10A 30VDC`)
- **Un transistor**: da a la bobina del relé la corriente que el pin del Arduino no puede dar
- **Un diodo**: protege el circuito del pico de tensión que genera la bobina al apagarse
- **Un LED**: se enciende cuando el relé está activado
- **3 pines** de control: VCC, GND e IN
- **3 bornas** de potencia: NO, COM y NC

## Las bornas de potencia

Funcionan igual que en un [final de carrera](/guias/sensores/finales-de-carrera):

| Borna | Nombre | Conectada a COM |
|---|---|---|
| **COM** | común | — |
| **NO** | *normally open*, normalmente abierto | cuando el relé está activado |
| **NC** | *normally closed*, normalmente cerrado | cuando el relé está en reposo |

Lo habitual es usar **COM y NO**: la carga se enciende solo cuando el Arduino activa el relé.

## Para qué sirve

- **Ventiladores, bombas de agua, electroválvulas** de 12 V: riego automático, refrigeración
- **Tiras de LEDs** o luces de 12 V
- **Cortar la alimentación** de los motores de un robot como parada de emergencia
- Cualquier carga cuya tensión o corriente un pin no puede manejar

:::danger[Tensión de red (230 V)]
Aunque el relé admita 230 V, trabajar con la red eléctrica de casa es **peligroso**: un error puede provocar una descarga grave o un incendio. En estas guías todo el montaje funciona con **12 V o menos**. Si algún día necesitas controlar un aparato enchufado, usa un enchufe inteligente o un dispositivo certificado, o pide ayuda a un electricista.
:::
