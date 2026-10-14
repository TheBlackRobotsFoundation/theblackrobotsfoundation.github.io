"""Placas de ordenador: Raspberry Pi 5, su cabecera GPIO y Jetson Orin Nano."""

import math
from lib import C, WIRE

PCB_VERDE = '#14301f'
PCB_VERDE_BORDE = '#3f6b4f'
METAL = '#bdbdbd'

# Cabecera de 40 pines (numeración física -> función)
GPIO40 = {
    1: '3V3', 2: '5V', 3: 'GPIO2', 4: '5V', 5: 'GPIO3', 6: 'GND', 7: 'GPIO4', 8: 'GPIO14',
    9: 'GND', 10: 'GPIO15', 11: 'GPIO17', 12: 'GPIO18', 13: 'GPIO27', 14: 'GND', 15: 'GPIO22',
    16: 'GPIO23', 17: '3V3', 18: 'GPIO24', 19: 'GPIO10', 20: 'GND', 21: 'GPIO9', 22: 'GPIO25',
    23: 'GPIO11', 24: 'GPIO8', 25: 'GND', 26: 'GPIO7', 27: 'GPIO0', 28: 'GPIO1', 29: 'GPIO5',
    30: 'GND', 31: 'GPIO6', 32: 'GPIO12', 33: 'GPIO13', 34: 'GND', 35: 'GPIO19', 36: 'GPIO16',
    37: 'GPIO26', 38: 'GPIO20', 39: 'GND', 40: 'GPIO21',
}
EXTRA = {3: 'SDA', 5: 'SCL', 8: 'TX', 10: 'RX', 12: 'PWM0', 19: 'MOSI', 21: 'MISO', 23: 'SCLK',
         24: 'CE0', 26: 'CE1', 27: 'ID_SD', 28: 'ID_SC', 32: 'PWM0', 33: 'PWM1', 35: 'PWM1'}
TIPO_COLOR = {'5V': '#d9665b', '3V3': '#e39a3b', 'GND': '#7a7a7a', 'GPIO': '#d0d0d0',
              'I2C': '#5fa8d3', 'SPI': '#c792ea', 'UART': '#6cc08b', 'ID': '#4a4a4a'}


def tipo_pin(n):
    f = GPIO40[n]
    if f in ('5V', '3V3', 'GND'):
        return f
    if n in (3, 5):
        return 'I2C'
    if n in (19, 21, 23, 24, 26):
        return 'SPI'
    if n in (8, 10):
        return 'UART'
    if n in (27, 28):
        return 'ID'
    return 'GPIO'


def raspberry(fig, cabecera=True):
    """Raspberry Pi 5 vista desde arriba (340x224), cabecera arriba y USB a la derecha."""
    fig.rect(0, 0, 340, 224, fill=PCB_VERDE, stroke=PCB_VERDE_BORDE, rx=10)
    for cx, cy in ((14, 14), (14, 210), (240, 14), (240, 210)):
        fig.circle(cx, cy, 6, fill=C['dark'], stroke='#c9a24a', sw=1.5)
    # cabecera GPIO
    if cabecera:
        fig.rect(28, 6, 204, 22, fill='#101010', stroke='#444', sw=1, rx=1)
        for i in range(20):
            for j in range(2):
                fig.rect(33 + i * 10, 9 + j * 10, 5, 5, fill='#c9a24a', stroke='none', sw=0)
    # SoC y RAM
    fig.rect(90, 80, 56, 56, fill='#bdbdbd', stroke='#8a8a8a', rx=3)
    fig.rect(96, 86, 44, 44, fill='#a8a8a8', stroke='none', sw=0, rx=2)
    fig.rect(160, 84, 34, 48, fill='#151515', stroke='#444', rx=2)
    fig.rect(40, 96, 30, 26, fill='#151515', stroke='#444', rx=2)          # RP1
    # USB y Ethernet (derecha)
    for y, w in ((14, 'USB'), (74, 'USB')):
        fig.rect(276, y, 74, 52, fill='#2a2a2a', stroke='#666', rx=3)
        fig.rect(284, y + 8, 60, 14, fill='#1f3d6e', stroke='none', sw=0, rx=1)
        fig.rect(284, y + 30, 60, 14, fill='#1f3d6e', stroke='none', sw=0, rx=1)
    fig.rect(270, 140, 80, 64, fill='#bdbdbd', stroke='#888', rx=3)
    fig.rect(286, 156, 48, 32, fill='#2a2a2a', stroke='none', sw=0, rx=2)
    # abajo: USB-C, 2 micro HDMI, conectores CSI/DSI
    fig.rect(26, 212, 26, 18, fill='#bdbdbd', stroke='#888', rx=6)
    for x in (76, 116):
        fig.rect(x, 212, 26, 16, fill='#bdbdbd', stroke='#888', rx=3)
    for x in (160, 196):
        fig.rect(x, 196, 26, 22, fill='#e8e8e8', stroke='#999', rx=1)
    fig.text(140, 168, 'Raspberry Pi 5', size=11, fill='#cfe3d6', anchor='middle', weight=600)
    return {'usb': (350, 40), 'gpio': (130, 6), 'usbc': (39, 230)}


def jetson(fig):
    """Jetson Orin Nano Developer Kit vista desde arriba (300x240)."""
    fig.rect(0, 0, 300, 240, fill='#141414', stroke='#4a4a4a', rx=8)
    for cx, cy in ((12, 12), (288, 12), (12, 228), (288, 228)):
        fig.circle(cx, cy, 5, fill=C['dark'], stroke='#666', sw=1)
    # cabecera de 40 pines (borde superior izquierdo)
    fig.rect(20, 8, 150, 18, fill='#101010', stroke='#444', sw=1, rx=1)
    for i in range(20):
        for j in range(2):
            fig.rect(24 + i * 7.3, 11 + j * 7, 4, 4, fill='#c9a24a', stroke='none', sw=0)
    # módulo con disipador y ventilador
    fig.rect(40, 44, 170, 150, fill='#1c1c1c', stroke='#5a5a5a', rx=4)
    for i in range(14):
        fig.rect(48 + i * 11.5, 50, 6, 138, fill='#2a2a2a', stroke='none', sw=0, rx=1)
    fig.circle(125, 119, 50, fill='#0f0f0f', stroke='#5a5a5a', sw=1.5)
    for i in range(7):
        a = i * 360 / 7
        fig.add(f'<path d="M 125 119 Q 150 95 168 112 Q 146 124 125 119 Z" fill="#262626" stroke="#3a3a3a" stroke-width="1" transform="rotate({a:.1f} 125 119)"/>')
    fig.circle(125, 119, 14, fill='#76b900', stroke='none', sw=0)
    # puertos (derecha)
    fig.rect(256, 22, 50, 30, fill='#bdbdbd', stroke='#888', rx=3)        # Ethernet
    for y in (62, 104):
        fig.rect(260, y, 46, 34, fill='#2a2a2a', stroke='#666', rx=3)
        fig.rect(266, y + 5, 36, 9, fill='#1f3d6e', stroke='none', sw=0, rx=1)
        fig.rect(266, y + 20, 36, 9, fill='#1f3d6e', stroke='none', sw=0, rx=1)
    fig.rect(262, 148, 42, 18, fill='#bdbdbd', stroke='#888', rx=3)        # DisplayPort
    fig.rect(266, 176, 36, 14, fill='#bdbdbd', stroke='#888', rx=6)        # USB-C
    fig.circle(282, 210, 11, fill='#2a2a2a', stroke='#888', sw=1.5)       # jack
    fig.circle(282, 210, 4, fill='#888', stroke='none', sw=0)
    # cámaras CSI (abajo)
    for x in (60, 120):
        fig.rect(x, 218, 44, 14, fill='#e8e8e8', stroke='#999', rx=1)
    fig.text(150, 212, 'Jetson Orin Nano', size=11, fill='#b6d77a', anchor='middle', weight=600)
    return {'usb': (306, 79)}


class CabeceraRPi:
    """Cabecera de 40 pines de la Raspberry dibujada en grande, en horizontal.

    Fila superior: pines pares (borde de la placa). Fila inferior: impares.
    pin(n) devuelve el centro del pin físico n.
    """

    def __init__(self, fig, x, y, used=(), paso=18, ancho=None, etiquetas=True):
        self.f, self.x, self.y, self.p = fig, x, y, paso
        self.used = set(used)
        self.pins = {}
        w = ancho or 20 * paso + 60
        f = fig
        f.rect(x, y, w, 150, fill=PCB_VERDE, stroke=PCB_VERDE_BORDE, rx=8)
        f.text(x + w - 14, y + 136, 'Raspberry Pi', size=13, weight=600, anchor='end', fill='#cfe3d6')
        hx = x + 30
        f.rect(hx - 6, y + 46, 20 * paso, 2 * paso + 4, fill='#101010', stroke='#444', sw=1, rx=2)
        for i in range(20):
            for j, n in ((0, 2 * i + 2), (1, 2 * i + 1)):
                px = hx + 3 + i * paso
                py = y + 46 + 2 + paso / 2 + j * paso
                hot = n in self.used
                col = TIPO_COLOR[tipo_pin(n)]
                f.rect(px - 5, py - 5, 10, 10, fill=col if hot else '#2e2e2e', stroke=col, sw=1.2, rx=1.5)
                self.pins[n] = (px, py)
                lab = GPIO40[n].replace('GPIO', '')
                if hot and etiquetas:
                    ly = y + 46 + 2 * paso + 14
                    f.text(px + 3.5, ly, f'{n} · {GPIO40[n]}', size=9, weight=600, anchor='end', rotate=-90, fill=C['text'])
        f.text(hx - 12, y + 46 + 2 + paso * 1.5 + 4, '1', size=9, fill=C['muted'], anchor='end')
        f.text(hx - 12, y + 46 + 2 + paso * 0.5 + 4, '2', size=9, fill=C['muted'], anchor='end')

    def pin(self, n):
        return self.pins[n]


def mpu6050_girado(fig):
    """GY-521 girado 180 grados: pines arriba, en orden inverso (INT ... VCC)."""
    PCB, EDGE = '#14202b', '#3e5466'
    fig.rect(0, 0, 112, 84, fill=PCB, stroke=EDGE, rx=4)
    for cx in (10, 102):
        fig.circle(cx, 74, 4, fill=C['dark'], stroke=EDGE, sw=1)
    fig.rect(42, 40, 28, 28, fill='#101010', stroke='#5a5a5a', rx=2)
    fig.circle(65, 63, 1.6, fill='#666', stroke='none', sw=0)
    fig.rect(12, 26, 12, 8, fill='#101010', stroke='#555', sw=1, rx=1)
    fig.text(90, 62, 'MPU6050', size=7, fill='#9fb3c8', anchor='middle')
    names = ['INT', 'AD0', 'XCL', 'XDA', 'SDA', 'SCL', 'GND', 'VCC']
    out = {}
    for i, n in enumerate(names):
        x = 7 + i * 14
        fig.text(x, 18, n, size=5.6, fill='#9fb3c8', anchor='middle')
        fig.line(x, 0, x, -12, stroke=METAL, sw=2.2)
        fig.rect(x - 4, -16, 8, 8, fill=C['accent'], stroke='none', sw=0, rx=1)
        out[n] = (x, -12)
    return out


def camara_rpi(fig):
    """Camera Module 3 (60x56) con su cable plano saliendo por abajo."""
    fig.rect(0, 0, 60, 56, fill='#14301f', stroke='#3f6b4f', rx=3)
    for cx, cy in ((6, 6), (54, 6), (6, 30), (54, 30)):
        fig.circle(cx, cy, 2.4, fill=C['dark'], stroke='#c9a24a', sw=1)
    fig.rect(18, 8, 24, 24, fill='#1a1a1a', stroke='#555', rx=2)
    fig.circle(30, 20, 9, fill='#0d0d0d', stroke='#777', sw=1.5)
    fig.circle(30, 20, 4, fill='#2a3a5a', stroke='none', sw=0)
    fig.rect(14, 46, 32, 10, fill='#e8e8e8', stroke='#999', rx=1)
    return {'cable': (30, 56)}
