import numpy as np
import matplotlib.pylab as plt
from scipy import signal

nx = 360
ny = 360
dem1 = np.random.rand(nx,ny)
#dem1 = numpy.random.rand(nx,ny)

#pylab.imshow(dem1)
#pylab.show()

# cobe
sizex = 60
sizey = 20

# wmap
sizex = 6
sizey = 2

# planck
sizex = 0.6
sizey = 0.2

x, y = np.mgrid[-sizex:sizex+1, -sizey:sizey+1]
g = np.exp(-0.333*(x**2/float(sizex)+y**2/float(sizey)))
filter = g/g.sum()

demSmooth = signal.convolve(dem1,filter,mode='valid')
demSmooth = (demSmooth - demSmooth.min()) / (demSmooth.max() - demSmooth.min())

print(dem1.shape)
print(demSmooth.shape)

plt.imshow(demSmooth)
plt.show()
