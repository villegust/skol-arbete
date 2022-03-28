###################################################################
#Författare Vilhelm
#höjd. Skriv ett program som beräknar hur många gånger en sådan
#boll studsar innan den blir still.
###################################################################

start = int(input("Hur långt släpper du bollen ifrån (i meter)? "))

#Definerar vad stop och drop är.
drop = 0.7
studs = 0


#Kollar om det användaren har är större än 0,01. 
while start >= 0.01:
    start = start * drop    #Om den är större än 0,01 så ska den gångras med 0.7.
    studs = studs + 1         #Kollar hur många gånger bollen studsar med hjälp av hur långt man släpper bollen från.


#printar svaret.
print("Den kommer studsa", studs, "gånger.")

