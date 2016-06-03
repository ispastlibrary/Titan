import numpy as np
import matplotlib.pyplot  as plt

x, y, sigma = np.loadtxt("barometarska.txt", unpack= True, delimiter = " ")

plt.plot(x,y)
plt.show()

l = len(x)
a = 1.3
b = 0.068

def f(a,b,x):
    return a*(np.exp(-b*x))

def hi(a,b,x,y,sigma,l):
    s = 0
    for i in range(0,l):
        hi =((y[i]-f(a,b,x[i]))**2)/(2*sigma[i]*sigma[i])
        s = s + hi
    return s

m = hi(1.3,0.068, x, y, sigma, l)
m1=hi(1.2,0.007400000000000004,x,y,sigma,l)
#print(m);
#print(m1);
min=m
i=0.5
inda=0
indb=0
while i<1.5:
    j=0.001
    while j<0.01:
        a=i;
        b=j;
        min = hi(a,b,x,y,sigma,l);
        #print(min);
        if min < m:
            m=min;
            inda=i
            indb=j
        j+=0.0001
    i+=0.01
print(inda);
print(indb);

plt.errorbar(x, y, yerr = sigma, fmt= "o")
plt.plot(x,inda*np.exp(-indb*x),color = 'red')
plt.show()
