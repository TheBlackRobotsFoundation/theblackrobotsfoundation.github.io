import math
from lib import *
from parts import *

# =========================== POTENCIÓMETRO =================================
D = 'sensores/potenciometro/'
f = Fig(640, 280)
p = place(f, potenciometro, 80, 40, s=2.4)
callout(f, 164, 92, 300, 50, 'Eje', sub='al girarlo mueve el cursor')
callout(f, 116, 240, 300, 150, 'Extremos', sub='a 5 V y a GND')
callout(f, 164, 240, 300, 220, 'Cursor (central)', sub='da la tensión al pin analógico')
f.save(D + 'anatomia.svg')

# pista resistiva
f = Fig(640, 280)
cx, cy, r = 170, 140, 90
f.path(f'M {cx + r * math.cos(math.radians(135))} {cy + r * math.sin(math.radians(135))} A {r} {r} 0 1 1 {cx + r * math.cos(math.radians(45))} {cy + r * math.sin(math.radians(45))}', stroke='#3a3a3a', sw=16)
f.path(f'M {cx + r * math.cos(math.radians(135))} {cy + r * math.sin(math.radians(135))} A {r} {r} 0 0 1 {cx + r * math.cos(math.radians(-60))} {cy + r * math.sin(math.radians(-60))}', stroke=WIRE['a'], sw=16)
a = math.radians(-60)
f.line(cx, cy, cx + (r - 2) * math.cos(a), cy + (r - 2) * math.sin(a), stroke=C['accent'], sw=3)
f.circle(cx, cy, 8, fill=C['body2'], stroke=C['accent'], sw=2)
f.circle(cx + r * math.cos(a), cy + r * math.sin(a), 6, fill=C['text'], stroke='none', sw=0)
for ang, lab in ((135, 'GND'), (45, '5 V')):
    x, y = cx + r * math.cos(math.radians(ang)), cy + r * math.sin(math.radians(ang))
    f.text(x + (-14 if ang == 135 else 14), y + 26, lab, size=12, weight=600, anchor='middle')
f.text(cx, cy + 40, 'cursor', size=11, fill=C['muted'], anchor='middle')
f.text(390, 100, 'Una pista resistiva entre 5 V y GND.', size=13, weight=600)
f.text(390, 124, 'El cursor toca la pista en un punto:', size=12, fill=C['muted'])
f.text(390, 142, 'cuanto más cerca de 5 V, más tensión.', size=12, fill=C['muted'])
for i, (v, n) in enumerate(((0, 'tope izquierdo'), (512, 'mitad'), (1023, 'tope derecho'))):
    f.text(390, 186 + i * 22, f'{v}', size=13, weight=600, mono=True, fill=WIRE['a'])
    f.text(440, 186 + i * 22, n, size=12, fill=C['muted'])
f.save(D + 'pista.svg')

f = Fig(640, 500)
u = Uno(f, 150, 220, used={'5V', 'GND', 'A0'})
p = place(f, potenciometro, 360, 50, s=1.2)
izq, cen, der = p['GND'], p['OUT'], p['VCC']
g, a0, v5 = u.pin('GND'), u.pin('A0'), u.pin('5V')
f.wire([izq, (izq[0], 180), (g[0], 180), g], 'gnd')
f.wire([cen, (cen[0], 170), (540, 170), (540, 458), (a0[0], 458), a0], 'a')
f.wire([der, (der[0], 160), (560, 160), (560, 472), (v5[0], 472), v5], 'vcc')
f.text(340, 92, 'Potenciómetro', size=13, weight=600, anchor='end')
f.text(340, 110, '10 kΩ', size=10.5, fill=C['muted'], anchor='end')
legend(f, 150, 492, [('vcc', '5 V'), ('a', 'cursor → A0'), ('gnd', 'GND')], gap=110)
f.save(D + 'conexion.svg')

# ================================ LDR =======================================
D = 'sensores/ldr/'
f = Fig(640, 260)
p = place(f, ldr, 120, 40, s=3)
callout(f, 186, 80, 300, 60, 'Pista fotosensible', sub='su resistencia baja con la luz')
callout(f, 162, 230, 300, 190, '2 patas', sub='sin polaridad: da igual el sentido')
f.save(D + 'anatomia.svg')

# curva resistencia - luz y divisor
f = Fig(640, 300)
f.rect(10, 10, 300, 280, fill='none', stroke=C['frame'], sw=1)
f.rect(330, 10, 300, 280, fill='none', stroke=C['frame'], sw=1)
f.title(28, 38, 'Resistencia según la luz')
gx, gy, gw, gh = 60, 70, 220, 170
f.line(gx, gy, gx, gy + gh, stroke=C['edge'], sw=1)
f.line(gx, gy + gh, gx + gw, gy + gh, stroke=C['edge'], sw=1)
pts = [(i / 60, 1 / (1 + 9 * (i / 60)) ** 1.3) for i in range(61)]
f.poly([(gx + px * gw, gy + gh - py * (gh - 10)) for px, py in pts], stroke=WIRE['a'], sw=2.5)
f.text(gx - 8, gy + 8, '1 MΩ', size=10, fill=C['muted'], anchor='end')
f.text(gx - 8, gy + gh, '1 kΩ', size=10, fill=C['muted'], anchor='end')
f.text(gx, gy + gh + 22, 'oscuridad', size=10.5, fill=C['muted'])
f.text(gx + gw, gy + gh + 22, 'mucha luz', size=10.5, fill=C['muted'], anchor='end')
f.title(348, 38, 'Divisor de tensión')
x = 440
f.text(x, 76, '5 V', size=12, weight=600, anchor='middle')
f.line(x, 82, x, 96, stroke=C['accent'], sw=2)
f.rect(x - 9, 96, 18, 46, fill=C['body2'], stroke=WIRE['a'], sw=2, rx=1)
f.line(x - 30, 100, x - 16, 112, stroke=C['muted'], sw=1.5, arrow='end')
f.line(x - 30, 116, x - 16, 128, stroke=C['muted'], sw=1.5, arrow='end')
f.text(x + 18, 124, 'LDR', size=12, weight=600, fill=WIRE['a'])
f.line(x, 142, x, 190, stroke=C['accent'], sw=2)
f.node(x, 166, 'b'); f.line(x, 166, 540, 166, stroke=WIRE['b'], sw=2)
f.text(548, 170, 'A0', size=12, weight=600, fill=WIRE['b'])
f.rect(x - 9, 190, 18, 46, fill=C['body2'], stroke=C['accent'], sw=2, rx=1)
f.text(x + 18, 218, '10 kΩ', size=11, fill=C['muted'])
f.line(x, 236, x, 252, stroke=C['accent'], sw=2)
for i, w in enumerate((22, 14, 6)):
    f.line(x - w / 2, 252 + i * 5, x + w / 2, 252 + i * 5, stroke=C['accent'], sw=2)
f.text(348, 280, 'más luz → menos resistencia → más tensión en A0', size=10.5, fill=C['dim'])
f.save(D + 'como-funciona.svg')

f = Fig(640, 540)
u = Uno(f, 150, 260, used={'5V', 'GND', 'A0'})
p = place(f, ldr, 330, 30, s=1.4)
izq, der = p['1'], p['2']
g, a0, v5 = u.pin('GND'), u.pin('A0'), u.pin('5V')
nodo = (der[0], 150)
r = place(f, resistencia, nodo[0], 150, s=0.8, rot=90, valor='10k', length=80)
f.wire([izq, (izq[0], 134), (120, 134), (120, 512), (v5[0], 512), v5], 'vcc')
f.wire([der, nodo], 'b')
f.wire([nodo, (540, 150), (540, 498), (a0[0], 498), a0], 'b')
f.wire([r['2'], (r['2'][0], 228), (g[0], 228), g], 'gnd')
f.node(*nodo, 'b')
f.text(310, 54, 'LDR', size=13, weight=600, anchor='end')
f.text(388, 186, '10 kΩ', size=11, fill=C['muted'])
legend(f, 150, 532, [('vcc', '5 V'), ('b', 'divisor → A0'), ('gnd', 'GND')], gap=110)
f.save(D + 'conexion.svg')
