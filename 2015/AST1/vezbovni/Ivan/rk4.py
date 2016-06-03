import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0, 10, 0.1)
y=y0=0
dx=0.1
x0=0
p=x0+dx/2

def fun(x, y):
    return -np.cos(x)

lista= []

q=y0+((fun(x, y))*dx)/2
t=y0+fun(p, q)*dx/2
u=
for i in range(len(x)):
    y = y + (-np.cos(x[i]))*dx
    lista.append(y)
    y0=y






