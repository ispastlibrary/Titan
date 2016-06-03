import pylab as pl
import numpy as np

pl.figure(figsize=(8, 6), dpi=80)

pl.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C = np.cos(X)
S = np.sin(X)

pl.plot(X, C, color="red", linewidth=1.0, linestyle="-")
pl.plot(X, S, color="purple", linewidth=1.0, linestyle="-")

pl.xlim(-4.0, 4.0)
pl.ylim(-1.0, 1.0)

pl.xticks(np.linspace(-4, 4, 2, endpoint=True))
pl.yticks(np.linspace(-1, 1, 4, endpoint=True))

pl.show()
