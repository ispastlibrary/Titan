import numpy as np
import pyplot as pl

t, x, y, z= np.loadtxt('mars.dat', delimiter=',', unpack= True)

nmax= 0

for i in range(len(x)):
    k= np.arcsin(z[i]/(x[i]**+ z[i]**2+ y[i]**2)**0.5))
    if k> nmax:
        nmax= k

def udaljenost(x, y, z):
    r= (x**2+ y**2+ z**2)
return r

def brzina(x, y, z, t):
    for i in range(len(x)):
        vx[i]= (v[x+1]- v[x])/(t[i+1]- t[i])
        vy[i]= (v[y+1]- v[y])/(t[i+1]- t[i]) 
        vz[i]= (v[z+1]- v[z])/(t[i+1]- t[i])
	return vx, vy, vz
 
vx, vy, vz= (udaljenost(x, y, z, t))
v= (vx**2+ vy**2+ vz**2)
      
plt.plot(x, y, z)
print(nmax)
pyplot.show
