import pylab as pl
import numpy as np

pl.figure(figsize=(8, 6), dpi=80) 
pl.subplot(1, 1, 1) 
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C = np.cos(x)
S = np.sin(x)

pl.plot(C, color="red")
pl.show()

