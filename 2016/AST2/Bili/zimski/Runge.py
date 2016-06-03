import numpy as np
import pylab as pl

A=[0]*10
B=[0]*10

def Fder(x,y):
    f=(x+y/4)**(1/2)
    return f

def Runge(x0, y0, h):
    k1=h*Fder(x0,y0)
    k2=h*Fder(x0+h/2, y0+ k1/2)
    k3=h*Fder(x0+h/2, y0+ k2/2)
    k4=h*Fder(x0+h, y0 +k3)
    y1=(k1+2*k2+2*k3+k4)/6 + y0
    return y1

x0=1
y0=1
h=1
xk=10
br=(xk-x0)//h
for i in range (0, br+1):
    A[i]=x0
    B[i]=y0
    y0=Runge(x0, y0, h)
    x0+=h   
print(B[br])
pl.plot(A, B)
pl.show()

