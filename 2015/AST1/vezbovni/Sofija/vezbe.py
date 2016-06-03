import numpy as np
l, T2, omega, dT2 = np.loadtxt('merenja.txt', unpack=True)

sum_w=np.sum(omega)

sum_wy = np.sum(omega*T2)

sum_wx = np.sum(omega*l)

sum_wxy = np.sum(omega*l*T2)

sum_wx2 = np.sum(omega*l*l)

d = sum_wx**2

brojilac = sum_wxy * sum_w - sum_wy * sum_wx
imenilac = sum_w * sum_wx2 - d

b = brojilac/imenilac
db = (sum_w/imenilac)**1/2

a = (sum_wy/sum_w) - b*sum_wx/sum_w
da = (sum_wx2/imenilac)**1/2 

g = 4 * (np.pi)**2 / b
dg = 4 * (np.pi)**2 * db

print(b)
print (g)
print (dg)
print (a)


import matplotlib.pyplot as plt

def fun(x, a, b):
    return a + b*x

x=np.arange(0.5, 1.2, 0.01)
y=fun(x, a, b)

plt.plot(x,y , '-r', label='fit')
plt.errorbar(l,T2, yerr=dT2, fmt='o')
plt.legend(loc='best')
plt.xlabel('l[m]')
plt.ylabel('T2[s^2]')
plt.title('Zavisnost kvadrata perioda matematickog klatna od duzine')
plt.show()


