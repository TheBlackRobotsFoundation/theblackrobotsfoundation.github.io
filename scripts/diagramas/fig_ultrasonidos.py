from lib import *
from parts import *
D = 'sensores/ultrasonidos/'

f = Fig(640, 300)
p = place(f, hcsr04, 40, 60, s=1.9)
callout(f, 120, 140, 120, 30, 'Emisor (T)', sub=None)
callout(f, 302, 140, 302, 30, 'Receptor (R)', sub=None)
callout(f, 238, 120, 430, 60, 'Cristal', sub='marca el ritmo del circuito')
callout(f, 230, 276, 430, 230, '4 pines', sub='VCC, Trig, Echo y GND')
f.save(D + 'anatomia.svg')

# eco
f = Fig(640, 400)
f.rect(10, 10, 620, 190, fill='none', stroke=C['frame'], sw=1)
f.title(28, 38, 'El eco', 'emite un pulso de sonido y mide cuánto tarda en volver')
place(f, hcsr04, 40, 82, s=0.62)
# ondas de ida y vuelta
for i, r in enumerate((24, 44, 64, 84)):
    f.path(f'M {175 + r * 2} {100 - r * 0.25} Q {183 + r * 2} 108 {175 + r * 2} {116 + r * 0.25}', stroke=WIRE['a'], sw=2)
f.line(160, 150, 470, 150, stroke=WIRE['a'], sw=1.5, arrow='end')
f.line(470, 168, 160, 168, stroke=WIRE['b'], sw=1.5, arrow='end')
f.text(315, 144, 'ida', size=10.5, fill=WIRE['a'], anchor='middle')
f.text(315, 186, 'vuelta', size=10.5, fill=WIRE['b'], anchor='middle')
f.rect(490, 70, 26, 110, fill='#2a2a2a', stroke=C['edge'], rx=2)
f.text(530, 120, 'objeto', size=11, fill=C['muted'])
# tiempos
f.rect(10, 214, 620, 176, fill='none', stroke=C['frame'], sw=1)
f.title(28, 242, 'Las señales')
axes(f, 110, 264, 480, 30, top='', bottom='')
f.text(28, 286, 'Trig', size=12, weight=600, fill=WIRE['a'])
wave(f, 110, 264, 480, 30, [(0, 0), (.06, 0), (.06, 1), (.1, 1), (.1, 0), (1, 0)], stroke=WIRE['a'])
f.text(110 + .08 * 480, 258, '10 µs', size=10, fill=C['muted'], anchor='middle')
axes(f, 110, 324, 480, 30, top='', bottom='')
f.text(28, 346, 'Echo', size=12, weight=600, fill=WIRE['b'])
wave(f, 110, 324, 480, 30, [(0, 0), (.2, 0), (.2, 1), (.72, 1), (.72, 0), (1, 0)], stroke=WIRE['b'])
f.line(110 + .2 * 480, 372, 110 + .72 * 480, 372, stroke=C['muted'], sw=1, arrow='both')
f.text(110 + .46 * 480, 386, 'duración = tiempo de ida y vuelta', size=10.5, fill=C['muted'], anchor='middle')
f.save(D + 'eco.svg')

# conexión
f = Fig(640, 520)
u = Uno(f, 150, 260, used={'5V', 'GND1', 'D9', 'D10'})
p = place(f, hcsr04, 230, 30, s=1.0)
g, v5, d9, d10 = u.pin('GND1'), u.pin('5V'), u.pin('D9'), u.pin('D10')
f.wire([p['VCC'], (p['VCC'][0], 170), (120, 170), (120, 504), (v5[0], 504), v5], 'vcc')
f.wire([p['Trig'], (p['Trig'][0], 220), (d10[0], 220), d10], 'a')
f.wire([p['Echo'], (p['Echo'][0], 200), (d9[0], 200), d9], 'b')
f.wire([p['GND'], (p['GND'][0], 180), (560, 180), (560, 492), (g[0], 492), g], 'gnd')
f.text(430, 70, 'HC-SR04', size=13, weight=600)
legend(f, 150, 516, [('vcc', '5 V'), ('a', 'Trig → 10'), ('b', 'Echo → 9'), ('gnd', 'GND')], gap=100)
f.save(D + 'conexion.svg')
