import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100, 0.01)
z = []

dX = 0.01
p = x + dX
x0 = 0
y0 = 0
pi = 3.141592653

def k1(x0, y0):
    return -np.cos(x0)

for i in range(len(x)):
    y = y0 + (-np.cos(x[i]))*x
    z.append(y)
    y0 = y
q = y + (-np.cos(x[i]))*dX
def k2(p, q):
    return -np.cos(p)

k = (k1(x, y) + k2(p, q)) / 2

for j in range(len(x)):
    y = x0 + k*dX

plt.plot(x,z)
plt.show()

