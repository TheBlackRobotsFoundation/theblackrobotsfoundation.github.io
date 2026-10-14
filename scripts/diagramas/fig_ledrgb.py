from lib import *
from parts import *
D = 'actuadores/led-rgb/'

# anatomía del LED RGB
f = Fig(640, 280)
p = place(f, led_rgb, 90, 20, s=2.2)
callout(f, 130, 86, 300, 40, 'Tres LEDs en uno', sub='rojo, verde y azul')
callout(f, 147, 257, 300, 250, 'Pata común', sub='la más larga: GND (cátodo común)')
callout(f, 116, 218, 300, 150, 'R, G y B', sub='una pata por color')
f.save(D + 'anatomia.svg')

# tira NeoPixel
f = Fig(640, 200)
p = place(f, neopixel, 30, 70, s=1.4, n=5)
callout(f, 40, 82, 40, 160, 'Entrada: 5V, DIN y GND')
callout(f, 120, 98, 250, 160, 'LED WS2812', sub='cada uno con su chip de control')
callout(f, 130, 56, 220, 30, 'Sentido de los datos')
callout(f, 362, 116, 430, 160, 'Se puede cortar', sub='por las líneas entre LEDs')
f.save(D + 'tira.svg')

# mezcla de colores
f = Fig(640, 280)
f.add('<g style="mix-blend-mode:screen">')
for cx, cy, col in ((180, 110, '#ff3b3b'), (240, 110, '#3bff5a'), (210, 162, '#3b6bff')):
    f.add(f'<circle cx="{cx}" cy="{cy}" r="62" fill="{col}" opacity="0.85"/>')
f.add('</g>')
rows = [('#ff3b3b', '255, 0, 0', 'rojo'), ('#3bff5a', '0, 255, 0', 'verde'), ('#3b6bff', '0, 0, 255', 'azul'),
        ('#ffff3b', '255, 255, 0', 'amarillo'), ('#3bffff', '0, 255, 255', 'cian'), ('#ff3bff', '255, 0, 255', 'magenta'),
        ('#ffffff', '255, 255, 255', 'blanco')]
for i, (col, v, n) in enumerate(rows):
    y = 46 + i * 30
    f.circle(380, y - 4, 8, fill=col, stroke='none', sw=0)
    f.text(400, y, v, size=12, mono=True, fill=C['accent'])
    f.text(520, y, n, size=12, fill=C['muted'])
f.text(380, 270, 'valores de rojo, verde y azul (0 – 255)', size=10.5, fill=C['dim'])
f.save(D + 'mezcla.svg')

# conexión LED RGB
f = Fig(640, 520)
u = Uno(f, 150, 260, used={'D9', 'D10', 'D11', 'GND'})
p = place(f, led_rgb, 300, 30, s=1.2)
g, d9, d10, d11 = u.pin('GND'), u.pin('D9'), u.pin('D10'), u.pin('D11')
rs = {}
for k in ('R', 'G', 'B'):
    x, y = p[k]
    rs[k] = place(f, resistencia, x, 150, s=0.6, rot=90, valor='220', length=80)
    f.wire([p[k], rs[k]['1']], {'R': 'vcc', 'G': 'c', 'B': 'b'}[k])
f.wire([rs['R']['2'], (rs['R']['2'][0], 230), (d11[0], 230), d11], 'vcc')
f.wire([rs['G']['2'], (rs['G']['2'][0], 214), (d10[0], 214), d10], 'c')
f.wire([rs['B']['2'], (rs['B']['2'][0], 206), (d9[0], 206), d9], 'b')
f.wire([p['−'], (p['−'][0], 244), (g[0], 244), g], 'gnd', halo=True)
f.text(280, 70, 'LED RGB', size=13, weight=600, anchor='end')
f.text(280, 88, 'cátodo común', size=10.5, fill=C['muted'], anchor='end')
f.text(380, 178, '3 × 220 Ω', size=11, fill=C['muted'])
legend(f, 150, 516, [('vcc', 'R → 11'), ('c', 'G → 10'), ('b', 'B → 9'), ('gnd', 'común → GND')], gap=100)
f.save(D + 'conexion-rgb.svg')

# conexión tira
f = Fig(640, 470)
u = Uno(f, 150, 220, used={'5V', 'GND', 'D6'})
p = place(f, neopixel, 280, 40, s=1.0, n=5, right=True)
g, v5, d6 = u.pin('GND'), u.pin('5V'), u.pin('D6')
x5, xd, xg = p['5V'][0] + 40, p['DIN'][0] + 26, p['GND'][0] + 12
xd, xg = 584, 570
f.wire([p['5V'], (600, p['5V'][1]), (600, 456), (v5[0], 456), v5], 'vcc')
r = place(f, resistencia, xd, 120, s=0.6, rot=90, valor='330', length=80)
f.wire([p['DIN'], (xd, p['DIN'][1]), r['1']], 'a')
f.wire([r['2'], (xd, 178), (d6[0], 178), d6], 'a')
f.wire([p['GND'], (xg, p['GND'][1]), (xg, 164), (g[0], 164), g], 'gnd')
f.text(300, 24, 'Tira WS2812 (NeoPixel)', size=13, weight=600)
f.text(xd - 24, 124, '330 Ω', size=11, fill=C['muted'], anchor='end')
legend(f, 150, 466, [('vcc', '5 V'), ('a', 'datos → 330 Ω → pin 6'), ('gnd', 'GND')], gap=150)
f.save(D + 'conexion-tira.svg')
