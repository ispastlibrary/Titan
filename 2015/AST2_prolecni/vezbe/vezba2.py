import numpy as np
import pylab as pl

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
U = np.arctan2(Y, X)

pl.scatter(X,Y, s=50, c=U, alpha=0.7)

pl.xlim(-1.5, 1.5)
pl.ylim(-2.0, 2.0)

pl.xticks(())
pl.yticks(())



pl.show()
