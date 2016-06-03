import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

distance, velocity, greske_v = np.loadtxt('data2.txt', unpack=True)

def func(x, a, b):
    return x*a + b

parametri, cov_m = curve_fit(func, distance, velocity, sigma=greske_v)
greske_parametara = np.sqrt(np.diag(cov_m))

print(parametri[0], greske_parametara[0]) # a i greska a - ovo je H
print(parametri[1], greske_parametara[1]) # b i greska b
print('Starost univerzuma: ', 1/parametri[0])

modelirano_x = np.array(np.linspace(distance[0], distance[len(distance)-1], num = 10))
modelirano_y = func(modelirano_x, parametri[0], parametri[1])

plt.plot(modelirano_x, modelirano_y, '-r', label='fit')

plt.errorbar(distance, velocity, yerr=greske_v, fmt='o')
plt.legend('best')
plt.xlabel('D [Mpc]')
plt.ylabel('Vrad [km/s]')
plt.xlim([25, 1500])
plt.ylim([3000, 64000])
plt.title('Hablov zakon')
plt.savefig('habl.png')
plt.show()

