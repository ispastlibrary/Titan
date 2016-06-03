import matplotlib.pyplot as plt
import numpy as np

p1x = []
p1y = []
p2x = []
p2y = []

m2 = 5.73*1.98e30
m1 = 1.22*1.98e30

r1 = np.array([0.61*1.5e11,0])
r2 = np.array([-0.13*1.5e11,0])

v1 = np.array([0,75.4e3])
v2 = np.array([0,-16e3])

G = 6.67e-11

T = 88.2*24*60*60

t = 0;
dt = 24*60*60

p1x.append(r1[0])
p1y.append(r1[1])
p2x.append(r2[0])
p2y.append(r2[1])

while t <= T :
    r12 = r2 - r1
    r21 = r1 - r2
    intR = np.sqrt(r12[0]**2 + r12[1]**2)    

    a1 = -G*m2/intR**3 * r21    
    a2 = -G*m1/intR**3 * r12

    dv1 = a1*dt
    dv2 = a2*dt
    
    v1 += dv1
    v2 += dv2

    dr1 = v1*dt
    dr2 = v2*dt

    r1 += dr1
    r2 += dr2

    p1x.append(r1[0])
    p1y.append(r1[1])
    p2x.append(r2[0])
    p2y.append(r2[1])
    t += dt

plt.scatter(p1x,p1y)
plt.scatter(p2x,p2y)
plt.show()
