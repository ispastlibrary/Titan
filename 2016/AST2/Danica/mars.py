import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
t,x,y,z=np.loadtxt('mars.dat', unpack=True, delimiter=',')

intenzitetr=np.sqrt(x**2+y**2+z**2)
inklinacija=np.arcsin(z/intenzitetr)
plt.plot(t, inklinacija)
plt.xlabel('t')
plt.ylabel('i')
#plt.show()
#print(max(inklinacija*(180/np.pi)))
per=max(intenzitetr)
af=min(intenzitetr)
#print(per,af)
i=np.argmax(intenzitetr)
print(t[i])
j=np.argmin(intenzitetr)
print(t[j])
dt=1e-6
f_po_x=interp1d([t[i],t[i+1]], [x[i],x[i+1]])
f_po_y=interp1d([t[i],t[i+1]], [y[i],y[i+1]])
f_po_z=interp1d([t[i],t[i+1]], [z[i],z[i+1]])
x1=(f_po_x(t[i+dt]-t[i])/dt #problem je u ovoj liniji zato sto pozivas funkciju u i+dt, i ti je inteks kada je perihelu. sto znaci da je
#vreme u tom trenutku t[i].
#Takodje, problem je isto u tome sto na granicama ova funkcija pobesni.
#a to se resava tako sto ne pozivas f_po_x(t[i]) vec samo kazes t[i] zato sto su u principu to iste vrednosti
y1=(f_po_y(t[i+dt]-t[i])/dt
z1=(f_po_z(t[i+dt)-t[i])/dt
V=np.sqrt(x1**2+y1**2+z1**2)
print(V)

