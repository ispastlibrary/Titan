import pylab as pl
x=[1,2,3]
y=[5,8,9]
pl.plot(x,y,'green')
x.append(4)
y.append(15)
pl.plot(x,y,'blue')
pl.show()
