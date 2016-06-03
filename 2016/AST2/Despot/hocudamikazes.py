"""

Hoću da mi kažeš:

1) Kolika je inklinacija orbite Marsa?
2) Kako se inklinacija menja sa vremenom?
3) Kolika je brzina Marsa u uzlaznom čvoru i perihelu?
4) Koliki je ekscentricitet Marsove orbite?
5) Koliko je rastojanje Marsa u perihelu i afelu?
6) Koliko je vremena potrebno da Mars stigne od uzlaznog čvora do afela?

"""

import matplotlib.pyplot as plt
import math as math
import numpy as np

t,x,y,z = np.loadtxt('mars.dat' , unpack = True , delimiter = ',')

r = []

def R(x, y, z):
    return np.sqrt(x**2 + y**2 + z**2)

j = 0

while j < len(t):
    r.append(R(x[j] , y [j] , z[j]))
    j = j+1


rmax = max(r)
rmin = min(r)
rmaxi = np.argmax(r)
rmini = np.argmin(r)

xrmax = x[rmaxi]
yrmax = y[rmaxi]

xrmin = x[rmini]
yrmin = y[rmini]


r2dmax = np.sqrt(xrmax**2 + yrmax**2)
r2dmin = np.sqrt(xrmin**2 + yrmin**2) 

r2d = r2dmax + r2dmin

tetar = np.arccos(r2d / (r[rmaxi] + r[rmini]))

tetas = tetar*180/math.pi

#print(tetas)



i = 0
k = 0


while i < len(t):
    if z[i] = 0
        z0 = i
        break
    elif z[i] < 0 and z[i+1] > 0
        z0 = i
        break
    i = i + 1




































