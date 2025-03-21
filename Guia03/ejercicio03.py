#3. Cuál es el determinante de la transformación
# si *î* = [1, 0] y *j* = [2, 2]

import numpy as np

A = np.array([
    [1,2],
    [2,2]
])

print(np.linalg.det(A))