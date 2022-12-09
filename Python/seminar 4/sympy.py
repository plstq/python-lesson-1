import sympy

x = sympy.Symbol('x')
b = 4*x**3 + 0*x**2 + x + 10
c = 8*x**9 + 3*x**2 + 9
print(sympy.simplify(c + b))