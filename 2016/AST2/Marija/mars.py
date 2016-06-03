import matplotlib.pyplot as plt
import numpy as np
from  scipy.interpolate import interp1d
t, x, y, z= np.loadtxt('mars.dat', unpack=True, delimiter=',')

r = np.sqrt(x**2+y**2+z**2)
maks=max(z)

i=np.argmax(z)

b=np.arcsin(z[i]/r[i])
a=(b*360)/(2*np.pi)
print(a)
perihel=np.argmin(r)
afel=np.argmax(r)
#plt.plot(t,r)
#plt.show()

#print(perihel,afel, t[perihel],t[afel])
dt=1e-6

f1=interp1d([t[perihel],t[perihel+1]], [x[perihel],x[perihel+1]])
x1=(f1(t[perihel]+dt)-x[perihel])/dt 
#izvod smo definisali kao (f(x+dx)-f(x))/ dx
#Nama je "x" iz jednacine zapravo vreme (t), a f(x) nam je rastojanje,
#Zato sto nam rastojanje zavisi od vremena
#sto znaci da umesto t treba da se pise koordinata gde oduzimas t[perihel]
#tu treba da stoji x[perihel] zato sto je to vrednost funkcije

#ako sam ovo nejasno objasnio, cimaj me da ti objasnim lepo
#(bas mi se spava)

f2=interp1d([t[perihel],t[perihel+1]], [y[perihel],y[perihel+1]])
y1=(f2(t[perihel]+dt)-y[perihel])/dt

#ovde ces imati -y[perihel]

f3=interp1d([t[perihel],t[perihel+1]], [z[perihel],z[perihel+1]])
z1=(f3(t[perihel]+dt)-z[perihel])/dt


v=np.sqrt(x1**2+y1**2+z1**2)*150000000/86400

print(v)

