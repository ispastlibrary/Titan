import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
t, l, dl  = np.loadtxt('gpodaci.txt', unpack = True)

def fun(x,a,b,c):
   return (a*(x**2) + b*x + c)

par, cov_m = curve_fit(fun, t, l, sigma=dl)
greske_par=np.sqrt(np.diag(cov_m))

print('parametar a je:', par[0], '+/-', greske_par[0])
print('parametar b je:', par[1], '+/-', greske_par[1])
print('parametar c je:', par[2], '+/-', greske_par[2])

x= np.arange(11.5, 13.5, 0.1)
y=fun(x, par[0], par[1], par[2])
greskey=dl
x0=-par[1]/(2*par[0])
print(x0)

t=t-x0

par1, cov1 = curve_fit(fun, t, l, sigma=dl)
g1=np.sqrt(np.diag(cov1))

x1=np.arange(-1, 1, 0.01)
y1=fun(x1, par1[0], par1[1], par1[2])

print('parametar a1 je:', par1[0], '+/-', g1[0])
print('parametar b1 je:', par1[1], '+/-', g1[1])
print('parametar c1 je:', par1[2], '+/-', g1[2])


plt.plot(x1, y1, '-r', label='Fit')
plt.errorbar(t,l, yerr=greskey, fmt=' ')
plt.legend(loc='best')
plt.xlabel('t[h]')
plt.ylabel('l[cm]')
plt.title('Zavisnost duzine senke od vremena')
plt.show()

