#VFörfattare Vilhelm 2F
#Skriv ett program som rekommenderar vilka kläder man ska ha på sig. Låt användaren mata in temperaturen och låt programmet skriva ut rekommenderad klädsel.

temp = int(input("Hur varmt är det? "))


#här kollar den vad användaren har skrivit in för tal och får utskrivet vad de sjka ha på sig under olika grader.
if 30 < temp < 50:
    print("Du behöver nog ingenting på dig")

elif 20 < temp < 30:
    print("Du kanske kan ta på dig en t-shirt")

elif 10 < temp < 20:
    print("Kanske en hoodie")

elif 0 < temp < 10:
    print("Ta på dig en jacka")

elif temp < 0:
    print("Det är för kallt ta på dig vinterkläder.")

elif temp > 50:
    print("Du kommer dö av en heat stroke")



