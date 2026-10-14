from lib import *
from parts import *
D = 'actuadores/reles/'

f = Fig(640, 250)
p = place(f, rele, 120, 30, s=1.7)
callout(f, 245, 60, 245, 16, 'Relé', sub=None)
callout(f, 164, 152, 164, 214, 'LED', sub='encendido = relé activado')
callout(f, 365, 50, 440, 20, 'Bornas de potencia', sub='NO, COM y NC: el circuito que conmutas')
callout(f, 104, 100, 40, 214, 'VCC, GND, IN', sub='al Arduino')
f.save(D + 'anatomia.svg')

# por dentro: bobina, palanca y contactos
def estado(f, x, tit, sub, on):
    f.rect(x, 10, 300, 250, fill='none', stroke=C['frame'], sw=1)
    f.title(x + 18, 38, tit, sub)
    # bobina
    bx, by = x + 50, 160
    f.rect(bx, by, 60, 60, fill=C['body2'], stroke=WIRE['vcc'] if on else C['edge'], sw=2, rx=3)
    for i in range(6):
        f.line(bx + 6, by + 8 + i * 9, bx + 54, by + 8 + i * 9, stroke=WIRE['vcc'] if on else '#3a3a3a', sw=2)
    f.text(bx + 72, by + 34, 'bobina', size=10.5, fill=C['muted'])
    # palanca
    px, py = x + 40, 130
    end = (x + 226, 156 if on else 112)
    f.circle(px, py, 5, fill=C['accent'], stroke='none', sw=0)
    f.line(px, py, *end, stroke=C['accent'], sw=4)
    f.text(px - 8, py - 10, 'COM', size=11, weight=600, anchor='middle')
    # contactos
    for (cy, n) in ((108, 'NC'), (160, 'NO')):
        f.rect(x + 222, cy - 4 if n == 'NC' else cy - 4, 30, 8, fill=C['body2'], stroke=C['accent'], sw=1.5, rx=1)
        f.text(x + 262, cy + 4, n, size=11, weight=600)
    hot = 'NO' if on else 'NC'
    f.text(x + 150, 245, f'COM conectado con {hot}', size=11, fill=WIRE['a'], anchor='middle')
    if on:
        f.path(f'M {x + 180} 140 L {x + 180} 156', stroke=C['muted'], sw=1.5, arrow='end')

f = Fig(640, 270)
estado(f, 10, 'IN apagado', 'la bobina no atrae la palanca', False)
estado(f, 330, 'IN activado', 'la bobina atrae la palanca', True)
f.save(D + 'por-dentro.svg')

# conexión
f = Fig(720, 540)
u = Uno(f, 60, 280, used={'5V', 'GND', 'D7'})
p = place(f, rele, 320, 40, s=1.0)
fan = place(f, ventilador, 600, 30, s=1.0)
src = place(f, fuente_top, 480, 330, s=1.0)
g, v5, d7 = u.pin('GND'), u.pin('5V'), u.pin('D7')
f.wire([p['VCC'], (40, p['VCC'][1]), (40, 516), (v5[0], 516), v5], 'vcc')
f.wire([p['GND'], (g[0], p['GND'][1]), g], 'gnd')
f.wire([p['IN'], (d7[0], p['IN'][1]), d7], 'a')
f.wire([p['NO'], fan['+']], '#d9665b')
f.wire([p['COM'], (520, p['COM'][1]), (520, 330), src['+']], '#d9665b')
f.wire([fan['−'], (560, fan['−'][1]), (560, 330), src['−']], '#7a7a7a')
f.text(400, 150, 'Módulo de relé', size=13, weight=600, anchor='middle')
f.text(650, 150, 'Ventilador 12 V', size=12, weight=600, anchor='middle')
f.text(612, 460, 'Circuito de potencia', size=11, fill=C['muted'], anchor='middle')
f.text(612, 476, 'separado del Arduino', size=11, fill=C['muted'], anchor='middle')
legend(f, 60, 532, [('vcc', '5 V'), ('gnd', 'GND'), ('a', 'IN → pin 7')], gap=110)
f.save(D + 'conexion.svg')
