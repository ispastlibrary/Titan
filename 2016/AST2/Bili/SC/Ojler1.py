import pylab as pl
import numpy as np

def func_izvod(x):
    y=2*x
    return y

def Ojler(h,y0,x0):
    y1=y0+h*func_izvod(x0)
    return y1
def kvadrat(x):
    y=x*x
    return y

x0=0
y0=0
h=0.4
n=400
gore=[]
dole=[]
gore1=[]
gore.append(y0)
dole.append(x0)
gore1.append(kvadrat(x0))


for i in range(n):
    y0=Ojler(h,y0,x0)
    x0+=h
    print(i,x0,y0)
    gore.append(y0)
    dole.append(x0)
    gore1.append(kvadrat(x0))

pl.scatter(dole,gore,color='orange')
pl.xlim(0,4)
pl.ylim(0,16)
pl.plot(dole,gore1,'blue')
pl.show()


       
