def fahr(a):
    F = (9.0/5)*a + 32
    print("temperatura je: ", F)
    return F

def cels(a):
    C = (a-32)*(5/9)
    print("temperatura je:", C)
    return C

prvo = fahr(100)
drugo = cels(212)


