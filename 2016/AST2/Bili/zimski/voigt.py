import math
import pylab as pl
from scipy.integrate import quad


def integrand(t,a,x):
    return math.exp(-t**2)/((x-t)**2+a**2)
def voigt(a,x):
    return quad(integrand,-float("inf"),float("inf"),args=(a,x)) 
def proced(a):
    i=0
    x=-5
    A1=[0]*1001 
    B1=[0]*1001 
    while (i<1001):
        A1[i]=x
        B1[i]=voigt(a,x)[0]
        x+=0.01
        i+=1
    return A1,B1 
a=0.2 
pl.plot(proced(a)[0],proced(a)[1],color='red') 
a=0.1
pl.plot(proced(a)[0],proced(a)[1],color='blue') 
a=1e-2
pl.plot(proced(a)[0],proced(a)[1],color='green') 
a=1e-3
pl.plot(proced(a)[0],proced(a)[1],color='darkorange') 
#a=1e-4 
#pl.plot(proced(a)[0],proced(a)[1],color='magenta')
#a=1e-5 
#pl.plot(proced(a)[0],proced(a)[1],color='black') 
pl.yscale('log')
pl.xlim(-5,5)
pl.show()
