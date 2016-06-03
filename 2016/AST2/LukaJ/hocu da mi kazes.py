"""
Hoću da mi kažeš:

1) Kolika je inklinacija orbite Marsa?
2) Kako se inklinacija menja sa vremenom?
3) Kolika je brzina Marsa u uzlaznom čvoru i perihelu?
4) Koliki je ekscentricitet Marsove orbite?
5) Koliko je rastojanje Marsa u perihelu i afelu?
6) Koliko je vremena potrebno da Mars stigne od uzlaznog čvora do afela?
"""

import numpy as np
import matplotlib.pyplot as plt
import math as math

r = []
 
t, x, y, z = np.loadtxt('mars.dat', unpack = True, delimiter = ',')

def R(A, B, C):
    return np.sqrt(A**2 + B**2 + C**2)

i = 0

while i < len(t):
    r.append(R(x[i], y[i], z[i]))
    i = i + 1

rmaxi = np.argmax(r)
rmini = np.argmin(r)

xrmaxi = x[rmaxi]
yrmaxi = y[rmaxi]

xrmini = x[rmini]
yrmini = y[rmini]

rxymax = np.sqrt(xrmaxi**2 + yrmaxi**2)
rxymin = np.sqrt(xrmini**2 + yrmini**2)

rxy = rxymax + rxymin

tetarad = np.arccos(rxy/(r[rmaxi]+r[rmini]))
teta = tetarad*180/math.pi

print(teta)

j = 0
k = 0


while j < len(t):
    if z[j] = 0:
        z0 = j
        (z[j-1]/2 + z[j+1]/2)*
    elif z[j] < 0 and z[j+1] > 0:
        z0 = j
        
        break
    j = j + 1
