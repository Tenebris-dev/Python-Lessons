class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    def __len__(self):
        return self.sayfa_sayısı
    def __del__(self):
        print("Kitap objesi siliniyor.......")

