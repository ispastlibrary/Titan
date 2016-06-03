import numpy as np
import pylab as plt

def f(x):
    y = a*x**4+b*x**3+c*x**2+d*x+e
    return y 

def velocity(x0,v0,x1):
    v1 = np.sqrt(2*(g*f(x0)+v0*v0/2-g*f(x1)))     
    return v1

koef = []
for i in range(5):
    koef.append(int(input()))
x = np.linspace(-3,5,num=100)
a = koef[0]
b = koef[1]
c = koef[2]
d = koef[3]
e = koef[4]
y = f(x)
first = plt.subplot(2,1,1)
first.scatter(x,y)

#m=1
g = 9.81
dx = 8/100
x0 = -3
v0 = 0
v = [0]*100
v[0] = v0
ac = [0]*100
ac[0] = 0
for i in range(99):
    x1 = x0+dx
    v1 = velocity(x0,v0,x1)
    s = np.sqrt((x1-x0)**2+(f(x1)-f(x0))**2)
    a0 = (v1**2-v0**2)/(2*s)
    v[i+1] = v1
    ac[i+1] = a0
    print(a0,i)
    #t = (v1-v0)/a
    v0 = v1
    x0 = x1
second = plt.subplot(2,1,2)
second.scatter(x,v)
#third = plt.subplot(2,1,2)
#third.scatter(x,ac)
plt.show()
