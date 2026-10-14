import math, random
from lib import *
from parts import *
D = 'sensores/lidar/'

f = Fig(640, 300)
p = place(f, rplidar, 50, 0, s=1.9)
callout(f, 174, 142, 380, 40, 'Cabeza giratoria', sub='emisor láser y receptor')
callout(f, 150, 202, 380, 120, 'Motor y correa', sub='la hacen girar 360°, 5 – 10 vueltas por segundo')
callout(f, 70, 230, 380, 200, 'Base', sub='se atornilla al robot')
callout(f, 300, 152, 380, 260, 'Conector', sub='al adaptador USB')
f.save(D + 'anatomia.svg')

# barrido: habitación vista desde arriba
f = Fig(640, 360)
cx, cy = 200, 190
room = [(-150, -130), (150, -130), (150, 40), (90, 40), (90, 130), (-150, 130)]
def ray(a):
    # intersección del rayo con las paredes de la habitación (polígono) y una caja
    dx, dy = math.cos(a), math.sin(a)
    best = 1e9
    segs = list(zip(room, room[1:] + room[:1]))
    box = [(-60, -70), (-20, -70), (-20, -30), (-60, -30)]
    segs += list(zip(box, box[1:] + box[:1]))
    for (x1, y1), (x2, y2) in segs:
        ex, ey = x2 - x1, y2 - y1
        den = dx * ey - dy * ex
        if abs(den) < 1e-9:
            continue
        t = ((x1) * ey - (y1) * ex) / den
        u = ((x1) * dy - (y1) * dx) / den
        if t > 0 and 0 <= u <= 1:
            best = min(best, t)
    return best
f.poly([(cx + x, cy + y) for x, y in room], stroke=C['frame'], sw=1.5, close=True)
f.rect(cx - 60, cy - 70, 40, 40, fill='none', stroke=C['frame'], sw=1.5, rx=1)
rnd = random.Random(2)
for i in range(0, 360, 2):
    a = math.radians(i)
    d = ray(a) + rnd.uniform(-1.5, 1.5)
    if i % 30 == 0:
        f.line(cx, cy, cx + d * math.cos(a), cy + d * math.sin(a), stroke=WIRE['vcc'], sw=0.8, dash='2 4')
    f.circle(round(cx + d * math.cos(a), 1), round(cy + d * math.sin(a), 1), 1.8, fill=C['accent'], stroke='none', sw=0)
f.circle(cx, cy, 10, fill=C['body2'], stroke=C['accent'], sw=1.5)
f.circle(cx, cy, 3, fill=WIRE['vcc'], stroke='none', sw=0)
f.text(420, 120, 'Cada punto es una medida:', size=13, weight=600)
f.text(420, 142, 'un ángulo y una distancia.', size=13, weight=600)
f.text(420, 176, 'En una vuelta completa dibuja', size=12, fill=C['muted'])
f.text(420, 194, 'el contorno de lo que le rodea:', size=12, fill=C['muted'])
f.text(420, 212, 'paredes, puertas y obstáculos.', size=12, fill=C['muted'])
f.text(420, 250, '360 medidas por vuelta', size=12, mono=True, fill=C['accent'])
f.text(420, 270, '≈ 8000 medidas por segundo', size=12, mono=True, fill=C['accent'])
f.save(D + 'barrido.svg')

# triangulación
f = Fig(640, 230)
f.rect(40, 90, 60, 50, fill=C['body'], stroke=C['edge'], rx=3)
f.circle(70, 102, 5, fill=WIRE['vcc'], stroke='none', sw=0)
f.rect(56, 120, 28, 10, fill='#101010', stroke='#777', sw=1, rx=1)
f.text(70, 80, 'láser', size=10.5, fill=C['muted'], anchor='middle')
f.text(70, 160, 'sensor de imagen', size=10.5, fill=C['muted'], anchor='middle')
for (x, lab) in ((360, 'cerca'), (560, 'lejos')):
    f.line(75, 102, x, 102, stroke=WIRE['vcc'], sw=1.5)
    f.line(x, 102, 72, 124, stroke=WIRE['vcc'], sw=1.2, dash='4 4')
    f.rect(x, 70, 8, 64, fill='#2a2a2a', stroke=C['edge'], rx=1)
    f.text(x + 4, 160, lab, size=11, fill=C['muted'], anchor='middle')
f.text(40, 200, 'El ángulo con el que vuelve la luz cambia con la distancia: el sensor lo mide y calcula a cuánto está.', size=11, fill=C['muted'])
f.save(D + 'triangulacion.svg')

# conexión
f = Fig(640, 230)
p = place(f, rplidar, 20, 40, s=1.0)
a = place(f, adaptador_usb, 260, 98, s=1.0)
o = place(f, ordenador, 450, 60, s=1.0)
f.wire([p['cable'], a['in']], '#5a5a5a')
f.wire([a['usb'], (360, 115), (360, 154), o['usb']], '#5a5a5a')
f.text(85, 30, 'RPLIDAR A1', size=12, weight=600, anchor='middle')
f.text(290, 82, 'Adaptador', size=12, weight=600, anchor='middle')
f.text(290, 150, 'UART → USB', size=10.5, fill=C['muted'], anchor='middle')
f.text(530, 186, 'Ordenador o Raspberry Pi', size=12, weight=600, anchor='middle')
f.text(530, 204, '/dev/ttyUSB0', size=10.5, fill=C['muted'], anchor='middle', mono=True)
f.save(D + 'conexion.svg')
