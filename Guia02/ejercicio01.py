from sympy import *


#Graficar la función f(x)=3x^2 +1
x = symbols('x')
f = (3*x**2) +1
plot(f)

# y su derivada
dx_f = diff(f)
print(dx_f)
plot(dx_f)

#¿Cuál es la pendiente en x=3?
print(dx_f.subs(x,3))

