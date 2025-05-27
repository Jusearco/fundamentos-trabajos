import numpy as np
import matplotlib.pyplot as plt

def proyeccion_vector(v, u):
    return np.dot(v, u) * u

def generar_unitario_random():
    vec = np.random.rand(2)
    return vec / np.linalg.norm(vec)

vectores = [(3, 4), (1, 2)]
for v in vectores:
    v = np.array(v)
    u1 = generar_unitario_random()
    u2 = generar_unitario_random()
    p1 = proyeccion_vector(v, u1)
    p2 = proyeccion_vector(v, u2)
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector original')
    plt.quiver(0, 0, p1[0], p1[1], angles='xy', scale_units='xy', scale=1, color='b', label='Proyección u1')
    plt.quiver(0, 0, p2[0], p2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Proyección u2')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.legend()
    plt.show()
