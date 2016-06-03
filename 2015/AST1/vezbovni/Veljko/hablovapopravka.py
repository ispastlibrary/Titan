import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
xdata, ydata, greskey = np.loadtxt('hablovapopravka.txt', unpack = True)
def fun(x, a, b):
    return x * a + b

parametri, cov_m = curve_fit(fun, xdata, ydata, sigma = greskey)
greskep = np.sqrt(np.diag(cov_m))

print(parametri[0])

mx = np.arange(1e21, 9e22, 0.5e21)
my = fun(mx, parametri[0], parametri[1])

plt.plot(mx, my, '-r', label = 'fit')
plt.errorbar(xdata, ydata, yerr = greskey, fmt = 'o')
plt.legend(loc='best')
plt.xlabel('X - OSA')
plt.ylabel('Y - OSA')
plt.xlim(0.9e21,2.5e22)
plt.ylim(0, 63000)
plt.title('Zavisnost udaljenosti od brzine')
plt.savefig('Habl.png')
plt.show()




