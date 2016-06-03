from const1 import *

N_tacaka = 200
T=300
V1 = c/(589.1e-9)
V2 = c/(588.9e-9)
dV = (V2 - V1)/N_tacaka

def E_W(x,y):
    EW=0
    tck=interpolate.splrep(x,y)
    i=0
    while(i<(N_tacaka-1)):
        EW+=interpolate.splint(x[i],x[i+1],tck)
        i+=1 
    return EW
	

def FWHM_G(T): #sirina na polovini max visine Gausa
    gamma_G=Dopl_sirina(T)  #scale parametar za Gausa
    Gg=2*np.sqrt(np.log(2))*gamma_G
    return Gg
# SAMO PRIRODNO SIRENJE!!!!!!!!!!!!! POSLE UBACITI STARKOVO I/ILI VAN DER WALSOVO SIRENJE USLED PRITISKA
def FWHM_L(L0): #sirina na polovini max visine Lorenca 
    gamma_L=A  #scale parametar za Lorenca, Rutten (3.45) 
    Gl=gamma_L/(2*np.pi)
    return Gl
T1=300
T2=600
T3=900
	
av1 = (A+vd_vals(nh)+stark(Nswe,Tswe))/Dopl_sirina(T1)
av2 = (A+vd_vals(nh)+stark(Nswe,Tswe))/Dopl_sirina(T2)
av3 = (A+vd_vals(nh)+stark(Nswe,Tswe))/Dopl_sirina(T3)

print(A,vd_vals(nh),stark(Nswe,Tswe),Dopl_sirina(T))

x = []; y = []; z = []; q = []

V = V1
for i in range(N_tacaka):
    y.append(izlazni(V,av1,T1))
    z.append(izlazni(V,av2,T2))
    q.append(izlazni(V,av3,T3))
    x.append(c/V)
    V += dV

x.reverse()
y.reverse()
z.reverse()
q.reverse()

print(E_W(x,z),'Prirodno+termalno',E_W(x,y),'pr+ter+vdW+S',E_W(x,q),'sve bez vdvw')
#print(av2, 'aPrirodno', av1, 'avdW+S')
plt.plot(x, y,'red')
plt.plot(x,z,'blue',lw=2)
plt.plot(x,q,'green')
plt.show()

