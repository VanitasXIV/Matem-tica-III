from sympy import *

x = symbols('x')
f = (3*x**2) +1
plot(f)

dx_f = diff(f)
print(dx_f)
plot(dx_f)