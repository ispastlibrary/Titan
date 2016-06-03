import numpy as np
import matplotlib.pyplot as plt

t, x, y, z = np.loadtxt('mars.dat', unpack=True, delimiter = ',')

def brzina(x, y, z, t):
    vx = np.zeros(np.len(x)-1)
    vy = np.zeros(np.len(x)-1)
    vz = np.zeros(np.len(x)-1)
    for i in range(np.len(x)-1):
        vx[i] = (x[i+1]-x[i])/(t[i+1]-t[i])
        vy[i] = (y[i+1]-y[i])/(t[i+1]-t[i])
        vz[i] = (z[i+1]-z[i])/(t[i+1]-t[i])
    return vx,vy,vz

def rastojanje(x,y,z):
    r = (x*x + y*y + z*z) 
    return r

def inklinacija(x,y,z):
    i = np.arcsin(z/(x*x+y*y+z*z)**0.5)
    return i

vx, vy, vz = brzina(x,y,z,t)
v = [0]*np.len(vx)
for i in range(len(vx)):
    v[i] = (vx[i]**2 + vy[i]**2 + vz[i]**2)**0.5
brzina_perihel = max(v)

i=0
while (inklinacija(x[i], y[i], z[i]) != 0):
    i +=1
brz_izlcvor = brzina(x[i], y[i], z[i], t[i]) 
max_inklinacija = max(inklinacija(x,y,z))
print(max(v), brz_izlcvor)
