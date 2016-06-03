broj = 42
initial = -1
while initial != broj:
    initial = int(input("Unesite broj: "))
    if initial < broj:
        print("Broj je manji!")
    elif initial > broj:
        print("Broj je veci!")
    else:
        print("Bravo!")
