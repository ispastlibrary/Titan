import math
import pylab as pl
import numpy as np

#pocetni uslovi
M=0.029
g=9.81 
R=8.314 
T=200 
ro=0.122 

h=2e+5 
m=1e-5 
v=4e+4
rom=8000
zr=np.pi/4

G=1
A=1.21
lamb=1
Z=6e+6

#funkcija koja za datu brzinu vraca koeficijent sjaja
def koef_bright(v):
    if (v>16000):
        temp_koef=0.024*math.pow((v/1000+8.8),-1)
    else:
        temp_koef=6.04*1e-4*math.pow((v/1000-8.8),-0.35)
    return temp_koef
#prvi izvod brzine po vremenu
def velocity_lost(t,v):
    fder1=-G*A*math.pow(m,-1/3)*math.pow(rom,-2/3)*density_atm(h)*v*v	
    return fder1
#prvi izvod mase po vremenu
def mass_lost(t,m):
    fder2=-(lamb*A*math.pow(m,2/3)*math.pow(rom,-2/3)*density_atm(h)*v*v*v)/(2*Z)
    return fder2
#RK4 metoda za izracunavanje mase    
def Runge_mass(t0,m0,dt):
    k1=dt*mass_lost(t0,m0)
    k2=dt*mass_lost(t0+dt/2,m0+k1/2)
    k3=dt*mass_lost(t0+dt/2,m0+k2/2)
    k4=dt*mass_lost(t0+dt,m0+k3)
    m1=m0+(k1+2*k2+2*k3+k4)/6	
    return m1
#RK4 metoda za izracunavanje brzine	
def Runge_velocity(t0,v0,dt):
    k1=dt*velocity_lost(t0,v0)
    k2=dt*velocity_lost(t0+dt/2,v0+k1/2)
    k3=dt*velocity_lost(t0+dt/2,v0+k2/2)
    k4=dt*velocity_lost(t0+dt,v0+k3)
    v1=v0+(k1+2*k2+2*k3+k4)/6	
    return v1		
#visina meteora nakon koraka dt
def height(h,v,dt):
    temp_height=h-v*zr*dt
    return temp_height
#gustina atmosfere na visini h
def density_atm(h):
    tempd=ro*math.exp(-(M*g*h)/(R*T))
    return tempd
#intenzitet zracenja	
def int_of_rad(m,v,h):    
    tau=koef_bright(v)
    intensity=-tau*(1/2)*v*v*mass_lost(t,m)
    return intensity	
#rastojanje meteora od posmatraca 		
def distance(h):
    dist=h/np.cos(zr)
    return dist
#prividna magnituda	
def app_magn(d,I):
    temp_magnitude=-14.8-2.5*math.log((683*I)/(4*np.pi*(d**2)),10)
    return temp_magnitude 		

m0=m
j=1
k=0
t=0
dt=0.001

I=int_of_rad(m,v,h)
#d=distance(h)
#magn=app_magn(d,I)
hei=[]
hei.append(h)
#magnitude=[]
#magnitude.append(magn)
#time=[]
#time.append(t)
#mass=[]
#velocity=[]

radiation=[]
radiation.append(I)

#integracija se nastavlja sve dok masa meteora ne postane 0.01% pocetne mase 
while (m > m0/1000):
    t+=dt               #posle koraka dt racuna se trenutna vrednost mase, brzine i visine, a nakon toga intenzitet zracenja i prividna magnituda
    #time.append(t)    
    m1=Runge_mass(t,m,dt)      
    v1=Runge_velocity(t,v,dt)  
    h1=height(h,v,dt)          
    hei.append(h1)
    I=int_of_rad(m1,v1,h1)
    #d=distance(h1)
    #magn=app_magn(d,I)
    #magnitude.append(magn)
    radiation.append(I)
    m=m1
    v=v1    
    h=h1
pl.plot(hei,radiation,'purple',label='')
pl.xlabel('visina[m]')
pl.ylabel('intenzitet zračenja[ J/s ]')
pl.suptitle('Grafik zavisnosti intenziteta zračenja meteora od visine') 
#graficki prikaz zavisnosti magnitude meteora od vremena; analogna zavisnost magnitude od visine, 
#intenziteta zracenja od vremena, intenziteta zracenja od visine
pl.legend(loc='upper right')
pl.show()
