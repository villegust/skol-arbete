#Författare Vilhelm
#Skriv ett program som läser in personnummer och avgör om det är en man eller kvinna.

personnummer = input("Skriv ditt personnummer. ")

personnummer_kvinna = personnummer[7:9] #Hittar den näst sista siffran

if int(personnummer_kvinna) % 2 == 0: #kollar om den siffran är helt delbart med 2
    print("Kvinna") # om ja så skriver den ut det

else: #annars skriver den ut detta.
    print("Man")