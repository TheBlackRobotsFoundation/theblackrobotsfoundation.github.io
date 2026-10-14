"""
Utilidades para dibujar los diagramas SVG de las guías.

Paleta: la misma de la web (fondo negro, grises y blanco). Los cables usan
colores apagados con el código habitual: rojo = alimentación, gris = GND,
y un color por cada señal.
"""

import math
import os

FONT = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

C = {
    'frame': '#242424',
    'body': '#141414',
    'body2': '#1c1c1c',
    'edge': '#4a4a4a',
    'pin': '#8a8a8a',
    'text': '#ffffff',
    'muted': '#909090',
    'accent': '#d0d0d0',
    'dim': '#5a5a5a',
    'dark': '#0a0a0a',
}

WIRE = {
    'vcc': '#d9665b',   # alimentación (5 V, 12 V, batería)
    'gnd': '#7a7a7a',   # masa
    'a': '#e3b341',     # señal 1 (ámbar)
    'b': '#5fa8d3',     # señal 2 (azul)
    'c': '#6cc08b',     # señal 3 (verde)
    'd': '#c792ea',     # señal 4 (violeta)
    'e': '#e0e0e0',     # señal 5 (blanco)
}

ROOT = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'img', 'guias')


def esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


class Fig:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.els = []
        self.defs = []
        self._markers = set()

    # --- primitivas -----------------------------------------------------
    def add(self, s):
        self.els.append(s)

    def rect(self, x, y, w, h, fill=None, stroke=None, sw=1.5, rx=2, dash=None, opacity=None):
        fill = C['body'] if fill is None else fill
        stroke = C['edge'] if stroke is None else stroke
        d = f' stroke-dasharray="{dash}"' if dash else ''
        o = f' opacity="{opacity}"' if opacity is not None else ''
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}{o}/>')

    def circle(self, cx, cy, r, fill=None, stroke=None, sw=1.5, dash=None):
        fill = C['body'] if fill is None else fill
        stroke = C['edge'] if stroke is None else stroke
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def line(self, x1, y1, x2, y2, stroke=None, sw=1.5, dash=None, arrow=None, cap='round'):
        stroke = C['accent'] if stroke is None else stroke
        d = f' stroke-dasharray="{dash}"' if dash else ''
        m = ''
        if arrow:
            mid = self.marker(stroke)
            if arrow in ('end', 'both'):
                m += f' marker-end="url(#{mid})"'
            if arrow in ('start', 'both'):
                m += f' marker-start="url(#{mid})"'
        self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}{m}/>')

    def path(self, d, stroke=None, sw=1.5, fill='none', dash=None, arrow=None, join='round'):
        stroke = C['accent'] if stroke is None else stroke
        ds = f' stroke-dasharray="{dash}"' if dash else ''
        m = ''
        if arrow:
            mid = self.marker(stroke)
            if arrow in ('end', 'both'):
                m += f' marker-end="url(#{mid})"'
            if arrow in ('start', 'both'):
                m += f' marker-start="url(#{mid})"'
        self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="{join}" stroke-linecap="round"{ds}{m}/>')

    def poly(self, pts, stroke=None, sw=1.5, fill='none', dash=None, arrow=None, close=False):
        d = 'M ' + ' L '.join(f'{x} {y}' for x, y in pts) + (' Z' if close else '')
        self.path(d, stroke=stroke, sw=sw, fill=fill, dash=dash, arrow=arrow)

    def text(self, x, y, s, size=12, fill=None, weight=None, anchor='start', rotate=None, mono=False, italic=False):
        fill = C['text'] if fill is None else fill
        w = f' font-weight="{weight}"' if weight else ''
        r = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ''
        f = f' font-family="{MONO}"' if mono else ''
        it = ' font-style="italic"' if italic else ''
        self.add(f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" text-anchor="{anchor}"{w}{r}{f}{it}>{esc(s)}</text>')

    def title(self, x, y, s, sub=None):
        self.text(x, y, s, size=15, weight=600)
        if sub:
            self.text(x, y + 18, sub, size=12, fill=C['muted'])

    def marker(self, color):
        mid = 'm' + color.replace('#', '')
        if mid not in self._markers:
            self._markers.add(mid)
            self.defs.append(
                f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                f'<path d="M0 0 L10 5 L0 10 z" fill="{color}"/></marker>')
        return mid

    # --- cables ---------------------------------------------------------
    def wire(self, pts, kind='a', sw=3, r=8, halo=False):
        """Cable con esquinas redondeadas entre una lista de puntos.

        halo=True dibuja un borde del color del fondo para que el cable
        pase limpiamente por encima de otro cuando se cruzan.
        """
        color = WIRE.get(kind, kind)
        d = f'M {pts[0][0]} {pts[0][1]}'
        for i in range(1, len(pts) - 1):
            (x0, y0), (x1, y1), (x2, y2) = pts[i - 1], pts[i], pts[i + 1]
            l1 = math.hypot(x1 - x0, y1 - y0)
            l2 = math.hypot(x2 - x1, y2 - y1)
            rr = min(r, l1 / 2, l2 / 2)
            if rr <= 0:
                d += f' L {x1} {y1}'
                continue
            ax = x1 - (x1 - x0) / l1 * rr
            ay = y1 - (y1 - y0) / l1 * rr
            bx = x1 + (x2 - x1) / l2 * rr
            by = y1 + (y2 - y1) / l2 * rr
            d += f' L {ax:.1f} {ay:.1f} Q {x1} {y1} {bx:.1f} {by:.1f}'
        d += f' L {pts[-1][0]} {pts[-1][1]}'
        if halo:
            dark = C['dark']
            self.add(f'<path d="{d}" fill="none" stroke="{dark}" stroke-width="{sw + 6}" stroke-linejoin="round" stroke-linecap="butt"/>')
        self.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>')
        for (x, y) in (pts[0], pts[-1]):
            self.add(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{color}"/>')

    def node(self, x, y, kind='a'):
        self.add(f'<circle cx="{x}" cy="{y}" r="4.5" fill="{WIRE.get(kind, kind)}"/>')

    # --- componentes en línea (símbolos IEC) ---------------------------
    def resistor(self, x, y, vertical=False, label=None, length=44, label_side=1):
        """Resistencia centrada en (x, y). Devuelve sus dos extremos."""
        if vertical:
            self.rect(x - 7, y - length / 2 + 8, 14, length - 16, fill=C['body2'], stroke=C['accent'], sw=1.5, rx=1)
            if label:
                self.text(x + 14 * label_side, y + 4, label, size=11, fill=C['accent'], anchor='start' if label_side > 0 else 'end')
            return (x, y - length / 2 + 8), (x, y + length / 2 - 8)
        self.rect(x - length / 2 + 8, y - 7, length - 16, 14, fill=C['body2'], stroke=C['accent'], sw=1.5, rx=1)
        if label:
            self.text(x, y - 13 if label_side > 0 else y + 24, label, size=11, fill=C['accent'], anchor='middle')
        return (x - length / 2 + 8, y), (x + length / 2 - 8, y)

    def save(self, rel):
        path = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        defs = f'<defs>{"".join(self.defs)}</defs>' if self.defs else ''
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
               f'font-family="{FONT}">\n{defs}\n' + '\n'.join(self.els) + '\n</svg>\n')
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(svg)
        return path


# ---------------------------------------------------------------------------
# Arduino UNO
# ---------------------------------------------------------------------------

UNO_W, UNO_H = 360, 220
_TOP = ['SCL', 'SDA', 'AREF', 'GND', '13', '12', '~11', '~10', '~9', '8', None,
        '7', '~6', '~5', '4', '~3', '2', 'TX 1', 'RX 0']
_BOT = ['IOREF', 'RESET', '3.3V', '5V', 'GND', 'GND', 'VIN', None,
        'A0', 'A1', 'A2', 'A3', 'A4', 'A5']
_P = 14


def _key(label, side, idx):
    if label is None:
        return None
    if label == 'GND':
        return 'GND' if side == 'top' else ('GND1' if idx == 4 else 'GND2')
    num = label.replace('~', '').replace('TX ', '').replace('RX ', '')
    if num.isdigit():
        return 'D' + num
    return label


class Uno:
    """Arduino UNO visto desde arriba, con el USB a la izquierda.

    pin(key) devuelve el centro del pin. Claves: D0..D13, A0..A5, 5V, 3.3V,
    VIN, GND (fila de arriba), GND1/GND2 (fila de abajo), SDA, SCL.
    """

    def __init__(self, fig, x, y, used=()):
        self.f, self.x, self.y = fig, x, y
        self.pins = {}
        self.used = set(used)
        self._draw()

    def pin(self, k):
        return self.pins[k]

    def _draw(self):
        f, x, y = self.f, self.x, self.y
        # conectores USB y jack
        f.rect(x - 16, y + 36, 46, 40, fill=C['body2'], stroke=C['edge'])
        f.rect(x - 10, y + 150, 40, 34, fill=C['body2'], stroke=C['edge'])
        # placa
        f.rect(x, y, UNO_W, UNO_H, fill=C['body'], stroke=C['edge'], sw=1.5, rx=6)
        for hx, hy in ((x + 14, y + 14), (x + UNO_W - 14, y + 70), (x + UNO_W - 14, y + UNO_H - 14), (x + 60, y + UNO_H - 14)):
            f.circle(hx, hy, 4, fill=C['dark'], stroke=C['edge'], sw=1)
        f.text(x + UNO_W / 2 + 20, y + UNO_H / 2 + 6, 'Arduino UNO', size=16, weight=600, anchor='middle', fill=C['accent'])
        f.text(x + 18, y + 62, 'USB', size=9, fill=C['muted'])
        # cabeceras
        x0 = x + UNO_W - 18 - (len(_TOP) - 1) * _P
        f.rect(x0 - 8, y + 6, (len(_TOP) - 1) * _P + 16, 16, fill=C['dark'], stroke=C['edge'], sw=1, rx=1)
        for i, lab in enumerate(_TOP):
            if lab is None:
                continue
            px, py = x0 + i * _P, y + 14
            k = _key(lab, 'top', i)
            self.pins[k] = (px, py)
            hot = k in self.used
            f.rect(px - 3.5, py - 3.5, 7, 7, fill=C['accent'] if hot else '#2e2e2e', stroke='none', sw=0, rx=1)
            f.text(px + 3.5, py + 14, lab, size=8.5, fill=C['text'] if hot else C['dim'],
                   weight=600 if hot else None, anchor='end', rotate=-90)
        f.text(x0 + 11 * _P, y + 62, 'DIGITAL (PWM ~)', size=8, fill=C['dim'])
        xb = x + UNO_W - 18 - (len(_BOT) - 1) * _P
        f.rect(xb - 8, y + UNO_H - 22, (len(_BOT) - 1) * _P + 16, 16, fill=C['dark'], stroke=C['edge'], sw=1, rx=1)
        for i, lab in enumerate(_BOT):
            if lab is None:
                continue
            px, py = xb + i * _P, y + UNO_H - 14
            k = _key(lab, 'bot', i)
            self.pins[k] = (px, py)
            hot = k in self.used
            f.rect(px - 3.5, py - 3.5, 7, 7, fill=C['accent'] if hot else '#2e2e2e', stroke='none', sw=0, rx=1)
            f.text(px + 3.5, py - 12, lab, size=8.5, fill=C['text'] if hot else C['dim'],
                   weight=600 if hot else None, anchor='start', rotate=-90)
        f.text(xb, y + UNO_H - 58, 'POWER', size=8, fill=C['dim'])
        f.text(xb + 8 * _P, y + UNO_H - 58, 'ANALOG IN', size=8, fill=C['dim'])
        # pines SDA/SCL también en A4/A5
        self.pins.setdefault('A4/SDA', self.pins['A4'])
        self.pins.setdefault('A5/SCL', self.pins['A5'])


# ---------------------------------------------------------------------------
# Módulos genéricos
# ---------------------------------------------------------------------------

def module(fig, x, y, w, h, name, pins, side='bottom', sub=None, pin_gap=None, name_y=None):
    """Placa de un módulo con una fila de pines. Devuelve {nombre: (x, y)}.

    side: lado donde están los pines ('bottom', 'top', 'left', 'right').
    """
    fig.rect(x, y, w, h, fill=C['body'], stroke=C['edge'], rx=4)
    ny = name_y if name_y is not None else (y + h / 2 + (0 if sub else 5))
    fig.text(x + w / 2, ny, name, size=13, weight=600, anchor='middle')
    if sub:
        fig.text(x + w / 2, ny + 16, sub, size=10.5, fill=C['muted'], anchor='middle')
    out = {}
    n = len(pins)
    if side in ('bottom', 'top'):
        gap = pin_gap or min(28, (w - 20) / max(n - 1, 1))
        x0 = x + w / 2 - gap * (n - 1) / 2
        py = y + h if side == 'bottom' else y
        for i, p in enumerate(pins):
            px = x0 + i * gap
            fig.rect(px - 4, py - 4, 8, 8, fill=C['accent'], stroke='none', sw=0, rx=1)
            ty = py - 12 if side == 'bottom' else py + 20
            fig.text(px, ty, p, size=9.5, fill=C['muted'], anchor='middle')
            out[p] = (px, py)
    else:
        gap = pin_gap or min(24, (h - 20) / max(n - 1, 1))
        y0 = y + h / 2 - gap * (n - 1) / 2
        px = x + w if side == 'right' else x
        for i, p in enumerate(pins):
            py = y0 + i * gap
            fig.rect(px - 4, py - 4, 8, 8, fill=C['accent'], stroke='none', sw=0, rx=1)
            tx = px - 10 if side == 'right' else px + 10
            fig.text(tx, py + 3.5, p, size=9.5, fill=C['muted'], anchor='end' if side == 'right' else 'start')
            out[p] = (px, py)
    return out


def label(fig, x, y, s, anchor='start', size=11, fill=None):
    fig.text(x, y, s, size=size, fill=fill or C['muted'], anchor=anchor)


def legend(fig, x, y, items, gap=96):
    """Leyenda de colores de cable: [(kind, texto), ...]."""
    for i, (k, t) in enumerate(items):
        xx = x + i * gap
        fig.line(xx, y, xx + 18, y, stroke=WIRE.get(k, k), sw=3)
        fig.text(xx + 24, y + 4, t, size=10.5, fill=C['muted'])


# ---------------------------------------------------------------------------
# Gráficas de señales
# ---------------------------------------------------------------------------

def axes(fig, x, y, w, h, top='5 V', bottom='0 V', xlabel=None):
    """Marco de una gráfica de señal: línea base, nivel alto y etiquetas."""
    fig.line(x, y + h, x + w, y + h, stroke=C['edge'], sw=1)
    fig.line(x, y, x + w, y, stroke=C['frame'], sw=1, dash='3 4')
    if top:
        fig.text(x - 8, y + 4, top, size=10, fill=C['muted'], anchor='end')
    if bottom:
        fig.text(x - 8, y + h + 4, bottom, size=10, fill=C['muted'], anchor='end')
    if xlabel:
        fig.text(x + w, y + h + 18, xlabel, size=10, fill=C['dim'], anchor='end')


def wave(fig, x, y, w, h, pts, stroke=None, sw=2):
    """Dibuja una señal a partir de puntos normalizados (0..1, 0..1; 1 = alto)."""
    fig.poly([(round(x + px * w, 1), round(y + h - py * h, 1)) for px, py in pts], stroke=stroke or C['accent'], sw=sw)


def square(duty, periods, t0=0.0):
    """Puntos normalizados de una onda cuadrada."""
    pts = [(0, 0)]
    T = 1 / periods
    for i in range(periods):
        a = i * T
        b = a + duty * T
        pts += [(a, 0), (a, 1), (b, 1), (b, 0)]
    pts.append((1, 0))
    return pts


def callout(fig, x1, y1, x2, y2, s, anchor='start', sub=None):
    """Línea fina desde un punto del componente hasta su etiqueta."""
    fig.line(x1, y1, x2, y2, stroke=C['dim'], sw=1)
    fig.circle(x1, y1, 2.5, fill=C['accent'], stroke='none', sw=0)
    dx = 6 if anchor == 'start' else -6
    fig.text(x2 + dx, y2 + 4, s, size=12, fill=C['text'], anchor=anchor, weight=600)
    if sub:
        fig.text(x2 + dx, y2 + 20, sub, size=10.5, fill=C['muted'], anchor=anchor)


def bottom_to_right(u, key, x_side, y_target, x_end, drop=16):
    """Ruta desde un pin de la fila inferior del UNO, rodeando la placa por la derecha."""
    px, py = u.pin(key)
    yb = u.y + UNO_H + drop
    return [(px, py), (px, yb), (x_side, yb), (x_side, y_target), (x_end, y_target)]


def bottom_to_left(u, key, x_side, y_target, x_end, drop=16):
    px, py = u.pin(key)
    yb = u.y + UNO_H + drop
    return [(px, py), (px, yb), (x_side, yb), (x_side, y_target), (x_end, y_target)]
