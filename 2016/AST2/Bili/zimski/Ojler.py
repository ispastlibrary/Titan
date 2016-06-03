import numpy as np 
import pylab as pl

 
def Fder (x,y):
    f=(x+y/4)**(1/2)
    return f

A=[0]*10
B=[0]*10

def Euler (x0, y0, xk, h):
    br=(xk-x0)//h
    for i in range(0, br+1):
        A[i]=x0
        B[i]=y0
        y0+=h*Fder(x0,y0)
        x0+=h
    return B[br]

x0=1
y0=1
h=1
xk=10
s=Euler(x0, y0, xk, h)
print(s)
#pl.scatter(A,B)
pl.plot(A,B, color='red')
pl.xlim(0,11)
pl.ylim(0,30)
pl.show()
