
import time

class Bilgisayar():
    
    def __init__(self,Pc_durum = "Kapalı",pc_ekran = "Ekran Kapalı",uygulamalar = "Chrome",uygulama_listesi = ["Chrome"]):
        
        self.Pc_durum = Pc_durum
        self.pc_ekran = pc_ekran
        self.uygulamalar = uygulamalar
        self.uygulama_listesi = uygulama_listesi
        
    def Pc_aç(self):
        if (self.Pc_durum == "Açık"):
            print("Pc zaten açık.")
        else:
            print("Pc Açılıyor...")
            self.Pc_durum = "Açık"
            
    def Pc_kapat(self):
        if (self.Pc_durum == "Kapalı"):
            print("Pc zaten kapalı")
        else:
            print("Pc kapanıyor...")
            self.Pc_durum = "Kapalı"
            
    def pc_ekran_aç (self):
        if (self.pc_ekran == "Ekran Açık"):
            print("Ekran zaten açık")
        else:
            print("Ekran açılıyor...")
            self.pc_ekran = "Ekran Açık"
            
    def pc_ekran_kapat (self):
        if (self.pc_ekran == "Ekran Kapalı"):
            print("Ekran zaten kapalı")
        else:
            print("Ekran kapanıyor...")
            self.pc_ekran = "Ekran Kapalı"
            
    def uygulama_ekle(self,uygulama_ismi):
        print("Uygulama Ekleniyor...")
        time.sleep(1)
        
        self.uygulama_listesi.append(uygulama_ismi)
        print("Uygulama Eklendi...")
        
    def __len__ (self):
        return len(self.uygulama_listesi)
    
    def __str__(self):
        return "PC Durumu: {}\nUygulama Listesi: {}\nŞu anki uygulama: {}\nPc Ekran: {}\n".format(self.Pc_durum,self.uygulama_listesi,self.uygulamalar,self.pc_ekran)
    

bilgisayar = Bilgisayar()

print("""
      Bilgisyar Uygulaması
      
      1. PC Aç\n
      2. PC Kapat\n
      3. Uygulama Ekle\n
      4. Uygulama Sayısını Öğrenme\n
      5. Ekran AÇ\n
      6. Ekran Kapat\n
      7. Bilgisayar Bilgileri\n
      
    Çıkmak İçin 'q' ya basın.      
      """)

while True:
    işlem = input("İşlem seçiniz:")
    
    if (işlem == "q"):
        print("Çıkış Yapılıyor...")
        time.sleep(1)
        break
    elif (işlem == "1"):
        bilgisayar.Pc_aç()
    elif (işlem == "2"):
        bilgisayar.Pc_kapat()
    elif (işlem == "3"):
        
        uygulama_isimler = input("Uygulama ismilerini ',' ile ayırarak giriniz:")
        uygulama_listesi = uygulama_isimler.split(",")
        
        for eklenecekler in uygulama_listesi:
            bilgisayar.uygulama_ekle(eklenecekler)
             
    elif (işlem == "4"):
        print ("Uygulama Sayısı:",len(bilgisayar))
        
    elif (işlem == "5"):
        bilgisayar.pc_ekran_aç()
        
    elif (işlem == "6"):
        bilgisayar.pc_ekran_kapat()
        
    elif (işlem ==  "7"):
        print(bilgisayar)
        
    else:
        print("Geçersiz İşlem")