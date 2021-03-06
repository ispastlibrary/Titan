from scipy.special import wofz
import numpy as np
import matplotlib.pyplot as plt
import math

def voigt(x,y):  #Fojtova funkcija  
    z = x + 1j*y
    w = wofz(z).real
    return w

e=1.60217657e-19 #elementarno naelektrisanje [C]
AU=149597871000 #Astronomska jedinica [m]
Na=6.02*1e+23 #Avogadrov broj
M=23*1e-3 #molarna masa Na [kg/mol]
me=9.1e-31 #masa elektrona[kg]
T=200  #temperatura [K]
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
E0=5.1*1.60217657e-19 #energija 3s orbitale [J]  (ODOKATIVNO)
Ejon=495.8e+3   #energija prve jonizacije [J/mol]

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
#vp=26600 #outflow brzina hidrodinamicka [m/s]
vp=400
Mh=0.001 #Molaena masa vodonika [kg/mol]
#ld=147e6 #duzina cerke [m] 
#lp=147e4 #duzina roditelja [m]
#ld=449e3
ld=44900e3
lp=147e5 

#nh = 10e19 #broj atoma vodonika po m^3
#nna = pow(10,-5.82)*nh #koncentracija atoma natrijuma
nnajonizovani = 0

dL = 5*1e-12 #od centralne talasne duzine[m]
L = L0-dL  #druga talasna duzina [m]

S=1/2

def part_funk(a,T):  #izracunavanje part f-je
    K=0
    for i in range(6):
        K += a[i]*pow(np.log(T),i) 
    Z = np.exp(K) 
    return Z
	
"""def kon(r):  #koncentracija Na opada eksponencijalno sa poluprecnikom kome
    konc=nna*math.exp(-10*r/Rk)
    return konc"""

def kon_Na_jezgro(Ro): #koncentracija Na u jezgru, sastav kao u Suncu
    mh=0.71*Ro*(4/3)*(Rn**3)*np.pi
    nh=(mh*Na/Mh)/((4/3)*(Rn**3)*np.pi)
    nna=pow(10,-5.82)*nh
    return nna
	
def kon_Na_koma(r):  #koncentracija Na Haserov model, u komi
    #Q=4*np.pi*Rn*Rn*kon_Na_jezgro(Ro)*vp
    Q=1e+30  
    Dr=r-Rn
    konc=(Q*ld*(np.exp(-Dr/lp)-np.exp(-Dr/ld)))/(4*np.pi*vp*r*r*(lp-ld))
    return konc
	

def MaxBol(T,r): #koncentracija Na u osnovnom 3s stanju (n0) na rastojanju r od kome         
    NaI = kon_Na_koma(r)
#    print(NaI)
    Z = part_funk(a,T)
    n0 = (NaI*g0*np.exp(-E0/(k*T)))/Z
    return n0	

def ajnstajnB(A): # za A(koef emisije) vraca B (Ajnstajnov koef apsorpcije za verovatnocu prelaza (3s-3p)[m^3s^-2J^-1])
    B=(L0**3*A*g1)/(8*np.pi*h*c*g0)
    return B

def Dopl_sirina(T): #Doplerova sirina u funkciji of temperature
    Dopler=np.sqrt(2*R*T/M)/L0
    return Dopler
	
def koef_aps(V,T,r):
    B = ajnstajnB(A)
    konc_aps = n0 = MaxBol(T,r)
    Dopler = Dopl_sirina(T)	
    apsor = ((B*n0*h*V)/(4*np.pi*Dopler))*Fojtov_profil(V)
    return apsor    
	
br_ljuspica = 1000
dr = Rk/br_ljuspica #koma je podeljena na 10000 ljuspica
		
def opt_dub(d,V,T): #opticka dubina za nehomogenu komu
   r1 = Rk
   suma_opt = 0
   broj = br_ljuspica - 1 - math.floor(d/dr)
   for i in range(broj):
       r2 = r1 - dr
       ds = np.sqrt(r1*r1 - d*d) - np.sqrt(r2*r2 - d*d)
       suma_opt += koef_aps(V,T,r1)*ds
       r1 = r2
   ds = np.sqrt(r1*r1 - d*d)
   suma_opt += koef_aps(V,T,r1)*ds
   suma_opt *= 2	
   return suma_opt

#def poc_intez(V,T): #pocetni intezitet preko plankove fje
#    plank=(2*h*V*V*V)/(c*c*(np.exp((h*V)/(k*T))-1))
#    return plank

#V2=5.0901e14 #588
#V1=V0-(V2-V0) #590
#dV=(V2-V1)/100

N_tacaka = 200

V1 = c/(589.1e-9)
V2 = c/(588.9e-9)
dV = (V2 - V1)/N_tacaka

def izlazni(V):
    tau = opt_dub(d,V,T) #2*Rk*koef_aps(V,T,Rk)   
    q = S*(1-np.exp(-tau))
    return q
	
def FWHM_G(T): #sirina na polovini max visine Gausa
    gamma_G=Dopl_sirina(T)  #scale parametar za Gausa
    Gg=2*np.sqrt(np.log(2))*gamma_G
    return Gg
# SAMO PRIRODNO SIRENJE!!!!!!!!!!!!! POSLE UBACITI STARKOVO I/ILI VAN DER WALSOVO SIRENJE USLED PRITISKA
def FWHM_L(L0): #sirina na polovini max visine Lorenca 
    gamma_L=A  #scale parametar za Lorenca, Rutten (3.45) 
    Gl=gamma_L/(2*np.pi)
    return Gl

def Fojtov_profil(V):
    av = FWHM_L(V0)/FWHM_G(T)
    F = voigt((V-V0)/Dopl_sirina(T),av)/np.sqrt(np.pi) #Fojtov normirani profil, u V0 0.56
    return F

d = 0
#dd = Rk/br_ljuspica

x = []
y = []

V = V1
for i in range(N_tacaka):
    y.append(izlazni(V))
    x.append(c/V)
    V += dV


#print(opt_dub(0,V0,T))
#for i in range(1000):
#    x.append(d)
#    y.append(opt_dub(d,V0,T))
#    d+=dd        	 
#d=np.linspace(0,Rk,1000) #rastojanje pravca od centra kome
#o=opt_dub(d,V0,T)
#plt.suptitle('opticka dubina za razlicite paralelne preseke za nehomogenu komu')
#plt.xlabel('rastojanje prave od centra kome [m]')
#plt.ylabel('opticka dubina')
plt.plot(x, y,'red')
plt.show()
