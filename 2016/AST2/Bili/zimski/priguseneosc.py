import math
import numpy as np
import pylab as pl

def prig(X0,b,m,w,fi0,t):
    beta=b/(2*m)
    X=X0*(math.exp(-beta*t))*math.sin(w*t+fi0)


X0=5
b=0
m=1
w=3
fi0=0
t=0
dt=1

i=0

A=[0]*200
B=[0]*200

while i<200:
    A[i]=t
    B[i]=prig(X0,b,m,w,fi0,t)
    t+=dt

pl.plot(A,B)
pl.show()
    
