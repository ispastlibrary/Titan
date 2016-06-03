import matplotlib.pyplot as plt
import numpy as np
x,y,gr= np.loadtxt('barometarska.txt', unpack=True)
y1=[]
i=0

xs=np.zeros((200,200))
a=np.linspace(0.5,1.5,200)
b=np.linspace(0,0.5,200)
for a in range(200):
    s=0
    for b in range(200):
        for i in range (len(x)):
            y1=a*np.exp(-b*x[i])
            s += (y[i]-y1[i])**2/(2*gr[i]**2) 
        xs[a,b]=s



        
    

plt.scatter(x,y)
plt.show()
