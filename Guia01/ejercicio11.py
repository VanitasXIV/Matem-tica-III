import numpy as np

mat = np.random.random(16).reshape(4,4)
print(mat)

suma = np.sum(mat)
print(suma)

desviado = np.std(mat)
print(desviado)

suma_columnas = np.sum(mat,axis=0)
print(suma_columnas)