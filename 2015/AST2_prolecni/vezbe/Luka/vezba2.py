import numpy as np
import pylab as pl


n = 1000000
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
U = np.arctan2(X,Y)

pl.scatter(X,Y, c=U, alpha=0.9)

pl.xlim(-1.5, 1.5)
pl.ylim(-2.0, 2.0)

pl.xticks(())
pl.yticks(())


pl.show()

