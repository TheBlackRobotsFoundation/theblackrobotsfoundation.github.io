"""
Componentes dibujados en coordenadas locales (origen arriba a la izquierda).

Cada función recibe la figura y devuelve un dict {pin: (x, y)} en coordenadas
locales. Se colocan con place(), que aplica traslación y escala.
"""

import math
from lib import C, WIRE

PCB = '#161616'
PCB_EDGE = '#4a4a4a'
METAL = '#bdbdbd'
HOLE = '#0a0a0a'
PIN_FILL = C['accent']


def place(fig, part, x, y, s=1.0, rot=0, **kw):
    fig.add(f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">')
    pins = part(fig, **kw)
    fig.add('</g>')
    a = math.radians(rot)
    ca, sa = math.cos(a), math.sin(a)
    return {k: (round(x + (px * ca - py * sa) * s, 1), round(y + (px * sa + py * ca) * s, 1))
            for k, (px, py) in pins.items()}


def _pins_row(fig, x0, y, names, gap, labels=True, below=False, size=9.5, rot=False):
    out = {}
    for i, n in enumerate(names):
        px = x0 + i * gap
        fig.rect(px - 4, y - 4, 8, 8, fill=PIN_FILL, stroke='none', sw=0, rx=1)
        if labels and n:
            if rot:
                if below:
                    fig.text(px + 3, y + 10, n, size=size, fill=C['muted'], anchor='end', rotate=-90)
                else:
                    fig.text(px + 3, y - 10, n, size=size, fill=C['muted'], anchor='start', rotate=-90)
            else:
                fig.text(px, y + 18 if below else y - 10, n, size=size, fill=C['muted'], anchor='middle')
        out[n] = (px, y)
    return out


def _legs(fig, xs, y0, y1):
    for x in xs:
        fig.line(x, y0, x, y1, stroke=METAL, sw=2.2)


# ---------------------------------------------------------------- sensores

def pulsador(fig):
    # pulsador táctil de 4 patas visto desde arriba (60x60).
    # Patas 1-2 (arriba) unidas entre sí; 3-4 (abajo) unidas entre sí.
    _legs(fig, (12, 48), -16, 0)
    _legs(fig, (12, 48), 60, 76)
    fig.rect(0, 0, 60, 60, fill='#1a1a1a', stroke=C['edge'], rx=3)
    for cx, cy in ((7, 7), (53, 7), (7, 53), (53, 53)):
        fig.circle(cx, cy, 2.2, fill=C['dark'], stroke=C['edge'], sw=1)
    fig.circle(30, 30, 16, fill='#232323', stroke=C['accent'], sw=1.5)
    fig.circle(30, 30, 10, fill='#2c2c2c', stroke='none', sw=0)
    return {'1': (12, -16), '2': (48, -16), '3': (12, 76), '4': (48, 76)}


def potenciometro(fig):
    # potenciómetro rotativo con eje (70 de ancho)
    _legs(fig, (15, 35, 55), 62, 84)
    fig.rect(2, 8, 66, 56, fill='#1a1a1a', stroke=C['edge'], rx=6)
    fig.circle(35, 34, 22, fill='#202020', stroke=C['edge'])
    fig.circle(35, 34, 13, fill='#2a2a2a', stroke=C['accent'])
    fig.line(35, 34, 35, 23, stroke=C['accent'], sw=2.5)
    return {'GND': (15, 84), 'OUT': (35, 84), 'VCC': (55, 84)}


def ldr(fig):
    # fotorresistencia (disco con pista en zigzag)
    _legs(fig, (14, 30), 34, 70)
    fig.circle(22, 22, 17, fill='#2a2418', stroke=C['edge'])
    d = 'M 10 14'
    for i in range(6):
        y = 14 + i * 3.2
        d += f' L {34 if i % 2 == 0 else 10} {y} L {34 if i % 2 == 0 else 10} {y + 3.2}'
    fig.path(d, stroke='#c9a24a', sw=1.4)
    return {'1': (14, 70), '2': (30, 70)}


def dht22(fig):
    # módulo DHT22 de 3 pines (caja blanca rejilla)
    fig.rect(0, 0, 70, 110, fill=PCB, stroke=PCB_EDGE, rx=4)
    fig.rect(10, 8, 50, 70, fill='#d8d8d8', stroke='#9a9a9a', rx=3)
    for r in range(5):
        for c in range(4):
            fig.rect(16 + c * 10.5, 14 + r * 11.5, 6, 7, fill='#8c8c8c', stroke='none', sw=0, rx=1)
    fig.text(35, 92, 'DHT22', size=9, fill=C['muted'], anchor='middle')
    for x, n in zip((19, 35, 51), ('+', 'OUT', '−')):
        fig.text(x, 105, n, size=8, fill=C['muted'], anchor='middle')
    _legs(fig, (19, 35, 51), 110, 124)
    return _pins_row(fig, 19, 124, ['+', 'OUT', '−'], 16, labels=False)


def hcsr04(fig):
    # sensor de ultrasonidos HC-SR04 (180x100), etiquetas serigrafiadas
    fig.rect(0, 0, 180, 100, fill='#14202b', stroke='#3e5466', rx=4)
    for cx in (42, 138):
        fig.circle(cx, 42, 31, fill='#bdbdbd', stroke='#8a8a8a', sw=1.5)
        fig.circle(cx, 42, 25, fill='#2a2a2a', stroke='#6a6a6a', sw=1)
        for r in (8, 14, 20):
            fig.circle(cx, 42, r, fill='none', stroke='#444', sw=1)
    fig.rect(78, 32, 24, 14, fill='#d4d4d4', stroke='#8a8a8a', rx=6)
    for x, n in zip((60, 80, 100, 120), ('VCC', 'Trig', 'Echo', 'GND')):
        fig.text(x, 92, n, size=7.5, fill='#9fb3c8', anchor='middle')
    _legs(fig, (60, 80, 100, 120), 100, 114)
    return _pins_row(fig, 60, 114, ['VCC', 'Trig', 'Echo', 'GND'], 20, labels=False)


def tcrt5000(fig):
    # módulo sigue-líneas TCRT5000 (70x130): sensor arriba, pines abajo
    fig.rect(0, 0, 70, 130, fill='#14202b', stroke='#3e5466', rx=4)
    fig.rect(20, 8, 30, 34, fill='#101010', stroke='#5a5a5a', rx=2)
    fig.circle(35, 17, 5.5, fill='#3a5fa0', stroke='none', sw=0)
    fig.circle(35, 33, 5.5, fill='#1e1e1e', stroke='#777', sw=1)
    fig.rect(23, 56, 24, 24, fill='#3a5fa0', stroke='#6c8cc5', rx=2)
    fig.circle(35, 68, 7, fill='#d0d0d0', stroke='none', sw=0)
    fig.line(31, 68, 39, 68, stroke='#3a5fa0', sw=1.6)
    fig.circle(12, 92, 2.6, fill='#e05555', stroke='none', sw=0)
    xs = (11, 27, 43, 59)
    for x, n in zip(xs, ('VCC', 'GND', 'DO', 'AO')):
        fig.text(x, 120, n, size=7, fill='#9fb3c8', anchor='middle')
    _legs(fig, xs, 130, 144)
    return _pins_row(fig, 11, 144, ['VCC', 'GND', 'DO', 'AO'], 16, labels=False)


def final_carrera(fig):
    # microinterruptor con palanca (terminales abajo)
    fig.path('M 10 6 L 92 -10', stroke=METAL, sw=3)
    fig.circle(92, -10, 6, fill='#2a2a2a', stroke=METAL, sw=1.5)
    fig.rect(0, 6, 100, 46, fill='#1d1d1d', stroke=C['edge'], rx=3)
    fig.rect(36, 2, 12, 6, fill='#c33', stroke='none', sw=0, rx=1)
    for cx in (16, 84):
        fig.circle(cx, 30, 4, fill=C['dark'], stroke=C['edge'], sw=1)
    for x in (18, 50, 82):
        fig.rect(x - 4, 52, 8, 18, fill=METAL, stroke='none', sw=0, rx=1)
    out = {}
    for x, n in ((18, 'COM'), (50, 'NC'), (82, 'NO')):
        fig.text(x, 46, n, size=8, fill=C['muted'], anchor='middle')
        out[n] = (x, 70)
    return out


def motor_encoder(fig):
    # motorreductor con encoder Hall en la parte trasera (vista lateral)
    fig.rect(-26, 44, 26, 12, fill=METAL, stroke='none', sw=0, rx=1)         # eje
    fig.rect(0, 20, 50, 60, fill='#c9a24a', stroke='#8a6f33', rx=3)          # reductora
    fig.rect(50, 18, 100, 64, fill='#9a9a9a', stroke='#6a6a6a', rx=10)       # motor
    fig.rect(150, 10, 10, 80, fill='#202020', stroke=C['edge'], rx=1)        # disco imán
    fig.rect(160, 2, 46, 96, fill='#14202b', stroke='#3e5466', rx=3)        # PCB encoder
    names = ['M1', 'GND', 'A', 'B', 'VCC', 'M2']
    out = {}
    for i, n in enumerate(names):
        py = 12 + i * 15.2
        fig.text(200, py + 3, n, size=7.5, fill='#9fb3c8', anchor='end')
        fig.line(206, py, 218, py, stroke=METAL, sw=2)
        fig.rect(218, py - 4, 8, 8, fill=PIN_FILL, stroke='none', sw=0, rx=1)
        out[n] = (222, py)
    return out


def mpu6050(fig):
    # módulo GY-521 con MPU6050 (112x84), pines abajo con serigrafía
    fig.rect(0, 0, 112, 84, fill='#14202b', stroke='#3e5466', rx=4)
    for cx in (10, 102):
        fig.circle(cx, 10, 4, fill=HOLE, stroke='#3e5466', sw=1)
    fig.rect(42, 16, 28, 28, fill='#101010', stroke='#5a5a5a', rx=2)
    fig.circle(47, 21, 1.6, fill='#666', stroke='none', sw=0)
    fig.rect(88, 50, 12, 8, fill='#101010', stroke='#555', sw=1, rx=1)
    # ejes serigrafiados
    fig.line(80, 38, 94, 38, stroke='#9fb3c8', sw=1.2, arrow='end')
    fig.line(80, 38, 80, 24, stroke='#9fb3c8', sw=1.2, arrow='end')
    fig.circle(80, 38, 2, fill='#9fb3c8', stroke='none', sw=0)
    fig.text(97, 41, 'X', size=7, fill='#9fb3c8')
    fig.text(77, 21, 'Y', size=7, fill='#9fb3c8')
    names = ['VCC', 'GND', 'SCL', 'SDA', 'XDA', 'XCL', 'AD0', 'INT']
    for i, n in enumerate(names):
        fig.text(7 + i * 14, 72, n, size=5.6, fill='#9fb3c8', anchor='middle')
    _legs(fig, [7 + i * 14 for i in range(8)], 84, 96)
    return _pins_row(fig, 7, 96, names, 14, labels=False)


def rplidar(fig):
    # RPLIDAR A1 visto desde arriba (base cuadrada + torreta)
    fig.rect(0, 20, 150, 110, fill='#1c1c1c', stroke=C['edge'], rx=10)
    fig.circle(65, 75, 46, fill='#121212', stroke='#5a5a5a')
    fig.circle(65, 75, 34, fill='#222', stroke='#6a6a6a')
    fig.rect(48, 64, 34, 22, fill='#0d0d0d', stroke='#777', rx=4)
    fig.circle(57, 75, 5, fill='#3a3a3a', stroke='none', sw=0)
    fig.circle(73, 75, 5, fill='#3a3a3a', stroke='none', sw=0)
    fig.rect(124, 60, 20, 30, fill='#14202b', stroke='#3e5466', rx=2)
    return {'cable': (144, 75)}


def zumbador(fig):
    # zumbador (cilindro negro visto desde arriba + patas)
    _legs(fig, (24, 44), 56, 84)
    fig.circle(34, 34, 30, fill='#121212', stroke=C['edge'])
    fig.circle(34, 34, 24, fill='none', stroke='#2a2a2a', sw=1)
    fig.circle(34, 34, 5, fill=HOLE, stroke='#444', sw=1)
    fig.text(20, 18, '+', size=11, fill=C['muted'], anchor='middle')
    return {'+': (24, 84), '−': (44, 84)}


# -------------------------------------------------------------- actuadores

def led_rgb(fig):
    # LED RGB de cátodo común: 4 patas, la más larga es el común
    xs = (12, 26, 40, 54)
    lens = (40, 58, 40, 40)
    for x, ln in zip(xs, lens):
        fig.line(x, 50, x, 50 + ln, stroke=METAL, sw=2.2)
    fig.path('M 6 50 L 6 26 A 27 27 0 0 1 60 26 L 60 50 Z', fill='#2c2c2c', stroke='#8a8a8a', sw=1.5)
    fig.rect(3, 48, 60, 6, fill='#2c2c2c', stroke='#8a8a8a', rx=1)
    for x, col in zip((18, 33, 48), ('#e05555', '#5fbf73', '#5f8fe0')):
        fig.circle(x, 30, 3.5, fill=col, stroke='none', sw=0)
    return {'R': (12, 90), '−': (26, 108), 'G': (40, 90), 'B': (54, 90)}


def neopixel(fig, n=4, right=False):
    # tira de LEDs WS2812. right=True: entrada por la derecha
    w = 30 + n * 46
    fig.rect(0, 0, w, 40, fill='#1a1a1a', stroke='#5a5a5a', rx=3)
    off = 0 if right else 26
    for i in range(n):
        x = 12 + off + i * 46
        fig.rect(x, 8, 24, 24, fill='#e8e8e8', stroke='#9a9a9a', rx=2)
        fig.circle(x + 12, 20, 8, fill='#fafafa', stroke='#c0c0c0', sw=1)
        if i < n - 1:
            fig.path(f'M {x + 35} 6 L {x + 35} 34', stroke='#5a5a5a', sw=1, dash='2 3')
    px = w - 16 if right else 4
    pads = {}
    for n_, y in (('5V', 8), ('DIN', 20), ('GND', 32)):
        fig.rect(px, y - 3.5, 12, 7, fill='#c9a24a', stroke='none', sw=0, rx=1)
        pads[n_] = (px + 12, y) if right else (px, y)
    if right:
        fig.line(w - 40, -10, w - 90, -10, stroke=C['muted'], sw=1, arrow='end')
    else:
        fig.line(40, -10, 90, -10, stroke=C['muted'], sw=1, arrow='end')
    return pads


def servo(fig):
    # micro servo SG90 visto desde arriba, cable a la izquierda abajo
    fig.rect(-14, 30, 128, 12, fill='#2d4f7c', stroke='#4a6d9a', rx=2)   # orejas
    for cx in (-6, 106):
        fig.circle(cx, 36, 3, fill=HOLE, stroke='none', sw=0)
    fig.rect(0, 0, 100, 76, fill='#2d4f7c', stroke='#4a6d9a', rx=4)
    fig.circle(30, 26, 18, fill='#355c8f', stroke='#5a7fb0', sw=1)
    fig.circle(30, 26, 7, fill='#e8e8e8', stroke='none', sw=0)
    fig.path('M 30 20 L 82 22 Q 88 26 82 30 L 30 32 Z', fill='#ededed', stroke='#b0b0b0', sw=1)
    for cx in (50, 62, 74):
        fig.circle(cx, 26, 1.6, fill='#999', stroke='none', sw=0)
    fig.text(62, 62, 'SG90', size=10, fill='#a9c0dd', anchor='middle', weight=600)
    # cable
    cols = ('#8b5a2b', '#d9665b', '#e39a3b')
    for i, col in enumerate(cols):
        fig.path(f'M {12 + i * 4} 76 L {12 + i * 4} 92 L {8 + i * 8} 104', stroke=col, sw=2.6)
    fig.rect(1, 104, 30, 16, fill='#1a1a1a', stroke='#555', rx=1)
    out = {}
    for i, n in enumerate(('GND', '5V', 'SIG')):
        out[n] = (8 + i * 8, 120)
    return out


def motor_dc(fig):
    # motor DC de juguete (vista lateral), terminales a la derecha
    fig.rect(-20, 30, 22, 10, fill=METAL, stroke='none', sw=0, rx=1)
    fig.rect(0, 6, 90, 58, fill='#a8a8a8', stroke='#6a6a6a', rx=8)
    fig.rect(0, 6, 18, 58, fill='#909090', stroke='#6a6a6a', rx=6)
    fig.rect(88, 14, 14, 42, fill='#b07a3a', stroke='#7a5528', rx=2)
    fig.rect(102, 18, 10, 6, fill=METAL, stroke='none', sw=0, rx=1)
    fig.rect(102, 46, 10, 6, fill=METAL, stroke='none', sw=0, rx=1)
    return {'+': (112, 21), '−': (112, 49)}


def l298n(fig):
    # módulo L298N (200x170). Bornas de motor a izquierda y derecha,
    # alimentación abajo-izquierda, pines de control abajo-derecha.
    fig.rect(0, 0, 200, 170, fill='#7a1f1f', stroke='#a04444', rx=5, opacity=0.35)
    fig.rect(0, 0, 200, 170, fill='none', stroke='#8a4a4a', rx=5)
    # disipador
    fig.rect(60, 6, 80, 70, fill='#1d1d1d', stroke='#555', rx=2)
    for i in range(7):
        fig.rect(66 + i * 10.5, 10, 5, 62, fill='#2e2e2e', stroke='none', sw=0, rx=1)
    fig.rect(78, 82, 44, 22, fill='#101010', stroke='#555', rx=2)
    fig.text(100, 97, 'L298N', size=9, fill=C['muted'], anchor='middle')
    def borna(x, y, n, vertical=True):
        pts = []
        for i in range(n):
            if vertical:
                bx, by = x, y + i * 20
                fig.rect(bx, by, 22, 20, fill='#2d5fa0', stroke='#6c8cc5', sw=1, rx=1)
                fig.circle(bx + 11, by + 10, 5, fill=METAL, stroke='#777', sw=1)
                pts.append((bx + 11, by + 10))
            else:
                bx, by = x + i * 22, y
                fig.rect(bx, by, 22, 22, fill='#2d5fa0', stroke='#6c8cc5', sw=1, rx=1)
                fig.circle(bx + 11, by + 11, 5, fill=METAL, stroke='#777', sw=1)
                pts.append((bx + 11, by + 11))
        return pts
    o12 = borna(4, 40, 2)
    o34 = borna(174, 40, 2)
    pw = borna(10, 140, 3, vertical=False)
    for (px, py), n in zip(o12, ('OUT1', 'OUT2')):
        fig.text(32, py + 3.5, n, size=8.5, fill=C['muted'])
    for (px, py), n in zip(o34, ('OUT3', 'OUT4')):
        fig.text(168, py + 3.5, n, size=8.5, fill=C['muted'], anchor='end')
    for (px, py), n in zip(pw, ('12V', 'GND', '5V')):
        fig.text(px, 134, n, size=8.5, fill=C['muted'], anchor='middle')
    names = ['ENA', 'IN1', 'IN2', 'IN3', 'IN4', 'ENB']
    x0 = 100
    out = {}
    fig.rect(x0 - 8, 160, 5 * 14 + 16, 14, fill='#101010', stroke='#555', sw=1, rx=1)
    for i, n in enumerate(names):
        px = x0 + i * 14
        fig.rect(px - 3.5, 163.5, 7, 7, fill=PIN_FILL, stroke='none', sw=0, rx=1)
        fig.text(px + 3, 155, n, size=7.5, fill=C['muted'], anchor='start', rotate=-90)
        out[n] = (px, 167)
    # jumpers de ENA y ENB
    out.update({'OUT1': o12[0], 'OUT2': o12[1], 'OUT3': o34[0], 'OUT4': o34[1],
                '12V': pw[0], 'GND': pw[1], '5V': pw[2]})
    return out


def rele(fig):
    # módulo de relé de 1 canal (160x84): pines a la izquierda, bornas a la derecha
    fig.rect(0, 0, 160, 84, fill='#14202b', stroke='#3e5466', rx=4)
    fig.rect(40, 12, 66, 52, fill='#2d5fa0', stroke='#6c8cc5', rx=2)
    fig.text(73, 36, 'SRD-05VDC', size=7.5, fill='#cfd9e8', anchor='middle')
    fig.text(73, 48, '10A 250VAC', size=7, fill='#9fb3c8', anchor='middle')
    fig.circle(26, 72, 3, fill='#e05555', stroke='none', sw=0)
    pts = {}
    for i, n in enumerate(('NO', 'COM', 'NC')):
        by = 6 + i * 24
        fig.rect(114, by, 42, 24, fill='#2d5fa0', stroke='#6c8cc5', sw=1, rx=1)
        fig.circle(144, by + 12, 6, fill=METAL, stroke='#777', sw=1)
        fig.text(126, by + 15, n, size=7.5, fill='#cfd9e8', anchor='middle')
        pts[n] = (156, by + 12)
    for i, n in enumerate(('VCC', 'GND', 'IN')):
        py = 18 + i * 22
        fig.text(7, py + 3, n, size=7.5, fill='#9fb3c8')
        fig.line(0, py, -14, py, stroke=METAL, sw=2)
        fig.rect(-18, py - 4, 8, 8, fill=PIN_FILL, stroke='none', sw=0, rx=1)
        pts[n] = (-14, py)
    return pts


def esc(fig):
    # variador ESC con funda termorretráctil (120x52)
    fig.rect(0, 0, 120, 52, fill='#1f2b38', stroke='#3e5466', rx=8)
    fig.text(60, 31, 'ESC 30A', size=11, fill='#a9c0dd', anchor='middle', weight=600)
    out = {}
    fig.path('M 0 14 L -30 14', stroke='#d9665b', sw=4)
    fig.path('M 0 38 L -30 38', stroke='#5a5a5a', sw=4)
    out['BAT+'] = (-30, 14)
    out['BAT−'] = (-30, 38)
    for i in range(3):
        y = 10 + i * 16
        fig.path(f'M 120 {y} L 150 {y}', stroke='#3a3a3a', sw=4)
        out['M' + str(i + 1)] = (150, y)
    for i, col in enumerate(('#8b5a2b', '#d9665b', '#e3e3e3')):
        x = 52 + i * 8
        fig.path(f'M {x} 52 L {x} 78', stroke=col, sw=2.5)
    fig.rect(44, 78, 32, 14, fill='#1a1a1a', stroke='#555', rx=1)
    out['GND'] = (52, 92)
    out['BEC'] = (60, 92)
    out['SIG'] = (68, 92)
    return out


def brushless(fig):
    # motor brushless exterior (vista superior)
    fig.circle(50, 50, 46, fill='#1d1d1d', stroke='#6a6a6a')
    for i in range(6):
        a = i * math.pi / 3
        fig.circle(50 + 30 * math.cos(a), 50 + 30 * math.sin(a), 6, fill='#0e0e0e', stroke='#444', sw=1)
    fig.circle(50, 50, 12, fill='#333', stroke='#888')
    fig.circle(50, 50, 4, fill=METAL, stroke='none', sw=0)
    out = {}
    for i in range(3):
        y = 36 + i * 14
        fig.path(f'M 96 {y} L 130 {y}', stroke='#3a3a3a', sw=4)
        out['M' + str(i + 1)] = (130, y)
    return out


def bateria(fig, texto='7,4 V', sub='LiPo 2S'):
    fig.rect(0, 0, 110, 50, fill='#1f1f1f', stroke=C['edge'], rx=6)
    fig.rect(110, 16, 6, 18, fill='#3a3a3a', stroke='none', sw=0, rx=1)
    fig.text(55, 24, texto, size=13, weight=600, anchor='middle')
    fig.text(55, 40, sub, size=10, fill=C['muted'], anchor='middle')
    return {'+': (116, 20), '−': (116, 30)}


def portapilas(fig, n=4, texto='6 V'):
    w = n * 26 + 16
    fig.rect(0, 0, w, 54, fill='#161616', stroke=C['edge'], rx=4)
    for i in range(n):
        x = 8 + i * 26
        fig.rect(x, 8, 22, 38, fill='#2a2a2a', stroke='#555', rx=6)
        fig.rect(x + 7, 4, 8, 4, fill='#777', stroke='none', sw=0, rx=1)
    fig.text(w / 2, 72, f'{n} × AA · {texto}', size=10, fill=C['muted'], anchor='middle')
    return {'+': (w, 16), '−': (w, 38)}


def fuente(fig, texto='12 V'):
    fig.rect(0, 0, 110, 56, fill='#1f1f1f', stroke=C['edge'], rx=4)
    fig.text(55, 26, 'Fuente', size=11, fill=C['muted'], anchor='middle')
    fig.text(55, 44, texto, size=14, weight=600, anchor='middle')
    return {'+': (110, 18), '−': (110, 38)}


def ordenador(fig):
    fig.rect(10, 0, 140, 90, fill='#141414', stroke=C['edge'], rx=5)
    fig.rect(18, 8, 124, 74, fill='#0d0d0d', stroke='#2e2e2e', rx=2)
    # nube de puntos en pantalla
    import random
    rnd = random.Random(3)
    for i in range(60):
        a = i / 60 * 2 * math.pi
        r = 26 + 6 * math.sin(3 * a) + rnd.uniform(-1.5, 1.5)
        fig.circle(80 + r * math.cos(a), 45 + r * 0.9 * math.sin(a), 1.1, fill=C['accent'], stroke='none', sw=0)
    fig.circle(80, 45, 2.5, fill='#d9665b', stroke='none', sw=0)
    fig.path('M 0 98 L 160 98 L 150 90 L 10 90 Z', fill='#1c1c1c', stroke=C['edge'], sw=1.5)
    return {'usb': (0, 94)}


def adaptador_usb(fig):
    fig.rect(0, 0, 60, 34, fill='#14202b', stroke='#3e5466', rx=3)
    fig.rect(60, 9, 14, 16, fill='#9a9a9a', stroke='#666', rx=1)
    fig.rect(10, 10, 14, 14, fill='#101010', stroke='#555', rx=1)
    return {'in': (0, 17), 'usb': (74, 17)}


BANDAS = {
    '10k': ('#7a4a2a', '#111111', '#e07b2a', '#c9a24a'),
    '220': ('#c0392b', '#c0392b', '#7a4a2a', '#c9a24a'),
    '330': ('#e07b2a', '#e07b2a', '#7a4a2a', '#c9a24a'),
    '100': ('#7a4a2a', '#111111', '#7a4a2a', '#c9a24a'),
    '1k': ('#7a4a2a', '#111111', '#c0392b', '#c9a24a'),
}


def resistencia(fig, valor='10k', length=80):
    # resistencia axial horizontal, centrada en x = length/2, y = 0
    fig.line(0, 0, length, 0, stroke=METAL, sw=2)
    bx = length / 2 - 20
    fig.rect(bx, -8, 40, 16, fill='#d9c49a', stroke='#a8946a', sw=1, rx=7)
    for i, col in enumerate(BANDAS[valor]):
        x = bx + 8 + i * 7 + (5 if i == 3 else 0)
        fig.rect(x, -8, 3.5, 16, fill=col, stroke='none', sw=0, rx=0)
    return {'1': (0, 0), '2': (length, 0)}


def condensador(fig, texto='1000 µF'):
    # electrolítico visto de lado, patas abajo (− a la derecha)
    _legs(fig, (10, 26), 44, 62)
    fig.rect(0, 0, 36, 46, fill='#1f3550', stroke='#4a6d9a', rx=5)
    fig.rect(26, 0, 10, 46, fill='#c9d4e3', stroke='none', sw=0, rx=2, opacity=0.6)
    fig.text(30, 26, '−', size=10, fill='#1f3550', anchor='middle', weight=600)
    fig.text(48, 26, texto, size=9.5, fill=C['muted'])
    return {'+': (10, 62), '−': (26, 62)}


def ventilador(fig):
    # ventilador de 12 V visto de frente (100x100), terminales a la izquierda
    fig.rect(0, 0, 100, 100, fill='#161616', stroke=C['edge'], rx=8)
    for cx, cy in ((10, 10), (90, 10), (10, 90), (90, 90)):
        fig.circle(cx, cy, 3, fill=C['dark'], stroke=C['edge'], sw=1)
    fig.circle(50, 50, 40, fill='#0e0e0e', stroke='#2a2a2a', sw=1)
    for i in range(5):
        a = i * 72
        fig.add(f'<path d="M 50 50 Q 70 32 82 50 Q 66 54 50 50 Z" fill="#2c2c2c" stroke="#444" stroke-width="1" transform="rotate({a} 50 50)"/>')
    fig.circle(50, 50, 12, fill='#222', stroke='#555', sw=1)
    return {'+': (0, 28), '−': (0, 80)}


def fuente_top(fig, texto='12 V'):
    # fuente con bornas arriba (+ a la izquierda)
    fig.rect(0, 0, 120, 56, fill='#1f1f1f', stroke=C['edge'], rx=4)
    fig.text(60, 30, 'Fuente', size=11, fill=C['muted'], anchor='middle')
    fig.text(60, 47, texto, size=14, weight=600, anchor='middle')
    fig.text(40, 14, '+', size=11, fill=C['muted'], anchor='middle')
    fig.text(80, 14, '−', size=11, fill=C['muted'], anchor='middle')
    return {'+': (40, 0), '−': (80, 0)}
