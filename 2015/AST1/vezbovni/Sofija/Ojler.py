Ximport numpy as np
import matplotlib.pyplot as plt

y0 = 0
x0 = 0
dx = 0.3
k = -1
n = 17

xn = []
yn = []

def fun(x, y):
    k = -np.cos(x)
    y = y + k * dx
    return y

x = x0
y = y0
xn.append(x)
yn.append(y)

for i in range(n):
    y = fun(x,y)
    yn.append(y)
    x = x + dx
    xn.append(x)

def fun2(y0, x0, k):
    return y0 + k * dx
      

plt.plot(xn, yn)
plt.show()
