#Författare Vilhelm Gustavsson
#Djurparken


for femhundrasedel in range(0, 66):
    hundrasedel = 65 - femhundrasedel    #kollar alla kombenationer av 100 och 500 sedlar.
    kostnad = 500 * femhundrasedel + 100 * hundrasedel  #den totala kostnaden
    
    #kollar när svaret blir 19700
    if kostnad == 19700:
        print("Det var", hundrasedel, "hundrasedlar och", femhundrasedel,  "femhundrasedel")



