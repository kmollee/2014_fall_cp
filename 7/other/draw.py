from array import array
from sympy import *
import WoyTools as Woy
from math import pi
from pylab import plot

print()
print("***********************************************************")
print(" Simulation of Webcutter Mechanism by Harish Kumar Thotli")
print("***********************************************************")
print()
print()
print("**********************************************")
print(" Newton-Raphson-Method for Webcutter Mechanism")
print("**********************************************")
print()

a = 4
b = 28
c = 40
d = 26
e = 4
t3 = Symbol('t3')
t4 = Symbol('t4')
w1 = Symbol('w1')
w3 = Symbol('w3')
w4 = Symbol('w4')
r1 = Symbol('r1')
r3 = Symbol('r2')
r4 = Symbol('r4')


def position(t2):
    tt3, tt4,  = 1.646, 2.2175

    f1 = a * cos(t2) + b * cos(t3) - c * cos(t4) - d
    f2 = a * sin(t2) + b * sin(t3) - c * sin(t4) + e

    tt3, tt4 = nsolve((f1, f2), (t3, t4), (tt3, tt4))
    return tt3, tt4


def velocity(t2, w2, t3, t4):
    ww3, ww4 = 1.1072, 0.9634

    f1 = -a * w2 * sin(t2) - b * w3 * sin(t3) + c * w4 * sin(t4)
    f2 = a * w2 * cos(t2) + b * w3 * cos(t3) - c * w4 * cos(t4)

    ww3, ww4 = nsolve((f1, f2), (w3, w4), (ww3, ww4))
    return ww3, ww4


def acceleration(t2, w2, t3, t4, w3, w4):
    rr3, rr4 = -7.516, -0.4014

    f1 = -a * r2 * sin(t2) - a * w2 * w2 * cos(t2) - b * r3 * sin(t3) - b * w3 * w3 * cos(t3)\
        + c * r4 * sin(t4) + c * w4 * w4 * cos(t4)

    f2 = a * r2 * cos(t2) - a * w2 * w2 * sin(t2) + b * r3 * cos(t3) - b * w3 * w3 * sin(t3)\
        - c * r4 * cos(t4) + c * w4 * w4 * sin(t4)

    rr3, rr4 = nsolve((f1, f2), (r3, r4), (rr3, rr4))
    return rr3, rr4


def animation(t2, t3, t4):
    t3, t4 = position(t2)

    Ax = a * cos(t2)
    Ay = a * sin(t2)
    t5 = 1.2
    t6 = 1.1
    Bx = -d * cos(t1) + c * cos(t4)
    By = -d * sin(t1) + c * sin(t4)
    La = b * cos(t5)
    Lb = b * sin(t5)
    Ma = c * cos(t6)
    Mb = c * sin(t6)

    Xa = float(Ax)
    Ya = float(Ay)
    Xb = float(Bx)
    Yb = float(By)

    Laa = float(La)
    Lbb = float(Lb)
    Maa = float(Ma)
    Mbb = float(Mb)

    grafics.line(0, 0, Xa, Ya, 'orange', 2)
    grafics.line(Xa, Ya, Xb, Yb, 'blue', 2)
    grafics.line(Xb, Yb, 28, -4, 'red', 2)
    grafics.line(Xb, Yb, Xb + 21, Yb + 2, 'black', 2)
    grafics.line(Xb, Yb, Xb + Maa, Mbb, 'black', 2)

    yes = eval(input("Please press the return button!"))

    grafics.line(0, 0, Xa, Ya, 'white', 2)
    grafics.line(Xa, Ya, Xb, Yb, 'white', 2)
    grafics.line(Xb, Yb, 28, -4, 'white', 2)
    grafics.line(Xb, Yb, Xb + 21, Yb + 2, 'white', 2)
    grafics.line(Xb, Yb, Xb + Maa, Mbb, 'white', 2)
    return Xa, Ya, Xb, Yb

grafics = Woy.WoyGraph(650, 650)
grafics.window(-50, 90, -50, 90)

pax = array('f')
pbx = array('f')
qax = array('f')
qbx = array('f')

print()
print("--------------------------------------------")
print(" Newton-Raphson-Method for Webcutter Results")
print("--------------------------------------------")
print()

print()
print(
    "-------------------------------------------------------------------------------")
print(
    "   Time,     Theta2,    Ax,      Ay,        Bx,        By,    Theta3,    Theta4")
print(
    "-------------------------------------------------------------------------------")
print()

for time in Woy.frange(0.0, 1.0, 0.05556):
    t2 = 2 * pi * time
    Ax = a * cos(t2)
    Ay = a * sin(t2)
    t1 = 2.989
    r2 = 0
    W = 2 * pi
    ta3, ta4 = position(t2)

    Bx = d + c * cos(ta4)
    By = -e + c * sin(ta4)

    tt2 = Woy.degree(t2)
    ttt3 = Woy.degree(ta3)
    ttt4 = Woy.degree(ta4)
    ttt1 = Woy.degree(t1)

    t2 = 2 * pi * time

    outstr = 8 * "%9.4f "

    print(outstr % (time, tt2, Ax, Ay, Bx, By, ttt3, ttt4))

    print()
    print(
        "--------------------------------------------------------------------------------")
    print("    Theta2,   vel. of AB,  vel. of BC,  acc. of AB,  acc. of BC")
    print(
        "--------------------------------------------------------------------------------")
    print()

for time in Woy.frange(0.0, 1.0, 0.05556):
    t2 = 2 * pi * time
    W = 2 * pi
    ta3, ta4 = position(t2)
    wa3, wa4 = velocity(t2, W, ta3, ta4)
    ra3, ra4 = acceleration(t2, W, ta3, ta4, wa3, wa4)

    tt2 = Woy.degree(t2)

    outstr = 5 * "%12.4f "
    print(outstr % (tt2, wa3, wa4, ra3, ra4))

for time in Woy.frange(0.0, 1.0, 0.05):

    t2 = 2 * pi * time
    r2 = 0
    W = 2 * pi
    ta3, ta4 = position(t2)
    ax, ay, bx, by = animation(t2, ta3, ta4)

    pax.append(ax)
    pbx.append(ay)
    qax.append(bx)
    qbx.append(by)

    t = Woy.arange(0.0, 1.0, 0.05)
    T2 = 2 * pi * t
    TT2 = Woy.degree(T2)
    Woy.subplot(2, 1, 1)
    plot(TT2, pax, 'g', TT2, pbx, '#FF33CC')
    Woy.ylabel('Ax(green),Ay(pink)')
    Woy.title('Positions')
    Woy.grid(True)

    Woy.subplot(2, 1, 2)
    plot(TT2, qax, 'b', TT2, qbx, 'r')
    Woy.ylabel('Bx(blue),By(Red)')
    Woy.xlabel('Driven angle(Degrees)')
    Woy.grid(True)

# ---------------------------------------------------------------------
# simulation of a Webcutter Mechanism - Analytical Method
#
# ---------------------------------------------------------------------
#

from WoyTools import *
from pylab import *

# mechanism parameters
a = 4
b = 28
c = 40
d = 26

time = arange(0, 1.01, 0.01)
theta2 = 720 * time

# Formulas R.L. Norton page 171
Axa = a * cosdeg(theta2)
Aya = a * sindeg(theta2)

S = (a * a - b * b + c * c - d * d) / (2 * (Axa - d))
R = (d - S) * (d - S) - c * c
Q = (2 * Aya * (d - S)) / (Axa - d)
P = (Aya * Aya / ((Axa - d) * (Axa - d))) + 1

# Calculation of position of point B
# Index 1 - open configuration
# Index 2 - crossed configuration

By1 = (-Q + sqrt(Q * Q - 4 * P * R)) / (2 * P)
By2 = (-Q - sqrt(Q * Q - 4 * P * R)) / (2 * P)
Bx1 = S - (2 * Aya * By1) / (2 * (Axa - d))
Bx2 = S - (2 * Aya * By2) / (2 * (Axa - d))

# Define and open the grafics window(Not Used)
grafics = WoyGraph(640, 640)
grafics.window(-30, 50, -50, 50)

# Define iterators
it1 = iter(Axa)
it2 = iter(Aya)
it3 = iter(Bx1)
it4 = iter(By1)

# Animtion of frames
for i in time:
    x = next(it1)
    y = next(it2)
    t6 = 63.025

    u = next(it3)
    v = next(it4)
    m = u + 21
    n = v + 1

    o = u + c * cosdeg(t6)
    p = c * sindeg(t6)

    # print x,y,u,v
    grafics.line(0, 0, x, y, 'blue', 2)
    grafics.line(x, y, u, v, 'red', 2)
    grafics.line(u, v, m, n, 'orange', 2)
    grafics.line(u, v, d, -4, 'green', 2)
    grafics.line(u, v, o, p, 'orange', 2)
    grafics.line(d, -4, 0, 0, 'white', 2)

    yes = eval(
        input(" This is Analytical Method! Please press the return button!"))

    grafics.line(0, 0, x, y, 'white', 2)
    grafics.line(x, y, u, v, 'white', 2)
    grafics.line(u, v, m, n, 'white', 2)
    grafics.line(u, v, o, p, 'white', 2)
    grafics.line(u, v, d, -4, 'white', 2)
    grafics.line(d, -4, 0, 0, 'white', 2)

    grid(True)
    show()
