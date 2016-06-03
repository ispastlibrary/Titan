import math
import numpy as np
import pylab as pl
from scipy import interpolate

wavelen=[]
intens=[]

g=open('NUM_PS_2_Podaci.txt','r')

i=0
p1=0
p2=0

while (i<100):
    line=g.readline() 
    linel=line.split(" ") 
    wavelen.append(float(linel[0]))
    intens.append(float(linel[1]))
    i+=1	
pl.scatter(wavelen,intens,'blue')


tck=interpolate.splrep(wavelen,intens,s=0)
x1=wavelen
y1=interpolate.splev(wavelen,tck,der=0)

pl.plot(x1,y1,'red')

i=0
while(i<99):
    p+=interpolate.splint(wavelen[i],wavelen[i+1],tck)
    #print(p)
    i+=1
#EW=((wavelen[99]-wavelen[0])-p)
#print(EW)


pl.xlim(wavelen[0]-0.03,wavelen[99]+0.03)
pl.ylim(0.77,1.01)
g.close()
pl.show()
