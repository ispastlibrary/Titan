import numpy as np
import matplotlib.pylab as pl 

def ubr(dx,m):
    a=-k*dx/m
    return a
    
dt=0.001
t=0
m1=2
m2=2
m3=2
k=0.1
x01=7
x02=8
x03=9
v1=10
v2=0
v3=10
L1=1
L2=1

#dx=L-np.abs(x02-x01)
dx1=L1-(x02-x01)
dx3=L2-(x03-x02)
a01=ubr(dx1,m1)
a02=ubr(dx1,m2)+ubr(dx3,m2)
a03=ubr(dx3,m3)
i=0
xosa=[]
yosa1=[]
yosa2=[] 
yosa3=[]
xosa.append(t) 
yosa1.append(x01)
yosa2.append(x02)
yosa3.append(x03)

while (i<30000):
    t+=dt
    v1+=dt*a01
    v2+=dt*a02
    v3+=dt*a03
    x1=x01+dt*v1  
    x2=x02+dt*v2
    x3=x03+dt*v3
    #dx1=(x1-x01)+(x2-x02)
    #dx3=(x3-x03)+(x2-x02)
    dx1=(x01-x1)+(x2-x02)
    dx3=(x03-x3)+(x2-x02)
    x01=x1
    x02=x2
    x03=x3
    a01=ubr(-dx1,m1)
    a03=ubr(-dx3,m3)
    a02=ubr(-dx1,m2)+ubr(-dx3,m2)	
    xosa.append(t)
    yosa1.append(x01)
    yosa2.append(x02)
    yosa3.append(x03)
    i+=1

pl.plot(xosa,yosa1,'green')
pl.plot(xosa,yosa2,'blue')
pl.plot(xosa,yosa3,'orange')
pl.show()
