from lib import *
from parts import *
D = 'sensores/pulsadores/'

# --- anatomía ---------------------------------------------------------------
f = Fig(640, 280)
p = place(f, pulsador, 70, 70, s=2.2)
callout(f, 136, 136, 250, 60, 'Botón', sub='al pulsarlo une las patas')
callout(f, 96, 237, 250, 230, '4 patas', sub='unidas de dos en dos por dentro')
# esquema interno
ox, oy = 420, 70
f.text(ox + 70, oy - 20, 'por dentro', size=11, fill=C['muted'], anchor='middle')
for (x, y) in ((ox, oy), (ox + 140, oy), (ox, oy + 140), (ox + 140, oy + 140)):
    f.circle(x, y, 5, fill=C['accent'], stroke='none', sw=0)
f.line(ox, oy, ox + 140, oy, stroke=C['accent'], sw=2)
f.line(ox, oy + 140, ox + 140, oy + 140, stroke=C['accent'], sw=2)
f.line(ox + 70, oy, ox + 70, oy + 48, stroke=C['accent'], sw=2)
f.line(ox + 70, oy + 140, ox + 70, oy + 92, stroke=C['accent'], sw=2)
f.line(ox + 52, oy + 52, ox + 92, oy + 74, stroke=C['accent'], sw=2.5)
f.circle(ox + 70, oy + 92, 3.5, fill=C['dark'], stroke=C['accent'], sw=2)
f.circle(ox + 70, oy + 48, 3.5, fill=C['dark'], stroke=C['accent'], sw=2)
f.text(ox + 160, oy + 74, 'interruptor', size=11, fill=C['muted'])
f.text(ox - 12, oy + 4, '1', size=11, fill=C['muted'], anchor='end')
f.text(ox + 152, oy + 4, '2', size=11, fill=C['muted'])
f.text(ox - 12, oy + 144, '3', size=11, fill=C['muted'], anchor='end')
f.text(ox + 152, oy + 144, '4', size=11, fill=C['muted'])
f.save(D + 'anatomia.svg')

# --- pull-up / pull-down ----------------------------------------------------
def gnd(f, x, y):
    for i, w in enumerate((22, 14, 6)):
        f.line(x - w / 2, y + i * 5, x + w / 2, y + i * 5, stroke=C['accent'], sw=2)

def boton(f, x, y1, y2):
    # interruptor vertical entre y1 e y2
    f.line(x, y1, x, y1 + 14, stroke=C['accent'], sw=2)
    f.line(x, y2 - 14, x, y2, stroke=C['accent'], sw=2)
    f.circle(x, y1 + 14, 3, fill=C['dark'], stroke=C['accent'], sw=2)
    f.circle(x, y2 - 14, 3, fill=C['dark'], stroke=C['accent'], sw=2)
    f.line(x, y2 - 14, x + 16, y1 + 18, stroke=C['accent'], sw=2.2)

f = Fig(640, 330)
f.rect(10, 10, 300, 310, fill='none', stroke=C['frame'], sw=1)
f.rect(330, 10, 300, 310, fill='none', stroke=C['frame'], sw=1)
f.title(28, 38, 'Pull-up', 'suelto = HIGH · pulsado = LOW')
f.title(348, 38, 'Pull-down', 'suelto = LOW · pulsado = HIGH')
# pull-up
x = 110
f.text(x, 82, '5 V', size=12, weight=600, anchor='middle')
f.line(x, 88, x, 104, stroke=C['accent'], sw=2)
f.rect(x - 8, 104, 16, 44, fill=C['body2'], stroke=C['accent'], sw=2, rx=1)
f.text(x - 18, 130, '10 kΩ', size=11, fill=C['muted'], anchor='end')
f.line(x, 148, x, 190, stroke=C['accent'], sw=2)
f.node(x, 172, 'a'); f.line(x, 172, 200, 172, stroke=WIRE['a'], sw=2); f.text(208, 176, 'pin', size=12, weight=600, fill=WIRE['a'])
boton(f, x, 190, 260)
gnd(f, x, 262)
# pull-down
x = 430
f.text(x, 82, '5 V', size=12, weight=600, anchor='middle')
f.line(x, 88, x, 92, stroke=C['accent'], sw=2)
boton(f, x, 92, 162)
f.line(x, 162, x, 192, stroke=C['accent'], sw=2)
f.node(x, 176, 'a'); f.line(x, 176, 520, 176, stroke=WIRE['a'], sw=2); f.text(528, 180, 'pin', size=12, weight=600, fill=WIRE['a'])
f.rect(x - 8, 192, 16, 44, fill=C['body2'], stroke=C['accent'], sw=2, rx=1)
f.text(x - 18, 218, '10 kΩ', size=11, fill=C['muted'], anchor='end')
f.line(x, 236, x, 262, stroke=C['accent'], sw=2)
gnd(f, x, 262)
f.text(28, 306, 'INPUT_PULLUP activa una resistencia interna', size=10.5, fill=C['dim'])
f.save(D + 'pull-up-pull-down.svg')

# --- rebote -----------------------------------------------------------------
f = Fig(640, 190)
axes(f, 60, 40, 540, 90, top='HIGH', bottom='LOW', xlabel='tiempo')
pts = [(0, 1), (.28, 1), (.28, 0), (.30, 0), (.30, 1), (.315, 1), (.315, 0), (.335, 0), (.335, .9), (.345, .9), (.345, 0), (1, 0)]
wave(f, 60, 40, 540, 90, pts, stroke=WIRE['a'], sw=2.2)
f.rect(60 + .27 * 540, 30, .1 * 540, 110, fill='#ffffff', stroke='none', sw=0, rx=2, opacity=0.04)
f.text(60 + .32 * 540, 160, 'rebote: unos milisegundos', size=11, fill=C['muted'], anchor='middle')
f.text(60 + .7 * 540, 160, 'pulsado', size=11, fill=C['muted'], anchor='middle')
f.text(60 + .12 * 540, 160, 'suelto', size=11, fill=C['muted'], anchor='middle')
f.save(D + 'rebote.svg')

# --- conexión ---------------------------------------------------------------
f = Fig(640, 480)
u = Uno(f, 150, 220, used={'D2', 'GND'})
p = place(f, pulsador, 300, 70, s=1.2)
d2, g = u.pin('D2'), u.pin('GND')
# pata 2 (arriba a la derecha) -> pin 2 ; pata 3 (abajo a la izquierda) -> GND
f.wire([p['2'], (p['2'][0], 36), (450, 36), (450, 170), (d2[0], 170), d2], 'a')
f.wire([p['3'], (p['3'][0], 180), (g[0], 180), g], 'gnd')
f.text(280, 108, 'Pulsador', size=13, weight=600, anchor='end')
f.text(280, 126, 'patas en diagonal', size=10.5, fill=C['muted'], anchor='end')
legend(f, 150, 466, [('a', 'señal → pin 2'), ('gnd', 'GND')], gap=130)
f.save(D + 'conexion.svg')
