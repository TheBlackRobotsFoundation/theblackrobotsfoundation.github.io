from lib import *
from parts import *
D = 'sensores/temperatura/'

f = Fig(640, 310)
p = place(f, dht22, 110, 30, s=2.0)
callout(f, 200, 80, 330, 60, 'Rejilla', sub='deja pasar el aire hasta el sensor')
callout(f, 140, 210, 330, 160, 'Placa del módulo', sub='incluye la resistencia pull-up')
callout(f, 180, 270, 330, 250, '3 pines', sub='alimentación, datos y GND')
f.save(D + 'anatomia.svg')

# trama de 40 bits
f = Fig(640, 230)
f.text(20, 34, 'Cada lectura: 40 bits por un solo cable', size=14, weight=600)
segs = [(16, 'Humedad', '16 bits', 'b'), (16, 'Temperatura', '16 bits', 'a'), (8, 'Control', '8 bits', 'gnd')]
x = 20
W = 600
for n, lab, sub, k in segs:
    w = W * n / 40
    f.rect(x + 2, 60, w - 4, 46, fill=C['body2'], stroke=WIRE[k], sw=2, rx=3)
    f.text(x + w / 2, 88, lab, size=13, weight=600, anchor='middle', fill=WIRE[k])
    f.text(x + w / 2, 128, sub, size=11, fill=C['muted'], anchor='middle')
    x += w
f.text(20, 170, 'Ejemplo:', size=11, fill=C['muted'])
f.text(90, 170, '652  →  65,2 %', size=12, mono=True, fill=WIRE['b'])
f.text(260, 170, '231  →  23,1 °C', size=12, mono=True, fill=WIRE['a'])
f.text(450, 170, 'suma de comprobación', size=11, fill=C['muted'])
f.text(20, 206, 'La librería se encarga de pedir los datos, recibirlos y comprobar que llegan bien.', size=11, fill=C['dim'])
f.save(D + 'trama.svg')

f = Fig(640, 510)
u = Uno(f, 150, 240, used={'5V', 'GND1', 'D2'})
p = place(f, dht22, 360, 30, s=0.9)
g, d2, v5 = u.pin('GND1'), u.pin('D2'), u.pin('5V')
f.wire([p['−'], (p['−'][0], 172), (560, 172), (560, 476), (g[0], 476), g], 'gnd')
f.wire([p['OUT'], (p['OUT'][0], 190), (d2[0], 190), d2], 'a')
f.wire([p['+'], (p['+'][0], 160), (120, 160), (120, 488), (v5[0], 488), v5], 'vcc')
f.text(340, 70, 'DHT22', size=13, weight=600, anchor='end')
f.text(340, 88, 'módulo de 3 pines', size=10.5, fill=C['muted'], anchor='end')
legend(f, 150, 504, [('vcc', '5 V'), ('a', 'datos → pin 2'), ('gnd', 'GND')], gap=120)
f.save(D + 'conexion.svg')
