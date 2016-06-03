from scipy.special import wofz
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate

e=1.60217657e-19 #elementarno naelektrisanje [C]
eV=1.60217657e-19 #eV u J
AU=149597871000 #Astronomska jedinica [m]
Na=6.02*1e+23 #Avogadrov broj
M=23*1e-3 #molarna masa Na [kg/mol]
me=9.1e-31 #masa elektrona[kg]
T=300  #temperatura [K]
Rk=0.1*AU #poluprecnik kome[m] 
k=1.38*10e-23 #Bolcmanova konst [J\K]    
dE=3.37*1e-19 # razlika energetskih stanja 3p i 3s, povezana sa talasnom duzinom [J] 
R=Na*k #Univerzalna gasna konstanta [J/(molK)]
L0=589e-9 #talasna duzina [m]
h=6.63*1e-34 #Plankova konstanta [Js]
c=299792458 #brzina svetlosti [m/s]
A=6.14e+7 #Ajnstajnov koef za verovatnocu spontane emisije[s^-1] (To smo nasli na Nistu (AKO JE TO, TO))
g0=1 # statisticka tezina 3s orbitale (s)
g1=3 # statisticka tezina 3p orbitale (px,py,pz)
V0=c/L0 #centralna frekvencija [s^-1]
Tef=5777 #efektivna temperatura Sunca [K]
#Ejon=495.8e+3   #energija prve jonizacije [J/mol]
d=0
#niz koef za NaI
#niz koef za NaII
#koeficijenti aproksimativne polinomne funkcije za izracunavanje particione f-je

a=[-2.60507178e+3,1.71419244e+3,-4.50632658e+2,5.91751503e+1,-3.88164070e+0,1.01752936e-1]

b=[-3.68868193e-6,2.28941495e-6,-5.66767833e-7,6.99552282e-8,-4.30495956e-9,1.05668164e-10]

#Ro=600 #Gustina komete [kg/m^3]
Ro=1000 #andreja
Rn=2.5e4 #poluprecnik jezgra [m]
#vt=4500 # termalna brzina gasa [m/s]
#vp=26600 #outflow brzina hidrodinamicka [m/s]
#ld=147e6 #duzina cerke [m] 
#lp=147e4 #duzina roditelja [m]
#ld=449e3
#lp=147e5 

dL = 5*1e-12 #od centralne talasne duzine[m]
L = L0-dL  #druga talasna duzina [m]

S=1/2
AMU=1.66*10e-27 #jedinica atomske mase u kg 
#mh20=18*AMU

sigma=5.670373e-8 #SB konstanta
#Lt=2.85*10e+6 #latentna sublimacija Na J/kg
 #solarna const u W/m2

def voigt(x,y):  #Fojtova funkcija  
    z = x + 1j*y
    w = wofz(z).real
    return w

def part_funk(a,T):  #izracunavanje part f-je
    K=0
    for i in range(6):
        K += a[i]*pow(np.log(T),i) 
    Z = np.exp(K) 
    return Z
	
def rastojanje(T):
    Lt=-582*(T-273)+2.62e6 #u c, ne u K 
    Sc=1361
    mh20=18.015*AMU
    Pr=1.2*(10**12)*np.exp(-6000/T)
    Zm=Pr*np.sqrt(mh20/(2*np.pi*k*T))
    rasto=np.sqrt(Sc/(sigma*T**4+Lt*Zm))
    return rasto
	
def Q_H20(T):
    mh20=18.015*AMU
    Pr=1.2*(10e+12)*np.exp((-6000)/T)
    prod=Pr*np.sqrt(1/(2*np.pi*k*T*mh20))
    prod=prod*4*np.pi*Rn*Rn
    return prod
#print(Q_H20(207))
def Q_Na(T):
    mna=22.9877*AMU
    Pr=1.2*(10e+12)*np.exp((-6000)/T)
    produ=Pr*np.sqrt(1/(2*np.pi*k*T*mna))
    produ=produ*4*np.pi*Rn*Rn
    return produ
print(Q_Na(207.6),rastojanje(207.6))
#print(rastojanje(273),rastojanje(233))	
def brz_izb(T):
    mna=22.9877*AMU
    #brz=20*pow(rastojanje(T),-0.41)*(10**3)
    brz = np.sqrt((2*k*T)/mna)
    return brz
 
def lp(T):
    #roditelj=lp0*pow(rastojanje(T),1.59)
    roditelj=brz_izb(T)*tau_p0*(rastojanje(T))**2
    return roditelj

v0=1.112*(10**3)
tau_p0=10**3
tau_d0=1.67*(10**5) 
lp0=v0*tau_p0
ld0=v0*tau_d0

def ld(T):
    #cerka=ld0*pow(rastojanje(T),1.59)
    cerka = brz_izb(T)*tau_d0*(rastojanje(T))**2
    return cerka
	
#T = np.linspace(200, 400, num = 170)
#Production = Q_H20(T)
#plt.plot(T, Production)
#plt.gca().set_yscale('log')
#plt.show()

#print(rastojanje(393.6059221199))
#print(rastojanje(393.6))
#print(Q_Na(393.6))    
alal=[]
lala=[]
#print(rastojanje(207.5),'temp na oko 1 AU')

def kon_Na_koma(T,r):  #koncentracija Na Haserov model, u komi
    #Q=1e+28  
    alal.append(r)
    Dr=r-Rn
    konc=(Q_Na(T)*ld(T)*(np.exp(-Dr/lp(T))-np.exp(-Dr/ld(T))))/(4*np.pi*brz_izb(T)*r*r*(lp(T)-ld(T)))
    #print(ld(T)-ld0,lp(T)-lp0)   
    lala.append(konc)
    #print(konc)
    return konc

def MaxBol(T,r): #koncentracija Na u osnovnom 3s stanju (n0) na rastojanju r od kome         
    NaI = kon_Na_koma(T,r)
    Z = part_funk(a,T)
    Er=5.1390767*eV #energija 3s za Natrijum, mora minus da bude
    n0 = (NaI*g0*np.exp(-Er/(k*T)))/Z
    #print(n0)
    return n0	

def ajnstajnB(A): # za A(koef emisije) vraca B (Ajnstajnov koef apsorpcije za verovatnocu prelaza (3s-3p)[m^3s^-2J^-1])
    B=(c**2*A*g1)/(8*np.pi*h*V0**3*g0)
    return B

def Dopl_sirina(T): #Doplerova sirina u funkciji of temperature
    Dopler=np.sqrt(2*R*T/M)*(V0/c)
    return Dopler
	
def koef_aps(V,T,r,av):
    B = ajnstajnB(A)
    konc_aps = n0 = MaxBol(T,r)#VRQTITI NA MAX BOLC
    Dopler = Dopl_sirina(T)	
    apsor = ((B*n0*h*V)/(4*np.pi*Dopler))*Fojtov_profil(V,av)
    return apsor    
	
br_ljuspica = 1000
dr = Rk/br_ljuspica #koma je podeljena na 10000 ljuspica

		
def opt_dub(d,V,T,av): #opticka dubina za nehomogenu komu
   r1 = Rk
   suma_opt = 0
   broj = br_ljuspica - 1 - math.floor(d/dr)
   for i in range(broj):
       r2 = r1 - dr
       ds = np.sqrt(r1*r1 - d*d) - np.sqrt(r2*r2 - d*d)
       suma_opt += koef_aps(V,T,r1,av)*ds
       r1 = r2
   ds = np.sqrt(r1*r1 - d*d)
   suma_opt += koef_aps(V,T,r1,av)*ds
   suma_opt *= 2	
   return suma_opt 

#def poc_intez(V,T): #pocetni intezitet preko plankove fje
#    plank=(2*h*V*V*V)/(c*c*(np.exp((h*V)/(k*T))-1))
#    return plank

N_tacaka = 300

V1 = c/(589.05e-9)
V2 = c/(588.95e-9)
dV = (V2 - V1)/N_tacaka

def izlazni(V,av):
    tau = opt_dub(d,V,T,av) #2*Rk*koef_aps(V,T,Rk)
    #print(brz_izb(T))  
    q = S*(1-np.exp(-tau))
    return q

def Fojtov_profil(V,av):
    F=voigt((V-V0)/Dopl_sirina(T),av)/(np.pi*Dopl_sirina(T))
    return F
	
def E_W(x,y):
    EkW=0
    tck=interpolate.splrep(x,y)
    i=0
    while(i<(N_tacaka-1)):
        EkW+=interpolate.splint(x[i],x[i+1],tck)
        i+=1 
    return EkW

T=np.linspace(150,500,20)
#print(rastojanje(393))
#av=A/Dopl_sirina(T)
#Q1=10**35    
#T=np.linspace(100,2000,100)
#av=A/Dopl_sirina(T)
T=150
dT=10
temp=[]
ekviv=[]
x=np.linspace(V1,V2,N_tacaka)
y1=[]

for i in range(300):
    temp.append(T)
    av=A/Dopl_sirina(T)
    print(y1)
    y1=izlazni(x,av)
    ekviv.append(E_W(x,y1))
    T+=dT


"""xt=np.linspace(100,1000,100)
yt=rastojanje(xt)
plt.plot(xt,yt)
plt.title('Grafik zavisnost heliocentričnog rastojanja od temperature')
plt.xlabel('Temperatura[K]')
plt.ylabel('Heliocentrično rastojanje[AU]')"""
"""xt=np.linspace(100,210,100)
yt=Q_Na(xt)
plt.plot(xt,yt)
plt.xlabel('Temperatura[K]')
plt.ylabel('Stopa produkcije Na[s^-1]')
plt.title('Garfik zavisnosti stope produkcije od temperature')"""
#x=c/x
#x=x*(10**10)
#y2=izlazni(x,av,Q1)
#plt.plot(x,y1,'blue')
#plt.yscale('log')
#plt.plot(alal,lala)
#plt.plot(x,y2,'red')
#EW=E_W(x,y)
#plt.plot(T,EW)
plt.plot(x,y1)
plt.show()