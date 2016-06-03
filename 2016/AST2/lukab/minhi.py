import numpy as np
from scipy import *
import matplotlib.pyplot as plt
xd, yd, sd=np.loadtxt('barometarska.txt', unpack=True)

e = np.exp(1)
a=np.linspace(0.9, 1.7, 300)
b=np.linspace(0.02, 0.08, 300)


hl=[]

for i in range(len(xd)):
	for j in range(len(xd)):
		n=(yd-a[i]*e**(-b[j]*xd))**2/(2*sd**2)
		h=sum(n)
		hl.append(h)

for a, b in enumerate(hl):
	if np.argmin(hl):
		print(i)
		print(j)
