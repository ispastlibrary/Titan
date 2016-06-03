#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
#importovati podatke i plotovati
#kod ima grske, potrebno je debagovati

x,y = np.loadtxt('NUM_PS_2_Podaci.txt', unpack=True)

x=x-x[0]

plt.plot(x,y,'-g', label='ime_linije')
plt.xscale('log')
plt.title('ime')
plt.show()
