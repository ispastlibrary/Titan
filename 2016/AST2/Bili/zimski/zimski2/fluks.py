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
Rk=400000#poluprecnik kome[m] ????????????????????????????? 
k=1.38*10e-23 #Bolcmanova konst [J\K]    
dE=3.37*1e-19 #razlika energetskih stanja 3p i 3s, povezana sa talasnom duzinom [J] 
R=Na*k #Univerzalna gasna konstanta [J/(molK)]
L0=589e-9 #centralna talasna duzina D2 linije [m]
h=6.63*1e-34 #Plankova konstanta [Js]
c=299792458 #brzina svetlosti [m/s]
A=6.14e+7 #Ajnstajnov koef za verovatnocu spontane emisije[s^-1] 3p-3s 
g0=1 # statisticka tezina 3s orbitale (s)
g1=3 # statisticka tezina 3p orbitale (px,py,pz)
V0=c/L0 #centralna frekvencija [Hz]
d=0 #rastojanje prave (posmatranog pravca) od centra jezgra
Ro=1000 #gustina jezgra [kg/m^3], Andrija
Rn=2.5e4 #poluprecnik jezgra [m]

S=1 #funkcija izvora

AMU=1.66*10e-27 #jedinica atomske mase u kg 
sigma=5.670373e-8 #Stefan - Bolcmanova konstanta[Wm^-2K^-4]

mna=22.9877*AMU #atomska masa Na u kg
mnaoh=39.998*AMU #masa NaOH u kg
mh20=18.015*AMU #masa H2O u kg 


def voigt(x,y):  #Fojtova funkcija, ali samo realni deo Faddeeva f-je   
    z = x + 1j*y
    w = wofz(z).real
    return w

def part_funk(a,T):  #izracunavanje part f-je
    K=0
    for i in range(6):
        K += a[i]*pow(np.log(T),i) 
    Zp = np.exp(K) 
    return Zp
	
def rastojanje(T): #heliocentricno rastojanje [AU]
    #Lt=-582*(T-273)+2.62e6 #latentna toplota sublimacije [J/kg], T u c, a ne u K
    Lt=2.62e6
    Sc=1361 #solarna const na 1AU [W/m^2]
    Pr=1.2*(10**12)*np.exp(-6000/T) #pritisak zasicene pare na povrsini komete
    Zm=Pr*np.sqrt(mh20/(2*np.pi*k*T)) #sublimacioni fluks H2O [kgs^-1m^-2] (masena stopa produktivnosti)
    rasto=np.sqrt(Sc/(sigma*T**4+Lt*Zm))
    return rasto

def Q_Na(T): #ukupna stopa produktivnosti Na [s^-1]
    Pr=1.2*(10e+12)*np.exp((-6000)/T) #pritisak zasicene pare 
    produ=Pr*np.sqrt(1/(2*np.pi*k*T*mna)) #stopa produktivnosti Na [m^-2s^-1] 
    produ=produ*4*np.pi*Rn*Rn #ukupna stopa 
    return produ

def brz_izb(T,masa): #brzina outflow (izlivanja)=termalna brzina [m/s] 
    brz = np.sqrt((2*k*T)/masa)
    return brz

tau_p0=10**3 #vreme dok se roditelj ne unisti [s]
tau_d0=1.67*(10**5) #vreme dok se cerka ne unisti [s] 
 
def lp(T): #skalirana duzina roditelja [m]
    roditelj = brz_izb(T,mnaoh)*tau_p0*(rastojanje(T))**2
    return roditelj

def ld(T): #skalirana duzina cerke [m]
    cerka = brz_izb(T,mna)*tau_d0*(rastojanje(T))**2
    return cerka

def kon_Na_koma(T,r):  #koncentracija Na u komi, Haserov model
    poluprecnik.append(r)
    Dr=r-Rn # redukovano trenutno rastojanje Rkome-Rjezgra
    konc=(Q_Na(T)*ld(T)*(np.exp(-Dr/lp(T))-np.exp(-Dr/ld(T))))/(4*np.pi*brz_izb(T,mna)*r*r*(lp(T)-ld(T)))
    kralj.append(konc)
    return konc

def Bol(T,r):
    NaI = kon_Na_koma(T,r)
    dE = h*c/L0
    odnos = g1*(np.exp(-dE/(k*T)))/g0
    n0 = NaI/(1+odnos)	
    return n0

def ajnstajnB(A): # za A(koef emisije) (3p-3s) vraca B (Ajnstajnov koef apsorpcije za verovatnocu prelaza (3s-3p)[m^3s^-2J^-1])
    B = (c**2*A*g1)/(8*np.pi*h*V0**3*g0)
    return B

def Dopl_sirina(T): #Doplerova sirina u funkciji of temperature [Hz]
    Dopler = np.sqrt(2*R*T/M)*(V0/c)
    return Dopler
	
def koef_aps(V,T,r,av): #koeficijent apsorpcije
    B = ajnstajnB(A)
    konc_aps = n0 = Bol(T,r) #MAXBOLC
    Dopler = Dopl_sirina(T)	
    apsor = ((B*n0*h*V)/(4*np.pi*Dopler))*Fojtov_profil(V,T,av)
    return apsor    
	
br_ljuspica = 100
dr = Rk/br_ljuspica #koma je podeljena na 50000 ljuspica

		
def opt_dub(d,V,T,av): #opticka dubina za nehomogenu komu
    r1=Rk
    r2 = r1 - dr
    suma_opt = 0
    broj = br_ljuspica - 1 - math.floor(d/dr)
    while (r1>(Rn+d)) and (r2>(Rn+d)):
        ds = np.sqrt(r1*r1 - d*d) - np.sqrt(r2*r2 - d*d)
        suma_opt += koef_aps(V,T,r1,av)*ds
        r1=r2
        r2=r1-dr
    ds = np.sqrt(r1*r1 - d*d)
    suma_opt += koef_aps(V,T,r1,av)*ds
    suma_opt *= 2	
    return suma_opt 

N_tacaka = 150
V1 = c/(589.02e-9)
V2 = c/(588.98e-9)
dV = (V2 - V1)/N_tacaka

def izlazni(V,T,av): #izlazni intenzitet normiran tako da je I0=1, a funkcija izvora S=1/2
    ukupno = 0    
    d = 0
    for i in range(br_ljuspica):
        tau = opt_dub(d,V,T,av) #opticka dubina
        q = ((1-np.exp(-tau)))/(rastojanje(T)**2)
        ukupno += q*2*(d+dr)*np.pi*dr
        d += dr
    return ukupno

def Fojtov_profil(V,T,av): 
    F=voigt((V-V0)/Dopl_sirina(T),av)/(np.pi*Dopl_sirina(T))
    return F
	
def E_W(x,y): #ekvivalentna sirina, metodom cubic spline
    EkW=0
    tck=interpolate.splrep(x,y)
    i=0
    while(i<(N_tacaka-1)):
        EkW+=interpolate.splint(x[i],x[i+1],tck)
        i+=1 
    return EkW

def obrni(x):
    for i in range(len(x)//2):
        prom1=x[i]
        prom2=x[len(x)-1-i]
        x[i]=prom2
        x[len(x)-1-i]=prom1
    return x
        
plt.figure(num = 1, figsize=(11,9), dpi=150)
plt.suptitle('', fontsize = 18)
poluprecnik=[]
kralj=[]
 
T = [0]*20
T[0] = 100
fluks = [0]*20
dT = 10
Temper = 160
hel_udalj = [0]*20
for i in range (20):
    T[i] = Temper + dT 
    print(rastojanje(T[i]),i)
    x=np.linspace(V1,V2,N_tacaka)
    av = A/Dopl_sirina(T[i])
    y0 = izlazni(x,T[i],av)    
    x = c/x
    x = obrni(x)
    fluks[i] = E_W(x,y0)
    Temper = T[i]  
    hel_udalj[i] = rastojanje(T[i])
plt.plot(hel_udalj, fluks)
plt.suptitle('Zavisnost fluksa linije Na od heliocentrične udaljenosti komete', fontsize =10)
plt.legend(loc='best')
plt.xlabel('rh [AU]', fontsize = 10)
plt.ylabel('F', fontsize = 10)
plt.yscale('log')
plt.show()
