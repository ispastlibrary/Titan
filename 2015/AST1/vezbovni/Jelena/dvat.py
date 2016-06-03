import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x,y,m,vx,vy = np.loadtxt('Koordinate_SS.txt', unpack = True)

r1x = x[0]
r1y = y[0]
r2x = x[2]
r2y = y[2]
m1 = m[0]
m2 = m[2]
v1x = vx[0]
v1y = vy[0]
v2x = vx[0]
v2y = vy[0]


