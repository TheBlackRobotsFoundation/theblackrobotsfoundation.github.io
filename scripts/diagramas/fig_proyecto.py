from lib import *
from parts import *
D = 'proyecto-esquiva-obstaculos/'

# --- diagrama de bloques ----------------------------------------------------
f = Fig(640, 250)
def caja(x, y, w, t, sub, k=None):
    f.rect(x, y, w, 58, fill=C['body'], stroke=WIRE[k] if k else C['edge'], rx=4)
    f.text(x + w / 2, y + 26, t, size=13, weight=600, anchor='middle')
    f.text(x + w / 2, y + 43, sub, size=10.5, fill=C['muted'], anchor='middle')
caja(20, 96, 140, 'HC-SR04', 'mide la distancia', 'b')
caja(250, 96, 140, 'Arduino UNO', 'decide qué hacer')
caja(480, 96, 140, 'L298N', 'mueve los motores', 'a')
caja(480, 186, 140, 'Batería', 'alimenta los motores', 'vcc')
caja(480, 6, 140, '2 motores', 'las ruedas')
f.line(162, 125, 246, 125, stroke=C['accent'], sw=1.5, arrow='end')
f.line(392, 125, 476, 125, stroke=C['accent'], sw=1.5, arrow='end')
f.line(550, 94, 550, 68, stroke=C['accent'], sw=1.5, arrow='end')
f.line(550, 184, 550, 158, stroke=C['accent'], sw=1.5, arrow='end')
f.text(204, 116, 'distancia', size=10, fill=C['muted'], anchor='middle')
f.text(434, 116, 'órdenes', size=10, fill=C['muted'], anchor='middle')
f.save(D + 'bloques.svg')

# --- lógica ---------------------------------------------------------------
f = Fig(640, 300)
def nodo(x, y, w, t, rombo=False, k=None):
    if rombo:
        h = 44
        f.poly([(x, y - h), (x + w / 2, y), (x, y + h), (x - w / 2, y)], close=True, fill=C['body'], stroke=WIRE[k] if k else C['edge'], sw=1.5)
    else:
        f.rect(x - w / 2, y - 22, w, 44, fill=C['body'], stroke=WIRE[k] if k else C['edge'], rx=4)
    f.text(x, y + 4, t, size=12, weight=600, anchor='middle')
nodo(110, 60, 170, 'Medir distancia', k='b')
nodo(110, 170, 170, '¿Menos de 25 cm?', rombo=True)
nodo(110, 270, 150, 'Avanzar')
nodo(460, 170, 220, 'Parar, retroceder y girar', k='a')
f.line(110, 82, 110, 124, stroke=C['accent'], sw=1.5, arrow='end')
f.line(110, 214, 110, 246, stroke=C['accent'], sw=1.5, arrow='end')
f.line(197, 170, 348, 170, stroke=C['accent'], sw=1.5, arrow='end')
f.text(118, 234, 'no', size=11, fill=C['muted'])
f.text(270, 162, 'sí', size=11, fill=C['muted'], anchor='middle')
f.path('M 35 270 L 14 270 L 14 60 L 23 60', stroke=C['dim'], sw=1.5, arrow='end')
f.path('M 460 148 L 460 60 L 197 60', stroke=C['dim'], sw=1.5, arrow='end')
f.text(330, 52, 'y vuelta a empezar', size=10.5, fill=C['dim'], anchor='middle')
f.save(D + 'logica.svg')

# --- conexión completa ------------------------------------------------------
f = Fig(760, 690)
u = Uno(f, 180, 420, used={'5V', 'GND', 'SDA', 'SCL', 'D11', 'D10', 'D9', 'D8', 'D7', 'D6'})
hc = place(f, hcsr04, 214, 60, s=0.7)
bat = place(f, bateria, 330, 121, s=1.0, texto='7,4 V', sub='batería motores')
q = place(f, l298n, 720, 120, s=1.0, rot=90)
ma = place(f, motor_dc, 685, 30, s=0.7, rot=90)
mb = place(f, motor_dc, 635.3, 408, s=0.7, rot=-90)

v5, gnd = u.pin('5V'), u.pin('GND')
# sensor
f.wire([hc['VCC'], (hc['VCC'][0], 360), (150, 360), (150, 656), (v5[0], 656), v5], 'vcc')
f.wire([hc['Trig'], (hc['Trig'][0], u.pin('SCL')[1])], 'b')
f.wire([hc['Echo'], (hc['Echo'][0], u.pin('SDA')[1])], 'c')
f.wire([hc['GND'], (hc['GND'][0], 390), (gnd[0], 390), gnd], 'gnd')
# batería
f.wire([bat['+'], (q['12V'][0], bat['+'][1])], 'vcc')
f.wire([bat['−'], (510, bat['−'][1]), (510, q['GND'][1]), q['GND']], 'gnd')
f.wire([(480, bat['−'][1]), (480, 200), (hc['GND'][0], 200)], 'gnd')
f.node(480, bat['−'][1], 'gnd')
f.node(hc['GND'][0], 200, 'gnd')
# control
pins = [('ENA', 'D11', 'a'), ('IN1', 'D10', 'e'), ('IN2', 'D9', 'e'), ('IN3', 'D8', 'e'), ('IN4', 'D7', 'e'), ('ENB', 'D6', 'a')]
for k, d, col in pins:
    a, b = q[k], u.pin(d)
    f.wire([a, (b[0], a[1]), b], col)
# motores
for (m, o1, o2) in ((ma, 'OUT1', 'OUT2'), (mb, 'OUT3', 'OUT4')):
    pts = sorted([m['+'], m['−']], key=lambda p: -p[0])
    outs = sorted([q[o1], q[o2]], key=lambda p: -p[0])
    for p_, o_ in zip(pts, outs):
        f.wire([p_, o_], '#9a9a9a')
f.text(277, 44, 'HC-SR04', size=12, weight=600, anchor='middle')
f.text(588, 60, 'Motor izquierdo', size=11, weight=600, anchor='end')
f.text(588, 386, 'Motor derecho', size=11, weight=600, anchor='end')
f.text(735, 220, 'L298N', size=12, weight=600, anchor='middle', rotate=90)
legend(f, 180, 684, [('vcc', '5 V y batería'), ('gnd', 'GND común'), ('b', 'Trig → A5'), ('c', 'Echo → A4'), ('a', 'ENA/ENB'), ('e', 'IN1 – IN4')], gap=96)
f.save(D + 'conexion.svg')
