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
#Tef=5777 #efektivna temperatura Sunca [K]
d=0 #rastojanje prave (posmatranog pravca) od centra jezgra
#niz koef za NaI
#niz koef za NaII
#koeficijenti aproksimativne polinomne funkcije za izracunavanje particione f-je

a=[-2.60507178e+3,1.71419244e+3,-4.50632658e+2,5.91751503e+1,-3.88164070e+0,1.01752936e-1]

b=[-3.68868193e-6,2.28941495e-6,-5.66767833e-7,6.99552282e-8,-4.30495956e-9,1.05668164e-10]

Ro=1000 #gustina jezgra [kg/m^3], Andrija
Rn=2.5e4 #poluprecnik jezgra [m]

S=1/2 #funkcija izvora

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
"""	
def Q_H20(T):
    mh20=18.015*AMU
    Pr=1.2*(10e+12)*np.exp((-6000)/T)
    prod=Pr*np.sqrt(1/(2*np.pi*k*T*mh20))
    prod=prod*4*np.pi*Rn*Rn
    return prod"""

def Q_Na(T): #ukupna stopa produktivnosti Na [s^-1]
    Pr=1.2*(10e+12)*np.exp((-6000)/T) #pritisak zasicene pare 
    produ=Pr*np.sqrt(1/(2*np.pi*k*T*mna)) #stopa produktivnosti Na [m^-2s^-1] 
    produ=produ*4*np.pi*Rn*Rn #ukupna stopa 
    return produ
# 207.6 K -> 1 AU, ~1e+32 ukupna stopa produktivnosti Na
def brz_izb(T,masa): #brzina outflow (izlivanja)=termalna brzina [m/s] 
    #brz=20*pow(rastojanje(T),-0.41)*(10**3)
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

#plt.gca().set_yscale('log')  

def kon_Na_koma(T,r):  #koncentracija Na u komi, Haserov model
    #poluprecnik.append(r)
    Dr=r-Rn # redukovano trenutno rastojanje Rkome-Rjezgra
    konc=(Q_Na(T)*ld(T)*(np.exp(-Dr/lp(T))-np.exp(-Dr/ld(T))))/(4*np.pi*brz_izb(T,mna)*r*r*(lp(T)-ld(T)))
    #kralj.append(konc)#print(ld(T),lp(T))
    return konc

def MaxBol(T,r): #koncentracija Na u osnovnom 3s stanju (n0) na rastojanju r od kome         
    NaI = kon_Na_koma(T,r) #ukupan broj Na iz Haserovog modela 
    Zp = part_funk(a,T) #particiona f-ja
    #Er=5.1390767*eV #energija 3s za Na [J]
    #dE=h*c/L0
    #Er=dE
    Er=0
    n0 =(NaI*g0*np.exp(-Er/(k*T)))/Zp #konc Na u osnovnom stanju
    return n0

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
	
br_ljuspica = 2500
dr = Rk/br_ljuspica #koma je podeljena na 50000 ljuspica

		
def opt_dub(d,V,T,av): #opticka dubina za nehomogenu komu
    #r1 = Rk
    #r2 = r1 - dr
    #r1=lp(T)+ld(T)
    r1=Rk
    r2 = r1 - dr
    suma_opt = 0
    broj = br_ljuspica - 1 - math.floor(d/dr)
    """for i in range(broj):
        r2 = r1 - dr
        ds = np.sqrt(r1*r1 - d*d) - np.sqrt(r2*r2 - d*d)
        suma_opt += koef_aps(V,T,r1,av)*ds
        r1 = r2"""
    while (r1>(Rn+d)) and (r2>(Rn+d)):
        ds = np.sqrt(r1*r1 - d*d) - np.sqrt(r2*r2 - d*d)
        suma_opt += koef_aps(V,T,r1,av)*ds
        r1=r2
        r2=r1-dr
    ds = np.sqrt(r1*r1 - d*d)
    suma_opt += koef_aps(V,T,r1,av)*ds
    suma_opt *= 2	
    return suma_opt 

"""def poc_intez(V,T): #pocetni intezitet preko plankove fje
    plank=(2*h*V*V*V)/(c*c*(np.exp((h*V)/(k*T))-1))
    return plank"""

N_tacaka = 150

V1 = c/(589.02e-9)
V2 = c/(588.98e-9)
dV = (V2 - V1)/N_tacaka

def izlazni(V,T,av): #izlazni intenzitet normiran tako da je I0=1, a funkcija izvora S=1/2
    tau = opt_dub(d,V,T,av) #opticka dubina
    #2*Rk*koef_aps(V,T,Rk)  
    q = S*(1-np.exp(-tau))
    return q

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

T1=np.linspace(190,290,20)
x1=np.linspace(c/V2,c/V1,N_tacaka)
dd=Rk/6

print('1')
d=0
y1=[]
EW1=[]
for i in range(20):
    av1=A/Dopl_sirina(T1[i])
    V=V1
    for j in range(N_tacaka):
        y1.append(izlazni(V,T1[i],av1))
        V+=dV
    EW1.append(E_W(x1,y1))
    y1=[]
plt.plot(EW1,T1,label='d=0 m')
#
print('2')
d=d+dd
y1=[]
EW2=[]
for i in range(20):
    av1=A/Dopl_sirina(T1[i])
    V=V1
    for j in range(N_tacaka):
        y1.append(izlazni(V,T1[i],av1))
        V+=dV
    EW2.append(E_W(x1,y1))
    y1=[]
plt.plot(EW2,T1,label='d=66666 m')
#
print('3')
d=d+dd
y1=[]
EW3=[]
for i in range(20):
    av1=A/Dopl_sirina(T1[i])
    V=V1
    for j in range(N_tacaka):
        y1.append(izlazni(V,T1[i],av1))
        V+=dV
    EW3.append(E_W(x1,y1))
    y1=[]
plt.plot(EW3,T1,label='d=133333 m')
#
print('4')
d=d+dd
y1=[]
EW4=[]
for i in range(20):
    av1=A/Dopl_sirina(T1[i])
    V=V1
    for j in range(N_tacaka):
        y1.append(izlazni(V,T1[i],av1))
        V+=dV
    EW4.append(E_W(x1,y1))
    y1=[]
plt.plot(EW4,T1,label='d=200000 m')
#
print('5')
d=d+dd
y1=[]
EW5=[]
for i in range(20):
    av1=A/Dopl_sirina(T1[i])
    V=V1
    for j in range(N_tacaka):
        y1.append(izlazni(V,T1[i],av1))
        V+=dV
    EW5.append(E_W(x1,y1))
    y1=[]
plt.plot(EW5,T1,label='d=266666 m')


plt.suptitle('Zavisnost ekvivalentne širine od temperature komete za različite preseke')
plt.ylabel('Temperatura [K]')
plt.xlabel('EW [m]')
plt.show()

"""T=np.linspace(100,250,100)

produkcija=Q_Na(T)
rastojanjee=rastojanje(T)
plt.plot(T,produkcija)
plt.suptitle('Zavisnost stope produkcije Na od temperature komete')
plt.xlabel('temperatura [K]')
plt.ylabel('stopa produkcije [s^-1]')
plt.show()"""
#plt.suptitle('Zavisnost ukupne koncentracije Na od rastojanja od jezgra, za različite temperature')
"""T=200
poluprecnik=[]
kralj=[]
print(rastojanje(T))
av=A/Dopl_sirina(T) 
x=np.linspace(V1,V2,N_tacaka) 
y0=izlazni(x,av)
plt.plot(poluprecnik,kralj,label='1.69 AU, 200K') 
#plt.xlim(0,0.2e+7) 
T=207
poluprecnik=[]
kralj=[] 
print(rastojanje(T)) 
av=A/Dopl_sirina(T) 
y1=izlazni(x,av)
plt.plot(poluprecnik,kralj,label='1.09 AU, 207K') 
#plt.xlim(0,0.2e+7) 
T=220 
poluprecnik=[]
kralj=[] 
print(rastojanje(T)) 
av=A/Dopl_sirina(T) 
y2=izlazni(x,av) 
plt.plot(poluprecnik,kralj,label='0.49 AU, 220K') 
#plt.xlim(0,0.2e+7) 
T=230
poluprecnik=[]
kralj=[] 
print(rastojanje(T)) 
av=A/Dopl_sirina(T) 
y3=izlazni(x,av) 
plt.plot(poluprecnik,kralj,label='0.27 AU, 230K') 
#plt.xlim(0,0.2e+7) 
T=250 
poluprecnik=[]
kralj=[] 
print(rastojanje(T)) 
av=A/Dopl_sirina(T) 
y4=izlazni(x,av) 
plt.plot(poluprecnik,kralj,label='0.10 AU, 250K') 
#plt.xlim(0,0.2e+7) 
T=260 
poluprecnik=[]
kralj=[] 
print(rastojanje(T)) 
av=A/Dopl_sirina(T) 
y5=izlazni(x,av) 
plt.plot(poluprecnik,kralj,label='0.06 AU, 260K') 
#plt.xlim(0,0.2e+7)
plt.legend(loc='best')
plt.show()
print(lp(200)+ld(200))
print(kon_Na_koma(260,200000))
print(kon_Na_koma(260,300000))
print(kon_Na_koma(260,400000))
print(kon_Na_koma(260,500000))"""


"""plt.suptitle('Zavisnost intenziteta linije Na od talasne duzine, sa Maksvel - Bolcmanovom statistikom') 
plt.plot(x,y2,label='0.49 AU, 220K') 
plt.plot(x,y3,label='0.27 AU, 230K') 
plt.plot(x,y4,label='0.10 AU, 250K') 
plt.plot(x,y5,label='0.06 AU, 260K') 
plt.legend(loc='best') 
plt.show()"""
"""xt=np.linspace(100,210,100) yt=Q_Na(xt) plt.plot(xt,yt) 
plt.xlabel('Temperatura[K]') plt.ylabel('Stopa produkcije Na[s^-1]') 
plt.title('Grafik zavisnosti stope produkcije od temperature')"""
#plt.yscale('log')
