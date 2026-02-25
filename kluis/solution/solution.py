# Geheime code
cijfer1 = 3
cijfer2 = 7
cijfer3 = 1

pogingen = 0

print("Welkom bij het kluis-spel!")
print("Raad de drie cijfers in de juiste volgorde.\n")

# Eerste cijfer
gok = int(input("Raad het eerste cijfer: "))
pogingen += 1

while gok != cijfer1:
    print("Fout. Probeer opnieuw.")
    gok = int(input("Raad het eerste cijfer: "))
    pogingen += 1

# Tweede cijfer
gok = int(input("Raad het tweede cijfer: "))
pogingen += 1

while gok != cijfer2:
    print("Fout. Probeer opnieuw.")
    gok = int(input("Raad het tweede cijfer: "))
    pogingen += 1

# Derde cijfer
gok = int(input("Raad het derde cijfer: "))
pogingen += 1

while gok != cijfer3:
    print("Fout. Probeer opnieuw.")
    gok = int(input("Raad het derde cijfer: "))
    pogingen += 1

print(f"Proficiat, u heeft de code geraden in {pogingen} beurten!")
