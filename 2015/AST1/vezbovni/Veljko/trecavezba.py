import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt



t, l, dell = np.loadtxt('parametritrecavezba.txt', unpack=True)

def fun(x, a, b, c):
    return a*x**2 + b*x + c

parametri, cov_m = curve_fit(fun, t, l,sigma=dell)

greske_parametara = np.sqrt(np.diag(cov_m))

print('Parametar a je: ', parametri[0], '+/-', greske_parametara[0])
print('Parametar b je: ', parametri [1], '+/-', greske_parametara[1])
print('Parametar c je: ', parametri [2], '+/-', greske_parametara[2])

x = np.arange(-80, 55, 5)
xo = -parametri[1]/(2*parametri[0])

t=t-xo

print(xo)
par1, cov1 =curve_fit(fun, t, l, sigma=dell)
g1=np.sqrt(np.diag(cov1))

print(xo)
y = fun(x, par1[0], par1[1], par1[2])

print(par1)
print(g1)

plt.plot(x, y, '-r', label = 'fit')
plt.errorbar(t, l, yerr=dell, fmt='o')
plt.legend(loc='best')
plt.xlabel('Vreme[min]')
plt.ylabel('Duzina[mm]')
plt.title('Geografska sirina i duzina')
plt.show()


