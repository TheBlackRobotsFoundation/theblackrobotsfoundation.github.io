from lib import *
from parts import *
D = 'sensores/infrarrojos/'

f = Fig(640, 340)
p = place(f, tcrt5000, 120, 14, s=2.1)
callout(f, 193, 50, 330, 30, 'Emisor infrarrojo', sub='un LED de luz invisible')
callout(f, 193, 84, 330, 84, 'Receptor', sub='un fototransistor que mide la luz que vuelve')
callout(f, 193, 157, 330, 150, 'Potenciómetro', sub='ajusta el umbral de blanco o negro')
callout(f, 145, 207, 330, 210, 'LED indicador', sub='se enciende al detectar')
callout(f, 210, 316, 330, 280, '4 pines', sub='VCC, GND, salida digital y analógica')
f.save(D + 'anatomia.svg')

# reflexión
f = Fig(640, 270)
for i, (x, tit, sub, fondo, vuelve) in enumerate(((10, 'Superficie blanca', 'refleja mucha luz', '#d8d8d8', True),
                                               (330, 'Línea negra', 'absorbe casi toda la luz', '#151515', False))):
    f.rect(x, 10, 300, 250, fill='none', stroke=C['frame'], sw=1)
    f.title(x + 18, 38, tit, sub)
    cx = x + 150
    f.rect(cx - 40, 76, 80, 30, fill='#101010', stroke='#5a5a5a', rx=3)
    f.circle(cx - 20, 106, 7, fill='#3a5fa0', stroke='none', sw=0)
    f.circle(cx + 20, 106, 7, fill='#1e1e1e', stroke='#777', sw=1)
    f.text(cx - 20, 70, 'emisor', size=10, fill=C['muted'], anchor='middle')
    f.text(cx + 20, 70, 'receptor', size=10, fill=C['muted'], anchor='middle')
    f.rect(x + 30, 200, 240, 30, fill=fondo, stroke=C['edge'], rx=2)
    f.line(cx - 20, 116, cx - 2, 196, stroke=WIRE['d'], sw=2, arrow='end')
    if vuelve:
        f.line(cx + 2, 196, cx + 20, 118, stroke=WIRE['d'], sw=2, arrow='end')
        f.text(x + 150, 250, 'salida DO: LOW', size=11, fill=C['accent'], anchor='middle', mono=True)
    else:
        f.line(cx + 2, 196, cx + 10, 160, stroke=WIRE['d'], sw=1.5, dash='3 4')
        f.text(x + 150, 250, 'salida DO: HIGH', size=11, fill=C['accent'], anchor='middle', mono=True)
f.save(D + 'reflexion.svg')

# conexión
f = Fig(640, 520)
u = Uno(f, 150, 260, used={'5V', 'GND', 'D2', 'A0'})
p = place(f, tcrt5000, 320, 20, s=1.0)
g, v5, d2, a0 = u.pin('GND'), u.pin('5V'), u.pin('D2'), u.pin('A0')
f.wire([p['VCC'], (p['VCC'][0], 196), (120, 196), (120, 504), (v5[0], 504), v5], 'vcc')
f.wire([p['GND'], (p['GND'][0], 212), (g[0], 212), g], 'gnd')
f.wire([p['DO'], (p['DO'][0], 222), (d2[0], 222), d2], 'a')
f.wire([p['AO'], (p['AO'][0], 190), (560, 190), (560, 494), (a0[0], 494), a0], 'b')
f.text(300, 60, 'TCRT5000', size=13, weight=600, anchor='end')
f.text(300, 78, 'módulo sigue-líneas', size=10.5, fill=C['muted'], anchor='end')
legend(f, 150, 516, [('vcc', '5 V'), ('gnd', 'GND'), ('a', 'DO → pin 2'), ('b', 'AO → A0')], gap=105)
f.save(D + 'conexion.svg')
