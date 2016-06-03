import numpy as np
import pylab as pl
import math

G=1
m1=1
m2=1
m3=1
dt=10e-8
A=[0]*169677
B=[0]*169677
C=[0]*169677
D=[0]*169677
E=[0]*169677
F=[0]*169677


A[0]=r1x=-0.6099928070 
B[0]=r1y=0 
C[0]=r2x=1.5896276310
D[0]=r2y=0 
E[0]=r3x=-0.9796348240
F[0]=r3y=0

v1x=0
v1y=1.5049370344
v2x=0 
v2y=0.1478049666
v3x=0 
v3y=-1.6527420010

i=1
k=0


alpha = math.pow(math.sqrt(math.pow(r2x-r1x,2)+math.pow(r2y-r1y,2)),3)
beta = math.pow(math.sqrt(math.pow(r3x-r1x,2)+math.pow(r3y-r1y,2)),3)
gama = math.pow(math.sqrt(math.pow(r3x-r2x,2)+math.pow(r3y-r2y,2)),3)

while (i < 169677):
    b1x = a1x = (G*m2*(r2x-r1x))/alpha + (G*m3*(r3x-r1x))/beta
    b1y = a1y = (G*m2*(r2y-r1y))/alpha + (G*m3*(r3y-r1y))/beta
    b2x = a2x = (G*m1*(r1x-r2x))/alpha + (G*m3*(r3x-r2x))/gama
    b2y = a2y = (G*m1*(r1y-r2y))/alpha + (G*m3*(r3y-r2y))/gama
    b3x = a3x = (G*m1*(r1x-r3x))/beta + (G*m2*(r2x-r3x))/gama
    b3y = a3y = (G*m1*(r1y-r3y))/beta + (G*m2*(r2y-r3y))/gama

    r1x += v1x*dt + (a1x*dt)/2
    r1y += v1y*dt + (a1y*dt)/2
    r2x += v2x*dt + (a2x*dt)/2
    r2y += v2y*dt + (a2y*dt)/2
    r3x += v3x*dt + (a3x*dt)/2
    r3y += v3y*dt + (a3y*dt)/2

    alpha = math.pow(math.sqrt(math.pow(r2x-r1x,2)+math.pow(r2y-r1y,2)),3)
    beta = math.pow(math.sqrt(math.pow(r3x-r1x,2)+math.pow(r3y-r1y,2)),3)
    gama = math.pow(math.sqrt(math.pow(r3x-r2x,2)+math.pow(r3y-r2y,2)),3)

    a1x = (G*m2*(r2x-r1x))/alpha + (G*m3*(r3x-r1x))/beta
    a1y = (G*m2*(r2y-r1y))/alpha + (G*m3*(r3y-r1y))/beta
    a2x = (G*m1*(r1x-r2x))/alpha + (G*m3*(r3x-r2x))/gama
    a2y = (G*m1*(r1y-r2y))/alpha + (G*m3*(r3y-r2y))/gama
    a3x = (G*m1*(r1x-r3x))/beta + (G*m2*(r2x-r3x))/gama
    a3y = (G*m1*(r1y-r3y))/beta + (G*m2*(r2y-r3y))/gama

    v1x += ((b1x+a1x)*dt)/2
    v1y += ((b1y+a1y)*dt)/2
    v2x += ((b2x+a2x)*dt)/2
    v2y += ((b2y+a2y)*dt)/2
    v3x += ((b3x+a3x)*dt)/2
    v3y += ((b3y+a3y)*dt)/2

    print(r1x, r1y, r2x, r2y, r3x, r3y)
    
    A[i] = r1x
    B[i] = r1y
    C[i] = r2x
    D[i] = r2y
    E[i] = r3x
    F[i] = r3y

    i+=1    

pl.plot(A, B)
pl.plot(C, D)
pl.plot(E, F)
pl.show()
