Bibliotheken, boekhandels en uitgevers gebruiken **ISBN-nummers** om boeken uniek te identificeren.  

Een ouder type ISBN bestaat uit **10 cijfers** en wordt een **ISBN-10** genoemd.  
Het laatste cijfer is geen willekeurig getal: het is een **controlecijfer** dat berekend wordt uit de eerste 9 cijfers.

Met dit controlecijfer kan een computersysteem snel controleren of een ISBN **correct werd ingevoerd**.  
Als één cijfer verkeerd wordt getypt, zal de controle meestal mislukken.

Jij schrijft een programma dat controleert of een ISBN-10 nummer geldig is.

---

# Input

Vraag aan de gebruiker **10 cijfers afzonderlijk**.

Gebruik de volgende variabelen:
- d1
- d2
- d3
- d4
- d5
- d6
- d7
- d8
- d9
- d10

Alle waarden zijn **1 cijfer**.

`d10` is het **controlecijfer**.

---

# Controleberekening

De controle gebeurt met de volgende formule: (1 x d1) + (2 x d2) + (3 x d3) + (4 x d4) + (5 x d5) + (6 x d6) + (7 x d7) + (8 x d8) + (9 x d9)

Daarna bereken je van die som, de **rest bij deling door 11 (modulus)**. Bijvoorbeeld de restwaarde (modulus) van 35 gedeeld door 11 is 2.

# Controle

Vergelijk het berekende controlecijfer met het ingegeven controlecijfer (`d10`).

Als controle_berekend niet gelijk is aan **d10**, toont het programma:
  > Ongeldig ISBN-nummer.

anders toont het programma
  > Geldig ISBN-nummer.
