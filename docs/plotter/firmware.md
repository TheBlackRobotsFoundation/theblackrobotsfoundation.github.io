---
id: plotter-firmware
title: Cargar el firmware (GRBL)
sidebar_label: Cargar el firmware
sidebar_position: 3
---

<div style={{textAlign: 'center'}}>
  <img src="/img/plotter/grbl-logo.png" alt="Logo de GRBL" width="320" />
</div>

# Cargar el firmware (GRBL)

Un Arduino recién comprado no sabe lo que es un plotter. Hay que darle un "cerebro": un programa llamado **GRBL** que recibe el G-code y se encarga de mover los motores. Esto solo se hace **una vez**.

## ¿Qué es GRBL?

GRBL es un firmware gratuito y open source, el estándar para controlar máquinas CNC con Arduino. Una vez cargado, el Arduino queda listo para entender las órdenes de movimiento.

## Pasos para cargarlo

La forma más cómoda es instalar GRBL directamente desde el **Gestor de librerías** del Arduino IDE, sin descargar ningún `.zip` a mano:

1. Abre el **Arduino IDE**
2. Ve a **Programa → Incluir librería → Gestionar bibliotecas…** (o pulsa el icono de los libros en la barra lateral)
3. En el buscador escribe **`grbl`** e instala la librería **GRBL** (la de *Sungeun K. Jeon*)
4. Abre **Archivo → Ejemplos → grbl → grblUpload**
5. Conecta el Arduino por USB y selecciona la placa **Arduino UNO** y el **puerto** correcto
6. Pulsa el botón **Subir** (la flecha →)
7. Cuando aparezca "Subido", GRBL ya está dentro del Arduino

:::note
No hace falta configurar nada todavía. Todos los parámetros (velocidad, pasos por milímetro, etc.) los ajustaremos más adelante de forma cómoda **desde UGS**, sin escribir comandos a mano.
:::
