from lib import *
from parts import *
D = 'actuadores/motores-dc/'

# anatomía: motor
f = Fig(640, 200)
p = place(f, motor_dc, 90, 50, s=1.6)
callout(f, 70, 105, 70, 175, 'Eje')
callout(f, 160, 70, 160, 24, 'Carcasa', sub=None)
callout(f, 180, 140, 330, 120, 'Imanes y bobinas', sub='por dentro: lo que lo hace girar')
callout(f, 268, 84, 330, 50, 'Terminales + y −', sub='al invertirlos, gira al revés')
f.save(D + 'motor.svg')

# anatomía: L298N
f = Fig(640, 350)
q = place(f, l298n, 170, 30, s=1.5)
callout(f, 320, 50, 470, 30, 'Disipador', sub='el chip se calienta: aquí se enfría')
callout(f, 187, 105, 120, 60, 'Motor A', sub='OUT1 y OUT2', anchor='end')
callout(f, 453, 105, 520, 100, 'Motor B', sub='OUT3 y OUT4')
callout(f, 186, 256, 120, 220, 'Batería', sub='12V (de 5 a 35 V)', anchor='end')
callout(f, 219, 256, 120, 290, 'GND', sub='común con el Arduino', anchor='end')
callout(f, 252, 256, 300, 316, '5V', sub='salida del regulador')
callout(f, 320, 280, 470, 290, 'ENA y ENB', sub='velocidad (PWM) de cada motor')
callout(f, 380, 280, 470, 230, 'IN1 – IN4', sub='sentido de giro')
f.save(D + 'l298n.svg')

# puente H
def puente(f, x, tit, sub, sentido):
    f.rect(x, 10, 300, 270, fill='none', stroke=C['frame'], sw=1)
    f.title(x + 18, 38, tit, sub)
    L, R, T, B = x + 70, x + 230, 80, 240
    f.line(L, T, R, T, stroke=C['edge'], sw=2)
    f.line(L, B, R, B, stroke=C['edge'], sw=2)
    f.text(x + 150, T - 8, '+ batería', size=10.5, fill=C['muted'], anchor='middle')
    f.text(x + 150, B + 20, 'GND', size=10.5, fill=C['muted'], anchor='middle')
    my = 160
    sw_pos = {'S1': (L, T, L, my), 'S2': (R, T, R, my), 'S3': (L, my, L, B), 'S4': (R, my, R, B)}
    on = ('S1', 'S4') if sentido > 0 else ('S2', 'S3')
    for n, (x1, y1, x2, y2) in sw_pos.items():
        ya, yb = y1 + 22, y2 - 22
        col = WIRE['a'] if n in on else C['edge']
        f.line(x1, y1, x1, ya, stroke=col, sw=2)
        f.line(x1, yb, x1, y2, stroke=col, sw=2)
        if n in on:
            f.line(x1, ya, x1, yb, stroke=col, sw=2.5)
        else:
            f.line(x1, yb, x1 + 14, ya + 4, stroke=col, sw=2)
        f.circle(x1, ya, 3, fill=C['dark'], stroke=col, sw=1.5)
        f.circle(x1, yb, 3, fill=C['dark'], stroke=col, sw=1.5)
        f.text(x1 + (-12 if x1 == L else 12), (y1 + y2) / 2 + 4, n, size=10.5, fill=C['muted'], anchor='end' if x1 == L else 'start')
    # motor
    f.line(L, my, x + 120, my, stroke=WIRE['a'], sw=2)
    f.line(x + 180, my, R, my, stroke=WIRE['a'], sw=2)
    f.circle(x + 150, my, 26, fill=C['body2'], stroke=C['accent'], sw=2)
    f.text(x + 150, my + 5, 'M', size=15, weight=600, anchor='middle')
    if sentido > 0:
        f.path(f'M {x + 132} {my - 38} A 26 26 0 0 1 {x + 172} {my - 34}', stroke=C['accent'], sw=1.5, arrow='end')
    else:
        f.path(f'M {x + 168} {my - 38} A 26 26 0 0 0 {x + 128} {my - 34}', stroke=C['accent'], sw=1.5, arrow='end')

f = Fig(640, 290)
puente(f, 10, 'Hacia delante', 'S1 y S4 cerrados', 1)
puente(f, 330, 'Hacia atrás', 'S2 y S3 cerrados', -1)
f.save(D + 'puente-h.svg')

# conexión: un motor
f = Fig(640, 560)
u = Uno(f, 150, 290, used={'D9', 'D10', 'D11', 'GND'})
q = place(f, l298n, 300, 40, s=1.0)
m = place(f, motor_dc, 166, 70, s=1.0)
b = place(f, bateria, 40, 172, s=1.0, texto='7,4 V', sub='batería')
g, d9, d10, d11 = u.pin('GND'), u.pin('D9'), u.pin('D10'), u.pin('D11')
f.wire([m['+'], (296, m['+'][1]), (296, q['OUT1'][1]), q['OUT1']], 'e')
f.wire([m['−'], (296, m['−'][1]), (296, q['OUT2'][1]), q['OUT2']], '#8a8a8a')
f.wire([b['+'], (190, b['+'][1]), (190, q['12V'][1]), q['12V']], 'vcc')
nodo = (q['GND'][0], 240)
f.wire([b['−'], (176, b['−'][1]), (176, 240), nodo, q['GND']], 'gnd')
f.wire([nodo, (nodo[0], 262), (g[0], 262), g], 'gnd')
f.node(*nodo, 'gnd')
f.wire([q['ENA'], (q['ENA'][0], 272), (d11[0], 272), d11], 'a')
f.wire([q['IN1'], (q['IN1'][0], 282), (d10[0], 282), d10], 'b')
f.wire([q['IN2'], (q['IN2'][0], 292), (d9[0], 292), d9], 'c')
f.text(400, 30, 'L298N', size=13, weight=600, anchor='middle')
f.text(216, 60, 'Motor A', size=12, weight=600, anchor='middle')
f.text(512, 150, 'Segundo motor:', size=10.5, fill=C['muted'])
f.text(512, 166, 'OUT3, OUT4,', size=10.5, fill=C['muted'])
f.text(512, 182, 'IN3, IN4 y ENB', size=10.5, fill=C['muted'])
legend(f, 150, 548, [('vcc', 'batería +'), ('gnd', 'GND común'), ('a', 'ENA → 11'), ('b', 'IN1 → 10'), ('c', 'IN2 → 9')], gap=92)
f.save(D + 'conexion.svg')
