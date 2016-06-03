import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
dx=1
xn=[]
yn=[]
x0=0
y0=0
k=[]
n=20

def f(y0, dx, k):
    return y0 + k*dx
def f2(k1, k2):
    return (k1 + k2)/2

def f3(x):
    return -np.cos(x)

x=x0
y=y0
xn.append(x)
yn.append(y)

for i in range(n):
    k1=f3(x)
    k2=f3(x+dx)
    k=f2(k1, k2)
    y=f(y0, dx, k)
    xn.append(x)
    x=x+dx
    yn.append(y)

plt.plot(xn, yn)
plt.show()
