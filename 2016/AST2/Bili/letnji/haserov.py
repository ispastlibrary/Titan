import numpy as np
import matplotlib.pyplot as plt

Q = 1e28 #1/s
v = 4500 #m/s
ld = 449e6 #m
lp = 147e4 #m
Rn = 3e4 #m
A=149597871000 #m
Rk=0.1*A

def konc(r):
    dR=r-Rn
    kon=(Q*ld*(np.exp(-dR/lp)-np.exp(-dR/ld)))/(4*np.pi*v*r*r*(lp-ld))
    return kon

y=[]
x=[]
dr=(Rk-Rn)/100

R=Rn
for i in range(100):
    y.append(konc(R))
    x.append(R)
    Rn+=dr

plt.plot(x,y,'blue')
plt.show()
