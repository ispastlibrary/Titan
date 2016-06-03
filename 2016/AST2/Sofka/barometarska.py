import numpy as np
import matplotlib.pyplot as plt

x,y,dy = np.loadtxt('barometarska.txt', unpack=True)

e = np.exp(1)
a = np.linspace(0.9, 1.7, 300)
b = np.linspace(0.04, 0.08, 300)

hi=[]

for i in range (len(x)):
	for j in range(len(x)):
		c = ((y[i] - a[i]*e**(-b[j]*x))**2/(2*dy)**2)
		h = sum(c)
		hi.append(h)

print(np.amin(hi))
for a,b in enumerate(hi):
	if np.amin(hi):
		print(i)
		print(j)

