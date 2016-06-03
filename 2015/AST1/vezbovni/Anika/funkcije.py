import matplotlib.pyplot as plt
import numpy as np

y0=0
x0=0
deltax=0.3
n=10

def f(x, y):
    k=-np.cos(x)
    return k

k=f(x0, y0)
y=y0+k*deltax

x=np.arange(0, 10, 0.3)
y=f(x,y0)

plt.plot(x, y, '-r', label='MCR')
plt.plot(x, -np.sin(x), '--b')
plt.show()    



