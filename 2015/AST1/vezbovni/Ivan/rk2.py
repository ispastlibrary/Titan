import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0, 10, 0.3)
y=y0=0
dx=0.3
x0=0
p=x+dx

def fun(x, y):
    return -np.cos(x)

lista= []

for i in range(len(x)):
    y = y + (-np.cos(x[i]))*dx
    lista.append(y)
    y0=y

q=y+(-np.cos(x[i]))*dx
   
k=(fun(x,y)+fun(p, q))/2

for t in range(len(x)):
    y = x0 + k*dx
       
plt.plot(x, lista)
plt.show()


