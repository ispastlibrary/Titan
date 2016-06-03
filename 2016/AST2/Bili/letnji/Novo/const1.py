import numpy as np
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
T=300 #temperatura [K]
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

a=[0]*6 #niz koef za NaI
b=[0]*6 #niz koef za NaII
#koeficijenti aproksimativne polinomne funkcije za izracunavanje particione f-je

a[0]=-2.60507178e+3
a[1]=1.71419244e+3
a[2]=-4.50632658e+2
a[3]=5.91751503e+1
a[4]=-3.88164070e+0
a[5]=1.01752936e-1

b[0]=-3.68868193e-6
b[1]=2.28941495e-6
b[2]=-5.66767833e-7
b[3]=6.99552282e-8
b[4]=-4.30495956e-9
b[5]=1.05668164e-10

Ro=600 #Gustina komete [kg/m^3]
Rn=3e4 #poluprecnik jezgra [m]
vt=4500 # termalna brzina gasa [m/s]
vp=26600 #outflow brzina hidrodinamicka [m/s]
Mh=0.001 #Molaena masa vodonika [kg/mol]
#ld=147e6 #duzina cerke [m] 
#lp=147e4 #duzina roditelja [m]
ld=449e3
lp=147e5 


aNa=22.989769 #atomska masa Na [a.j.m.]
aH=1.00794 #atomska masa H [a.j.m.]
ao=5.3e-11 #Bohrov radijus [m]
Eh=13.6 #Energija jonizacije vodonika [eV]
Ei=5.1390767 #Energija I jonizacije Na [eV]
E0=-Ei*eV #energija 3s orbitale [J]  (ODOKATIVNO)
E1=E0+2.1044*eV #energija 3p orbirale [J]
Zr=1 #Jonizaciono stanje emitera/NaI, Z=1
l0=0 #orbitalni broj za s
l1=1 #orbitalni broj za p
Eh1=10.19880570432 #Korigovan energija(NIST) za prvo pobudjeno stanje HI(2p) J= 1/2
Eh2=10.19885106866 #____,,___ J=3/2
Jh1=1/2 #NIST sluzi za g
Jh2=3/2 #NIST sluzi za g

nh = 5*10e16 #broj atoma vodonika po m^3
nna = pow(10,-5.82)*nh #koncentracija atoma natrijuma
"""koncentracija perturbera 10^35 je primetna """

dL = 5*1e-12 #od centralne talasne duzine[m]
L = L0-dL  #druga talasna duzina [m]

S=1/2

K=0
for i in range(6):
    K += a[i]*pow(np.log(T),i) 
Z = np.exp(K) 

Nswe=10**5 #elektroni u cm^-3, nije 10**12
Tswe=4e3#Telektrona [K]

B=(L0**3*A*g1)/(8*np.pi*h*c*g0)

br_ljuspica = 1000
dr = Rk/br_ljuspica #koma je podeljena na 10000 ljuspica

d = 0

'''def kon_Na_koma(r):  #koncentracija Na opada eksponencijalno sa poluprecnikom kome
    konc=nna*math.exp(-10*r/Rk)
    return konc'''

def voigt(x,y):  #Fojtova funkcija  
    z = x + 1j*y
    w = wofz(z).real
    return w

def Dopl_sirina(T): #Doplerova sirina u funkciji of temperature
    Dopler=np.sqrt(2*R*T/M)*(V0/c)
    return Dopler

def Fojtov_profil(V,av):
    F = voigt((V-V0)/Dopl_sirina(T),av)/np.sqrt(np.pi) #Fojtov normirani profil, u V0 0.56
    return F


def koef_aps(V,T,r,av):
    n0 = MaxBol(T,r)
    Dopler = Dopl_sirina(T)	
    apsor = ((B*n0*h*V)/(4*np.pi*Dopler))*Fojtov_profil(V,av)
    return apsor

def MaxBol(T,r): #koncentracija Na u osnovnom 3s stanju (n0) na rastojanju r od kome         
    NaI = kon_Na_koma(r)
    Er=5.1390767*eV #energija 3s za Natrijum, mora minus da bude
    n0 = (NaI*g0*np.exp(-Er/(k*T)))/Z
    return n0

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


def izlazni(V,av,T):
    tau = opt_dub(d,V,T,av) #2*Rk*koef_aps(V,T,Rk)   
    q = S*(1-np.exp(-tau))
    return q


def stark(n,T): #starkova polusirina u angstremima
    Zr=2    
    ni=Zr*((Eh/np.abs(E0/eV))**(1/2))
    nj=Zr*((Eh/np.abs(E1/eV))**(1/2))
    L0c=L0*100 #u cm
    Ri=(1/2)*((ni/Zr)**2)*(5*ni*ni+1-3*l0*(l0+1)) #na kvadrat
    Rj=(1/2)*((nj/Zr)**2)*(5*nj*nj+1-3*l1*(l1+1)) #na kvadrat
    ws=0.4430*(10e-8)*L0c*L0c*n*(Ri+Rj)/(math.pow(T,1/2))
    ws=ws/(10**10)
    ws=2*(c*ws)/(L0**2) #sirina linije u Hz
    return ws

def vd_vals(n):
    mi= 1/aNa + 1/aH
    gh1=2*Jh1+1 #statisticke tezine za vodonik
    gh2=2*Jh2+1
    Ep=(Eh1*gh1+Eh2*gh2)/(gh1+gh2)
    np_vals=Zr*((Eh/np.abs(E1/eV))**1/2)
    ns_vals=Zr*((Eh/np.abs(E0/eV))**1/2)
    Rs=((ns_vals**2)/2)*(5*ns_vals**2+1-3*l0*(l0+1)) #3s
    Rs=Rs**2
    Rp=((np_vals**2)/2)*(5*np_vals**2+1-3*l1*(l1+1)) #3p
    Rp=Rp**2
    Red=Rp**2-Rs**2 #to je na kvadrat
    alfa=(9/2)*math.pow(ao,3)*math.pow((3*Eh)/(4*Ep),2)
    alfa=alfa*(10**6) #mora u cm^-3
    w=(8.18e-12)*L0*L0*math.pow(alfa*Red,2/5)*math.pow(T*mi,3/10)*n
    w=2*(c*w)/(L0**2) #sirina, a ne polusirina u Hz
    return w

def kon_Na_jezgro(Ro): #koncentracija Na u jezgru, sastav kao u Suncu
    mh=0.71*Ro*(4/3)*(Rn**3)*np.pi
    nh=(mh*Na/Mh)/((4/3)*(Rn**3)*np.pi)
    nna=pow(10,-5.82)*nh
    return nna
	
def kon_Na_koma(r):  #koncentracija Na Haserov model, u komi
    Q=4*np.pi*Rn*Rn*kon_Na_jezgro(Ro)*vp
    #Q=1e+28  
    Dr=r-Rn
    konc=(Q*ld*(np.exp(-Dr/lp)-np.exp(-Dr/ld)))/(4*np.pi*vt*r*r*(lp-ld))
    return konc

