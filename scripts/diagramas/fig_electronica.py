import math
from lib import *

D = 'electronica/'

# --- Ley de Ohm --------------------------------------------------------------
f = Fig(640, 260)
# circuito: pila a la izquierda, resistencia arriba
x0, y0, x1, y1 = 60, 50, 300, 210
f.poly([(x0, 112), (x0, y0), (150, y0)], stroke=C['accent'], sw=2)
f.poly([(210, y0), (x1, y0), (x1, y1), (x0, y1), (x0, 148)], stroke=C['accent'], sw=2)
f.rect(150, y0 - 10, 60, 20, fill=C['body2'], stroke=C['accent'], sw=2, rx=1)
f.text(180, y0 - 20, 'R', size=14, weight=600, anchor='middle')
# pila
f.line(x0 - 20, 112, x0 + 20, 112, stroke=C['accent'], sw=2.5)
f.line(x0 - 11, 124, x0 + 11, 124, stroke=C['accent'], sw=4)
f.line(x0 - 20, 136, x0 + 20, 136, stroke=C['accent'], sw=2.5)
f.line(x0 - 11, 148, x0 + 11, 148, stroke=C['accent'], sw=4)
f.text(x0 - 30, 134, 'V', size=14, weight=600, anchor='end')
f.text(x0 + 28, 116, '+', size=12, fill=C['muted'])
# corriente
f.path(f'M {x1 + 18} 90 L {x1 + 18} 170', stroke=WIRE['a'], sw=2, arrow='end')
f.text(x1 + 30, 134, 'I', size=14, weight=600, fill=WIRE['a'])
# fórmula
f.text(470, 120, 'V = I × R', size=30, weight=600, anchor='middle')
f.text(470, 152, 'tensión = corriente × resistencia', size=12, fill=C['muted'], anchor='middle')
f.text(470, 184, 'voltios · amperios · ohmios', size=11, fill=C['dim'], anchor='middle')
f.save(D + 'ley-de-ohm.svg')

# --- Señal digital vs analógica ----------------------------------------------
f = Fig(640, 230)
f.rect(10, 10, 300, 210, fill='none', stroke=C['frame'], sw=1)
f.rect(330, 10, 300, 210, fill='none', stroke=C['frame'], sw=1)
f.title(28, 38, 'Digital', 'solo dos valores: 0 o 1')
f.title(348, 38, 'Analógica', 'cualquier valor intermedio')
axes(f, 66, 90, 224, 100)
wave(f, 66, 90, 224, 100, [(0, 0), (.12, 0), (.12, 1), (.38, 1), (.38, 0), (.5, 0), (.5, 1), (.62, 1), (.62, 0), (.82, 0), (.82, 1), (1, 1)], stroke=WIRE['a'], sw=2.5)
axes(f, 386, 90, 224, 100)
pts = [(i / 80, 0.5 + 0.38 * math.sin(i / 80 * 2 * math.pi * 1.3) + 0.08 * math.sin(i / 80 * 13)) for i in range(81)]
wave(f, 386, 90, 224, 100, pts, stroke=WIRE['b'], sw=2.5)
f.save(D + 'digital-analogico.svg')

# --- Conversión analógica 0..1023 -------------------------------------------
f = Fig(640, 150)
f.text(20, 40, '0 V', size=13, weight=600)
f.text(620, 40, '5 V', size=13, weight=600, anchor='end')
f.rect(20, 54, 600, 14, fill=C['body2'], stroke=C['edge'], rx=7)
f.add('<defs><linearGradient id="gr" x1="0" x2="1"><stop offset="0" stop-color="#1c1c1c"/><stop offset="1" stop-color="#d0d0d0"/></linearGradient></defs>')
f.rect(20, 54, 600, 14, fill='url(#gr)', stroke='none', sw=0, rx=7)
for v, lab in ((0, '0'), (0.25, '256'), (0.5, '512'), (0.75, '767'), (1, '1023')):
    x = 20 + v * 600
    f.line(x, 74, x, 84, stroke=C['edge'], sw=1)
    f.text(x, 102, lab, size=12, fill=C['accent'], anchor='middle', mono=True)
f.text(320, 134, 'analogRead() convierte la tensión en un número de 0 a 1023', size=12, fill=C['muted'], anchor='middle')
f.save(D + 'conversion-adc.svg')

# --- PWM ---------------------------------------------------------------------
f = Fig(640, 330)
rows = [(0.25, '25 %', 'brillo bajo'), (0.5, '50 %', 'brillo medio'), (0.75, '75 %', 'brillo alto')]
for i, (d, pct, txt) in enumerate(rows):
    y = 30 + i * 100
    axes(f, 70, y, 420, 50, top='5 V' if i == 0 else '', bottom='0 V' if i == 2 else '')
    wave(f, 70, y, 420, 50, square(d, 5), stroke=WIRE['a'], sw=2.2)
    avg = y + 50 - d * 50
    f.line(70, avg, 490, avg, stroke=C['muted'], sw=1, dash='4 4')
    f.text(520, y + 22, pct, size=18, weight=600)
    f.text(520, y + 42, txt, size=11, fill=C['muted'])
f.text(70, 322, 'la línea discontinua es la tensión media que "ve" el componente', size=11, fill=C['dim'])
f.save(D + 'pwm.svg')

# --- Divisor de tensión ------------------------------------------------------
f = Fig(640, 300)
cx = 150
f.text(cx, 28, 'Vin', size=13, weight=600, anchor='middle')
f.circle(cx, 40, 3.5, fill=C['accent'], stroke='none', sw=0)
f.line(cx, 40, cx, 62, stroke=C['accent'], sw=2)
f.rect(cx - 9, 62, 18, 54, fill=C['body2'], stroke=C['accent'], sw=2, rx=1)
f.text(cx - 22, 94, 'R1', size=13, weight=600, anchor='end')
f.line(cx, 116, cx, 172, stroke=C['accent'], sw=2)
f.rect(cx - 9, 172, 18, 54, fill=C['body2'], stroke=C['accent'], sw=2, rx=1)
f.text(cx - 22, 204, 'R2', size=13, weight=600, anchor='end')
f.line(cx, 226, cx, 254, stroke=C['accent'], sw=2)
for i, w in enumerate((26, 16, 6)):
    f.line(cx - w / 2, 254 + i * 6, cx + w / 2, 254 + i * 6, stroke=C['accent'], sw=2)
f.text(cx + 24, 276, 'GND', size=11, fill=C['muted'])
f.node(cx, 144, 'a')
f.line(cx, 144, 250, 144, stroke=WIRE['a'], sw=2)
f.circle(254, 144, 4, fill=C['dark'], stroke=WIRE['a'], sw=2)
f.text(266, 149, 'Vout', size=13, weight=600, fill=WIRE['a'])
f.text(470, 132, 'Vout = Vin × R2 / (R1 + R2)', size=17, weight=600, anchor='middle')
f.text(470, 162, 'con R1 = R2, la salida es la mitad', size=12, fill=C['muted'], anchor='middle')
f.text(470, 182, '5 V  →  2,5 V', size=12, fill=C['dim'], anchor='middle', mono=True)
f.save(D + 'divisor-de-tension.svg')

# --- Bus I2C -----------------------------------------------------------------
f = Fig(640, 250)
f.rect(30, 70, 130, 90, fill=C['body'], stroke=C['edge'], rx=4)
f.text(95, 110, 'Arduino', size=14, weight=600, anchor='middle')
f.text(95, 128, 'controlador', size=11, fill=C['muted'], anchor='middle')
ys = {'SDA': 96, 'SCL': 134}
for n, y in ys.items():
    k = 'b' if n == 'SDA' else 'a'
    f.line(160, y, 610, y, stroke=WIRE[k], sw=3)
    f.text(170, y - 8, n, size=11, weight=600, fill=WIRE[k])
devs = [(280, 'IMU', '0x68'), (420, 'Pantalla', '0x3C'), (540, 'Sensor', '0x29')]
for x, n, addr in devs:
    f.rect(x - 50, 180, 100, 52, fill=C['body'], stroke=C['edge'], rx=4)
    f.text(x, 202, n, size=13, weight=600, anchor='middle')
    f.text(x, 220, addr, size=11, fill=C['muted'], anchor='middle', mono=True)
    for dx, (nn, y) in zip((-14, 14), ys.items()):
        k = 'b' if nn == 'SDA' else 'a'
        f.line(x + dx, y, x + dx, 180, stroke=WIRE[k], sw=2)
        f.node(x + dx, y, k)
f.text(30, 40, 'Dos cables compartidos. Cada dispositivo responde a su dirección.', size=12, fill=C['muted'])
f.save(D + 'bus-i2c.svg')

# --- GND común ---------------------------------------------------------------
f = Fig(640, 270)
boxes = [(30, 'Arduino', 'lógica 5 V'), (245, 'Driver', 'control'), (460, 'Fuente', 'motores 12 V')]
for x, n, sub in boxes:
    f.rect(x, 50, 150, 90, fill=C['body'], stroke=C['edge'], rx=4)
    f.text(x + 75, 92, n, size=14, weight=600, anchor='middle')
    f.text(x + 75, 110, sub, size=11, fill=C['muted'], anchor='middle')
f.wire([(180, 80), (245, 80)], 'a')
f.text(212, 72, 'señal', size=10, fill=C['muted'], anchor='middle')
f.wire([(460, 80), (395, 80)], 'vcc')
f.text(428, 72, '12 V', size=10, fill=C['muted'], anchor='middle')
for x in (105, 320, 535):
    f.line(x, 140, x, 200, stroke=WIRE['gnd'], sw=3)
    f.node(x, 200, 'gnd')
f.line(105, 200, 535, 200, stroke=WIRE['gnd'], sw=3)
f.text(320, 228, 'GND común: todas las masas unidas', size=13, weight=600, anchor='middle')
f.text(320, 248, 'así todos miden las tensiones desde la misma referencia', size=11, fill=C['muted'], anchor='middle')
f.save(D + 'gnd-comun.svg')
