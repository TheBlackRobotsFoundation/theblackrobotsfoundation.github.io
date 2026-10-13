from lib import *
D = 'ros2/'


def nodo(f, x, y, t, sub=None, w=150, k=None):
    f.rect(x - w / 2, y - 26, w, 52, fill=C['body'], stroke=WIRE[k] if k else C['edge'], sw=1.5, rx=26)
    f.text(x, y + (0 if sub else 5), t, size=13, weight=600, anchor='middle')
    if sub:
        f.text(x, y + 16, sub, size=10, fill=C['muted'], anchor='middle')


def topic(f, x1, y1, x2, y2, t, k='a', pos=0.5, dy=-8, pts=None):
    pts = pts or [(x1, y1), (x2, y2)]
    f.poly(pts, stroke=WIRE[k], sw=2, arrow='end')
    (ax, ay), (bx, by) = pts[-2], pts[-1]
    if pts is not None and len(pts) > 2:
        (ax, ay), (bx, by) = pts[1], pts[2]
    mx, my = ax + (bx - ax) * pos, ay + (by - ay) * pos
    f.text(mx, my + dy, t, size=11, mono=True, fill=WIRE[k], anchor='middle')


# --- grafo de un robot móvil ------------------------------------------------
f = Fig(680, 336)
nodo(f, 100, 70, 'LiDAR', 'rplidar_node', k='b')
nodo(f, 100, 260, 'Motores', 'driver + encoders', k='c')
nodo(f, 400, 165, 'Navegación', 'Nav2', w=170)
nodo(f, 600, 40, 'Mando', 'teleop', w=120)
f.poly([(175, 70), (300, 70), (330, 140)], stroke=WIRE['b'], sw=2, arrow='end')
f.text(238, 60, '/scan', size=11, mono=True, fill=WIRE['b'], anchor='middle')
f.poly([(175, 245), (300, 245), (330, 190)], stroke=WIRE['c'], sw=2, arrow='end')
f.text(238, 235, '/odom', size=11, mono=True, fill=WIRE['c'], anchor='middle')
f.poly([(470, 190), (520, 280), (176, 280)], stroke=WIRE['a'], sw=2, arrow='end')
f.text(350, 298, '/cmd_vel', size=11, mono=True, fill=WIRE['a'], anchor='middle')
f.path('M 600 66 L 600 280 L 520 280', stroke=WIRE['a'], sw=2, dash='5 5')
f.text(612, 150, '/cmd_vel', size=11, mono=True, fill=WIRE['a'])
f.text(20, 322, 'nodos (óvalos) que se pasan mensajes por topics (flechas)', size=11, fill=C['dim'])
f.save(D + 'grafo-robot.svg')

# --- topic, servicio y acción ---------------------------------------------------
f = Fig(680, 560)
def panel(y, h, tit, sub):
    f.rect(10, y, 660, h, fill='none', stroke=C['frame'], sw=1)
    f.title(28, y + 28, tit, sub)
# topic
panel(10, 180, 'Topic', 'un flujo continuo de mensajes: uno publica, cualquiera escucha')
nodo(f, 130, 120, 'Publicador', 'sensor', w=140)
f.rect(268, 100, 150, 40, fill=C['body2'], stroke=WIRE['a'], sw=1.5, rx=4)
f.text(343, 125, '/distancia', size=12, mono=True, fill=WIRE['a'], anchor='middle')
nodo(f, 560, 90, 'Suscriptor', 'navegación', w=140)
nodo(f, 560, 150, 'Suscriptor', 'registro', w=140)
f.line(200, 120, 264, 120, stroke=WIRE['a'], sw=2, arrow='end')
f.line(420, 114, 488, 94, stroke=WIRE['a'], sw=2, arrow='end')
f.line(420, 126, 488, 146, stroke=WIRE['a'], sw=2, arrow='end')
# servicio
panel(200, 140, 'Servicio', 'una pregunta y una respuesta, cuando se necesita')
nodo(f, 160, 295, 'Cliente', w=140)
nodo(f, 520, 295, 'Servidor', w=140)
f.line(232, 284, 448, 284, stroke=WIRE['b'], sw=2, arrow='end')
f.line(448, 308, 232, 308, stroke=WIRE['c'], sw=2, arrow='end')
f.text(340, 276, 'petición: ¿pausar?', size=11, fill=WIRE['b'], anchor='middle')
f.text(340, 326, 'respuesta: hecho', size=11, fill=WIRE['c'], anchor='middle')
# acción
panel(350, 200, 'Acción', 'una tarea larga, con avisos de progreso y resultado final')
nodo(f, 160, 465, 'Cliente', w=140)
nodo(f, 520, 465, 'Servidor', 'navegar a un punto', w=160)
f.line(232, 438, 438, 438, stroke=WIRE['b'], sw=2, arrow='end')
f.line(438, 465, 232, 465, stroke=WIRE['d'], sw=2, arrow='end', dash='4 4')
f.line(438, 492, 232, 492, stroke=WIRE['c'], sw=2, arrow='end')
f.text(335, 430, 'objetivo: ve a (2, 3)', size=11, fill=WIRE['b'], anchor='middle')
f.text(335, 458, 'progreso: quedan 1,2 m', size=11, fill=WIRE['d'], anchor='middle')
f.text(335, 510, 'resultado: he llegado', size=11, fill=WIRE['c'], anchor='middle')
f.save(D + 'comunicacion.svg')

# --- workspace ---------------------------------------------------------------
f = Fig(640, 340)
filas = [
    (0, 'ros2_ws/', 'tu espacio de trabajo', C['text']),
    (1, 'src/', 'el código: aquí van tus paquetes', WIRE['a']),
    (2, 'mi_robot/', 'un paquete', C['text']),
    (3, 'package.xml', 'nombre, versión y dependencias', C['muted']),
    (3, 'setup.py', 'cómo se instala y qué programas tiene', C['muted']),
    (3, 'mi_robot/', 'los nodos en Python', C['muted']),
    (3, 'launch/', 'los archivos de lanzamiento', C['muted']),
    (1, 'build/', 'lo genera colcon al compilar', C['dim']),
    (1, 'install/', 'lo genera colcon: aquí está el setup.bash', C['dim']),
    (1, 'log/', 'registros de compilación', C['dim']),
]
for i, (lvl, n, sub, col) in enumerate(filas):
    y = 34 + i * 30
    x = 40 + lvl * 28
    if lvl:
        f.path(f'M {x - 16} {y - 18} L {x - 16} {y - 4} L {x - 6} {y - 4}', stroke=C['edge'], sw=1.2)
    f.text(x, y, n, size=13, mono=True, weight=600 if n.endswith('/') else None, fill=col)
    f.text(330, y, sub, size=11, fill=C['muted'])
f.save(D + 'workspace.svg')

# --- grafo de turtlesim --------------------------------------------------------
f = Fig(720, 150)
nodo(f, 90, 75, '/dibujante', w=140, k='a')
nodo(f, 360, 75, '/turtlesim', w=140)
nodo(f, 630, 75, '/vigilante', w=140, k='b')
f.line(162, 75, 286, 75, stroke=WIRE['a'], sw=2, arrow='end')
f.line(432, 75, 556, 75, stroke=WIRE['b'], sw=2, arrow='end')
f.text(224, 62, '/turtle1/cmd_vel', size=10.5, mono=True, fill=WIRE['a'], anchor='middle')
f.text(494, 62, '/turtle1/pose', size=10.5, mono=True, fill=WIRE['b'], anchor='middle')
f.text(360, 138, 'lo mismo que muestra rqt_graph con los tres nodos en marcha', size=10.5, fill=C['dim'], anchor='middle')
f.save(D + 'grafo-turtlesim.svg')

# --- ROS 2 y Arduino -----------------------------------------------------------
f = Fig(680, 220)
f.rect(20, 70, 130, 70, fill=C['body'], stroke=C['edge'], rx=4)
f.text(85, 100, 'Arduino', size=13, weight=600, anchor='middle')
f.text(85, 118, 'HC-SR04', size=10.5, fill=C['muted'], anchor='middle')
f.line(152, 105, 226, 105, stroke='#8a8a8a', sw=4)
f.text(189, 96, 'USB', size=10.5, fill=C['muted'], anchor='middle')
f.text(189, 124, 'D 42.5', size=10.5, mono=True, fill=WIRE['b'], anchor='middle')
f.rect(232, 30, 430, 150, fill='none', stroke=C['frame'], sw=1, rx=6)
f.text(244, 50, 'Raspberry Pi o Jetson · ROS 2', size=11, fill=C['muted'])
nodo(f, 320, 105, 'puente_arduino', w=150, k='b')
nodo(f, 580, 105, 'vigilante', w=130)
f.line(396, 105, 512, 105, stroke=WIRE['b'], sw=2, arrow='end')
f.text(454, 96, '/distancia', size=11, mono=True, fill=WIRE['b'], anchor='middle')
f.text(454, 124, 'sensor_msgs/Range', size=9.5, mono=True, fill=C['dim'], anchor='middle')
f.text(20, 210, 'el puente lee el puerto serie y publica cada medida en ROS 2', size=11, fill=C['dim'])
f.save(D + 'arduino-ros.svg')

# --- TF: sistemas de coordenadas ------------------------------------------------
f = Fig(680, 330)
def ejes(f, x, y, ang=0, l=34, nombre=None, k='e'):
    import math
    a = math.radians(ang)
    f.line(x, y, x + l * math.cos(a), y - l * math.sin(a), stroke='#d9665b', sw=2.2, arrow='end')
    f.line(x, y, x - l * math.sin(a), y - l * math.cos(a), stroke='#6cc08b', sw=2.2, arrow='end')
    f.circle(x, y, 3.5, fill=C['accent'], stroke='none', sw=0)
    if nombre:
        f.text(x + 8, y + 18, nombre, size=11, mono=True, fill=C['accent'])
# robot visto desde arriba, girado 30 grados
f.rect(20, 20, 330, 290, fill='none', stroke=C['frame'], sw=1)
f.text(36, 46, 'map', size=11, mono=True, fill=C['muted'])
ejes(f, 50, 280, 0, l=40)
f.text(60, 300, 'origen del mapa', size=10, fill=C['dim'])
f.add('<g transform="rotate(-30 210 170)">')
f.rect(150, 130, 120, 80, fill=C['body2'], stroke=C['edge'], rx=10)
f.rect(160, 118, 36, 12, fill='#2a2a2a', stroke='none', sw=0, rx=3)
f.rect(160, 210, 36, 12, fill='#2a2a2a', stroke='none', sw=0, rx=3)
f.circle(250, 170, 14, fill='#121212', stroke=C['accent'], sw=1.5)
f.add('</g>')
ejes(f, 210, 170, 30, l=46)
f.text(160, 240, 'base_link', size=11, mono=True, fill=C['accent'])
import math
lx, ly = 210 + 40 * math.cos(math.radians(30)), 170 - 40 * math.sin(math.radians(30))
f.text(lx + 22, ly - 24, 'laser', size=11, mono=True, fill=WIRE['b'])
f.circle(lx, ly, 4, fill=WIRE['b'], stroke='none', sw=0)
f.line(lx + 4, ly - 4, lx + 20, ly - 20, stroke=C['dim'], sw=1)
# árbol
def nodo_tf(x, y, t, k=None):
    w = len(t) * 8 + 26
    f.rect(x - w / 2, y - 15, w, 30, fill=C['body'], stroke=WIRE[k] if k else C['edge'], sw=1.5, rx=15)
    f.text(x, y + 4, t, size=12, mono=True, anchor='middle', fill=WIRE[k] if k else C['text'])
nodo_tf(470, 50, 'map')
nodo_tf(470, 120, 'odom')
nodo_tf(470, 190, 'base_link', 'e')
nodo_tf(390, 270, 'laser', 'b')
nodo_tf(470, 270, 'imu', 'c')
nodo_tf(560, 270, 'camara', 'a')
for (x1, y1, x2, y2) in ((470, 65, 470, 104), (470, 135, 470, 174), (455, 205, 400, 254), (470, 205, 470, 254), (485, 205, 550, 254)):
    f.line(x1, y1, x2, y2, stroke=C['dim'], sw=1.5, arrow='end')
f.text(510, 54, 'el mapa', size=10.5, fill=C['muted'])
f.text(510, 124, 'donde empezó a moverse', size=10.5, fill=C['muted'])
f.text(535, 194, 'el centro del robot', size=10.5, fill=C['muted'])
f.text(470, 316, 'los sensores, fijos al robot', size=10.5, fill=C['muted'], anchor='middle')
f.save(D + 'tf.svg')
