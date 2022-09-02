import time
from random import*

rand=randint(1, 100)
sayac=0
 
while True:
    sayac+=1
    sayi=int(input("1 ile 100 arasında değer girin (0 Çıkış):"))
    if(sayi==0):
        print("Oyunu İptal Ettiniz")
        time.sleep(1)
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        time.sleep(1)
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        time.sleep(1)
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))