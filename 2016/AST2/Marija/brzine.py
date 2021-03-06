import matplotlib.pyplot as plt
import numpy as np
from  scipy.interpolate import interp1d
t, x, y, z= np.loadtxt('mars.dat', unpack=True, delimiter=',')

r = np.sqrt(x**2+y**2+z**2)
p=np.argmin(r)

neg=np.extract(z<0,z)
indNeg=np.argmax(neg)
indZ=np.flatnonzero(z==neg[indNeg])
u=indZ+1
u=u[0]

dt=1e-6

#brzina u perihelu
f1=interp1d([t[p],t[p+1]], [x[p],x[p+1]])
x1=(f1(t[p]+dt)-x[p])/dt

f2=interp1d([t[p],t[p+1]],[y[p],y[p+1]])
y1=(f2(t[p]+dt)-y[p])/dt

f3=interp1d([t[p],t[p+1]], [z[p],z[p+1]])
z1=(f3(t[p]+dt)-z[p])/dt

v1=np.sqrt(x1**2+y1**2+z1**2)*150000000/86400

print(v1)

#brzina u uzlaznom covru
f4=interp1d([t[u],t[u+1]], [x[u],x[u+1]])
x2=(f4(t[u]+dt)-x[u])/dt

f5=interp1d([t[u],t[u+1]],[y[u],y[u+1]])
y2=(f5(t[u]+dt)-y[u])/dt

f6=interp1d([t[u],t[u+1]], [z[u],z[u+1]])
z2=(f6(t[u]+dt)-z[u])/dt

v2=np.sqrt(x2**2+y2**2+z2**2)*150000000/86400

print(v2)
