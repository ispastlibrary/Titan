import matplotlib.pyplot as plt
import numpy as np
from  scipy.interpolate import interp1d
t, x, y, z= np.loadtxt('mars.dat', unpack=True, delimiter=',')

r = np.sqrt(x**2+y**2+z**2)
T=max(t)
T=T/365
a=np.power(T**2,1/3)
Rp=min(r)

e=1-Rp/a

print(e)

