import numpy as np
import matplotlib.pyplot as plt

l, t2, omega, dt2 = np.loadtxt('merenja.txt', unpack = True)

#b brojilac
swxy = np.sum(omega*l*t2)
sw = np.sum(omega)
swy = np.sum(omega*t2)
swx = np.sum(omega*l)
somega = np.sum(omega)

#delta
swx2 = np.sum(omega * (l**2))
s2w2x2 = (np.sum(swx))**2
delta = sw * swx2 - s2w2x2

#b
b = (swxy * somega - swy * swx) / delta

#delta b
db = (sw / delta) ** (1/2) 

#a
a = (swx2 * swy - swx * swxy) / delta

#delta a
da = (swx2 / delta) ** (1/2)

#g
g = 4 * (np.pi ** 2) / b
  
#delta g
dg = g * db / b

print(g)
print(dg)

greskey = dt2

def lin(x, a, b):
    return a + b * x

x = np.arange(0.4, 1.1, 0.01)
y = lin(x,a,b)

print (x, y)

plt.plot(x, y, '-r', label = 'fit')
plt.errorbar(l,t2,yerr = greskey, fmt = 'o')
plt.legend(loc = 'best')
plt.xlabel('l[m]')
plt.ylabel('T^2[s^2]')
plt.title("Grafik zavisnosti T^2 od l")
plt.xlim([0.38, 1.1])
plt.show()
