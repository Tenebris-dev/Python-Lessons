class Araba():
    model= "BMW"
    renk = "Gri"
    beygir_gucu = 650
    silindir = 8
print("\nModel:",Araba.model,"\nRenk:",Araba.renk,"\nBeygir:",Araba.beygir_gucu,"\nSilindir:",Araba.silindir)

class Motor():
    
    def __init__(self,model = "BilgiYok",renk = "BilgiYok",beygir_gucu = 110,silindir=4):
        print("\nİnit Fonksiyonu Çağırıldı")
        
        self.model = model
        self.renk = renk
        self.beygir_gucu = beygir_gucu
        self.silindir = silindir
        
motor = Motor("Honda","Siyah",13,1)
print(print("\nModel:",motor.model,"\nRenk:",motor.renk,"\nBeygir:",motor.beygir_gucu,"\nSilindir:",motor.silindir))