import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

t ,x ,y ,z  = np.loadtxt("mars.dat", unpack = True, delimiter = ',')

min = 5
max = 0
a = 0
b = 0 
Brzinauuzlaznomcvoru = 0
VA = 0
for i in range(len(t)):
    d = (x[i]**2+y[i]**2+z[i]**2)**(1/2)
    if (d < min):
        min = d
        b = i
    if (d > max):
        max = d
        deltat = t[i]-t[i-1]
        deltas = ((x[i]-x[i-1])**2+(z[i]-z[i-1])**2+(y[i]-y[i-1])**2)**0.5
        VA = deltas/deltat *1.496*100000000/24/3600
        a = i
print("Afel:", max,"AU")
print("Perihel:", min,"AU")
vremeafela = t[a]
vremeuzlaznogcvora = 0
brzinauuzlaznomcvorumarsa = 0
for i in range(len(t)):
    if(z[i] >=0 and z[i-1] <0):
        vremeuzlaznogcvora = t[i]
        vremeuzlaznogcvora2= t[i-1]
        deltat = t[i]-t[i-1]
        deltas = ((x[i]-x[i-1])**2+(y[i]-y[i-1])**2+(z[i]-z[i-1])**2 )**0.5
        brzinauuzlaznomcvorumarsa = deltas/deltat *1.496*100000000/24/3600    
zmaj = 0
incmax = 0 
for i in range(len(t)):
    if(zmaj<z[i]):
        zmaj = z[i]
        incmax=np.arcsin((zmaj/(x[i]**2+y[i]**2+z[i]**2)**0.5))*180/3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
print("Inklinacija:", incmax," deg")
e=((max-min)/(max+min))
print("Ekscentricitet:", e)
vremeodpdoa = (((t[a]-t[b])**2)**0.5)*2
vremeoddo = vremeafela-vremeuzlaznogcvora + vremeodpdoa
plt.plot(t,z/(x**2+z**2+y**2)**0.5 *180/3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342217067982148086513282306647069)
plt.show()
print("Vreme od uzlaznog cvora do afela je:", vremeoddo, "dana")
print("Brzina u uzlaznom cvoru je:", brzinauuzlaznomcvorumarsa, "km/s")
print("Brzina u afelu je:", VA, "km/s")
