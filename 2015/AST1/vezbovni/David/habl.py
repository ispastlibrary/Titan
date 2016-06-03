import numpy as np
#import matplot.pyplot as plt

d, V, wi, deltav = np.loadtxt(habl.txt, unpac=True)

sum_wi = np.sum(wi)

sum_wy = np.sum()

sum_wx = np.sum()

sum_wxy = np.sum(wi*d*V)

sum_wx2 = no.sum(wi*d*d)

b = (sum_wxy * sum_wi -sum_wy * sum_wx) / (sum_wi * sum_wx2 - (sum_wx)**2)
print(b)
