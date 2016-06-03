import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, l, deltal = np.loadtxt('podaci3.txt', unpack=True)

def pera(x, a, b, c):
    return a*(x**2) + b*x + c


parametri, cov = curve_fit(pera, t, l, sigma=deltal)

greske=np.sqrt(np.diag(cov))

print(parametri[0], 'greske ', greske[0])
print(parametri[1], 'greske ', greske[1])
print(parametri[2], 'greske ', greske[2])

xo=(-parametri[1])/(2*parametri[0])
print('xo je: ', xo)

yo=parametri[0]*((67.915)**2) + parametri[1]*(67.915)+parametri[2]
print('yo je: ', yo)

x = np.arange(0, 110, 3)
y = pera(x,parametri[0], parametri[1], parametri[2])

plt.plot(x, y, '-r', label='fit')
plt.errorbar(t, l, yerr=deltal, fmt='o')
plt.legend(loc='best')
plt.xlabel('t[min]')
plt.ylabel('l[cm]')
plt.title('Gnomon')
plt.show()


