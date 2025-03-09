import numpy as np

a = np.array([1,2,3]) #Creamos un array de una dimension ( 1 x 3)
print(type(a), a.shape, a[0], a[1], a[2])
a[0] = 5
print(a)
print(a.shape)

b = np.zeros((2,2)) #Crea un array lleno de ceros
print(b)

c = np.ones((2,2)) #Crea un array lleno de unos
print(c)

d = np.full((2,2), 7) #Crea un array con el mismo numero en todas las posiciones
print(d)

e = np.eye(2) #Crea una matriz identidad
print(e)

f = np.random.random((2,2)) #Crea una matriz con valores
#random en cada posicion
print(f)



