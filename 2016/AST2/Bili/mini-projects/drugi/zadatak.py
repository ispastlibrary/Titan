import numpy as np
import matplotlib.pyplot as plt
import pylab
#from mpl_toolkits.mplot3d import Axes3D

t, x, y, z = np.loadtxt('mars.dat', unpack = True, delimiter = ',')

nmax = 0

def MaxI(i): #Racunanje inklinacije u svakoj tacki
    n=np.arcsin(z[i]/((x[i]**2 + y[i]**2 + z[i]**2)**(0.5)))
    return n

def Udaljenost(): #lista udaljenosti od Sunca
    d = np.zeros(len(x))
    for i in range(len(x)):
        d[i] = (x[i]**2 + y[i]**2 + z[i]**2)**(0.5)
    return d

def Perihel(): #Dobijanje indeksa perihela
    d = Udaljenost()
    dmax = 0
    for i in range(len(x)): #Afel
        if d[i] > dmax:
            dmax = d[i]
            afel = i
    dmin = dmax
    for i in range(len(x)): #Perihel
        if d[i] < dmin:
            dmin = d[i]
            perh = i
    return perh, afel, dmax, dmin

In = []

for i in range(len(x)):  #Racunanje inklinacije i cvora
    In.append(MaxI(i))
    if MaxI(i) > nmax:
        nmax = MaxI(i)
    if ((z[i] < 0) and (z[i+1] > 0)):
        cvor = i

def brzina(x, y, z, t, i):
    vx = (x[i+1] - x[i])/(t[i+1] - t[i])
    vy = (y[i+1] - y[i])/(t[i+1] - t[i])
    vz = (z[i+1] - z[i])/(t[i+1] - t[i])
    v = (vx**2 + vy**2 + vz**2)**(0.5)
    return v

def Ekscen(dmin, dmax):
    r = (dmax-dmin)/(dmax+dmin)
    return r

#fig = pylab.figure()
#ax = Axes3D(fig)

perh, afel, dmax, dmin = Perihel()

def Vreme(afel, cvor):
    if (t[afel] > t[cvor]):
        tp = t[afel] - t[cvor]
    else:
        tp = t[len(t) - 1] - t[cvor] + t[afel]
    return tp
print(t[afel], t[cvor])
#ax.scatter(x, y, z)
#ax.scatter(0, 0, 0)
#plt.scatter(d, tk)
plt.plot(t,In)
plt.title('Zavisnost inklinacije od vremena')
plt.xlabel('Vreme[dan]')
plt.ylabel('Inklinacija[rad]')
print("Inklinacija: ", nmax*180/3.14, "Brzina u perihelu i cvoru:", brzina(x, y, z, t, perh)*1.5e8/86400, brzina(x, y, z, t, cvor)*1.5e8/86400, "Ekscen:", Ekscen(dmin,dmax), "Afel:", dmax, "Perihel:", dmin, "Vreme potrebno od cvora do afela", Vreme(afel, cvor))

plt.show()
