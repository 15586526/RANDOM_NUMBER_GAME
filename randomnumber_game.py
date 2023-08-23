import random
random_number=round(random.random()*50)

print(str(random_number)[0])    ##"str" İLE İLK KARAKTERİ "STRİNG"E ÇEVİRİYORUZ YANİ İLK KARAKTER GÖZÜKMÜCEK!!!!
      
input_number =int(input("Enter a number between 0 and 50:"))

while random_number != input_number:
    if input_number > random_number:
        print("YOU ENTERED A LARGE NUMBER")
    else:
        print("YOU ENTERED A SMALL NUMBER")
    input_number=int(input("Enter a number between 0 and 50:"))
print("YOU ARE WON!")

