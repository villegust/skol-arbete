#Författare Vilhelm
#Skriv ett program som visar en tabell med värdena för uttrycket 2x^2 − 5x + 1.

#en funktion som funktionerar matte
def f(x):
    return 2 * x ** 2 - 5 * x + 1 

print("Värderna för f(x) = 2x^2 - 5x + 1 om x är mellan -10 och 10")

#kollar vad svaret blir mellan nummerna -10 och 10
for n in range(-10, 11):
    print(f"{f(n)}", end=", ")
