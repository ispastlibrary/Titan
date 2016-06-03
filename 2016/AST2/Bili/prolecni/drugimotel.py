import math
import pylab as pl
import numpy as np

M=0.029
g=9.81
R=8.314
T=200
ro=0.122

h=2e+5
m=1e-5
v=4e+4
rom=3000
zr=np.pi/4

G=1
A=1.21
lamb=1
Z=6e+6

def koef_bright(v):
    if (v>16000):
        temp_koef=0.024*math.pow((v/1000+8.8),-1)
    else:
        temp_koef=6.04*1e-4*math.pow((v/1000-8.8),-0.35)
    return temp_koef

def velocity_lost(t,v):
    fder1=-G*A*math.pow(m,-1/3)*math.pow(rom,-2/3)*density_atm(h)*v*v	
    return fder1

def mass_lost(t,m):
    fder2=-(lamb*A*math.pow(m,2/3)*math.pow(rom,-2/3)*density_atm(h)*v*v*v)/(2*Z)
    return fder2
  
def Runge_mass(t0,m0,dt):
    k1=dt*mass_lost(t0,m0)
    k2=dt*mass_lost(t0+dt/2,m0+k1/2)
    k3=dt*mass_lost(t0+dt/2,m0+k2/2)
    k4=dt*mass_lost(t0+dt,m0+k3)
    m1=m0+(k1+2*k2+2*k3+k4)/6	
    return m1
	
def Runge_velocity(t0,v0,dt):
    k1=dt*velocity_lost(t0,v0)
    k2=dt*velocity_lost(t0+dt/2,v0+k1/2)
    k3=dt*velocity_lost(t0+dt/2,v0+k2/2)
    k4=dt*velocity_lost(t0+dt,v0+k3)
    v1=v0+(k1+2*k2+2*k3+k4)/6	
    return v1		

def height(h,v,dt):
    temp_height=h-v*zr*dt
    return temp_height

def density_atm(h):
    tempd=ro*math.exp(-(M*g*h)/(R*T))
    return tempd
def int_of_rad1(m,v,h):    
    tau=koef_bright(v)
    intensity=-tau*(1/2)*v*v*mass_lost(t,m)
    return intensity	
	
def int_of_rad2(m,v,h):    
    tau=koef_bright(v)
    intensity=-tau*((1/2)*v*v*mass_lost(t,m)+m*v*velocity_lost(t,v))
    return intensity	
		
def distance(h):
    dist=h/np.cos(zr)
    return dist
		
def app_magn(d,I):
    temp_magnitude=-14.8-2.5*math.log((683*I)/(4*np.pi*(d**2)),10)
    return temp_magnitude 		

m0=m
j=1
k=0
t=0
dt=0.001

I1=int_of_rad1(m,v,h)
I2=int_of_rad2(m,v,h)
#d=distance(h)
#magn=app_magn(d,I)
#hei=[]
#hei.append(h)
#magnitude=[]
#magnitude.append(magn)
time=[]
#mass=[]
#velocity=[]
radiation1=[]
radiation2=[]
time.append(t)
radiation1.append(I1)
radiation2.append(I2)

while (m > m0/1000):
    t+=dt
    time.append(t)    
    m1=Runge_mass(t,m,dt)
    v1=Runge_velocity(t,v,dt)
    h1=height(h,v,dt)
    #hei.append(h1)
    I1=int_of_rad1(m1,v1,h1)
    I2=int_of_rad2(m1,v1,h1)
    #d=distance(h1)
    #magn=app_magn(d,I)
    #magnitude.append(magn)
    radiation1.append(I1)
    radiation2.append(I2)
    m=m1
    v=v1    
    h=h1
pl.plot(time,radiation1,"blue",label='početni model')
pl.plot(time,radiation2,"red",label='drugačiji model')
pl.xlabel('vreme[s]')
pl.ylabel('intenzitet zračenja[ J/s ]')
pl.suptitle('Grafik zavisnosti intenziteta zračenja meteora od vremena')
pl.legend(loc='upper left') 
pl.show()
