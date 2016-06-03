import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

d, v, dv = np.loadtxt('habl.txt', unpack=True)

def fun(x, a, b):
    return x*a + b

parametri, cov_m = curve_fit(fun, d, v, sigma = dv)
greske_parametra = np.sqrt(np.diag(cov_m))
print('parametar a je: ', parametri[0], '+/-', greske_parametra[0])
print('parametar b je: ', parametri[1], '+/-', greske_parametra[1])
print('starost_svemira je', ((1/parametri[0])*10**6*206265*150*10**6)/(86400*365.2422))

x=np.linspace(40, 1200, num = 100)
y=fun(x, parametri[0], parametri[1])

plt.plot(x, y, '-r', label='fit')
plt.errorbar(d, v, dv, fmt=' ')
plt.legend(loc='best')
plt.xlabel('d')
plt.ylabel('v')
plt.xlim(0, 1200)
plt.ylim(500, 63000)
plt.title('Hablova konstanta')
plt.show()
