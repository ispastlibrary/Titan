import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
t, l, dl = np.loadtxt('gnomon.txt' , unpack=True)
def func(x, a, b, c):
    return a*x**2 + b*x + c

t = t - 67.71942158

parametri, cov_m = curve_fit(func, t, l, sigma=dl)

greske_parametara = np.sqrt(np.diag(cov_m))

print('Parametar a je:' , parametri[0], '+/-', greske_parametara[0])
print('Parametar b je:' , parametri[1], '+/-', greske_parametara[1])
print('Parametar c je:' , parametri[2], '+/-', greske_parametara[2])

x0 = -parametri[1]/(2*parametri[0])
print(x0)
mod_t =np.arange(-100, 100, 5)
mod_l =func(mod_t, parametri[0], parametri[1], parametri[2]) 

dx=1/(2*parametri[0])*greske_parametara[1]+1/(2*parametri[0]**2)*parametri[1]*greske_parametara[0]
print(dx)

plt.plot(mod_t, mod_l, '-r', label='fit')
plt.errorbar(t,l,yerr=dl, fmt='o')
plt.legend(loc='best')
plt.xlabel('t[min]')
plt.ylabel('l[mm]')
#plt.xlim([0, 120])
#plt.ylim([0, 100])
plt.title('Zavisnost dužine senke od vremena')
plt.savefig('gnomon.png')
plt.show()

