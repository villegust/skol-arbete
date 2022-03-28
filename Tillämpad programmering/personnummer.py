from math import ceil

pers_nummer = input("Skriv in ditt personnummer: ")

pers_lista = list(pers_nummer)

pers_lista_2 = pers_lista[-10:-1]

print(pers_nummer)

i = 0
siffer_summa = 0

# while i > len(pers_lista_2):
#     if pers_lista_2[i] % 2 == 0:
#         siffer_summa = pers_lista_2 * 2 
#         if 
    
#     else:
#         siffer_summa = pers_lista_2 * 1

for idx, val in enumerate(pers_lista_2):
    if not ((idx + 1)&1 == 0):
        if int(val) * 2 > 9:
            for n in str(int(val) * 2):
                siffer_summa += int(n)
        else:    
            siffer_summa += int(val) * 2
    else:
        siffer_summa += int(val)

kontroll_siffra = (ceil(siffer_summa/ 10) * 10) - siffer_summa

print(f"Kontrollsiffran är {kontroll_siffra}")

if kontroll_siffra == int(pers_lista[-1]):
    print(f"Det stämmer!")

else:
    print(f"Det stämmer inte!")