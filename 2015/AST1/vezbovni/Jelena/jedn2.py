import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dx = 0.5
xn = []
yn = []
x0 = 0
y0 = 0
k = []
n = 50

def funy(y0, dx, k):
    return y0 + k * dx

def funk(k1,k2):
    return (k1 + k2) / 2

def funk1(x):
    return -np.cos(x)

x = x0
y = y0
xn.append(x)
yn.append(y)

for i in range(n):
    k1 = funk1(x)
    k2 = funk1(x + dx)
    k = funk(k1,k2)
    y = funy(y,dx,k)
    x += dx
    xn.append(x)
    yn.append(y)

plt.plot(xn,yn)
plt.show()
