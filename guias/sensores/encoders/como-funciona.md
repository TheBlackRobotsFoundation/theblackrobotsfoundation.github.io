---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

El disco tiene **imanes con los polos alternados** (norte, sur, norte, sur...). Al girar, cada sensor Hall ve pasar los polos uno tras otro y su salida cambia entre HIGH y LOW.

![Disco magnético con polos alternados y los sensores A y B](/img/guias/sensores/encoders/disco.svg)

Cada cambio es un **pulso**. Contándolos sabes cuánto ha girado el eje.

## Dos sensores para saber el sentido

Con un solo sensor sabrías cuánto gira, pero no hacia dónde. Por eso hay dos, **A** y **B**, colocados de forma que sus señales quedan desplazadas un cuarto de ciclo (**90°**). Es lo que se llama **encoder de cuadratura**:

![Señales A y B desfasadas: el orden en que cambian indica el sentido de giro](/img/guias/sensores/encoders/cuadratura.svg)

- Si **A cambia antes que B**, gira en un sentido
- Si **B cambia antes que A**, gira en el otro

En la práctica: en el momento en que A sube, miras cómo está B. Si B está en LOW, cuentas +1; si está en HIGH, −1.

## Resolución: cuántos pulsos por vuelta

El fabricante indica los **PPR** (*pulses per revolution*) del encoder en el eje del motor, por ejemplo 11 PPR. La reductora multiplica esa cifra en la rueda:

```
pulsos por vuelta de rueda = PPR × reducción
```

Con 11 PPR y una reductora de 1:30:

```
11 × 30 = 330 pulsos por vuelta de rueda
```

Si cuentas todos los cambios de A y de B (subidas y bajadas), obtienes **4 veces más** resolución: 1320 cuentas por vuelta. A esto se le llama decodificación **×4**, y a esa cifra, **CPR** (*counts per revolution*).

## De pulsos a distancia

Una vuelta de rueda avanza lo que mide su circunferencia:

```
distancia = (pulsos / pulsos_por_vuelta) × π × diámetro
```

Con una rueda de 65 mm y 330 pulsos por vuelta, cada pulso son unos **0,62 mm**.

## Por qué hacen falta interrupciones

Un motor a 200 rpm con 330 pulsos por vuelta da más de **1000 pulsos por segundo**. Si el programa lee el pin dentro de `loop()`, se perderá muchos mientras hace otras cosas.

Las **interrupciones** lo resuelven: el Arduino deja lo que esté haciendo en el instante en que el pin cambia, ejecuta una función muy corta que cuenta el pulso y vuelve. En el UNO, los pines con interrupción son el **2** y el **3**.
