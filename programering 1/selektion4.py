#Författare Vilhelm 2F
#Programet ska låta användaren mata in sin ålder och priset på varan. Skriv sedan ut priset som användaren ska betala och hur mycket eventuell rabatt blir.

age = int(input("Vad är din ålder? "))
pris = int(input("Vad är priset på varan? "))
discount = 0.8

#kollar om din ålder är mindre än 12 eller mer än 65 och ger dig ditt nya pris
if age <= 65 or age >= 12:
    print("Du kommer att få rabatt på din vara." + " Ditt nya pris kommer att vara", pris * discount, "kr") 

else:
    print("Du kommer inte få någon rabatt" + " Ditt pris kommer att vara", pris, "kr")
