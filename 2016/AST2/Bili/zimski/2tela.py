import numpy as np
import pylab as pl
import math

G=1
m1=0.75
m2=0.25
dt=0.01

r1x=-0.625
r1y=0 
r2x=1.875 
r2y=0
v1x=0
v1y=-0.0866050400 
v2x=0 
v2y=0.2598076211

i=0
k=0
X1=[0]*20001
Y1=[0]*20001
X2=[0]*20001
Y2=[0]*20001

X1[0]=r1x
Y1[0]=r1y
X2[0]=r2x
Y2[0]=r2y

while i<200000:
    
    r=math.sqrt(math.pow(r1x-r2x,2)+math.pow(r1y-r2y,2))
    a1x=(G*m2*(r2x-r1x))/(math.pow(r,3))
    a1y=(G*m2*(r2y-r1y))/(math.pow(r,3))
    a2x=(G*m1*(r1x-r2x))/(math.pow(r,3))
    a2y=(G*m1*(r1y-r2y))/(math.pow(r,3))

    v1x+=a1x*dt
    v1y+=a1y*dt
    r1x+=v1x*dt 
    r1y+=v1y*dt

    v2x+=a2x*dt
    v2y+=a2y*dt
    r2x+=v2x*dt 
    r2y+=v2y*dt

    if i%10==0:
        k+=1
        X1[k]=r1x
        Y1[k]=r1y
        X2[k]=r2x
        Y2[k]=r2y
        print(i,r1x,r1y,r2x,r2y);
    i+=1
     
pl.plot(X1,Y1,color='red')
pl.plot(X2,Y2,color='blue')
pl.show()
