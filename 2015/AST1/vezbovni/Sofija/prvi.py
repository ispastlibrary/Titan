#!/usr/bin/python3
broj = 23
initial = -5

while initial!=broj:
    initial = int(input('unesite broj'))
    if initial < broj:
        print("Broj je manji!")
    elif initial > broj:
        print("Broj je veci!")
    else:
        print("Bravo!!")
