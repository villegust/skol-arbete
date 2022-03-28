##################################################################
#Författare Vilhelm 2F
#Användare ska skriva in ett tal och se om den är delbar på 3 och 5.
##################################################################


heltal = int(input("Vad är ditt tal? "))


#Här kollar den om det tal användaren har skrivit in är delbart med 3 och 5, bara 3 eller 5 eller inget av dem.
if heltal % 3 == 0 and heltal % 5 == 0:
    print("Talet går att dela på både 3 och 5")

elif heltal % 3 == 0:
    print("Talet går att dela på bara 3")

elif heltal % 5 == 0:
    print("Talet går bara att dela på 5")

else:
    print("Talet går inte att dela på 3 och 5")