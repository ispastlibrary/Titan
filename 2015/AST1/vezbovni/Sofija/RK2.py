import numpy as np
import matplotlib.pyplot as plt

y0 = 0
x0 = 0
dx = 0.3
k = -1
n = 17

xn = []
yn = []

def fun(x, y):
    k = -np.cos(x)
    return k
    
#y = y0 + k * dx
x0 = 0
y0 = 0

x = x0
y = y0

for i in range(n):
    k1 = fun(x, y)
    y1 = y + k1 * dx
    x1 = x + dx
    k2 = fun(x1, y1)
    y2 = y + k2 * dx
    x2 = x + dx
    k = (k1 + k2)/2
    y = y + k * dx
    x = x + dx
    xn.append(x)
    yn.append(y)

plt.plot(xn, yn)
plt.show()
