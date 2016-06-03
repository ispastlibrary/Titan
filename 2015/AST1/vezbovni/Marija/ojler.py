import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

dx = 0.3
n = 10
y0= 0
x0= 0

yn = []
xn= []

x = np.linspace(x0, np.pi, 10)
print(x)

print (-np.cos(x0)) #k1

def df (x0, y0):
    return -np.cos(x)
x=x0
y=y0
n_l= np.arange(x0, 7, 0.3)
xn.append(x)
yn.append(y)

for i in range (n):
    k1= df(x, y)*dx
    y=y + df(x, y)*dx
    x += dx
    k2= df(x, y)*dx
    y= y + df(x, y)*dx
    xn.append(x)
    yn.append(y)
 
plt.plot(xn, yn, '-r')
plt.legend(loc= 'best')
plt.xlabel('x-osa')
plt.ylabel('y-osa')
plt.title('Ojler')
plt.show()

