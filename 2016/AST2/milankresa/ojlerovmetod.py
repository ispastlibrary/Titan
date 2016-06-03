import numpy as np
import pylab as pl

def Fder (x, y):
    f = (x+y/4)**(1/2)
    return f

A=[0]*10
B=[0]*10

def Euler(x0, y0, xk, h):
    br = (xk-x0)//h
    for i in range(0, br+1):
        y0 = y0 +  h * Fder(x0, y0)
        x0 = x0 + h
        A[i]=x0
        B[i]=y0
    return y0


y0=1
x0=1
h=1
xk=10
s=Euler(x0, y0, xk, h)

pl.plot(A,B)

pl.show()
