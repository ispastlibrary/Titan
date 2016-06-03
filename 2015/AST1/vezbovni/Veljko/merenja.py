import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

d, v, delv = np.loadtxt('podaci2.txt', unpack=True)

#Sume
#sum_omega = np.sum(omega)
#sum_wy = np.sum(omega*t2)
#sum_wxy = np.sum(omega*l*t2)
#sum_wx = np.sum(omega*l)
#sum_wx2 = np.sum(omega*l**2)
#sum_w2x2 = sum_wx**2
#Sume

#Br = sum_wxy*sum_omega - sum_wy*sum_wx
#Im = sum_omega*sum_wx2 - sum_w2x2

#b = Br/Im
#db = (sum_omega/Im)**1/2

#c = sum_wy/sum_omega
#d = sum_wx/sum_omega

#a = c - b * d

#g = 4* (np.pi)**2/b
#dg = 4*(np.pi)**2 * db

#funkcija


def fun(d , v , delv ):
    return d*v + delv

parametri, cov_m = curve_fit ( fun, d, v, sigma=delv)
greske_parametara = np.sqrt(np.diag(cov_m))

#print('Parametar v je: ', parametri[0], '+/-', greske_parametara[0])
#print('Parametar delv je: ', parametri[1], '+/-', greske parametara[1])

#@x = [1.36E+021, 1.75E+022, 503.05]
#y = fun(d, v, delv)
x = np.linspace(1.36e21, 1.75e22, 100)
y = fun(x, parametri[0], parametri[1])

 
plt.plot(x, y, '-r', label = 'fit')
plt.errorbar(d, v, yerr=delv, fmt=' ')
plt.legend(loc='best')
plt.xlabel('d[km]')
plt.ylabel('V[km/s]')
#plt.xlim([x1,x2])
#plt.ylim([y1,y2])
plt.title('Hablova konstanta')
plt.savefig('hablovakonst.png')
plt.show()
