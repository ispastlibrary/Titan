def Celzijus(F):
    C = (F - 32) / 1.8
    print(C)
    return C

def Farenhajt(C):
    F = C * 1.8 + 32
    print(F)
    return F


x = Celzijus(90)
y = Farenhajt(35)
