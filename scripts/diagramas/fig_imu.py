import math, random
from lib import *
from parts import *
D = 'sensores/imu/'

f = Fig(640, 300)
p = place(f, mpu6050, 60, 30, s=2.4)
callout(f, 220, 72, 360, 40, 'Chip MPU6050', sub='acelerómetro y giroscopio de 3 ejes')
callout(f, 252, 121, 360, 100, 'Ejes serigrafiados', sub='indican cómo está orientado')
callout(f, 285, 160, 360, 160, 'Regulador', sub='permite alimentarlo a 5 V')
callout(f, 110, 260, 360, 230, 'VCC, GND, SCL y SDA', sub='los cuatro que necesitas (I2C)')
f.save(D + 'anatomia.svg')

# ejes y rotaciones en isométrica
f = Fig(640, 330)
ox, oy = 210, 190
def iso(x, y, z):
    return (ox + (x - y) * 0.87, oy + (x + y) * 0.5 - z)
# placa
pts = [iso(-70, -50, 0), iso(70, -50, 0), iso(70, 50, 0), iso(-70, 50, 0)]
f.poly(pts, stroke='#3e5466', fill='#14202b', close=True, sw=1.5)
f.poly([iso(-12, -12, 2), iso(12, -12, 2), iso(12, 12, 2), iso(-12, 12, 2)], stroke='#5a5a5a', fill='#101010', close=True, sw=1)
for (v, n, k, rot) in (((130, 0, 0), 'X', 'a', 'roll (alabeo)'), ((0, 130, 0), 'Y', 'c', 'pitch (cabeceo)'), ((0, 0, 120), 'Z', 'b', 'yaw (guiñada)')):
    x0, y0 = iso(0, 0, 0)
    x1, y1 = iso(*v)
    f.line(x0, y0, x1, y1, stroke=WIRE[k], sw=2.5, arrow='end')
    f.text(x1 + (10 if n != 'Y' else -14), y1 + (4 if n != 'Z' else -6), n, size=15, weight=600, fill=WIRE[k], anchor='start' if n != 'Y' else 'end')
# arcos de rotación
x1, y1 = iso(95, 0, 0)
f.path(f'M {x1 - 10} {y1 - 22} A 16 26 0 1 1 {x1 + 12} {y1 + 18}', stroke=WIRE['a'], sw=1.5, arrow='end')
x1, y1 = iso(0, 95, 0)
f.path(f'M {x1 + 12} {y1 - 22} A 16 26 0 1 0 {x1 - 12} {y1 + 18}', stroke=WIRE['c'], sw=1.5, arrow='end')
x1, y1 = iso(0, 0, 90)
f.path(f'M {x1 - 30} {y1 + 4} A 30 10 0 1 0 {x1 + 26} {y1 - 4}', stroke=WIRE['b'], sw=1.5, arrow='end')
for i, (n, k, t, sub) in enumerate((('X', 'a', 'Roll (alabeo)', 'giro sobre X: inclinarse a un lado'),
                                    ('Y', 'c', 'Pitch (cabeceo)', 'giro sobre Y: morro arriba o abajo'),
                                    ('Z', 'b', 'Yaw (guiñada)', 'giro sobre Z: girar a izquierda o derecha'))):
    y = 90 + i * 64
    f.text(410, y, t, size=13, weight=600, fill=WIRE[k])
    f.text(410, y + 18, sub, size=11, fill=C['muted'])
f.save(D + 'ejes.svg')

# fusión de sensores
f = Fig(640, 260)
rnd = random.Random(7)
gx, gy, gw, gh = 60, 50, 540, 150
f.line(gx, gy + gh / 2, gx + gw, gy + gh / 2, stroke=C['frame'], sw=1, dash='3 4')
f.text(gx - 8, gy + gh / 2 + 4, 'real', size=10, fill=C['muted'], anchor='end')
N = 120
acc = [(i / N, 0.5 + rnd.uniform(-0.22, 0.22)) for i in range(N + 1)]
gyr = [(i / N, 0.5 + 0.35 * (i / N) ** 1.4) for i in range(N + 1)]
fus = [(i / N, 0.5 + rnd.uniform(-0.025, 0.025)) for i in range(N + 1)]
wave(f, gx, gy, gw, gh, acc, stroke='#6a6a6a', sw=1.2)
wave(f, gx, gy, gw, gh, gyr, stroke=WIRE['b'], sw=2)
wave(f, gx, gy, gw, gh, fus, stroke=WIRE['a'], sw=2.5)
f.text(20, 30, 'Ángulo medido con el sensor quieto', size=13, weight=600)
legend(f, 60, 236, [('#6a6a6a', 'acelerómetro: ruido'), ('b', 'giroscopio: deriva'), ('a', 'fusión: estable')], gap=170)
f.save(D + 'fusion.svg')

# conexión
f = Fig(640, 520)
u = Uno(f, 150, 270, used={'5V', 'GND', 'A4', 'A5'})
p = place(f, mpu6050, 261, 40, s=1.0)
v5, g, a4, a5 = u.pin('5V'), u.pin('GND'), u.pin('A4'), u.pin('A5')
f.wire([p['VCC'], (p['VCC'][0], 170), (120, 170), (120, 504), (v5[0], 504), v5], 'vcc')
f.wire([p['GND'], g], 'gnd')
f.wire([p['SDA'], (p['SDA'][0], 170), (560, 170), (560, 504), (a4[0], 504), a4], 'b')
f.wire([p['SCL'], (p['SCL'][0], 184), (546, 184), (546, 492), (a5[0], 492), a5], 'a')
f.text(241, 80, 'MPU6050', size=13, weight=600, anchor='end')
f.text(241, 98, 'módulo GY-521', size=10.5, fill=C['muted'], anchor='end')
legend(f, 150, 516, [('vcc', '5 V'), ('gnd', 'GND'), ('b', 'SDA → A4'), ('a', 'SCL → A5')], gap=105)
f.save(D + 'conexion.svg')
