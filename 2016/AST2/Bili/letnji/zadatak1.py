import numpy as np
import matplotlib.pyplot as plt

Na=6.02*1e+23 #Avogadrov broj
M=23*1e-3 #molarna masa Na [kg/mol]
zastupljenost=3.34*1e-5 #maseni udeo Na u komi u odnosu na celu masu kome  
Rj=8*1e+3  #prosecni poluprecnik jezgra [m]
roj=600   #prosecna gustina jezgra [kg/m^3]
me=9.1e-31  #masa elektrona[kg]
T=5000  #temperatura [K]
Rk=5e+7 #poluprecnik kome kada je najveca [m]   
rok=1e-10 # gustina kome [kg/m^3]
ne=1e+15   #koncentracija elektrona   
#ako se uzme prosecni poluprecnik i gustina jezgra (Rj,roj) i ako se pretpostavi se sva materija iz jezgra rasprsi u komu, za max vrednost 
#poluprecnika kome (Rk) dobije se gustina 1e-9, tako da smo uzeli za red velicine manju gustinu (rok), jer ce gustina biti sigurno manja
#bilo zbog sublimacije, bilo zbog odbacivanja omotaca u medjuzvezdanu materiju itd. (GRUBA APROKSIMACIJA,ovo moramo da procenimo nekako...) 
k=1.38*1e-23 #Bolcmanova konstanta [J/K] 
dE=3.37*1e-19 # razlika energetskih stanja 3p i 3s, povezana sa talasnom duzinom [J] 
R=Na*k #Univerzalna gasna konstanta [J/(molK)]
L = 589.592e-9 #talasna duzina [m]
h=6.63*1e-34 #Plankova konstanta [Js]
c=3*1e+8 #brzina svetlosti [m/s]
A = 6.14e+7 #Ajnstajnov koef za verovatnocu spontane emisije[s^-1] (To smo nasli na Nistu (AKO JE TO, TO))
g0 = 1 # statisticka tezina 3s orbitale (s)
g1 = 3 # statisticka tezina 3p orbitale (px,py,pz)

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

N=1e+17 #ukupan broj atoma
Nna=0.912*N*pow(10,-5.82) #iz zastupljenosti Sunca, ukupan broj Na

print("ukupno svih atoma:",N,"ukupno natrijuma:",Nna)

def part_funk(a,T):  #izracunavanje part f-je
    K=0
    for i in range(6):
        K+=a[i]*pow(np.log(T),i) 
    Z=np.exp(K) 
    return Z

def Saha(T,ne): #broj neutralnih Na (NaI)
     n=Nna
     ZI=part_funk(a,T) #part f-ja za neutralne 
     ZII=part_funk(b,T)	#part f-ja za jednom jonizovane
     smena=pow(2*np.pi*me*k*T/(h*h),3/2)*np.exp(-Ejon/(k*T))*(ZII/ZI)*(2/ne)
     NaI=n/(smena+1)
     return NaI

	
def MaxBol(T): #broj Na u osnovnom 3s stanju (n0)        
    NaI=Saha(T,ne)
    print("neutralni Na:",NaI)  
    Z=part_funk(a,T)
    n0=(NaI*g0*np.exp(-E0/(k*T)))/Z
    return n0	

print("osnovno 3s stanje, a neutralni Na:",MaxBol(T))

