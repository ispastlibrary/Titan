import numpy as np
import matplotlib.pylab as plt

import numpy
from matplotlib import pylab

nx = 360
ny = 360
dem1 = np.random.rand(nx,ny)
#dem1 = numpy.random.rand(nx,ny)

#pylab.imshow(dem1)
#pylab.show()

sizex = 30
sizey = 10

x, y = np.mgrid[-sizex:sizex+1, -sizey:sizey+1]
g = np.exp(-0.333*(x**2/float(sizex)+y**2/float(sizey)))
filter = g/g.sum()

plt.imshow(filter)
plt.show()
