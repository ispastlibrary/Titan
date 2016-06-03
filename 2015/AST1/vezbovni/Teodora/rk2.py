import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

xo = 0
yo = 0
dx = 0.3

def fun(x, y):
    return -np.cos(x)

xl = np.linspace(xo, np.pi, 10)
x = xo
y = yo

nizy = []
nizx = []

for x in range(len(xl)):
    y1 = y + fun(x,y)*dx
    x1 = x + dx
    y2 = y + fun(x1, y1)*dx
    x2 = x1 + dx
    k = (fun(x, y) + fun(x1, y2))/2
    y = y + k*dx
    x = x + dx
    nizx.append(x)
    nizy.append(y)
   

plt.plot(nizx, nizy)
plt.show()










