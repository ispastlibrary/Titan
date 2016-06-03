import numpy as np
#import  matplotlib.pyplot as plt
l,t2, omega = np.loadtxt('merenja.txt.save', unpack=True)
sum_w = np.sum(omega)
sum_wy = np.sum(omega * t2)
sum_xwy = np.sum(l*t2*omega)
sum_wx = np.sum(omega*l)
sum_wx2 = np.sum(omega*l*l)
sum_na2 = sum_wx**2


brojilac = sum_xwy * sum_w - sum_wx * sum_wy
imenilac = sum_w * sum_wx2 - sum_na2

b = brojilac/imenilac
db = (sum_w/imenilac)**1/2

a  = (sum_wy/sum_w) - b*(sum_wx/sum_w) 
da = (sum_wx2/imenilac)**1/2
 
print(a,da) 
#def fun(x, a, b):
    
# return a + b*x

#print(a, b)


#x = np.arange(0.1, 1.1, 0.15)
#fun(x, a, b)


#l1 = np.linspace(0.1, 1.1, 1000)

#print(l1)

#plt.plot(l1, fun(l1, a, b), '-r', label = 'fit')
#plt.errorbar(l, t2, yerr = dt2, fmt = 'o')
#plt.legend(loc = 'best')
#plt.xlabel('l[m]')
#plt.ylabel('T^2[s^2]')
#plt.title('Zavisnost kvadrata perioda matematickog klatna od njegove duzine')
#plt.show()
