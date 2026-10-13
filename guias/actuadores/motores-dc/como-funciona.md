---
sidebar_position: 2
title: Cómo funciona
sidebar_custom_props:
  icon: /img/guias/iconos/conceptos.svg
---

# Cómo funciona

## Por dentro del motor

Un motor DC tiene **imanes fijos** en la carcasa y **bobinas** en la parte que gira. Al pasar corriente, las bobinas se convierten en electroimanes que son atraídos y repelidos por los imanes, y el eje gira.

Unas **escobillas** rozan contra el eje e invierten la corriente de las bobinas en el momento justo de cada vuelta, para que el empuje siga siempre en el mismo sentido.

Dos reglas que usarás todo el rato:

- **Invertir la polaridad** → gira al revés
- **Más tensión** → más velocidad

## El puente H: cambiar el sentido

Para invertir la polaridad sin tocar cables se usa un circuito llamado **puente H**: cuatro interruptores (transistores) colocados en forma de H, con el motor en el centro.

<img src="/img/guias/actuadores/motores-dc/puente-h.svg" alt="Puente H: cerrando S1 y S4 gira hacia delante; cerrando S2 y S3, hacia atrás" />

- Cerrando **S1 y S4**, la corriente cruza el motor de izquierda a derecha
- Cerrando **S2 y S3**, lo cruza al revés

El L298N lleva **dos puentes H**, uno por motor. Tú decides qué interruptores se cierran con los pines **IN**:

| IN1 | IN2 | Motor A |
|---|---|---|
| HIGH | LOW | gira hacia delante |
| LOW | HIGH | gira hacia atrás |
| LOW | LOW | se para (libre) |
| HIGH | HIGH | se para (frenado) |

Con **IN3 e IN4** se controla el motor B exactamente igual.

:::caution
Cerrar **S1 y S3** a la vez (los dos de un mismo lado) uniría la batería directamente con GND. El chip del puente H está diseñado para impedirlo: con los pines IN solo puedes elegir combinaciones seguras.
:::

## La velocidad: PWM en ENA

El pin **ENA** enciende y apaga el puente H del motor A. Si le mandas una señal [PWM](/guias/electronica/pwm), el motor recibe pulsos de batería y gira a una velocidad intermedia:

| `analogWrite(ENA, ...)` | Velocidad |
|---|---|
| 0 | parado |
| 128 | ~media |
| 255 | máxima |

Por debajo de cierto valor (a menudo 60 – 100) el motor **zumba sin llegar a girar**: no tiene fuerza suficiente para vencer el rozamiento. Cada motor tiene su mínimo; búscalo probando.

## Por qué no giran igual dos motores

Dos motores del mismo modelo siempre tienen pequeñas diferencias: con el mismo PWM, uno gira algo más rápido. Por eso un robot con dos ruedas tiende a desviarse aunque le mandes ir recto. Se compensa ajustando un poco la velocidad de uno de ellos o, mejor, midiendo cada rueda con [encoders](/guias/sensores/encoders).
