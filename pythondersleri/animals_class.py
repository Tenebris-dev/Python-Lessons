import time


class Hayvanlar():
    
    def __init__(self,ayak_sayısı,bosaltım,solunum,omurgalı_omurgasız,boy,kilo):
        
        self.ayak_sayısı = ayak_sayısı
        self.bosaltım = bosaltım
        self.solunum = solunum
        self.omurgalı_omurgasız = omurgalı_omurgasız
        self.boy = boy
        self.kilo = kilo
        
class köpek(Hayvanlar):
    
    def köpek(self,özelliği):
        super().__init__(self.ayak_sayısı,self.bosaltım,self.solunum,self.omurgalı_omurgasız,self.boy,self.kilo)
        self.özelliği = özelliği
        
    def bilgilerigoster(self):
        print("\nKöpek Sınıfının bilgileri....\n")
        
        print("\nAyak Sayısı: {}\nBosaltım: {}\nSolunum: {}\nomurgalı mı? omurgasız mı?: {}\nboy: {}\nKilo: {}\n".format(self.ayak_sayısı,self.bosaltım,self.solunum,self.omurgalı_omurgasız,self.boy,self.kilo))
    
class kuş(Hayvanlar):
    
    def kuş(self,konuşma):
        super().__init__(self.ayak_sayısı,self.bosaltım,self.solunum,self.omurgalı_omurgasız,self.boy,self.kilo)
        self.konuşma = konuşma
        
    def bilgilerigoster(self):
        print("\nKuş Sınıfının bilgileri....\n")
        
        print("\nAyak Sayısı: {}\nBosaltım: {}\nSolunum: {}\nomurgalı mı? omurgasız mı?: {}\nboy: {}\nKilo: {}\n".format(self.ayak_sayısı,self.bosaltım,self.solunum,self.omurgalı_omurgasız,self.boy,self.kilo))
        
class At(Hayvanlar):
    
    def at(self,uysallık):
        super().__init__(self.ayak_sayısı,self.bosaltım,self.solunum,self.omurgalı_omurgasız,self.boy,self.kilo)
        self.uysallık = uysallık
        
    def bilgilerigoster(self):
        print("\nAt Sınıfının bilgileri....\n")
        
        print("\nAyak Sayısı: {}\nBosaltım: {}\nSolunum: {}\nomurgalı mı? omurgasız mı?: {}\nboy: {}\nKilo: {}\n".format(self.ayak_sayısı,self.bosaltım,self.solunum,self.omurgalı_omurgasız,self.boy,self.kilo))
        
a = köpek(4,"Yapar","Yapar","Omurgalı",1.60,50)
köpek.bilgilerigoster(a)

b = kuş(2,"Yapar","Yapar","Omurgalı","30 cm","50 gram")
kuş.bilgilerigoster(b)

c = At(4,"Yapar","Yapar","Omurgalı",200,150)
At.bilgilerigoster(c)
        
   