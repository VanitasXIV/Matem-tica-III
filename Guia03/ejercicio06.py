import numpy as np

print("6. ¿La siguiente matriz es linealmente dependiente? ¿Por qué sí o por qué no?")

A = np.array([
    [2,1],
    [6,3]
])

detA = np.linalg.det(A)

print(detA)

print(f"La determinante de A es {detA}. Por lo tanto es linealmente dependiente")
