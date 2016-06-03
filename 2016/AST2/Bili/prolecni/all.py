import pylab as pl
from scipy import interpolate


i=0
p1=0
p2=0
wavelen=[]
intens=[]

g=open('NUM_PS_2_Podaci.txt','r')

while (i<100):
    line=g.readline()
    linel=line.split(" ")
    wavelen.append(float(linel[0]))
    intens.append(float(linel[1]))
    i+=1
pl.scatter(wavelen,intens,c='blue',label='podaci')


tck=interpolate.splrep(wavelen,intens)
#intens_spline=interpolate.splev(wavelen,tck,der=0)
pl.plot(wavelen,tck,'red',label='cubic spline')


def lin_f(x):
    y=y0+((y1-y0)*(x-x0))/(x1-x0)
    return y 
def simp_int(a,b):
    area=((b-a)/6)*(lin_f(a)+4*lin_f((a+b)/2)+lin_f(b))
    return area 

i=98
while (i>=0):
    x0=wavelen[i]
    y0=intens[i]
    x1=wavelen[i+1]
    y1=intens[i+1]
    p1+=interpolate.splint(x0,x1,tck)
    a=x1
    b=x1		
    dx=(x1-x0)/6
    j=0	
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

EW1=(wavelen[99]-wavelen[0])-p1
EW2=(wavelen[99]-wavelen[0])-p2	
	
g.close()
print('cubic spline:',EW1,'linear interpolation:',EW2)
