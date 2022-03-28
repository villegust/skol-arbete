#Författare Vilhelm
#Detta program som läser in ett flyttal (flyt-tal är decimaltal) som representerar bruttoinkomst och beräknar nettoinkomst

skattesats = 0.3

#skriver in din bruttoinkomst
bruttolön = int(float(input("Bruttoinkomst: ")))

nettolön = (bruttolön - bruttolön * skattesats)

#här räknas din nettolön ut
print("Din nettolön är", nettolön)
