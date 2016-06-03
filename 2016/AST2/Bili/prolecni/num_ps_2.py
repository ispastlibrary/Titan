import pylab as pl
from scipy import interpolate


i=0
p1=0
p2=0
wavelen=[]
intens=[]

g=open('NUM_PS_2_Podaci.txt','r')  #otvaranje fajla za citanje

while (i<100): #citanje iz fajla
    line=g.readline()
    linel=line.split(" ")
    wavelen.append(float(linel[0]))
    intens.append(float(linel[1]))
    i+=1
pl.scatter(wavelen,intens,c='blue',label='podaci') #graficki prikaz uredjenih parova iz seta podataka wavelen[i],intens[i]   


tck=interpolate.splrep(wavelen,intens,k=3) #funkcija koja vraca osobine funkcije: koordinate tacaka kroz koje prolazi interpolirajuca polinomna funkcija spline
#, koeficijente polinoma i stepen polinoma (po default-u je polinom treceg stepena)  
intens_spline=interpolate.splev(wavelen,tck,der=0) #za dato x vraca f(x), a kao argument uzima i osobine polinoma (tck), kao i stepen izvoda
pl.plot(wavelen,intens_spline,'red',label='cubic spline')

#jednacina prave kroz dve tacke
def lin_f(x):
    y=y0+((y1-y0)*(x-x0))/(x1-x0)
    return y 
#Simpsonovo pravilo za numericko resavanje odredjenog integrala u intervalu [a,b]
def simp_int(a,b):
    area=((b-a)/6)*(lin_f(a)+4*lin_f((a+b)/2)+lin_f(b))
    return area 

i=98
#racunanje integrala   
while (i>=0):
    x0=wavelen[i]
    y0=intens[i]
    x1=wavelen[i+1]
    y1=intens[i+1]
    p1+=interpolate.splint(x0,x1,tck)  #f-ja vraca vrednost integrala u intervalu [x0,x1], za interpolirajucu polinomnu funkciju 
    a=x1
    b=x1		
    dx=(x1-x0)/6
    j=0	
	#linearna interpolacija na +5 tacaka, i racunanje integrala pomocu Simpsonovog pravila
    while (j<=5):	
        a-=dx
        if (j!=5):
            wavelen.append(a)
            intens.append(lin_f(a))
        p2+=simp_int(a,b)
        b=a
        j+=1
    i-=1
pl.plot(wavelen,intens,'green',label='linearna interpolacija')
pl.xlabel('talasna dužina')
pl.ylabel('fluks zračenja')
pl.xlim(wavelen[0]-0.03,wavelen[99]+0.03)
pl.ylim(0.77,1.01)
pl.legend(loc='best')
pl.show()

EW1=(wavelen[99]-wavelen[0])-p1 #p1 je povrsina ispod grafika funkcije cubic spline, a za apsorpcionu liniju je neophodno izracunati povrsinu iznad grafika      
EW2=(wavelen[99]-wavelen[0])-p2	#p2 je porvsina ispod grafika linearne funkcije na malim intervalima    
	
g.close()
print('cubic spline:',EW1,'linear interpolation:',EW2)
