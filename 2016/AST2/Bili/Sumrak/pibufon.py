import numpy as np
import matplotlib.pyplot as plt
import math

n = 500 #broj cackalica
d = 4 #razmak izmedju grida
p = 50 #duzina po x
q = 50 #duzina po y
l = 3 #duzina cackalice


x = p*np.random.rand(n)
y = q*np.random.rand(n)
teta = (np.pi/2)*np.random.rand(n)
np = 0

def Min(Milan, Nastasija):
    if (Milan > Nastasija):
        return Nastasija
    else:
        return Milan

plt.scatter(x,y)

for i in range(n):
    m = Min(x[i]%d, d-x[i]%d)
    if (m < l*math.sin(teta[i])/2):
        np += 1
        plt.scatter(x[i], y[i], color='red')

h = 0

for i in range(q//d+1):
    plt.axvline(x = h)
    h += d

ZaLazu = 2*l*n/(d*np)

print(ZaLazu)
plt.show()
