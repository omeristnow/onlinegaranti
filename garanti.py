from dijitalgaranti import randomx
from dijitalgaranti import satis
from dijitalgaranti import kontrol

while True :
    giristuru = input ("GARANTİ VER [1] - GARANTİ SORGULA [2] : ")
    if giristuru == "1":
        print ("Hoşgediliniz...")
        urunkodu = input ("Ürün Kodu ? : ")
        musteri = satis(urunkodu)
        garanti_no = musteri.garanti_no()
        donut = musteri.kontrolet()
        if donut is True :
            musteri.yazdir()

        else :
            pass
    elif giristuru == "2":
        print ("HOŞGELDİNİZ ONLİNE İŞLEM OLARAK SİZE VERİLEN BİLGİLERİ DOĞRU BİR ŞEKİLDE LÜTFEN SİSTEME İŞLEYİNİZ")
        urun_kodu = input ("Ürün kodu ? : ")
        musteri_no = input ("Müşteri no ? : ")
        garanti_no = input ("Garanti No ? : ")
        musterisorgu = kontrol(urun_kodu,musteri_no,garanti_no)
        musterisorgu.sorgula()
    elif giristuru == "GM":
        pass

    else :
        pass
