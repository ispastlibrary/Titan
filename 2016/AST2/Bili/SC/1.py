import matplotlib.pyplot as plt
import numpy as np

I=np.loadtxt('nesto.txt',unpack=True)
plt.figure(1)
plt.hist(I, bins=100)

b=np.reshape(I,[1024,1024])
plt.figure(2) #pravi matricu 1024x1024
plt.imshow(b,cmap='hot')
plt.colorbar()  #log skala
plt.show()
