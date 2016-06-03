import numpy as np
import matplotlib.pyplot as plt

x0 = np.arange(0, np.pi *4, 0.3)
dx = 0.3
y0 = np.zeros(len(x0))
y0[0] = 0
suma = 0

for i in range(1, len(x0)):
    y0[i] = y0[i-1] - dx * np.cos(x0[i])
    suma += -np.cos(x0[i])

k0 = suma/(len(x0)-1)

x1 = np.arange(0.3, np.pi *4, 0.3)
y1 = np.zeros(len(x1))
y1[0] = k0*dx
sum = 0

for i in range(1, len(x1)):
    y1[i] = y1[i-1] - dx * np.cos(x1[i]) 
    sum += -np.cos(x1[i])

k1 = sum/(len(x1)-1)

y2 = np.zeros(len(x0))
y2[0] = 0
k2 = 1/2 * (k1+k0)

for i in range(1, len(x0)):
    y2[i] = y2[i-1] + k2 * dx

plt.plot(x0, y2, '-b', label = 'fit')
plt.show()



