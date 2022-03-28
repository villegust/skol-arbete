def shift(char, s): 

    #kollar om karaktärerna å ä ö är med i strängen
    if char == "å":
        return "å"
    
    elif char == "ä":
        return "ä"
    
    elif char == "ö":
        return "ö"
    
    elif char == "Å":
        return "Å" 
    
    elif char == "Ä":
        return "Ä"
    
    elif char == "Ö":
        return "Ö"

    elif ord(char) == 32:
            return chr(32)
    #kollar om karaktären är liten, skifter den och lägger in den i resultatet
    elif char.isupper():
        return chr((ord(char) + s - 65) % 26 + 65)

    #kollar om karaktären är stor, skifter den och lägger in den i resultatet
    elif char.islower():
        return chr((ord(char) + s - 97) % 26 + 97)

    else:
        return ""

def kryptera(text, s):
    txt = ""    
    #för varje karaktär skiftar den med ett antal
    for char in text:
        txt += shift(char, s)
    
    return txt

 
#1
def forcera(text):
    for antal_shiftningar in range(26):
        txt = kryptera(text, antal_shiftningar) 
        print(f"Antal skiftningar: {antal_shiftningar}")
        print(txt) #printar ut resultalten
        print("-" * 35)


 
fråga = input("Vad vill du göra. Tryck 1 om du vill kryptera med caesarchiffer eller 0 om du vill forcera en text: ")

if fråga == "1":
    text_som_ska_krypteras = input("Skriv vad du vill som ska krypteras: ")
    s = int(input("Hur många steg vill du shifta: "))

    krypterad_text = kryptera(text_som_ska_krypteras, s)
    print(f"Chiffer: {krypterad_text}")

elif fråga =="0":
    forced_text = input("Vad vill du forcera: ")
    forcera(forced_text)
