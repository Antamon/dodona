Hieronder staat de **ruwe Markdown broncode**. Je kan dit rechtstreeks kopiëren naar je leerplatform of GitHub.

# De Digitale Kluis

Je schrijft een Python-programma dat een geheime code beveiligt.  
De code bestaat uit **drie cijfers** die al vastliggen in het programma:

```python
cijfer1 = 3
cijfer2 = 7
cijfer3 = 1
```

De gebruiker moet deze code **cijfer per cijfer** raden.

De gebruiker mag onbeperkt proberen, maar het aantal pogingen moet worden bijgehouden.

---

## Wat moet je programma doen?

### 1️⃣ Start van het programma

Wanneer het programma start, verschijnt:

```
Welkom bij het kluis-spel!
Raad de drie cijfers in de juiste volgorde.
```

---

### 2️⃣ Eerste cijfer raden

Daarna vraagt het programma:

```
Raad het eerste cijfer:
```

- Als het antwoord **fout** is:

```
Fout. Probeer opnieuw.
Raad het eerste cijfer:
```

Dit blijft herhalen tot het juiste cijfer wordt ingevoerd.

- Als het antwoord **juist** is:

```
Eerste cijfer correct!
```

Pas daarna mag het programma verdergaan naar het tweede cijfer.

---

### 3️⃣ Tweede cijfer raden

Het programma toont:

```
Raad het tweede cijfer:
```

- Bij een fout antwoord:

```
Fout. Probeer opnieuw.
Raad het tweede cijfer:
```

- Bij een correct antwoord:

```
Tweede cijfer correct!
```

---

### 4️⃣ Derde cijfer raden

Het programma toont:

```
Raad het derde cijfer:
```

- Bij een fout antwoord:

```
Fout. Probeer opnieuw.
Raad het derde cijfer:
```

- Bij een correct antwoord:

```
Derde cijfer correct!
```

---

### 5️⃣ Wanneer de volledige code geraden is

Op het einde verschijnt:

```
Proficiat, u heeft de code geraden in X beurten!
```

**X** is het totaal aantal keren dat de gebruiker een cijfer heeft ingevoerd.  
Elke invoer telt als één poging, ook als die fout is.

---

## 💡 Denk eerst even na

- Wanneer moet je de teller verhogen?
- Wanneer stopt een `while`-lus?
- Wat betekent `!=` precies?

```

```
