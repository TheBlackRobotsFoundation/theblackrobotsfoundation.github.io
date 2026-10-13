import math
from lib import *
from parts import *
D = 'actuadores/brushless/'

f = Fig(640, 300)
m = place(f, brushless, 40, 40, s=1.8)
callout(f, 130, 60, 130, 20, 'Campana', sub=None)
callout(f, 130, 130, 60, 250, 'Eje', sub='aquí va la hélice', anchor='start')
callout(f, 250, 130, 250, 250, '3 cables', sub='las tres fases')
e = place(f, esc, 400, 100, s=1.4)
callout(f, 470, 110, 470, 40, 'ESC', sub='variador electrónico')
callout(f, 380, 120, 360, 60, 'Batería', sub=None, anchor='end')
callout(f, 610, 114, 620, 60, 'Motor', sub=None, anchor='end')
callout(f, 495, 229, 470, 270, 'Cable de servo', sub='señal, GND y BEC (5 V)', anchor='end')
f.save(D + 'anatomia.svg')

# estator y fases
f = Fig(640, 300)
cx, cy = 160, 150
f.circle(cx, cy, 120, fill='#1a1a1a', stroke=C['edge'], sw=1.5)   # campana con imanes
for i in range(14):
    a = math.radians(i * 360 / 14)
    col = '#5a3434' if i % 2 else '#34405a'
    x, y = cx + 108 * math.cos(a), cy + 108 * math.sin(a)
    f.add(f'<rect x="{x - 8:.1f}" y="{y - 12:.1f}" width="16" height="24" rx="2" fill="{col}" transform="rotate({i * 360 / 14 + 90:.1f} {x:.1f} {y:.1f})"/>')
fases = ['a', 'c', 'b']
for i in range(12):
    a = math.radians(i * 30)
    k = fases[i % 3]
    x, y = cx + 70 * math.cos(a), cy + 70 * math.sin(a)
    f.add(f'<rect x="{x - 9:.1f}" y="{y - 20:.1f}" width="18" height="40" rx="3" fill="{C["body2"]}" stroke="{WIRE[k]}" stroke-width="2" transform="rotate({i * 30 + 90} {x:.1f} {y:.1f})"/>')
f.circle(cx, cy, 34, fill=C['body'], stroke=C['edge'])
f.circle(cx, cy, 6, fill='#bdbdbd', stroke='none', sw=0)
for i, (k, n) in enumerate((('a', 'Fase A'), ('c', 'Fase B'), ('b', 'Fase C'))):
    y = 70 + i * 24
    f.rect(330, y - 9, 14, 14, fill=C['body2'], stroke=WIRE[k], sw=2, rx=2)
    f.text(354, y + 3, n, size=12, weight=600, fill=WIRE[k])
f.rect(330, 145, 14, 14, fill='#34405a', stroke='none', sw=0, rx=2)
f.rect(346, 145, 14, 14, fill='#5a3434', stroke='none', sw=0, rx=2)
f.text(370, 157, 'imanes de la campana (N y S)', size=12, fill=C['muted'])
f.text(330, 200, 'El ESC activa las bobinas por turnos.', size=13, weight=600)
f.text(330, 220, 'Los imanes persiguen al campo magnético', size=12, fill=C['muted'])
f.text(330, 238, 'y la campana gira alrededor del estator.', size=12, fill=C['muted'])
f.save(D + 'por-dentro.svg')

# conexión
f = Fig(640, 540)
u = Uno(f, 150, 290, used={'GND', 'D9'})
e = place(f, esc, 272, 90, s=1.0)
b = place(f, bateria, 60, 84, s=1.0, texto='11,1 V', sub='LiPo 3S')
m = place(f, brushless, 610, 190, s=0.9, rot=180)
g, d9 = u.pin('GND'), u.pin('D9')
f.wire([b['+'], (200, b['+'][1]), (200, e['BAT+'][1]), e['BAT+']], 'vcc')
f.wire([b['−'], (210, b['−'][1]), (210, e['BAT−'][1]), e['BAT−']], '#5a5a5a')
for i, k in enumerate(('M1', 'M2', 'M3')):
    tgt = sorted(m.values(), key=lambda p: p[1])[i]
    f.wire([e[k], (440, e[k][1]), (440, tgt[1]), tgt], '#5a5a5a')
f.wire([e['GND'], (e['GND'][0], 240), (g[0], 240), g], 'gnd')
f.wire([e['SIG'], (e['SIG'][0], 240), (d9[0], 240), d9], 'a')
f.line(e['BEC'][0], e['BEC'][1] + 2, e['BEC'][0], e['BEC'][1] + 22, stroke='#d9665b', sw=2.5, dash='3 3')
f.text(e['BEC'][0] + 30, e['BEC'][1] + 20, 'BEC (rojo): sin conectar', size=10.5, fill=C['muted'])
f.text(332, 76, 'ESC', size=13, weight=600, anchor='middle')
f.text(553, 214, 'Motor brushless', size=12, weight=600, anchor='middle')
f.text(553, 230, 'sin hélice para probar', size=10.5, fill=WIRE['vcc'], anchor='middle')
legend(f, 150, 534, [('gnd', 'marrón → GND'), ('a', 'señal → pin 9'), ('vcc', 'batería')], gap=130)
f.save(D + 'conexion.svg')
