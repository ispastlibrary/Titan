import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

V, D, dV = np.loadtxt('podaci.txt', unpack = True)


def fucn(x, a, b):
    return x*a + b

parametri, cov_m = curve_fit(fucn, D, V, sigma = dV)

greskepar = np.sqrt(np.diag(cov_m))

print('Parametar a je', parametri[0], '+/-', greskepar[0])
print('Parametar b je', parametri[1], '+/-', greskepar[1])

H=parametri[0]
dH=greskepar[0]
print(H)
t=1/H
T=t/(60*60*24*365.2422)

H1=H*(3e16)
dH1=dH*(3e16)
print('H konstanta je:', H1, '+/-', dH1)

dt=t*dH1/H1

print('starost:', T, '+/-', dt)

x=np.linspace(min(D), max(D), num = 10)
y=fucn(x, parametri[0], parametri[1])

plt.plot(x, y, '-r', label='fit')
plt.errorbar(D, V, yerr=dV, fmt='o')
plt.legend(loc='best')
plt.xlabel('Udaljenost [Mpc]')
plt.ylabel('Brzina [km/s]')
plt.title('Hablova konstanta')
plt.savefig('x.png')
plt.show()


