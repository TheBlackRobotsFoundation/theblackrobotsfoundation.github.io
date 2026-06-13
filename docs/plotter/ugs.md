---
id: plotter-ugs
title: UGS - conexión y configuración
sidebar_label: UGS (configuración)
sidebar_position: 7
---

# UGS: conexión y configuración

**UGS** (Universal G-code Sender) es el programa que usamos en el ordenador para hablar con el plotter: conectarnos a él, configurarlo, moverlo a mano y enviarle los dibujos. Toda la configuración de la máquina la haremos desde aquí.

![Captura de UGS](/img/plotter/ugs.png)

## Instalar UGS

1. UGS necesita tener **Java** instalado en el ordenador
2. Descarga UGS desde su página oficial (**universalgcodesender.com**)
3. Descomprime el archivo y abre el programa (no necesita instalación)

## Conectar con el plotter

1. Conecta el Arduino al ordenador por **USB**
2. Abre UGS
3. En la parte superior, selecciona:
   - **Firmware**: GRBL
   - **Puerto**: el que corresponde al Arduino
   - **Baudios**: 115200
4. Pulsa el botón de **conectar** (el icono del enchufe)
5. Si todo va bien, aparecerá el mensaje de bienvenida de GRBL en la consola

## Configurar los parámetros

Aquí está la ventaja de UGS: no hay que escribir comandos raros. Abre el panel de **Firmware Settings** (Ajustes del firmware) y verás una **tabla** con todos los parámetros de la máquina y su valor. Cambias el que quieras, guardas, y UGS lo envía al Arduino al momento.

Valores de partida recomendados:

| Parámetro | Qué controla | Valor inicial |
|---|---|---|
| `$100` | Pasos por mm del eje X | 80 |
| `$101` | Pasos por mm del eje Y | 80 |
| `$110` | Velocidad máxima X (mm/min) | 8000 |
| `$111` | Velocidad máxima Y (mm/min) | 8000 |
| `$120` | Aceleración X | 500 |
| `$121` | Aceleración Y | 500 |

:::note
No verás parámetros para el motor del slot A: al estar clonado del eje Y, copia automáticamente sus valores.
:::

## Calibrar los pasos por mm

Los valores `$100` y `$101` casi nunca son exactos a la primera. Para afinarlos, todo desde UGS:

1. Con los botones de movimiento (**jog**), mueve el eje X una distancia conocida, por ejemplo **100 mm**
2. Mide con una regla cuánto se movió **de verdad**
3. Calcula el valor correcto:
   `nuevo = valor_actual × (100 / lo_que_midió)`
4. Pon ese nuevo valor en `$100` (o `$101` para el eje Y) en Firmware Settings
5. Repite hasta que 100 mm pedidos sean 100 mm reales

Cuando los dos ejes estén calibrados, el plotter ya dibuja a escala real.
