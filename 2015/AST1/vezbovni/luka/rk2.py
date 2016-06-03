import numpy as np
import matplotlib as mlib
mlib.use('Agg')
import matplotlib.pyplot as plt

x0=0
y0=0
dx=0.05

def k1(x0, y0):
    return -np.cos(x0)
print(k1(x0, y0))


def k2(x0, y0):
    return -np.cos(x0)
print(k2(x0+dx, y0+k1(x0, y0)*dx))

k =((k1(x0, y0)+k2(x0+dx, y0+k1(x0, y0)*dx))/2)
print(k)

y=[y0]*100
x=np.linspace(0, 5, num=100)

for i in range(len(x)-1):
    k = ((k1(x[i], y[i])+k2(x[i]+dx, y[i]+k1(x[i], y[i])*dx))/2)
    y[i+1] = y[i]+ k*dx
plt.plot(x, y, '-r')
plt.savefig('rk2')
plt.show()
