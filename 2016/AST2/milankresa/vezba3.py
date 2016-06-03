import numpy as np
import pylab as pl

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

pl.bar(X, +Y1, facecolor="red", edgecolor="white", alpha=0.5)
pl.bar(X, -Y2, facecolor="blue", edgecolor="white", alpha=0.5)

for x, y in zip(X, Y1):
    pl.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    pl.text(x + 0.4, - y - 0.01, '%.2f' % y, ha='center', va='top')

pl.xlim(-0.2, n)
pl.ylim(-1.25, +1.25)

pl.show()
