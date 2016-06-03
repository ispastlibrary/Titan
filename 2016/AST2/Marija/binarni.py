import matplotlib.pyplot as plt
import numpy as np

r1x=0.61*1.5e11
r1y=0

r2x=-0.13*1.5e11
r2y=0

v1x=0
v1y=75.4e3

v2x=0
v2y=-16.3e3

P=7084800
G=6.67e-11
b=0
dt=10

x1=[]
y1=[]
x2=[]
y2=[]

m1=5.73e30
m2=e30
while b<P:
    x1.append(r1x)
    y1.append(r1y)

    x2.append(r2x)
    y2.append(r2y)
    
    rx=r1x-r2x
    ry=r1y-r2y
    
    r=np.sqrt(rx**2+ry**2)
    
    a1x=-G*m2*rx/r**3
    a1y=-G*m2*ry/r**3

    a2x=-G*m1*rx/r**3
    a2y=-G*m1*ry/r**3
    
    v1x=v1x+a1x*dt
    v1y=v1y+a1y*dt
  
    v2x=v2x+a2x*dt
    v2y=v2y+a2y*dt

    r1x=r1x+v1x*dt
    r1y=r1y+v1y*dt

    r2x=r2x+v2x*dt
    r2y=r2y+v2y*dt

    b+=dt

plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.show()
