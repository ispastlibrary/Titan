import numpy as np
import pylab as pl
import math

G=6.67384e-11 
M=1.9891e+30 
m=5.97219e+24 
dt=160

#def RK4(h,x0,y0):
#    k1=h*f(x0,y0)
#    k2=h*f(x0+h/2,y0+k1/2)
#    k3=h*f(x0+h/2,y0+k2/2)
 #   k4=h*(x0+h,y0+k3)
 #   k=(1/6)*(k1+2(k2+k3)+k4)
 #   return 
mi=G*(M+m)


e=0.0167
a=149.6e+9


r1x=0
r1y=0 
r2x=(1+e)*a 
r2y=0
v1x=0
v1y=0
v2x=0 
v2y=math.sqrt(((1-e)/(1+e))*mi/a) 



i=0
k=0
X1=[0]*2000001
Y1=[0]*2000001
X2=[0]*2000001
Y2=[0]*2000001

X1[0]=r1x
Y1[0]=r1y
X2[0]=r2x
Y2[0]=r2y

while i<20000000:
    
    r=math.sqrt(math.pow(r1x-r2x,2)+math.pow(r1y-r2y,2))
    a1x=(G*m*(r2x-r1x))/(math.pow(r,3))
    a1y=(G*m*(r2y-r1y))/(math.pow(r,3))
    a2x=(G*M*(r1x-r2x))/(math.pow(r,3))
    a2y=(G*M*(r1y-r2y))/(math.pow(r,3))

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
     
pl.plot(X1,Y1,color='blue')
pl.plot(X2,Y2,color='yellow')
pl.show()
