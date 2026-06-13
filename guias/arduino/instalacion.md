---
sidebar_position: 2
title: Instalación del IDE
sidebar_custom_props:
  icon: /img/guias/iconos/instalacion.svg
---

# Instalación del Arduino IDE

![El Arduino IDE](/img/guias/arduino-ide.png)

## ¿Qué es el IDE?

El **IDE** (*Integrated Development Environment*, entorno de desarrollo integrado) es el programa donde escribes tu código y lo subes a la placa. El **Arduino IDE** reúne en una sola ventana todo lo que necesitas: el **editor** para escribir el programa, el **compilador** que lo traduce a algo que entiende el microcontrolador, y la herramienta que lo **envía a la placa** por USB.

## Descargar e instalar

1. Ve a **[arduino.cc/en/software](https://www.arduino.cc/en/software)**
2. Descarga la versión para tu sistema operativo (Windows, Mac o Linux)
3. Instálalo como cualquier programa

## Configurar la placa

1. Conecta el Arduino al ordenador con el cable USB
2. Abre el Arduino IDE
3. Ve a **Herramientas → Placa** y selecciona tu modelo (ej. *Arduino UNO*)
4. Ve a **Herramientas → Puerto** y elige el puerto que aparece
   - En Windows será algo como `COM3`
   - En Linux/Mac será `/dev/ttyUSB0` o similar

## Verificar que funciona

Ve a **Archivo → Ejemplos → 01.Basics → Blink** y pulsa el botón de subir (la flecha →).

Si el LED de la placa empieza a parpadear, ¡todo está listo!

:::caution
Si el puerto no aparece en Windows, puede que necesites instalar el driver **CH340** o **CP2102**, según el chip USB de tu placa (muy común en placas clónicas).
:::
