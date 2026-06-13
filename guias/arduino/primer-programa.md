---
sidebar_position: 3
title: Tu primer programa
sidebar_custom_props:
  icon: /img/guias/iconos/ejemplos.svg
---

# Tu primer programa: Blink

El "Hola Mundo" de Arduino es hacer parpadear un LED. Usaremos el LED integrado en el pin 13, así que no necesitas ningún componente extra.

```cpp
void setup() {
  pinMode(13, OUTPUT);  // Configura el pin 13 como salida
}

void loop() {
  digitalWrite(13, HIGH);  // Enciende el LED
  delay(1000);             // Espera 1 segundo
  digitalWrite(13, LOW);   // Apaga el LED
  delay(1000);             // Espera 1 segundo
}
```

Pega este código en el IDE y pulsa el botón de subir (→). El LED parpadeará cada segundo.

## ¿Qué está pasando?

- `setup()` se ejecuta **una sola vez** al arrancar. Aquí configuramos el pin 13 como salida.
- `loop()` se repite **infinitamente**. Aquí encendemos, esperamos, apagamos y esperamos.
- `HIGH` = 5V (encendido), `LOW` = 0V (apagado).
- `delay(1000)` pausa el programa 1000 milisegundos = 1 segundo.

## Prueba a modificarlo

Cambia los `1000` por `200` y vuelve a subir el código. El LED parpadeará mucho más rápido. ¡Acabas de programar tu primer comportamiento!

## Monta tu propio LED (opcional)

El LED de la placa está bien para empezar, pero es mucho más satisfactorio ver parpadear un LED **tuyo**. Lo mejor: **el mismo código vale**, porque el pin 13 también sale a un pin físico de la placa.

Para montarlo necesitas un LED y una resistencia. Tienes los componentes, el esquema de conexión y más detalles en la guía del **[LED](/guias/actuadores/led/que-es)**.
