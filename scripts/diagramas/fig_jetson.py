from lib import *
from parts import place
from placas import jetson
D = 'jetson/'

# --- placa anotada -----------------------------------------------------------
f = Fig(690, 340)
place(f, jetson, 200, 60, s=1.0)
callout(f, 270, 70, 270, 24, 'GPIO: 40 pines', sub='mismo formato que la Raspberry')
callout(f, 325, 179, 150, 120, 'Módulo Jetson Orin', sub='con disipador y ventilador', anchor='end')
callout(f, 480, 96, 580, 50, 'Ethernet')
callout(f, 486, 150, 580, 120, 'USB 3', sub='4 puertos')
callout(f, 484, 217, 580, 190, 'DisplayPort')
callout(f, 486, 243, 580, 240, 'USB-C')
callout(f, 482, 270, 580, 290, 'Alimentación', sub='jack de 19 V')
callout(f, 282, 299, 150, 300, '2 cámaras CSI', sub=None, anchor='end')
callout(f, 215, 230, 150, 220, 'M.2 (SSD NVMe)', sub='por debajo', anchor='end')
f.save(D + 'placa.svg')

# --- CPU frente a GPU ----------------------------------------------------------
f = Fig(640, 280)
f.rect(10, 10, 300, 260, fill='none', stroke=C['frame'], sw=1)
f.rect(330, 10, 300, 260, fill='none', stroke=C['frame'], sw=1)
f.title(28, 38, 'CPU', 'pocos núcleos muy capaces')
f.title(348, 38, 'GPU', 'cientos de núcleos sencillos')
for i in range(2):
    for j in range(3):
        f.rect(46 + j * 80, 82 + i * 80, 66, 66, fill=C['body2'], stroke=WIRE['b'], sw=1.5, rx=4)
for i in range(12):
    for j in range(22):
        f.rect(352 + j * 12, 80 + i * 12, 9, 9, fill='#2b3d14', stroke='#76b900', sw=0.8, rx=1)
f.text(160, 254, 'una tarea compleja detrás de otra', size=11, fill=C['muted'], anchor='middle')
f.text(480, 254, 'miles de operaciones iguales a la vez', size=11, fill=C['muted'], anchor='middle')
f.save(D + 'cpu-gpu.svg')

# --- JetPack: las capas -------------------------------------------------------
f = Fig(640, 330)
capas = [
    ('Tus programas', 'Python, ROS 2, visión, IA', C['text'], '#1c1c1c'),
    ('TensorRT · cuDNN · VPI', 'aceleran redes neuronales y visión', '#b6d77a', '#18210c'),
    ('CUDA', 'programación de la GPU', '#b6d77a', '#18210c'),
    ('Jetson Linux (Ubuntu 22.04)', 'el sistema operativo con los drivers de NVIDIA', C['accent'], '#161616'),
    ('Módulo Jetson', 'CPU Arm + GPU NVIDIA + memoria compartida', C['muted'], '#121212'),
]
for i, (t, sub, col, bg) in enumerate(capas):
    y = 20 + i * 58
    f.rect(120, y, 400, 50, fill=bg, stroke=C['edge'], rx=4)
    f.text(140, y + 22, t, size=13, weight=600, fill=col)
    f.text(140, y + 39, sub, size=10.5, fill=C['muted'])
f.path('M 100 76 L 92 76 L 92 250 L 100 250', stroke=C['dim'], sw=1.5)
f.text(84, 168, 'JetPack', size=12, weight=600, anchor='middle', rotate=-90, fill='#76b900')
f.save(D + 'jetpack.svg')
