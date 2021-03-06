import numpy as np
import pylab as pl
n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

pl.plot(X, Y + 1, color='red', alpha=1.00)
pl.plot(X, Y - 1, color='blue', alpha=1.00)
pl.show()
