# 5. Resolver el siguiente sistema de ecuaciones
# $$ 3x + y + 0z= 54 $$
# $$ 2x + 4y + z = 12 $$
# $$ 3x + y + 8z = 6 $$

#Podemos representar en papel el sistema como matrices
# A representa los factores que multiplican a x, y b los valores
# del segundo miembro

import numpy as np

A = np.array([
    [3,1,0],
    [2,4,1],
    [3,1,8]
    ])

b = np.array(
    [54,
     12,
     6]
)

solution = np.linalg.solve(A,b)
#Genera un arreglo numpy de 0 a 2 donde cada elemento representa
# x,y,z respectivamente.

print("La solución del sistema es:")
print(f"x = {solution[0]}")
print(f"y = {solution[1]}")
print(f"z = {solution[2]}")