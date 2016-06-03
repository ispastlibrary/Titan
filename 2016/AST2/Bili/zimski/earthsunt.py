import numpy as np
import pylab as pl
import math

def efftemp(D):
    L=3.846e+26
    A=0.367
    sigma=5.670373e-8
    T=(L*(1-A)/(16*np.pi*sigma*D*D))**(1/4)
    return T


G=6.67384e-11 
M=1.9891e+30 
m=5.97219e+24 
dt=160

mi=G*(M+m)


e=0.0167
a=149.6e+9

D=(1+e)*a

r1x=0
r1y=0 
r2x=D 
r2y=0
v1x=0
v1y=0
v2x=0 
v2y=math.sqrt(((1-e)/(1+e))*mi/a) 


i=0
k=0
t=0
T=efftemp(D)
X=[0]*2000001
Y=[0]*2000001


X[0]=t
Y[0]=T

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
        t=(i+1)*dt
        D=r
        T=efftemp(D)
        X[k]=t
        Y[k]=T
        print(i,r1x,r2x,r1y,r2y)
    i+=1
     
pl.plot(X,Y,color='blue')
pl.show()

