# Oefening 1: De Poortwachter van Codeholm

In de stad **Codeholm** staat een oude metalen stadspoort die bewaakt wordt door een poortwachter.  
Om de stad binnen te mogen, moet een reiziger drie controles doorstaan:

1. Het **juiste wachtwoord**
2. Een **code**
3. Een **controlegetal**

Als één van deze controles niet klopt, weigert de poortwachter je toegang en zegt hij **waarom** je niet binnen mag.

Schrijf een Python-programma dat deze controle uitvoert.

---

## Input

Vraag aan de gebruiker:

1. Het **wachtwoord** (tekst)
2. De **code** (een geheel getal)
3. Het **controlegetal** (een geheel getal)

---

## Regels

De poort werkt volgens de volgende regels:

- Het juiste wachtwoord is `"Seismologie"`

- De juiste code is `404`

- Het **controlegetal** moet gelijk zijn aan:
    - code gedeeld door 10 zonder restwaarde
    - plus de restwaard van de code gedeeld door 10

Bijvoorbeeld:
  - de gehele deling van 632 door 10 is 63 (de 0.2 valt weg)
  - de restwaarde van de gehele deling van 632 door 10 is 2 (modulus!)
  - het juiste controlegetal is 63 + 2 = 65

---

## Output

Je programma moet **exact één boodschap** tonen.

Controleer in deze volgorde:

1. Als het wachtwoord **niet gelijk** is aan `"Seismologie"`:
    > Fout wachtwoord.

2. Anders, als het controlegetal **niet gelijk** is aan de berekende waarde:
    > Controlegetal klopt niet.

3. Anders, als de code **niet gelijk** is aan `404`:
    > Ongeldige code.

4. Als alles correct is:
    > Toegang verleend. De poort schuift open.
