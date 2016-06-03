#!/usr/bin/env python3
import numpy as np
import math
import pylab as pl

x=np.zeros((3,3))

#zelimo da popunimo matricu nekim brojevima

for i in range(len(x[0])):
    for j in range(len(x[:][2])):
        x[i][j]=i+j**2+1

print(x)

