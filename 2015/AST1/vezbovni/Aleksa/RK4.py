import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100, 0.01)
z = []

dX = 0.01
x0 = 0
p = x0 + dX/2
y0 = 0
pi = 3.141592653

def k1(x0, y0):
    return -np.cos(x0)

for i in range(len(x)):
    y = y0 + (-np.cos(x[i]))*x
    z.append(y)
    y0 = y
q = y0 + ((-np.cos(x[i]))*dX)/2

k = (k1(x, y)+k1(p, q))/2
t = (y0 + k1(p, q)*dX/2)
b =  

plt.plot(x,z)
plt.show()

