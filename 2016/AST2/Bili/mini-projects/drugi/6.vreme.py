import numpy as np
import matplotlib.pyplot as plt
import pylab

t, x, y, z = np.loadtxt('mars.dat', unpack = True, delimiter = ',')
dmax = 0
d = []

for i in range(len(t)):
	d.append(((x[i]**2 + y[i]**2 + z[i]**2)**0.5))
	if d[i] > dmax:
		dmax = d[i]
		tafl = t[i]
	if ((z[i] < 0) and (z[i+1] > 0)):
		tuzl = (t[i+1] + t[i])/2
print(dmax, tafl, tuzl)
if (tafl > tuzl):
    t = (tafl - tuzl)
else:
    t = (t[len(t)-1] - tuzl + tafl) 

print("vreme od uzlaznog cvora do afela:",t,"dana")
