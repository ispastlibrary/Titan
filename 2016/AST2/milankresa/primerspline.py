import numpy as np
from scipy import interpolate
from scipy import integrate
import math

x = linspace(0, 10, 10)
y = sin(x)
tck = splrep(x,y)
x2 = linspace(0, 10, 200)
y2 = splev(x2, tck)
plot(x,y,'o', x2, y2)
