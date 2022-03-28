#Författare Vilhelm Gustavsson
#Listor Del A

import random

d = int(input("Hur många dagar ska du hämta data från: "))

a = float(input("Skriv in din undre gräns: "))
b = float(input("Skriv in din övre gräns: "))

tider = ["07:00", "12:00", "19:00", "02:00"]

def generate(d, a, b):
    temperatur = []
    for i in range(d):
        dagar = []
        for n in range(d):
            dagar.append(random.randint(a * 10, b * 10) / 10)
        
        temperatur.append(dagar)
        return temperatur

def tabell(temp):
    dag = 1
    print("Tid\t", end="")
    for n in temp:
        print(f"dag {dag:2}", end="")
        dag += 1

    print()

    for x in range(d):
        for n in range(4):
            print(f"{temp, [dag], [tider]}\t", end="")
    print()
