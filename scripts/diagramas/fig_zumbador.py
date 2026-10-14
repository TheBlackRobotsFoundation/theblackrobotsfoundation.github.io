from lib import *
from parts import *
D = 'actuadores/zumbador/'

f = Fig(640, 270)
for x, tit, sub, pasivo in ((10, 'Activo', 'pita solo al darle 5 V', False), (330, 'Pasivo', 'suena a la frecuencia que le mandes', True)):
    f.rect(x, 10, 300, 250, fill='none', stroke=C['frame'], sw=1)
    f.title(x + 18, 38, tit, sub)
    # vista superior
    cx, cy = x + 85, 150
    f.circle(cx, cy, 46, fill='#121212', stroke=C['edge'])
    f.circle(cx, cy, 36, fill='none', stroke='#2a2a2a', sw=1)
    f.circle(cx, cy, 7, fill=C['dark'], stroke='#444', sw=1)
    f.text(cx - 22, cy - 22, '+', size=13, fill=C['muted'], anchor='middle')
    f.text(cx, 222, 'arriba', size=10.5, fill=C['muted'], anchor='middle')
    # vista inferior
    cx = x + 215
    if pasivo:
        f.circle(cx, cy, 46, fill='#1f4d2e', stroke='#3f7a52')
        f.path(f'M {cx - 22} {cy - 20} Q {cx} {cy - 34} {cx + 18} {cy - 10}', stroke='#c9a24a', sw=2)
        f.path(f'M {cx - 18} {cy + 18} Q {cx + 4} {cy + 30} {cx + 24} {cy + 6}', stroke='#c9a24a', sw=2)
    else:
        f.circle(cx, cy, 46, fill='#0d0d0d', stroke=C['edge'])
        f.circle(cx, cy, 30, fill='#151515', stroke='none', sw=0)
    f.circle(cx - 10, cy, 3.5, fill=METAL, stroke='none', sw=0)
    f.circle(cx + 10, cy, 3.5, fill=METAL, stroke='none', sw=0)
    f.text(cx, 222, 'abajo: ' + ('placa verde visible' if pasivo else 'sellado en negro'), size=10.5, fill=C['muted'], anchor='middle')
f.save(D + 'tipos.svg')

f = Fig(640, 260)
rows = [(4, 'La4 · 440 Hz', 'grave'), (8, 'La5 · 880 Hz', 'una octava más aguda'), (12, 'Mi6 · 1319 Hz', 'aguda')]
for i, (n, t, sub) in enumerate(rows):
    y = 30 + i * 76
    axes(f, 40, y, 400, 38, top='', bottom='')
    wave(f, 40, y, 400, 38, square(0.5, n), stroke=WIRE['a'], sw=2)
    f.text(470, y + 18, t, size=13, weight=600)
    f.text(470, y + 36, sub, size=11, fill=C['muted'])
f.text(40, 252, 'más pulsos por segundo = nota más aguda', size=11, fill=C['dim'])
f.save(D + 'frecuencia.svg')

f = Fig(640, 520)
u = Uno(f, 150, 260, used={'D8', 'GND1'})
p = place(f, zumbador, 330, 40, s=1.3)
g, d8 = u.pin('GND1'), u.pin('D8')
mas = p['+']
r = place(f, resistencia, mas[0], 166, s=0.6, rot=90, valor='100', length=80)
f.wire([mas, r['1']], 'a')
f.wire([r['2'], (r['2'][0], 236), (d8[0], 236), d8], 'a')
f.wire([p['−'], (p['−'][0], 172), (560, 172), (560, 504), (g[0], 504), g], 'gnd')
f.text(310, 80, 'Zumbador', size=13, weight=600, anchor='end')
f.text(310, 98, 'pasivo o activo', size=10.5, fill=C['muted'], anchor='end')
f.text(374, 200, '100 Ω', size=11, fill=C['muted'])
legend(f, 150, 516, [('a', '+ → 100 Ω → pin 8'), ('gnd', '− → GND')], gap=160)
f.save(D + 'conexion.svg')
