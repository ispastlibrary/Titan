import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

d, v, dv = np.loadtxt('hablov_zakon.dat', unpack = True)

def f(x, a, b):
    return a*x + b

h, cov_m = curve_fit(f, d, v, sigma = dv)

a = h[0]
b = h[1]

print(a, 'habl')

plt.plot(d, f(d, a, b), '-r', label = 'habl')
plt.errorbar(d, f(d, a, b), yerr = dv, fmt = 'o')
plt.show()
