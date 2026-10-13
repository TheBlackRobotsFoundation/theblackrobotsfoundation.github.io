import math
from lib import *
from parts import *
D = 'actuadores/servomotores/'

f = Fig(640, 320)
p = place(f, servo, 80, 40, s=2.0)
callout(f, 220, 92, 360, 40, 'Brazo (bocina)', sub='se atornilla al eje: aquí va lo que mueves')
callout(f, 140, 92, 360, 100, 'Eje de salida', sub='gira de 0° a 180°')
callout(f, 72, 112, 360, 160, 'Orejas', sub='para atornillarlo')
callout(f, 120, 260, 360, 230, 'Cable de 3 hilos', sub='marrón GND · rojo 5 V · naranja señal')
f.save(D + 'anatomia.svg')

# por dentro: bucle de control
f = Fig(640, 230)
bx = [(20, 'Señal', 'pulso del Arduino'), (170, 'Circuito', 'compara posiciones'), (320, 'Motor', 'y engranajes'), (470, 'Eje', 'llega al ángulo')]
for x, t, sub in bx:
    f.rect(x, 50, 130, 60, fill=C['body'], stroke=C['edge'], rx=4)
    f.text(x + 65, 78, t, size=13, weight=600, anchor='middle')
    f.text(x + 65, 96, sub, size=10.5, fill=C['muted'], anchor='middle')
for x in (150, 300, 450):
    f.line(x + 2, 80, x + 18, 80, stroke=C['accent'], sw=1.5, arrow='end')
f.rect(320, 150, 130, 50, fill=C['body'], stroke=WIRE['a'], rx=4)
f.text(385, 172, 'Potenciómetro', size=13, weight=600, anchor='middle', fill=WIRE['a'])
f.text(385, 189, 'mide el ángulo real', size=10.5, fill=C['muted'], anchor='middle')
f.path('M 535 110 L 535 175 L 452 175', stroke=WIRE['a'], sw=1.5, arrow='end')
f.path('M 318 175 L 235 175 L 235 112', stroke=WIRE['a'], sw=1.5, arrow='end')
f.text(20, 30, 'El servo se corrige solo hasta que el ángulo real coincide con el pedido', size=12, fill=C['muted'])
f.save(D + 'por-dentro.svg')

# pulsos y ángulos
f = Fig(640, 330)
rows = [(1.0, '1 ms', 0), (1.5, '1,5 ms', 90), (2.0, '2 ms', 180)]
for i, (ms, t, ang) in enumerate(rows):
    y = 30 + i * 100
    axes(f, 70, y, 340, 44, top='5 V' if i == 0 else '', bottom='0 V' if i == 2 else '')
    w = ms / 20 * 340 * 3   # escala exagerada x3 para que se vea el pulso
    wave(f, 70, y, 340, 44, [(0, 0), (0.04, 0), (0.04, 1), (0.04 + w / 340, 1), (0.04 + w / 340, 0), (1, 0)], stroke=WIRE['a'], sw=2.2)
    f.text(70 + 0.04 * 340 + w / 2, y - 6, t, size=11, fill=C['accent'], anchor='middle')
    # servo con brazo
    cx, cy = 520, y + 30
    f.path(f'M {cx - 40} {cy} A 40 40 0 0 1 {cx + 40} {cy}', stroke=C['frame'], sw=1.5)
    a = math.radians(180 - ang)
    f.line(cx, cy, cx + 36 * math.cos(a), cy - 36 * math.sin(a), stroke=C['text'], sw=5)
    f.circle(cx, cy, 6, fill=C['body2'], stroke=C['accent'], sw=1.5)
    f.text(cx + 54, cy + 4, f'{ang}°', size=15, weight=600)
f.text(70, 322, 'Un pulso cada 20 ms. Su duración (entre 1 y 2 ms) fija el ángulo.', size=11, fill=C['dim'])
f.save(D + 'pulsos.svg')

# conexión
f = Fig(640, 520)
u = Uno(f, 150, 270, used={'5V', 'GND', 'D9'})
p = place(f, servo, 274, 40, s=1.0)
g, v5, d9 = u.pin('GND'), u.pin('5V'), u.pin('D9')
f.wire([p['GND'], (p['GND'][0], 230), (g[0], 230), g], 'gnd')
f.wire([p['SIG'], (p['SIG'][0], 200), (d9[0], 200), d9], 'a')
f.wire([p['5V'], (p['5V'][0], 214), (560, 214), (560, 504), (v5[0], 504), v5], 'vcc', halo=True)
f.text(400, 90, 'Servo SG90', size=13, weight=600)
legend(f, 150, 516, [('gnd', 'marrón → GND'), ('vcc', 'rojo → 5 V'), ('a', 'naranja → pin 9')], gap=140)
f.save(D + 'conexion.svg')
