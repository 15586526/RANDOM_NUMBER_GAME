import random
rastgelesayı_olusturuyobusalak=round(random.random()*50)

print(str(rastgelesayı_olusturuyobusalak)[0])   
      
numarayı_girlan =int(input("0 ile 50 arasında bir sayı gir bakma öyle:"))

while rastgelesayı_olusturuyobusalak != numarayı_girlan:
    if numarayı_girlan > rastgelesayı_olusturuyobusalak:
        print("Büyük sayı girdin bro")
    else:
        print("Küçük sayı girdin bro")
    numarayı_girlan=int(input("0 ile 50 arasında bir sayı gir bakma öyle:"))
print("HADİ YİNE İYİSİN AMK KAZANDIN")

