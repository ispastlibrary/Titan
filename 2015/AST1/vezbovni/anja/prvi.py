broj = 42
initial = -1

while initial!=broj :
    initial = int(input("unesite broj: "))
    if initial < broj:
        print("broj je manji")
    elif initial > broj:
        print (" broj je veci")
    else:
        print("bravo")

