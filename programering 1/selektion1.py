#Författare Vilhelm 2F
#Programent om undersöker om ett inmatat tal är jämnt delbart med 7. Om det är jämnt delbart med 7 skrivs detta ut.

num = int(input("Vad är ditt nummer? "))

if num % 7 == 0:
    print("Det kan delas med 7")

else:
    print("Det går inte att dela på 7")