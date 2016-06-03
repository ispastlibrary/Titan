import numpy as np 
from scipy.optimize import curve_fit 
import matplotlib.pyplot as plt

def fun(x, a, b):
    return a*x + b

d, v, dv = np.loadtxt('podaci.txt', unpack=True)

d = d*3.08567758e19

parametri, cov = curve_fit(fun, d, v, sigma=dv)

greske_parametra = np.sqrt(np.diag(cov))

print('Paremetar a je: ', parametri[0], '+/-', greske_parametra[0])
print('Parametar b je: ', parametri[1], '+/-', greske_parametra[1])

print('starost univerzuma je: ', (1/parametri[0])/(86400*365.2422)) 

x = np.linspace(min(d), max(d), num=100)
y = fun(x, parametri[0], parametri[1])

plt.plot(x, y, '-r', label='fit')
plt.errorbar(d, v, yerr=dv, fmt='o')
plt.legend(loc='best')
plt.xlabel('Udaljenost [MPc]')
plt.ylabel('Brzina [km/s]')
plt.xlim([0*3.08e19,1260*3.08e19])
plt.ylim([1000,65000])
plt.title(['Hablova konstanta'])
plt.savefig('Habl.png')
plt.show()
