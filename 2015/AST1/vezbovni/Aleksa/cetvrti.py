pi = 3.14159265
def povrs(a,b):
    P = a*b
    print("Za vrednost a i b: ", a, b)
    print("Povrsina je: ", P)
    return P

prvi=povrs(3,6)
drugi=povrs(4,12)

def Obim(a,b):
     O=2*a+2*b
     print("Za vrednost a i b: ", a, b)
     print("Obim je : ", O)
     return O

x=Obim(3,7)
y=Obim(33,6)

def Obimkruga(r):
    Z=2*r*pi
    print ("Za vrednost r: ", r)
    print("Obim kruga je: ", Z)
    return Z

D=Obimkruga(4) 

def CuFiRiK(C):
    F=C*9/5+32
    R=C*4/5
    K=C+273
    print("Za vrednost Celzijusa: ", C)
    print("Farenhajta je: ", F)
    print("Reomira je: ", R)
    print("Kelvina je: ", K)
    return F
    return R
    return K

E=CuFiRiK(45)
T=CuFiRiK(22)
