import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def func(x, a, b, c):
    return a*x**2 + b*x + c

t, l, dl = np.loadtxt('podaci3.txt', unpack=True)

t=t-t[0]
t=t*60

print(t)

par, cov_m = curve_fit(func, t, l, sigma=dl)
dpar = np.sqrt(np.diag(cov_m))

print(par[0], dpar[0])
print(par[1], dpar[1])
print(par[2], dpar[2])


#modelirano_x = np.arange(t[0], t[len(t) - 1], 0.1)
#modelirano_y = func(modelirano_x, parametri[0], parametri[1], parametri[2])

#plt.plot(modelirano_x, modelirano_y, '-r', label='fit')
#plt.errorbar(t, l, yerr=dl, fmt='o')
#plt.xlabel('t[h]')
#plt.ylabel('l[mm]')
#plt.xlim([11.5, 13.5])
#plt.ylim([70, 97])
#plt.savefig('gn.png')
#plt.show()
