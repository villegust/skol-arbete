#Författare Vilhelm 2F
#Detta program ska låta användaren mata in hur tre lampknappar ska ställas. Varje lampknapp kan vara antingen av (0) eller på (1). 



knapp1 = int(input("On eller off (1 eller 0)? "))
knapp2 = int(input("On eller off (1 eller 0)? "))
knapp3 = int(input("On eller off (1 eller 0)? "))


#kollar vilka knappar användaren har skrivit är av och på 
if knapp1 == 1 and knapp2 == 1 and knapp3 == 0:
    print("Lampa 1 lyser")

elif knapp1 == 0 and knapp2 == 1 and knapp3 == 1:
    print("Lampa 2 lyser.")

elif knapp1 == 1 and knapp2 == 1 and knapp3 == 1:
    print("Alla lampor lyser")

else:
    print("Inga lampor är tända")
