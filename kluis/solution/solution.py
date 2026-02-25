# Geheime code
cijfer1 = 3
cijfer2 = 7
cijfer3 = 1

pogingen = 0

print("Raad de drie cijfers in de juiste volgorde.\n")

# Eerste cijfer
gok = int(input("Raad het eerste cijfer: "))
pogingen += 1

while gok != cijfer1:
    gok = int(input("Raad het eerste cijfer opnieuw: "))
    pogingen += 1

# Tweede cijfer
gok = int(input("Raad het tweede cijfer opnieuw: "))
pogingen += 1

while gok != cijfer2:
    gok = int(input("Raad het tweede cijfer opnieuw: "))
    pogingen += 1

# Derde cijfer
gok = int(input("Raad het derde cijfer: "))
pogingen += 1

while gok != cijfer3:
    gok = int(input("Raad het derde cijfer: "))
    pogingen += 1

print(f"Proficiat, u heeft de code geraden in {pogingen} beurten!")
