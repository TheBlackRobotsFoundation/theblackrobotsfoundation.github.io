import math
from lib import *
from parts import *
D = 'sensores/encoders/'

f = Fig(640, 270)
p = place(f, motor_encoder, 60, 60, s=1.6)
callout(f, 100, 180, 100, 240, 'Reductora', sub=None)
callout(f, 220, 170, 220, 240, 'Motor DC')
callout(f, 308, 82, 250, 30, 'Disco magnético', anchor='end')
callout(f, 332, 205, 440, 240, 'Placa del encoder', sub='dos sensores Hall: A y B')
callout(f, 422, 82, 460, 40, '6 cables', sub='motor, alimentación, A y B')
f.save(D + 'anatomia.svg')

# disco + pulsos
f = Fig(640, 260)
cx, cy, r = 130, 130, 80
for i in range(12):
    a0, a1 = i * 30, i * 30 + 30
    col = '#3a3a3a' if i % 2 else '#1a1a1a'
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    f.path(f'M {cx} {cy} L {x0:.1f} {y0:.1f} A {r} {r} 0 0 1 {x1:.1f} {y1:.1f} Z', fill=col, stroke=C['edge'], sw=1)
f.circle(cx, cy, 22, fill=C['dark'], stroke=C['edge'])
f.path(f'M {cx + 30} {cy - 100} A 100 100 0 0 1 {cx + 100} {cy - 30}', stroke=C['muted'], sw=1.5, arrow='end')
for (sx, sy, n, k) in ((cx + 96, cy - 18, 'A', 'a'), (cx + 92, cy + 34, 'B', 'c')):
    f.rect(sx, sy - 9, 22, 18, fill=C['body'], stroke=WIRE[k], sw=2, rx=2)
    f.text(sx + 30, sy + 4, n, size=13, weight=600, fill=WIRE[k])
f.text(cx, 245, 'imanes N y S alternados', size=11, fill=C['muted'], anchor='middle')
f.text(330, 70, 'Al girar, cada sensor ve pasar', size=13, weight=600)
f.text(330, 90, 'los polos uno detrás de otro', size=13, weight=600)
f.text(330, 120, 'y da un pulso por cada cambio.', size=12, fill=C['muted'])
f.text(330, 150, 'Contando pulsos sabes cuánto', size=12, fill=C['muted'])
f.text(330, 168, 'ha girado el eje.', size=12, fill=C['muted'])
f.save(D + 'disco.svg')

# cuadratura
f = Fig(640, 300)
def fila(y, nombre, k, desfase):
    pts = []
    n = 4
    for i in range(n):
        a = (i + desfase) / n
        b = a + 0.5 / n
        pts += [(a, 0), (a, 1), (b, 1), (b, 0)]
    pts = [(0, 0)] + [(min(max(x, 0), 1), yv) for x, yv in pts] + [(1, 0)]
    axes(f, 80, y, 210, 34, top='', bottom='')
    wave(f, 80, y, 210, 34, pts, stroke=WIRE[k], sw=2.2)
    f.text(70, y + 24, nombre, size=13, weight=600, fill=WIRE[k], anchor='end')
f.rect(10, 10, 300, 280, fill='none', stroke=C['frame'], sw=1)
f.rect(330, 10, 300, 280, fill='none', stroke=C['frame'], sw=1)
f.title(28, 38, 'Sentido horario', 'A cambia antes que B')
fila(110, 'A', 'a', 0.05)
fila(180, 'B', 'c', 0.175)
f.line(90 + 0.05 / 4 * 240 * 4 / 4 * 4 / 4, 0, 0, 0, stroke='none') if False else None
f.text(160, 266, '90° de desfase', size=11, fill=C['muted'], anchor='middle')
# panel derecho: desplazado
f.add('<g transform="translate(320 0)">')
f.title(28, 38, 'Sentido antihorario', 'B cambia antes que A')
fila(110, 'A', 'a', 0.175)
fila(180, 'B', 'c', 0.05)
f.text(160, 266, 'el orden indica el sentido', size=11, fill=C['muted'], anchor='middle')
f.add('</g>')
f.save(D + 'cuadratura.svg')

# conexión
f = Fig(640, 530)
u = Uno(f, 150, 270, used={'5V', 'GND1', 'D2', 'D3'})
p = place(f, motor_encoder, 100, 40, s=1.0)
v5, g, d2, d3 = u.pin('5V'), u.pin('GND1'), u.pin('D2'), u.pin('D3')
yv, yb, ya, yg = p['VCC'][1], p['B'][1], p['A'][1], p['GND'][1]
f.wire([p['VCC'], (336, yv), (336, 200), (120, 200), (120, 514), (v5[0], 514), v5], 'vcc')
f.wire([p['B'], (350, yb), (350, 230), (d3[0], 230), d3], 'c')
f.wire([p['A'], (364, ya), (364, 218), (d2[0], 218), d2], 'a')
f.wire([p['GND'], (378, yg), (378, 206), (560, 206), (560, 502), (g[0], 502), g], 'gnd')
f.text(392, p['M1'][1] + 4, 'M1 y M2: al driver del motor', size=10.5, fill=C['muted'])
f.text(100, 26, 'Motor con encoder', size=13, weight=600)
legend(f, 150, 526, [('vcc', '5 V'), ('gnd', 'GND'), ('a', 'A → pin 2'), ('c', 'B → pin 3')], gap=105)
f.save(D + 'conexion.svg')
