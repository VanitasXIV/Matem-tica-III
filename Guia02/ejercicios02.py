import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

# a) f(x) = (2x+1)^3
f = (2 * x + 1) ** 3
f_prime = sp.diff(f, x)

# b) g(x) = (x^3 - 3x^2 + 1)^(-3)
g = (x**3 - 3 * x**2 + 1) ** -3
g_prime = sp.diff(g, x)

# c) h(x) = (x - 1/x^2)^5
h = (x - 1 / x**2) ** 5
h_prime = sp.diff(h, x)

# d) j(x) = ln(x^2)
j = sp.ln(x**2)
j_prime = sp.diff(j, x)

# e) k(x) = e^(sqrt(x))
k = sp.exp(sp.sqrt(x))
k_prime = sp.diff(k, x)

# f) z(x) = sqrt(ln(sin(x)))
z = sp.sqrt(sp.ln(sp.sin(x)))
z_prime = sp.diff(z, x)

# Mostrar los resultados
print("a) f'(x) =", sp.simplify(f_prime))
print("b) g'(x) =", sp.simplify(g_prime))
print("c) h'(x) =", sp.simplify(h_prime))
print("d) j'(x) =", sp.simplify(j_prime))
print("e) k'(x) =", sp.simplify(k_prime))
print("f) z'(x) =", sp.simplify(z_prime))