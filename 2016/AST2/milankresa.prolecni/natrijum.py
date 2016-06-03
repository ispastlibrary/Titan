import math
import numpy as np

Roj = 0.6e+3
T = 350
Rj = 8e+3
M = 23e-3
Na = 6.024e+23

N = (Roj*4*Rj**3*np.pi*3.34e-5*Na)/(3*M)

Nh = (((4*Rj**3*np.pi)/3)/22.4e-3)*Na

print(N, Nh)
