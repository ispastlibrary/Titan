import matplotlib.pyplot as plt
import numpy as np
from  scipy.interpolate import interp1d
t, x, y, z= np.loadtxt('mars.dat', unpack=True, delimiter=',')

r = np.sqrt(x**2+y**2+z**2)

a=np.argmax(r)
neg=np.extract(z<0,z)
p=np.argmax(neg)
b=np.flatnonzero(z==neg[p])
c=max(t)
t=c-(t[b+1]-t[a])
print(t[0])

