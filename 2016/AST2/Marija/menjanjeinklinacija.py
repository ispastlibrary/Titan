import matplotlib.pyplot as plt
import numpy as np
from  scipy.interpolate import interp1d
t, x, y, z= np.loadtxt('mars.dat', unpack=True, delimiter=',')

r = np.sqrt(x**2+y**2+z**2)
b = np.arcsin(z/r)
plt.plot(t,b)
plt.show()

