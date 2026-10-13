from lib import *
from parts import place, l298n, motor_dc, bateria, servo
from placas import CabeceraRPi, mpu6050_girado, camara_rpi, raspberry
D = 'raspberry/'

# --- motor DC con L298N -------------------------------------------------------
f = Fig(640, 440)
h = CabeceraRPi(f, 60, 270, used={30, 32, 36, 38}, ancho=520)
q = place(f, l298n, 330, 20, s=1.0)
m = place(f, motor_dc, 210, 52, s=1.0)
b = place(f, bateria, 100, 180, s=1.0, texto='7,4 V', sub='batería motores')
f.wire([m['+'], (322 + 8, m['+'][1]), (330, q['OUT1'][1]), q['OUT1']], 'e')
f.wire([m['−'], (318, m['−'][1]), (318, q['OUT2'][1]), q['OUT2']], '#8a8a8a')
f.wire([b['+'], (300, b['+'][1]), (300, q['12V'][1]), q['12V']], 'vcc')
gx = h.pin(30)[0]
f.wire([b['−'], (q['GND'][0], b['−'][1]), q['GND']], 'gnd')
f.wire([(gx, b['−'][1]), h.pin(30)], 'gnd')
f.node(gx, b['−'][1], 'gnd')
for k, n, y, col in (('ENA', 32, 228, 'a'), ('IN1', 36, 240, 'b'), ('IN2', 38, 252, 'c')):
    p = q[k]; d = h.pin(n)
    f.wire([p, (p[0], y), (d[0], y), d], col)
f.text(266, 44, 'Motor', size=12, weight=600, anchor='middle')
f.text(430, 14, 'L298N', size=12, weight=600, anchor='middle')
legend(f, 60, 436, [('a', 'ENA → GPIO12'), ('b', 'IN1 → GPIO16'), ('c', 'IN2 → GPIO20'), ('gnd', 'GND común')], gap=130)
f.save(D + 'motor.svg')

# --- servo ---------------------------------------------------------------------
f = Fig(640, 400)
h = CabeceraRPi(f, 60, 220, used={4, 6, 12}, ancho=520)
s_ = place(f, servo, 120, 30, s=1.0)
p4, p6, p12 = h.pin(4), h.pin(6), h.pin(12)
f.wire([s_['SIG'], (s_['SIG'][0], 180), (p12[0], 180), p12], 'a')
f.wire([s_['GND'], (s_['GND'][0], 196), (p6[0], 196), p6], 'gnd')
f.wire([s_['5V'], (s_['5V'][0], 188), (p4[0], 188), p4], 'vcc', halo=True)
f.text(250, 70, 'Servo SG90', size=12, weight=600)
legend(f, 60, 396, [('a', 'señal → GPIO18 (pin 12)'), ('vcc', '5 V (pin 4)'), ('gnd', 'GND (pin 6)')], gap=180)
f.save(D + 'servo.svg')

# --- IMU por I2C ------------------------------------------------------------------
f = Fig(640, 400)
h = CabeceraRPi(f, 60, 20, used={3, 5, 9, 17}, ancho=520, etiquetas=False)
mp = place(f, mpu6050_girado, 52, 280, s=1.0)
dest = {'SDA': 3, 'SCL': 5, 'GND': 9, 'VCC': 17}
cols = {'SDA': 'b', 'SCL': 'd', 'GND': 'gnd', 'VCC': '#e39a3b'}
alturas = {'SDA': 196, 'SCL': 208, 'GND': 220, 'VCC': 232}
for k in ('SDA', 'SCL', 'GND', 'VCC'):
    p = mp[k]; d = h.pin(dest[k])
    f.wire([p, (p[0], alturas[k]), (d[0], alturas[k]), d], cols[k])
f.text(180, 316, 'MPU6050 (GY-521)', size=12, weight=600)
f.text(180, 334, 'girado para que los cables lleguen rectos', size=10.5, fill=C['muted'])
legend(f, 60, 392, [('#e39a3b', 'VCC → 3,3 V (pin 17)'), ('gnd', 'GND (pin 9)'), ('b', 'SDA (pin 3)'), ('d', 'SCL (pin 5)')], gap=140)
f.save(D + 'imu.svg')

# --- cámara ------------------------------------------------------------------------
f = Fig(740, 300)
pi = place(f, raspberry, 240, 30, s=1.0)
cam = place(f, camara_rpi, 60, 60, s=1.6)
# cable plano hasta el conector CAM/DISP de la derecha (x = 240 + 196..222, y = 30 + 196)
f.path('M 108 150 L 108 270 L 449 270 L 449 248', stroke='#d8d8d8', sw=10, join='miter')
f.path('M 108 150 L 108 270 L 449 270 L 449 248', stroke='#c9a24a', sw=1, join='miter', dash='2 6')
callout(f, 108, 92, 30, 40, 'Camera Module 3', sub=None)
callout(f, 449, 240, 610, 200, 'Conector CAM/DISP', sub='hay dos: vale cualquiera')
f.text(270, 290, 'cable plano: los contactos dorados, hacia el lado indicado en el conector', size=10.5, fill=C['dim'], anchor='middle')
f.save(D + 'camara.svg')
