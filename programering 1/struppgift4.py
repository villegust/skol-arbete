#Författare Vilhelm
    # Skriv ett program som läser in en mening, bestående av minst två ord. Programmet ska
    # sedan visa ett meddelande där det dels talar om hur många tecken användaren skrev
    # och dels talar om vilket som var det första resp. det sista ordet. Du får anta att det står
    # (minst) ett blankt tecken mellan varje ord. Det kan också finnas blanktecken före det
    # första ordet och efter det sista.

mening = str(input("Vad är din mening? "))

ord = mening.split() #det delar upp ord i en lista.

if len(ord) < 2: #kollar så att det är mer än ett ord
    print("Det måste vara 2 ord")

else:
    print("Första och sista ordet är:", ord[0], ord[-1]) # kollar första och sista ordet
    print("Det var", len(mening), "tecken.") #kolar hur många tecken som finns.
