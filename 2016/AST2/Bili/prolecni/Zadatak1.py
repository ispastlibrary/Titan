import math as math
import pylab as pl
import numpy as np

G = 1
A = 1.21
L = 1
Z = 6e+6
Ro = 0.122
M = 0.029
g = 9.81
R = 8.314
T = 200

zr = np.pi/4 #degrees
ho = 2e+5 #km
vo = 4e+4 #m/s
mo = 1e-5 #kg
Rm = 3000 #kg/m3

intezitet = [0]
vreme = [0]

#print(round(math.sin(math.radians(30)),2))Za uglove

def brzinabi(v1,t):
    brzina=-(G*A*m1**(-1/3)*(Rm**(-2/3))*Ra*(v1**2))
    return brzina

def brzinaRunge(v0,t0,dt):
    k1=brzinabi(v0,t0)
    k2=brzinabi(v0+k1/2,t0+dt/2)
    k3=brzinabi(v0+k2/2,t0+dt/2)
    k4=brzinabi(v0+k3,t0+dt)
    v1=v0+(k1+2*k2+2*k3+k4)/6
    return v1

def masabi(m1,t):
    masa=-(L*A*math.pow(m1,2/3)*math.pow(Rm,-2/3)*v1*v1*v1*Ra)/(2*Z)
    return masa

def masaRunge(m0,t0,dt):
    k1=masabi(m0,t0)
    k2=masabi(m0+k1/2,t0+dt/2)
    k3=masabi(m0+k2/2,t0+dt/2)
    k4=masabi(m0+k3,t0+dt)
    m1=m0+(k1+2*k2+2*k3+k4)/6
    return m1

#def koef_sjaja(v):  #tu kasnije ide v1
#   if (v<=16000): tau = 6.04e-4*((v/1000)-8.8)**(-0.35)
#    else:  tau = 0.024*((v/1000)+8.8)**(-1)
#    return tau

def visinabi(v1):
    visina = ho - v1*zr*dt
    return visina

def ro_atmo(h1):
    Ra=Ro*math.exp(-(M*g*h1)/(R*T))
    return Ra

#def magn_app(I, d):
#    Mapp =-14.8-2.5*math.log((683*I)/(4*np.pi*(d**2)),10)
#    return Mapp

#def inte_zra(m, v, h):
#    inte = -koef_sjaja(v)*(1/2)*v**2*masabi(m,t)
#    return inte

#def udaljenost_posma(h):
#    d = h/round(math.cos(math.radians(zr)),2)
#    return d
    

m1 = mo
v1 = vo
h1 = ho
t1 = 0
dt = 0.1
d = 282885.43
#tau = 4.918e-4

while (m1>mo/1000):
    print(m1,v1)
    #tau = koef_sjaja(v1)
    Ra = ro_atmo(h1)
    #I = inte_zra(m1, v1, h1)
    #intezitet.append(I)
    #Mapp = magn_app(I,d)
    v2 = brzinaRunge(v1,t1,dt)
    m2 = masaRunge(m1,t1,dt)
    h2=visinabi(v1)
    t1=t1+dt
    vreme.append(t1)
    #d = udaljenost_posma(h1)
    m1=m2
    v1=v2
    h1=h2 #Udaljenost od posmatraca

#pl.plot(intezitet, vreme, 'ro')
pl.show()
