
class Yazilimci():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara =numara
        self.maaş =maaş
        self.diller =diller
    def bilgilerigoster(self):
        print("""
            Çalışan Bilgisi:
        
            İsim :  {}
        
            Soyisim : {}
        
            Şirket Numarası: {}
        
            Maaş :  {}
        
            Diller: {}
            """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    def dil_ekle(self,yenidil):
        print("\nDil Ekleniyor...")
        self.diller.append(yenidil)
    def yukselt(self,zam_miktarı):
        print("\nZam Yapılıyor...")
        
        self.maaş += zam_miktarı
        
        
yazilimci1 = Yazilimci("Mert","Yolseven",441,0,["c#","python","Deep Learning","Machine Learning"])
yazılımcı2 = Yazilimci("Serhat","Say",23456,3500,["Matlab","R","SmallTalk"])
yazilimci1.yukselt(1500)
yazilimci1.dil_ekle("java")
yazilimci1.bilgilerigoster()
yazılımcı2.bilgilerigoster()
