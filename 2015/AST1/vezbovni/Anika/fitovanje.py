import numpy as np
import matplotlib.pyplot as plt

d, V, 1/dv2, deltaV = np.loadtxt('', unpack=True)
# 1/dv2 je 1/delta od t na kvadrat

Somxy = np.sum(om * d * V) # suma om xy
Som = np.sum(om) # suma omega
Somy = np.sum(om * V) # suma omega*y
Somx = np.sum(om*d) #suma omega*x
Somx2= np.sum(om*(d**2)) #suma omega*x2
Somxkv = Somx**2
Sx= np.sum(d)
Sy= np.sum(V)


b = (Somxy*Som-Somy*Somx)/(Som*Somx2-Somxkv)
deltaBkv = np.sqrt(Som/(Som*Somx2-Somxkv))

print(b)
print(deltaBkv)

g = 4*(np.pi**2)/b
dg = deltaBkv*g/b


print(g)
print(dg)

a= Sx/Som-b*Sy/Som
deltaakv= (np.sqrt(Somx2/(Som*Somx2-Somxkv)))

print(a)
print(deltaakv)


def lin(x, a, b):
    return a + b*x

x = np.arange(d[len(d)-1], d[0], 0.01)
y = lin(x, a, b)

plt.plot(x, y, '-r', label='fit')
plt.errorbar(d, t2, yerr = deltaV, fmt='o')
plt.legend(loc = 'best')
plt.xlabel('d [km]')
plt.ylabel('V[km/s]')
plt.title('Hablova konstanta')
plt.show()

