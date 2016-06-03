import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

l, V, dV = np.loadtxt('merenja.txt', unpack = True)

def func(x, a, b):
    return x*a + b

parametri, cov_m = curve_fit(func, l, V,sigma = dV)

greske_parametara = np.sqrt(np.diag(cov_m))

print('Parametar a je: ', parametri[0], '+/-', greske_parametara[0])
print('Parametrar b je: ', parametri[1], '+/-', greske_parametara[1])

H=parametri[0]
dH=greske_parametara[0]
print(H)
t=1/H
t=t/(60*60*24*365.2422)

H1=H*3.085e19
dH1=dH*3.085e19
print("habl je ", H1, '+/-', dH1)

dt=t*dH1/H1

print("starost je:", t, "+/-", dt)

x=np.arange(7e20, 2e22, 1e20)
y=func(x, parametri[0], parametri[1])

plt.plot(x, y, '-r', label='fit')
plt.errorbar(l, V, yerr=dV, fmt='o')
plt.legend(loc = 'best')
plt.xlabel('l[km]')
plt.ylabel('v[km/s]')
plt.ylim([0, 65000])
plt.title('Zavisnost radijalne brzine od udaljenosti')
plt.savefig('vezba_2_sa_tackom.png')
plt.show()
