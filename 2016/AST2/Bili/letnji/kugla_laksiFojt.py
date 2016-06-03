from scipy.special import wofz
import numpy as np
import matplotlib.pyplot as plt

def voigt(x,y):  #Fojtova funkcija  
    z = x + 1j*y
    w = wofz(z).real
    return w

e=1.60217657e-19 #elementarno naelektrisanje [C]
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

E0=2.1*1.60217657e-19 #energija 3s orbitale [J]  (ODOKATIVNO)
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

nh=10e19 #broj atoma vodonika po m^3
nna=pow(10,-5.82)*nh #koncentracija atoma natrijuma 
nnajonizovani=0

dL=5*1e-12 #od centralne talasne duzine[m]
L=L0-dL  #druga talasna duzina [m]

def part_funk(a,T):  #izracunavanje part f-je
    K=0
    for i in range(6):
        K+=a[i]*pow(np.log(T),i) 
    Z=np.exp(K) 
    return Z
	
def MaxBol(T): #koncentracija Na u osnovnom 3s stanju (n0)        
    NaI=nna  
    Z=part_funk(a,T)
    n0=(NaI*g0*np.exp(-E0/(k*T)))/Z
    return n0	

def ajnstajnB(A): # za A(koef emisije) vraca B (Ajnstajnov koef apsorpcije za verovatnocu prelaza (3s-3p)[m^3s^-2J^-1])
    B=(L0**3*A*g1)/(8*np.pi*h*c*g0)
    return B

def Dopl_sirina(T): #Doplerova sirina u funkciji of temperature
    Dopler=np.sqrt(2*R*T/M)/L0
    return Dopler
	
def koef_aps(V,T): #koeficijent apsorpcije u f-ji od talasne duzine 
    B=ajnstajnB(A)
    konc_aps=n0=MaxBol(T)
    Dopler=Dopl_sirina(T)	
    apsor=((B*n0*h*V)/(4*np.pi*Dopler))*Fojtov_profil(V)
    return apsor

def opt_dub(Rk,V): #opticka dubina za homogenu komu
    argh=koef_aps(V,T)
    tau=argh*2*Rk
    return tau

	
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
    av=FWHM_L(V0)/FWHM_G(T)
    F=voigt((V-V0)/Dopl_sirina(T),av)/np.sqrt(np.pi) #Fojtov normirani profil, u V0 0.56
    return F
y=[]
	 
x=np.linspace(0,Rk,1000)
y=opt_dub(np.sqrt(Rk*Rk-x*x),V0)
plt.suptitle('opticka dubina za razlicite paralelne preseke')
plt.xlabel('rastojanje prave od centra kome [m]')
plt.ylabel('opticka dubina')
plt.plot(x,y,'red')
plt.show()
