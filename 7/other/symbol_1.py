#import sympy
'''
alpha1, r1_x, r1_y = sympy.var("alpha1 r1_x r1_y")
B1 = sympy.exp(-alpha1 * (r1_x**2 + r1_y**2))
print(B1.integrate(r1_x))
#Integral(exp(-alpha1*(r1_x**2 + r1_y**2)), r1_x)
print(B1.expand(alpha1))
#exp(-alpha1*r1_x**2)*exp(-alpha1*r1_y**2)
print(B1.expand(alpha1).integrate(r1_x))
#sqrt(pi)*exp(-alpha1*r1_y**2)*erf(sqrt(alpha1)*r1_x)/(2*sqrt(alpha1))
'''
'''
a=sympy.Symbol('a')
b=sympy.Symbol('b')
c=sympy.Symbol('c')
e=( a*b*b+2*b*a*b )**c
print(e)
#b^(2*c)*a^c*3^c
'''
'''
a=sympy.Symbol('a')
b=sympy.Symbol('b')
e=(a+b)**5
print(e)
#(b+a)^5
print(e.expand())
#10*a^3*b^2+5*b^4*a+a^5+b^5+5*a^4*b+10*a^2*b^3
'''
'''
a=sympy.Symbol('a')
b=sympy.Symbol('b')
e=sympy.log((a+b)**5)
print(e)
#5*log(b+a)
e=sympy.exp(e)
print(e)
#exp(5*log(b+a))
e=sympy.log(sympy.exp((a+b)**5))
print(e)
#(b+a)^5
'''
'''
from sympy import Symbol, solve
a = Symbol("a")
b = Symbol("b")
c = Symbol("c")
exp = (a+b)*40-(c-a)/0.5
print(solve(exp))
'''
'''
{a: [0.0476190476190476*c - 0.952380952380952*b],
b: [0.05*c - 1.05*a],
c: [20.0*b + 21.0*a]}
'''
import sympy

a, b, c, x, y = sympy.symbols('a b c x y')
exp = (a + b) * 40 - (c - a) / 0.5
print(exp.evalf(6, subs={a: 6, b: 5, c: 2}))
print(sympy.solve(sympy.Eq(x ** 3 + 2 * x ** 2 + 4 * x + 8, 0), x))
print(
    sympy.solve([sympy.Eq(x + 5 * y, 2), sympy.Eq(-3 * x + 6 * y, 15)], [x, y]))
