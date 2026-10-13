# Diagramas de las guías

Scripts en Python que generan los SVG de `static/img/guias/` (electrónica, sensores, actuadores, Raspberry Pi, Jetson y ROS 2).

- `lib.py`: paleta, figura, cables y el Arduino UNO
- `parts.py`: componentes (sensores, módulos, motores...)
- `placas.py`: Raspberry Pi, su cabecera de 40 pines y Jetson
- `fig_*.py`: un script por guía

Para regenerar una guía:

```bash
cd scripts/diagramas
python3 fig_ultrasonidos.py
```

Solo usan la librería estándar de Python. Los colores de los cables siguen siempre el mismo código: rojo alimentación, gris GND y un color por señal.
