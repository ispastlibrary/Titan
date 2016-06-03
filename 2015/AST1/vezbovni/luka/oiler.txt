import numpy as np
import matplotlib as mlib
mlib.use('Agg')
import matplotlib.pyplot as plt

x0=0
y0=0
dx=0.5

def f(x0, y0):
    return -np.cos(x0)

print(f(x0, y0))

y=[y0]*10

x=np.linspace(0, 5, num=10)
#y=(y0+ f(x, y) *dx)
#i=0
#print (f(x[i], y))
#print(x)
#print(y)

for i in range(len(x)-1):
    y[i+1] = y[i] + f(x[i], y[i])*dx

plt.plot(x, y, '-r', label = 'fit')
plt.savefig('oiler.png')
plt.show()
