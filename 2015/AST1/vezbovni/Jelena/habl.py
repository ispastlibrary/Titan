import numpy as np
import matplotlib.pyplot as plt

d, V, dv2, dV = np.loadtxt('merenjahabla.txt', unpack = True)

#dv^2 je reciprocna vrednost od dv^2 
#b brojilac
swxy = np.sum(dv2*d*V)
sw = np.sum(dv2)
swy = np.sum(dv2*V)
swx = np.sum(dv2*d)
somega = np.sum(dv2)

#delta
swx2 = np.sum(dv2 * (d**2))
s2w2x2 = (np.sum(swx))**2
delta = sw * swx2 - s2w2x2

#H
H = (swxy * somega - swy * swx) / delta

#delta H
dH = (sw / delta) ** (1/2) 

#a
a = (swx2 * swy - swx * swxy) / delta

#delta a
da = (swx2 / delta) ** (1/2)


print('Dobijena hablova konstanta je ', H)
print('sa greskom ', dH)

greskey = dV

def lin(x, a, H):
    return a + H * x

x = np.arange(0.4, 1.1, 0.01)
y = lin(x,a,H)

print (x, y)

plt.plot(x, y, '-r', label = 'fit')
plt.errorbar(l,t2,yerr = greskey, fmt = 'o')
plt.legend(loc = 'best')
plt.xlabel('d[km]')
plt.ylabel('V[km/s]0')
plt.title("Grafik zavisnosti V od d")
plt.xlim([0.38, 1.1])
plt.show()
