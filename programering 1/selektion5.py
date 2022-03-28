year = int(input("Vad är ditt årtal du vill kolla om det är skottår? "))


#kollar om året är delbart med 4 och 400 men inte med 100
if year % 400 == 0 or year % 4 == 0 and year != 0:
    print("År", year, "är ett skottår")

else:
    print("År", year, "är inte ettskottår")
