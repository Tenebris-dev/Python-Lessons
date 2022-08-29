from datetime import *

before = datetime.now()

text = "merhabalar ben python.Ben bir programlama diliyim."
print("Başlayabilirsiniz: {}".format(text))

if text == input(": "):
    after = datetime.now()
    
    speed = after - before
    seconds = speed.total_seconds()
    letter_per_second = round(len(text) / seconds, 1)
    
    print("Kazandınız")
    print("Skorunuz: {} saniye.".format(seconds))
    print("saniye başına harf sayınız: {}".format(letter_per_second))
else:
    print("Kaybettiniz :(")