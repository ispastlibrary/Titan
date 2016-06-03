import numpy as np
import matplotlib.pylab as pl 

def ubr(dx,m):
    a=-k*dx/m
    return a
    
dt=0.01
t=0
m1=2
m2=1
k=0.05
x01=8
x02=8.5
v01=0
v02=0
L=1

#dx=L-np.abs(x02-x01)
dx = L-(x02-x01)
a01=ubr(dx,m1)
a02=ubr(-dx,m2)
i=0
xosa=[]
yosa1=[]
yosa2=[] 
xosa.append(t) 
yosa1.append(x01)
yosa2.append(x02)


while (i<5700):
    t+=dt
    v1=v01+dt*a01
    v2=v02+dt*a02
    x1=x01+dt*v01  
    x2=x02+dt*v02    
    v01=v1
    v02=v2
    x01=x1
    x02=x2
    d=(x02-x01)
    dx=L-d
#    if ((x01<x02)and(L<d))or((x01>x02)and(L>d)):
#        a01=ubr(-dx,m1)
#        a02=ubr(dx,m2)
#    else:
    a01=ubr(dx,m1)
    a02=ubr(-dx,m2)  
    xosa.append(t)
    yosa1.append(x01)
    yosa2.append(x02)
    i+=1

pl.plot(xosa,yosa1,'green')
pl.plot(xosa,yosa2,'blue')
pl.show()
