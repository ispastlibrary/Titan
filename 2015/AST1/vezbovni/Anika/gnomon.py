import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

t, l, deltal = np.loadtxt('gnomon.txt', unpack=True)

def fun (x,a,b,c):
    return a*x**2+b*x+c

parametri, cov_m = curve_fit(fun, t, l, sigma = deltal)
greske_parametara = np.sqrt(np.diag(cov_m))

print ('parametar a je: ', parametri[0], '+/-', greske_parametara[0])
print ('parametar b je: ', parametri[1], '+/-', greske_parametara[1])
print ('parametar c je: ', parametri[2], '+/-', greske_parametara[2])

x = np.arange(-60, 60, 5)
y = fun (x, parametri[0], parametri[1], parametri[2])

plt.plot(x, y, '-r', label='fit')
plt.errorbar(t, l, yerr=deltal, fmt='o')
plt.xlabel('t')
plt.ylabel('l')
plt.title('geografska duzina i sirina')
plt.show()


