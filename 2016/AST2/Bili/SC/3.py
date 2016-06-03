import numpy as np
import matplotlib.pyplot as plt

def a_x(r0x,r0y):
    a1x=0
    for i in range(1,n+1):
        r=np.sqrt((r0x-Rx[i])**2+(r0y-Ry[i])**2)
        a1x+=-g*M[i]*(Rx[i]-r0x)/r**3
    return a1x

def a_y(r0x,r0y):
    a1y=0
    for i in range(1,n+1):
        r=np.sqrt((r0x-Rx[i])**2+(r0y-Ry[i])**2)
        a1y+=-g*M[i]*(Ry[i]-r0y)/r**3
    return a1y

dt=1
i=0
g=6.67e-11
j=0
n=1

Rx=[0]*2
Ry=[0]*2
M=[0]*2
Rx[1]=50
Ry[1]=50
M[1]=1000000

rx=0
ry=0
v=5
alpha=np.pi/3
vx=v*np.cos(alpha)
vy=v*np.sin(alpha)

X=[]
Y=[]

while (j<1000):
    r1x=rx
    r1y=ry
    v1x=vx
    v1y=vy
    a1x=a_x(r1x,r1y)
    a1y=a_y(r1x,r1y)

    r2x=r1x+v1x*dt/2
    r2y=r1y+v1y*dt/2
    v2x=v1x+a1x*dt/2
    v2y=v1y+a1y*dt/2
    a2x=a_x(r2x,r2y)
    a2y=a_y(r2x,r2y)

    r3x=r1x+v2x*dt/2
    r3y=r1y+v2y*dt/2
    v3x=v1x+a2x*dt/2
    v3y=v1y+a2y*dt/2
    a3x=a_x(r3x,r3y)
    a3y=a_y(r3x,r3y)


    r4x=r1x+v3x*dt
    r4y=r1y+v3y*dt
    v4x=v1x+a3x*dt
    v4y=v1y+a3y*dt
    a3x=a_x(r4x,r4y)
    a3y=a_y(r4x,r4y)

    vx=dt/6*(v1x+2*v2x+2*v3x+v4x)
    vy=dt/6*(v1y+2*v2y+2*v3y+v4y)
    rx=dt/6*(r1x+2*r2x+2*r3x+r4x)
    ry=dt/6*(r1y+2*r2y+2*r3y+r4y)
    if (i%10==0):
        print(j,rx,ry)
        X.append(rx)
        Y.append(ry)
    j+=1

plt.scatter(X,Y)
plt.show()
