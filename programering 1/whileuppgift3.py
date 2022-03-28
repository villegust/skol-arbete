##########################################################
#Författare Vilhelm
#Skriv ett program som läser in ett heltal n och som 
# beräknar den sk. harmoniska serien 1/1+1/2+1/3+....+1/n
#########################################################

n = int(input("Nummer? "))

summa = 0
k = 1   

while k<= n:
    summa = summa + 1 / k
    k = k + 1                  

print("Summan blir", summa)