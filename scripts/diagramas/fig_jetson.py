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

# --- detección de objetos --------------------------------------------------------
f = Fig(680, 330)
f.rect(20, 20, 440, 290, fill='#101418', stroke=C['edge'], rx=4)
# suelo y pared
f.rect(20, 220, 440, 90, fill='#151a1e', stroke='none', sw=0)
# persona
f.circle(120, 112, 22, fill='#3a4450', stroke='none', sw=0)
f.rect(92, 138, 56, 110, fill='#3a4450', stroke='none', sw=0, rx=14)
# taza sobre una mesa
f.rect(250, 200, 160, 10, fill='#2a3036', stroke='none', sw=0, rx=2)
f.rect(300, 168, 30, 32, fill='#4a5560', stroke='none', sw=0, rx=4)
f.path('M 330 176 Q 344 184 330 192', stroke='#4a5560', sw=5)
# perro
f.rect(250, 248, 90, 40, fill='#3f3a34', stroke='none', sw=0, rx=14)
f.circle(345, 246, 16, fill='#3f3a34', stroke='none', sw=0)
for x in (262, 320):
    f.rect(x, 280, 10, 22, fill='#3f3a34', stroke='none', sw=0, rx=3)
def caja(x, y, w, h, t, k):
    f.rect(x, y, w, h, fill='none', stroke=WIRE[k], sw=2.2, rx=2)
    f.rect(x - 1, y - 18, len(t) * 7 + 10, 18, fill=WIRE[k], stroke='none', sw=0, rx=2)
    f.text(x + 4, y - 5, t, size=11, weight=600, fill=C['dark'], mono=True)
caja(84, 84, 74, 170, 'persona 0.91', 'c')
caja(294, 162, 54, 42, 'taza 0.84', 'a')
caja(240, 226, 128, 80, 'perro 0.88', 'b')
f.text(490, 60, 'Cada fotograma', size=14, weight=600)
f.text(490, 82, 'pasa por la red neuronal', size=12, fill=C['muted'])
f.text(490, 100, 'y sale con una lista:', size=12, fill=C['muted'])
for i, (t, k) in enumerate((('qué es', 'c'), ('dónde está', 'a'), ('con qué seguridad', 'b'))):
    y = 136 + i * 26
    f.circle(496, y - 4, 3.5, fill=C['accent'], stroke='none', sw=0)
    f.text(508, y, t, size=12)
f.text(490, 240, 'yolo11n en una Jetson', size=11, fill=C['dim'], mono=True)
f.text(490, 258, 'decenas de fotogramas', size=11, fill=C['dim'])
f.text(490, 274, 'por segundo', size=11, fill=C['dim'])
f.save(D + 'deteccion.svg')
