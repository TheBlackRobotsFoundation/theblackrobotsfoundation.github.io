---
sidebar_position: 3
title: Cómo se conecta
sidebar_custom_props:
  icon: /img/guias/iconos/conexion.svg
---

# Cómo se conecta

## Lista de componentes

| Componente | Cantidad |
|---|---|
| Arduino UNO | 1 |
| Motor brushless (por ejemplo 2212 920KV) | 1 |
| ESC de 20 – 30 A | 1 |
| Batería LiPo 3S (11,1 V) con su conector | 1 |
| Algo para sujetar el motor: una tabla y tornillos | 1 |

## Esquema de conexión

![Esquema: batería LiPo al ESC, ESC al motor y cable de servo al Arduino](/img/guias/actuadores/brushless/conexion.svg)

### Potencia

| De | A |
|---|---|
| Batería (+ y −) | cables gruesos del ESC (rojo y negro) |
| 3 cables del ESC | 3 cables del motor, en cualquier orden |

### Señal

| Cable de servo del ESC | Arduino |
|---|---|
| Señal (blanco o amarillo) | pin digital **9** |
| GND (marrón o negro) | **GND** |
| BEC (rojo) | sin conectar |

:::caution[Antes de conectar la batería]
1. **Quita la hélice**. Todas las pruebas, sin ella
2. **Sujeta el motor** a una tabla o un soporte firme: al arrancar da un tirón
3. Conecta primero el **Arduino por USB** y carga el programa del [código básico](./codigo-basico), que manda la señal de motor parado
4. Conecta la **batería** la última. El ESC pitará al armarse
:::

## El cable BEC

El cable rojo del conector de servo da **5 V** desde el ESC. Con el Arduino conectado por USB, déjalo **sin conectar**: dos fuentes de 5 V unidas pueden dañar el USB del ordenador.

Si en el robot final el Arduino no lleva otra alimentación, el BEC puede alimentarlo a través del pin **5V**. Hazlo solo con el USB desconectado.

## Conectores de la batería

Las baterías LiPo y los ESC suelen usar conectores **XT60** o **T-Plug (Deans)**. Si no coinciden, hay adaptadores. Comprueba siempre que el rojo va con el rojo.

Con todo conectado, pasa al [código básico](./codigo-basico).
