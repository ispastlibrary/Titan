import numpy as np
import matplotlib.pyplot as plt

l, T2, omega, greska = np.loadtxt('podaci.txt', unpack=True)

sum_w = np.sum(omega)
sum_wy = np.sum(omega*T2)
sum_wxy = np.sum(omega*T2*l)
sum_wx = np.sum(omega*l)
sum_wx2 = np.sum(omega*l*l)
sum_w2x2 = np.sum(omega*l)**2

b=(sum_wxy*sum_w-sum_wx*sum_wy) / (sum_w*sum_wx2-sum_w2x2)

print(b)

deltab = np.sqrt(sum_w/(sum_w*sum_wx2-sum_w2x2))

print(deltab)

g = 4*np.pi**2/b
 
print(g)

deltag = deltab*g/b

print(deltag)

a = sum_wy/sum_w-b*sum_wx/sum_w

print(a)

deltaa = np.sqrt(sum_wx2/(sum_w*sum_wx2-sum_w2x2))

print(deltaa)

def lin(l, a, b):
    return a+b*l 

x = np.arange(0.3, 1.1, 0.01)
y = lin(x, a, b)


plt.plot(x,y, '-r', label='fit')
plt.errorbar(l, T2, yerr=greska, fmt='o')
plt.xlim([0.2,1.2])
plt.legend(loc='best')
plt.xlabel('L-osa [m]')
plt.ylabel('T^2-osa [s^2]')
plt.title('Matematicko klatno')
plt.show()

