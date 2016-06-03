import numpy as np
from scipy.interpolate import interp1d
x,y = np.loadtxt("lajna.txt", unpack = True)
lgf_new = interp1d(x, y, kind = "cubic")
y = 1-y
z = np.linspace(5395.8, 5396.28, 500)
z1 = lgf_new(z)

def SimpS(a,a+2):
    p = (x[a+2]-x[a])/6 * (z1(a) + z1[a+2] + 4* z1[a+1])
    return p
   
def lin(x0, y0, x1, y1, x):
    y = y0 + (y1-y0) * (x-x0) / (x1-x0)
    return y 

def simps(x0, y0, x1, y1):
    p = (x1 - x0)/6 * (y0 + y1 + 4 * lin(x0, y0, x1, y1, (x0 + x1)/2))
    return p

def simps1(x0, y0, x1, y1):
    p =(x1-x0)/6 * (y0 + y1 + 4 * lgf_new((x0+x1)/2))
    return p

def trap(x0, y0, x1, y1):
    s = (y0 + y1)/2 * (x1-x0)
    return s

suma1 = 0
for i in range(len(x)-1):
    suma1 += simps(x[i], y[i], x[i+1], y[i+1])
print(suma1,"Linearna interpolacija + moj simpson")

suma2 = 0
for i in range(len(x)-1):
    suma2 += trap(x[i], y[i], x[i+1], y[i+1])
print(suma2, "Trapezno pravilo")

suma3 = 0
for i in range(len(x)-1):
    suma3 += simps1(x[i],y[i],x[i+1],y[i+1])
print(suma3, "Cubic spline + moj simpson")

suma4 = 0
for i in range(len(z)):
    suma4 += SimpS(2*i+1, 2*i+3)
print(suma3, "Gusti cubic spline")
