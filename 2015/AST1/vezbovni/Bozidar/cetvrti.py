pi=3.141592

def Povrs(r):
    P = r**2 * pi
    print(P)
    return P

def Obim(r):
    O = 2 * r * pi
    print(O)
    return O

def PovrsPravougaonik(A, B):
    P = A * B
    print(P)
    return P

def IPovrsIObim(r):
    P = Povrs(r)
    O = Obim(r)
    print(P,0)
    return P, O
