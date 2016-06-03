import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
t , l , dl=np.loadtxt('merenja3.txt' , unpack=True)

def fun(x,a,b,c):
    return a*x*x+b*x+c

parametri, cov=curve_fit(fun, t, l , sigma=dl)
greske_parametara=np.sqrt(np.diag(cov))

print('Parametar a je:', parametri[0],'+/-', greske_parametara[0])
#ovo nula mi je prvi clan svih parametara, dakle a
print('parametar be je:', parametri[1], '+/-', greske_parametara[1])
print('Parametar c je:', parametri[2], '+/-', greske_parametara[2])
x0=-parametri[1]/(2*parametri[0])
apsx0=-x0
dx=(greske_parametara[1]/parametri[1]+greske_parametara[0]/parametri[0])*apsx0/2
h=np.arctan(0.185/parametri[2])*180/np.pi
lam=(14-(x0+700)/60)*15-30.5/60
dlam=(greske_parametara[1]/(2*parametri[0])+(parametri[1]*greske_parametara[0]/(2*parametri[0]**2)))/4
fi = 90+22.2-h
print(lam)
print(dlam)
print('najkraca duzina senke gnomona', x0,'+/-', dx)
#print(dfi,'dasklfjas;ldkfhas;dkfhaspdlkfahso;jdfh')
#print(x0, 'ovo uzmi!!!')
#print('h je', h)
#print('Geografska sirina je: ', fi,'.')
#print('Geografska duzina je', lam, '+/-', dlam,'.')
t=t-x0
#print(x0, 'ovo je x0')

par1, cov1=curve_fit(fun, t, l , sigma=dl)
g1=np.sqrt(np.diag(cov1))

x1=np.arange(-65, 60, 2)
y1=fun(x1,par1[0],par1[1],par1[2])
plt.plot(x1, y1 , '-r', label='fit')
plt.errorbar(t ,l ,dl , fmt='o')
plt.legend(loc='best')
plt.xlabel('t[min]')
plt.ylabel('l[m]')
plt.xlim([-65,50])
plt.title('Grafik zavisnosti duzine senke od vremena')
plt.show()





