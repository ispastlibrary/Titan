import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


t, x, y, z = np.loadtxt('mars.dat', delimiter=',', unpack=True)
intenziteti = []
for i in range (len(x)):
    intenzitet = np.sqrt(x[i]**2+y[i]**2+z[i]**2)
    intenziteti.append(intenzitet)
intenzitetmax = max(intenziteti)
intenzitetmin = min(intenziteti)
a = (intenzitetmin+intenzitetmax)/2
e = 1-(intenzitetmin/a)
#print (e, intenzitetmin, intenzitetmax)
zmax = max(z)
ymax = max(y)
xmax = max(x)
intenzitetxy = np.sqrt(y**2+x**2)
inklinacija = np.arcsin(zmax/intenzitetmax)
#print (inklinacija)
period = max(t)
t1 = (period*70)/360
print (t1)
