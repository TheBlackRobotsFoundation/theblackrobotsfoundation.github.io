from lib import *
from parts import *
D = 'sensores/finales-de-carrera/'

f = Fig(640, 250)
p = place(f, final_carrera, 70, 50, s=2.2)
callout(f, 262, 28, 400, 30, 'Palanca', sub='la pieza que empuja la máquina')
callout(f, 175, 55, 400, 100, 'Botón interno', sub='hace clic al llegar al tope')
callout(f, 180, 205, 400, 180, '3 terminales', sub='COM, NC y NO')
f.save(D + 'anatomia.svg')

def estado(f, x, tit, sub, pulsado):
    f.rect(x, 10, 300, 230, fill='none', stroke=C['frame'], sw=1)
    f.title(x + 18, 38, tit, sub)
    cx = x + 70
    pts = {'COM': (cx, 170), 'NC': (cx + 160, 110), 'NO': (cx + 160, 200)}
    for n, (px, py) in pts.items():
        f.circle(px, py, 5, fill=C['dark'], stroke=C['accent'], sw=2)
        f.text(px + (-14 if n == 'COM' else 14), py + 4, n, size=12, weight=600, anchor='end' if n == 'COM' else 'start')
    dest = pts['NO'] if pulsado else pts['NC']
    f.line(cx + 5, 170, dest[0] - 8, dest[1] + (-3 if pulsado else 6), stroke=WIRE['a'], sw=3)
    other = 'NC' if pulsado else 'NO'
    f.text(x + 150, 228, ('COM–NO cerrado · COM–NC abierto' if pulsado else 'COM–NC cerrado · COM–NO abierto'), size=10.5, fill=C['muted'], anchor='middle')

f = Fig(640, 250)
estado(f, 10, 'En reposo', 'nada empuja la palanca', False)
estado(f, 330, 'Pulsado', 'la máquina llega al tope', True)
f.save(D + 'estados.svg')

# homing
f = Fig(640, 170)
f.rect(40, 100, 560, 10, fill=C['body2'], stroke=C['edge'], rx=3)
f.rect(300, 66, 90, 34, fill=C['body'], stroke=C['accent'], rx=3)
f.text(345, 88, 'carro', size=11, fill=C['muted'], anchor='middle')
f.line(290, 83, 150, 83, stroke=WIRE['a'], sw=2, arrow='end')
place(f, final_carrera, 40, 52, s=0.7, rot=0)
f.text(40, 30, 'Final de carrera', size=12, weight=600)
f.text(40, 144, '1. el carro se mueve despacio hacia el final de carrera', size=11, fill=C['muted'])
f.text(40, 162, '2. al pulsarse, se para: esa posición pasa a ser el cero', size=11, fill=C['muted'])
f.save(D + 'homing.svg')

f = Fig(640, 470)
u = Uno(f, 150, 220, used={'GND', 'D2'})
p = place(f, final_carrera, 300, 70, s=1.2)
g, d2 = u.pin('GND'), u.pin('D2')
f.wire([p['COM'], (p['COM'][0], 180), (g[0], 180), g], 'gnd')
f.wire([p['NO'], (p['NO'][0], 180), (d2[0], 180), d2], 'a')
f.text(290, 60, 'Final de carrera', size=13, weight=600, anchor='end')
f.text(290, 78, 'COM y NO', size=10.5, fill=C['muted'], anchor='end')
legend(f, 150, 462, [('a', 'NO → pin 2'), ('gnd', 'COM → GND')], gap=130)
f.save(D + 'conexion.svg')
