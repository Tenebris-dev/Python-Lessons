
class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan Sınıfının init Fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        print("Çalışan Sınıfının bilgileri....")
        
        print("\nİsim : {}\nMaaş: {}\nDepartman: {}".format(self.isim,self.maaş,self.departman))
    def depatmandegistir(self,yeni_departman):
        print("Departman değiştiriliyor...")
        self.departman = yeni_departman


class Yönetici(Çalışan):
    def __init__(self, isim, maaş, departman,kişi_sayisi):
        super().__init__(isim, maaş, departman)
        print("Yönetici Sınıfının init Fonksiyonu")
    
        self.kişi_sayisi = kişi_sayisi
    def bilgilerigoster(self):
        print("Yönetici Sınıfının bilgileri....")
        
        print("\nİsim : {}\nMaaş: {}\nDepartman: {}".format(self.isim,self.maaş,self.departman))
    
    def zam_yap(self,zam_miktarı):
        print("Maaş'a zam yapılıyor...")
        self.maaş += zam_miktarı
c =Yönetici("Mert Yolseven",5500,"Deep Learning",1)
Yönetici.bilgilerigoster(c)