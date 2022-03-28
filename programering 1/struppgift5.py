#Författare Vilhelm
#Skriv ett program som läser in ett personnummer och skriver ut meddelandet: Grattis!
#Om den aktuella personen har födelsedag. Personnummer anges med 10 siffror (utan
#minustecken).

personnummer = input("Vad är ditt personnummer? ")

dd = personnummer[4:6] #kollar var datumet är 
mm = personnummer[2:4] #kollar var månaden är 

datum = "2020-09-25"

datum_mm = datum[5:7] #kollar var månaden är 
datum_dd = datum[8:10] #kollar var dagen är 

if dd == datum_dd and mm == datum_mm: #kollar om dagen och månaden du har skrivit in stämmer med det andra datumet
    print("Grattis, du fyller år idag!")

else:
    print("Du fyller inte år idag")