import math as math
import pylab as pl
import numpy as np

#Početne konstante
G = 1
A = 1.21
L = 1
Z = 6e+6
Ro = 0.122
M = 0.029
g = 9.81
R = 8.314
T = 200

zr = 45 #degrees
ho = 2e+5 #km
vo = 4e+4 #m/s
mo = 1e-5 #kg
Rm = 3000 #kg/m3

intezitet = []
vreme = [0]

#print(round(math.sin(math.radians(30)),2))Za uglove

def brzinabi(t,v):
    brzina=-(G*A*m**(-1/3)*Rm**(-2/3)*Ra*v**2)
    return brzina

def brzinaRunge(t0,v0,dt):
    k1=dt*brzinabi(t0,v0)
    k2=dt*brzinabi(t0+dt/2,v0+k1/2)
    k3=dt*brzinabi(t0+dt/2,v0+k2/2)
    k4=dt*brzinabi(t0+dt,v0+k3)
    v1=v0+(k1+2*k2+2*k3+k4)/6	
    return v1

def masabi(t,m):
    masa=-(L*A*m**(2/3)*Rm**(-2/3)*v*v*v*Ra)/(2*Z)
    return masa

def masaRunge(t0,m0,dt):
    k1=dt*masabi(t0,m0)
    k2=dt*masabi(t0+dt/2,m0+k1/2)
    k3=dt*masabi(t0+dt/2,m0+k2/2)
    k4=dt*masabi(t0+dt,m0+k3)
    m1=m0+(k1+2*k2+2*k3+k4)/6	
    return m1

def koef_sjaja(v):  #tu kasnije ide v1
    if (v<=16000): koef_sja = 6.04e-4*((v/1000)-8.8)**(-0.35)
    else:  koef_sja = 0.024*((v/1000)+8.8)**(-1)
    return koef_sja

def visinabi(v,dt):
    visina = h - v*round(math.cos(math.radians(zr)),2)*dt
    return visina

def ro_atmo(h):
    Ra=Ro*math.exp(-(M*g*h)/(R*T))
    return Ra

def magn_app(I, d):
    Mapp =-14.8-2.5*math.log((683*I)/(4*3.14*(d**2)),10)
    return Mapp

def inte_zra(m, v, h):
    inte = ((tau*L*A)/(4*Z))*m**(2/3)*Rm**(-2/3)*ro_atmo(h)*v**5
    return inte

def udaljenost_posma(h):
    d = h/round(math.cos(math.radians(zr)),2)
    return d
    

m = mo
v = vo
h = ho
t = 0.001
dt = 0.001
d = 282885.43
tau = koef_sjaja(v)  #4.918e-4
Ra = ro_atmo(h)

I=inte_zra(m,v,h)
intezitet.append(I)

while (m > mo/1000):
    Ra = ro_atmo(h)
    m1=masaRunge(t,m,dt)
    v1=brzinaRunge(t,v,dt)  
    h1=visinabi(v,dt)          
    tau = koef_sjaja(v1)
    I=inte_zra(m1,v1,h1)   
    intezitet.append(I)
    m=m1
    v=v1    
    h=h1
    t = t + dt
    vreme.append(t)

pl.plot(vreme, intezitet, 'orange')
pl.show()
