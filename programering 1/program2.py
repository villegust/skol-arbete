#Författare Vilhelm
#Detta program ska frågar användaren efter ett heltal och sedan skriver ut om talet är udda eller jämt.

num = int(input("Write a number "))

#Här räknar den ut om det är ett hel eller udda tal.

if (num % 2) == 0:
    print("It's a even number")

else:
    print("It's a odd number")