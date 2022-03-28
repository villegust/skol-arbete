#Författare Vilhelm 2F
#Programet ska fråga användaren efter ett tal. Ange om talet är större eller mindre än 10.

num = int(input("Vad är ditt nummer "))


#kollar om numeret användaren har skrivit in är större, lika med eller mindre än 10
if num > 10:
    print(str(num), "är större än 10")

elif num == 10:
    print(str(num), "är lika med 10")

else:
    print(str(num), "är mindre än 10")


#kollar om nummeret är mellan intervallerna.
if 0 < num < 10:
    print("Det ligger i intervallet 0-10")

elif 10 < num < 20:
    print("Det ligger i intervallet 10-20")

else:
    print("Det ligger i intervallet 20-30")