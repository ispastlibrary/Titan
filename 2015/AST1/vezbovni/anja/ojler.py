import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

dx = 0.3
 
y0= 0
x0=0
n = 10
x= np.linspace (x0, np.pi, 10)
print (x)

y= y0

def df (x, y):
    return -np.cos(x)
x_n = []
y_n = []

x=x0
y=y0
x_n.append(x)
y_n.append(y)

lista = np.arange(x0, 7, 0.3) 
for i in range (n):
    y = y+df(x,y)*dx
    x += dx
    y = y0 + df(x, y)*0.3 
    x = 
    x_n.append(x)
    y_n.append(y)
   
plt.plot(x_n, y_n, '-r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('ojler')
plt.show()

