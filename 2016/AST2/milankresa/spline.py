import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy import integrate
k = np.inf

file = np.loadtxt('podaci.txt')
tal = file[:,0]
inte = file[:,1] 

spl = InterpolatedUnivariateSpline(tal, inte, k=3)
spl.set_smoothing_factor(0.1)
xs = file[:,0]
ys = spl(xs)
plt.plot(tal, inte, '.-')
plt.plot(xs, ys)
plt.show()

print (spl.integral(0, np.inf))
