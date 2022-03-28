#Författare vilhelm
#uppgift 8

#användaren skriver in sin vikt
kg = float(input("Hur mycket väger du? "))

#kollar om det användaren har skrivit stämmer in med påståenden nedan.
if kg < 20:
    print("Du kommer behöva", kg * 0.05, "mg medicin")

if 20 <= kg <= 40:
    print("Du kommer behöva", kg * 0.1, "mg medicin")

if kg > 40:
    print("Du kommer behöva", kg * 0.15, "mg medicin")  