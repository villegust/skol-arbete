###########################################################
#Författare Vilhelm
# Beräkning av summan 1+4+9+16+....+n^2.
###########################################################

n= int(input("Nummer? "))

summa = 0
k = 1   

while k<= n:
    summa = summa + k ** 2     #Ökar k med 2
    k = k + 1                  #Plusar på ett till k

print("Summan blir", summa)