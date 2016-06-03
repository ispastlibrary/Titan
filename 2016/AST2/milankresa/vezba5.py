import numpy as np
import pylab as pl

def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

n = 10
x = np.linspace(-3, 3, 4 * n)
y = np.linspace(-3, 3, 3 * n)
X, Y = np.meshgrid(x, y)
pl.imshow(f(X, Y), interpolation='nearest', cmap='bone', alpha=0.75)

pl.colorbar(shrink=0.90)
pl.xticks(())
pl.yticks(())

pl.show()
