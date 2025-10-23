# Invoer
naam = input("Wat is je naam? ")
bananen = int(input("Hoeveel bananen wil je? "))
aardbeien = int(input("Hoeveel aardbeien wil je? "))
korting = float(input("Hoeveel procent korting krijg je? "))

# Berekeningen
prijs_bananen = bananen * 0.40
prijs_aardbeien = aardbeien * 0.25
totaal = prijs_bananen + prijs_aardbeien

# Korting toepassen
totaal = totaal - (totaal * korting / 100)

# Afronden op 2 cijfers
totaal = round(totaal, 2)

# Output met concateneren
print("Hallo " + naam + ", je smoothie kost " + str(totaal) + " euro.")
