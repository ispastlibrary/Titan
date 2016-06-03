import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

xo=0
yo=0
dx=0.3

n_1 = np.linspace(xo, np.pi, 10)

def fun(x, y):
    return -np.cos(x)

print (fun(xo, yo))

x=xo
y=yo

r = []
for x in range(len(n_1)):
    y=y+fun(x, y)*dx
    r.append(y)
    x=x+dx
print(r)




plt.plot(n_1, r,'-r')
plt.show()



