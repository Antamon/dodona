# Oefening 1 - Modeloplossing: De Poortwachter van Codeholm

wachtwoord = input("Geef het wachtwoord: ")
code = int(input("Geef je badgecode (geheel getal): "))
controle = int(input("Geef het controlegetal (geheel getal): "))

verwacht_wachtwoord = "AETHER"
verwacht_badge = 407

# berekening controlegetal volgens de regel
verwacht_controle = (badge // 10) + (badge % 10)

if wachtwoord != verwacht_wachtwoord:
    print("Fout wachtwoord.")
elif controle != verwacht_controle:
    print("Controlegetal klopt niet.")
elif code != verwacht_badge:
    print("Ongeldige code.")
else:
    print("Toegang verleend. De poort schuift open.")
