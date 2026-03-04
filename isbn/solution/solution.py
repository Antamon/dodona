d1 = int(input("Cijfer 1: "))
d2 = int(input("Cijfer 2: "))
d3 = int(input("Cijfer 3: "))
d4 = int(input("Cijfer 4: "))
d5 = int(input("Cijfer 5: "))
d6 = int(input("Cijfer 6: "))
d7 = int(input("Cijfer 7: "))
d8 = int(input("Cijfer 8: "))
d9 = int(input("Cijfer 9: "))
d10 = int(input("Controlecijfer: "))

som = (1*d1) + (2*d2) + (3*d3) + (4*d4) + (5*d5) + (6*d6) + (7*d7) + (8*d8) + (9*d9)

controle_berekend = som % 11

if controle_berekend != d10:
    print("Ongeldig ISBN-nummer.")
else:
    print("Geldig ISBN-nummer.")
