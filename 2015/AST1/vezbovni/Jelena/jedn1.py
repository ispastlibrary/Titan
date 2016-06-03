import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dx = 0.05
xn = []
yn = []
y0 = 0
x0 = 0
k = []
n = 500

def funy(y0,dx,k):
    return y0 + k * dx
x = x0
y = y0
xn.append(x)
yn.append(y)

for i in range(n):
    prom=-np.cos(x)
    y = funy(y,dx,prom)
    x += dx
    xn.append(x) 
    yn.append(y)

print(x)
print(y)
plt.plot(xn,yn)
plt.show() 
