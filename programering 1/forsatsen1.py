#Författare Vilhelm
#Träna for satsen
#Skriv ett program som läser in ett heltal n och som beräknar summan,
#1+4+9+16+....+n^2. TIPS n^2 = n*n.

num = int(input("Vad är ditt heltal? "))
k = 0
sum = 0

#Kollar vilket ta användaren har skrivit
for n in range(0, num + 1):
    sum += k ** 2
    k = k + 1

print("Summan blir", sum)