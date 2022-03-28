#Författare Vilhelm
#Yatzy
inmatat_tal = int(input("Skriv ett tal du vill kontrollera: "))

är_primtal = True
for i in range(2, inmatat_tal):
    if inmatat_tal % i == 0:
        är_primtal = False

if är_primtal:
    print(inmatat_tal, "är ett primtal")

else:
    print(inmatat_tal, "är inte ett primtal")