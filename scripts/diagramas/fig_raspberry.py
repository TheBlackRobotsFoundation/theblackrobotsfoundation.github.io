from lib import *
from parts import place, resistencia, pulsador, led_rgb, hcsr04, ordenador, METAL
from placas import raspberry, jetson, CabeceraRPi, GPIO40, EXTRA, TIPO_COLOR, tipo_pin
D = 'raspberry/'

# --- placa anotada ----------------------------------------------------------
f = Fig(640, 330)
place(f, raspberry, 150, 60, s=1.0)
callout(f, 200, 72, 200, 22, 'GPIO: 40 pines', sub=None)
callout(f, 250, 150, 110, 104, 'Procesador', sub='4 núcleos a 2,4 GHz', anchor='end')
callout(f, 470, 100, 560, 70, 'USB', sub='4 puertos')
callout(f, 470, 230, 560, 230, 'Ethernet')
callout(f, 189, 290, 130, 316, 'USB-C', sub=None, anchor='end')
callout(f, 252, 288, 290, 316, '2 × micro-HDMI')
callout(f, 335, 278, 440, 312, 'Cámara y pantalla')
callout(f, 152, 200, 110, 210, 'microSD', sub='por debajo', anchor='end')
f.save(D + 'placa.svg')

# --- tres cerebros ---------------------------------------------------------
f = Fig(720, 300)
# Arduino (placa reducida)
f.add('<g transform="translate(20 70) scale(0.5)">')
Uno(f, 0, 0)
f.add('</g>')
place(f, raspberry, 262, 70, s=0.55)
place(f, jetson, 506, 64, s=0.6)
for x, t, sub1, sub2 in ((110, 'Arduino', 'microcontrolador', 'pines, tiempo real'),
                         (355, 'Raspberry Pi', 'ordenador con Linux', 'Python, ROS 2, red'),
                         (596, 'Jetson', 'ordenador con GPU', 'visión e IA')):
    f.text(x, 40, t, size=15, weight=600, anchor='middle')
    f.text(x, 222, sub1, size=12, fill=C['accent'], anchor='middle')
    f.text(x, 240, sub2, size=11, fill=C['muted'], anchor='middle')
f.line(40, 274, 680, 274, stroke=C['edge'], sw=1, arrow='end')
f.text(40, 292, 'más sencillo', size=10.5, fill=C['dim'])
f.text(680, 292, 'más potencia de cálculo', size=10.5, fill=C['dim'], anchor='end')
f.save(D + 'tres-cerebros.svg')

# --- instalación -------------------------------------------------------------
def monitor(f, x, y, w=120, h=80):
    f.rect(x, y, w, h, fill='#141414', stroke=C['edge'], rx=5)
    f.rect(x + 7, y + 7, w - 14, h - 14, fill='#0d0d0d', stroke='#2e2e2e', rx=2)
    f.rect(x + w / 2 - 8, y + h, 16, 12, fill='#1c1c1c', stroke=C['edge'], sw=1)
    f.rect(x + w / 2 - 30, y + h + 12, 60, 6, fill='#1c1c1c', stroke=C['edge'], sw=1, rx=2)


def teclado(f, x, y, w=120):
    f.rect(x, y, w, 34, fill='#161616', stroke=C['edge'], rx=4)
    for r in range(3):
        for c in range(int((w - 12) / 11)):
            f.rect(x + 6 + c * 11, y + 5 + r * 9, 8, 6, fill='#2a2a2a', stroke='none', sw=0, rx=1)


def raton(f, x, y):
    f.rect(x, y, 24, 36, fill='#161616', stroke=C['edge'], rx=12)
    f.line(x + 12, y + 2, x + 12, y + 14, stroke=C['edge'], sw=1)


f = Fig(680, 400)
def paso(x, y, n, t, sub):
    f.circle(x, y, 13, fill=C['body2'], stroke=C['accent'], sw=1.5)
    f.text(x, y + 5, str(n), size=12, weight=600, anchor='middle')
    f.text(x, y + 150, t, size=13, weight=600, anchor='middle')
    f.text(x, y + 168, sub, size=10.5, fill=C['muted'], anchor='middle')
place(f, ordenador, 40, 60, s=0.75)
paso(100, 30, 1, 'Raspberry Pi Imager', 'graba el sistema')
f.path('M 318 70 L 352 70 L 362 80 L 362 130 L 318 130 Z', fill='#1d1d1d', stroke=C['accent'], sw=1.5)
for i in range(5):
    f.rect(322 + i * 7, 74, 4, 12, fill='#c9a24a', stroke='none', sw=0)
f.text(340, 116, 'SD', size=11, fill=C['muted'], anchor='middle')
paso(340, 30, 2, 'microSD', 'se la pones a la Raspberry')
place(f, raspberry, 500, 62, s=0.4)
paso(568, 30, 3, 'Primer arranque', 'el sistema termina de prepararse')
for x0, x1 in ((168, 304), (376, 490)):
    f.line(x0, 100, x1, 100, stroke=C['dim'], sw=1.5, arrow='end')
# bifurcación
f.path('M 568 216 L 568 236 L 180 236 L 180 256', stroke=C['dim'], sw=1.5, arrow='end')
f.path('M 568 236 L 500 236 L 500 256', stroke=C['dim'], sw=1.5, arrow='end')
f.text(340, 228, 'y la usas como prefieras', size=10.5, fill=C['dim'], anchor='middle')
monitor(f, 60, 262, w=110, h=62)
teclado(f, 180, 300, w=86)
raton(f, 274, 298)
f.text(180, 372, 'Con pantalla, teclado y ratón', size=13, weight=600, anchor='middle')
f.text(180, 390, 'como un ordenador de escritorio', size=10.5, fill=C['muted'], anchor='middle')
f.rect(440, 266, 120, 64, fill=C['body'], stroke=C['edge'], rx=4)
f.text(452, 290, '$ ssh', size=11, mono=True, fill=WIRE['c'])
f.text(452, 308, 'usuario@robot', size=11, mono=True, fill=C['accent'])
f.text(500, 372, 'A distancia, por SSH', size=13, weight=600, anchor='middle')
f.text(500, 390, 'desde la terminal de tu ordenador', size=10.5, fill=C['muted'], anchor='middle')
f.save(D + 'instalacion.svg')

# --- conexiones para usarla con pantalla ----------------------------------------
f = Fig(680, 380)
pi = place(f, raspberry, 230, 110, s=0.75)
monitor(f, 20, 20, w=160, h=104)
teclado(f, 490, 40, w=150)
raton(f, 600, 100)
# alimentación (USB-C, el conector de la izquierda)
uc = (230 + 39 * 0.75, 110 + 230 * 0.75)
f.wire([uc, (uc[0], 306), (200, 306)], 'vcc', sw=4)
f.rect(110, 290, 90, 32, fill='#1f1f1f', stroke=C['edge'], rx=4)
f.text(155, 311, '5 V · 5 A', size=11, weight=600, anchor='middle')
f.text(155, 282, 'USB-C', size=11, fill=C['muted'], anchor='middle')
# micro-HDMI -> pantalla
hd = (230 + 89 * 0.75, 110 + 230 * 0.75)
f.wire([hd, (hd[0], 346), (100, 346), (100, 160)], '#8a8a8a', sw=4)
f.text(200, 366, 'micro-HDMI → HDMI', size=11, fill=C['muted'], anchor='middle')
# USB -> teclado y ratón
f.wire([(230 + 350 * 0.75, 110 + 30 * 0.75), (565, 132), (565, 76)], '#8a8a8a', sw=4)
f.wire([(230 + 350 * 0.75, 110 + 50 * 0.75), (612, 148), (612, 138)], '#8a8a8a', sw=4)
f.text(600, 176, 'USB', size=11, fill=C['muted'], anchor='middle')
f.save(D + 'escritorio.svg')

# --- pinout ------------------------------------------------------------------
f = Fig(640, 560)
cx = 320
f.rect(cx - 40, 30, 80, 20 * 24 + 12, fill='#101010', stroke='#444', sw=1, rx=4)
for i in range(20):
    for j, n in ((0, 2 * i + 1), (1, 2 * i + 2)):
        y = 48 + i * 24
        x = cx - 16 + j * 32
        t = tipo_pin(n)
        col = TIPO_COLOR[t]
        f.circle(x, y, 8, fill=col if t != 'GPIO' else '#2a2a2a', stroke=col, sw=1.5)
        f.text(x, y + 3.5, str(n), size=8, weight=600, anchor='middle', fill=C['dark'] if t != 'GPIO' else C['accent'])
        lab = GPIO40[n]
        ex = EXTRA.get(n)
        if j == 0:
            f.text(cx - 52, y + 4, lab, size=11.5, weight=600, anchor='end', fill=col if t != 'GPIO' else C['text'])
            if ex:
                f.text(cx - 52 - 9 * len(lab) - 10, y + 4, ex, size=10, anchor='end', fill=C['muted'])
        else:
            f.text(cx + 52, y + 4, lab, size=11.5, weight=600, fill=col if t != 'GPIO' else C['text'])
            if ex:
                f.text(cx + 52 + 9 * len(lab) + 10, y + 4, ex, size=10, fill=C['muted'])
leg = [('5V', '5 V'), ('3V3', '3,3 V'), ('GND', 'GND'), ('GPIO', 'GPIO'), ('I2C', 'I2C'), ('SPI', 'SPI'), ('UART', 'UART')]
for i, (k, t) in enumerate(leg):
    x = 40 + i * 84
    f.circle(x, 542, 6, fill=TIPO_COLOR[k] if k != 'GPIO' else '#2a2a2a', stroke=TIPO_COLOR[k], sw=1.5)
    f.text(x + 12, 546, t, size=11, fill=C['muted'])
f.text(cx, 20, 'el pin 1 está en el extremo de la cabecera más alejado de los puertos USB', size=10.5, fill=C['dim'], anchor='middle')
f.save(D + 'pinout.svg')

# --- LED y pulsador -----------------------------------------------------------
f = Fig(640, 420)
h = CabeceraRPi(f, 60, 240, used={12, 14, 16, 20}, paso=18, ancho=520)
from parts import led_rgb as _x  # noqa
# LED sencillo dibujado aquí
def led(f, x, y):
    f.line(x + 6, y + 30, x + 6, y + 60, stroke=METAL, sw=2.2)
    f.line(x + 20, y + 30, x + 20, y + 52, stroke=METAL, sw=2.2)
    f.path(f'M {x} {y + 30} L {x} {y + 12} A 13 13 0 0 1 {x + 26} {y + 12} L {x + 26} {y + 30} Z', fill='#3a2222', stroke='#d9665b', sw=1.5)
    f.rect(x - 2, y + 28, 30, 4, fill='#3a2222', stroke='#d9665b', sw=1, rx=1)
    return {'+': (x + 6, y + 60), '−': (x + 20, y + 52)}
L = led(f, 120, 30)
r = place(f, resistencia, L['+'][0], 104, s=0.6, rot=90, valor='220', length=80)
f.wire([L['+'], r['1']], 'a')
p12, p14, p16, p20 = h.pin(12), h.pin(14), h.pin(16), h.pin(20)
f.wire([r['2'], (r['2'][0], 170), (p12[0], 170), p12], 'a')
f.wire([L['−'], (L['−'][0], 150), (p14[0], 150), p14], 'gnd')
b = place(f, pulsador, 300, 66, s=0.9)
# patas en diagonal: 3 (abajo izquierda) y 2 (arriba derecha)
f.wire([b['3'], (b['3'][0], 146), (p16[0], 146), p16], 'b')
f.wire([b['2'], (b['2'][0], 40), (400, 40), (400, 160), (p20[0], 160), p20], 'gnd')
f.text(104, 50, 'LED', size=12, weight=600, anchor='end')
f.text(r['2'][0] - 12, 108, '220 Ω', size=11, fill=C['muted'], anchor='end')
f.text(360, 60, 'Pulsador', size=12, weight=600)
legend(f, 60, 412, [('a', 'LED → GPIO18 (pin 12)'), ('b', 'pulsador → GPIO23 (pin 16)'), ('gnd', 'GND (pines 14 y 20)')], gap=190)
f.save(D + 'led-pulsador.svg')

# --- Raspberry y Arduino por USB ---------------------------------------------
f = Fig(720, 300)
place(f, raspberry, 20, 50, s=0.75)
f.add('<g transform="translate(400 60) scale(0.6)">')
Uno(f, 0, 0)
f.add('</g>')
f.wire([(282, 80), (330, 80), (330, 92), (390, 92)], '#8a8a8a', sw=4)
f.text(336, 76, 'USB', size=11, fill=C['muted'], anchor='middle')
f.text(147, 30, 'Raspberry Pi: el cerebro', size=13, weight=600, anchor='middle')
f.text(147, 238, 'decide, procesa, ROS 2, red', size=11, fill=C['muted'], anchor='middle')
f.text(508, 30, 'Arduino: los músculos', size=13, weight=600, anchor='middle')
f.text(508, 214, 'lee sensores y mueve motores', size=11, fill=C['muted'], anchor='middle')
for i, (t, msg, k) in enumerate((('Arduino → Raspberry', 'D 42.5', 'b'), ('Raspberry → Arduino', 'M 150 150', 'a'))):
    y = 262 + i * 22
    f.text(250, y, t, size=11, fill=C['muted'])
    f.text(400, y, msg, size=11, mono=True, fill=WIRE[k])
f.text(470, 262, 'distancia en cm', size=10.5, fill=C['dim'])
f.text(470, 284, 'velocidad de los motores', size=10.5, fill=C['dim'])
f.save(D + 'arduino-usb.svg')
