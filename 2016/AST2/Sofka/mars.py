import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.interpolate import interp1d
 
t, x, y, z = np.loadtxt('mars.dat', unpack=True, delimiter = ',')

#maximum = 0
#for i in range(len(x)):
#    if x[i]>maximum:
#        maximum = x[i]
#        index = 1   
#print(x[i])


#r = np.sqrt(x**2, y**2, z**2)
#maximum = 0
#for i in range (len(z)):
#    if z[i]>maximum:
#        maximum = z[i]
#print(maximum)
maksimum = max(z)
i = np.argmax(z)
r = np.sqrt(x**2 + y**2 + z**2)
a=np.arcsin(maksimum/r[i])
inklinacija= (a*360)/(2*np.pi)
print(inklinacija)

perihel=np.argmax(r)
afel=np.argmin(r)
#plt.plot(t,r)
#plt.show()
print(perihel)
print(afel)
print(t[perihel])
print(t[afel])

dt = 1e-6
fx = interp1d([t[perihel],t[perihel+1]], [x[perihel],x[perihel+1]])
x1 = ((fx(t[perihel]+dt)-t[perihel])/dt)
fz = interp1d([t[perihel],t[perihel+1]], [z[perihel],z[perihel+1]])
x2 = ((fz(t[perihel]+dt)-t[perihel])/dt)
fy = interp1d([t[perihel],t[perihel+1]], [y[perihel],y[perihel+1]])
x3 = ((fy(t[perihel]+dt)-t[perihel])/dt)
print(x1, x2, x3)

v =np.sqrt(x1**2 + x2**2 + x3**2)
print(v)
v2 = (v * 86400)/150e9
print(v2)

