import numpy as np
import matplotlib.pyplot as plt

d, V, wi, deltav = np.loadtxt('podaci2.txt', unpack=True)

sum_wi = np.sum(wi)

sum_wy = np.sum(wi*V)

sum_wx = np.sum(wi*d)

sum_wxy = np.sum(wi*d*V)

sum_wx2 = np.sum(wi*d*d)

b = (sum_wxy*sum_wi-sum_wy*sum_wx)/(sum_wi*sum_wx2-(sum_wx)**2)
print('Hablova konst JE: ', b)

deltab = (sum_wi/(sum_wi*sum_wx2-(sum_wx)**2))**.5
print('deltab je: ', deltab)

t=(1/b)*3.09e19
print('Starost univerzuma je: ', (t)/(3600*24*365*(10**9)))

deltat = (t*(deltab/b))/(3600*24*365*(10**9))
print('Greska za t', deltat)

deltab = (sum_wi/(sum_wi*sum_wx2-(sum_wx)**2))**.5
print('deltab je: ', deltab)

a = sum_wy/sum_wi-b*(sum_wx/sum_wi)

#g=(4*(np.pi)**2)/b
#print('g je: ', g)

#deltag = g*deltab/b**2
#print('deltag je: ', deltag)

def fun(x, a, b):
    return a+b*x
x = np.arange(45, 1150, 20)
y = fun(x, a, b) 

print(a)
print(b)
plt.plot(x, y, '-r', label='fit')
plt.errorbar(d, V, yerr=deltav, fmt='o')
plt.legend(loc='best')
plt.xlabel('d[MPc]')
plt.ylabel('V[km/s]')
plt.title('Starost univerzuma')
plt.show()
