import random
import os
import time

def randomx ():
    global deger
    deger = random.randint (100,999999)
    return deger

class satis ():
    def __init__ (self,urunkodu):
        print ("Bu numaranızı asla unutmayın.. Müşteri NO : {}".format(deger))
        self.urunkodu = urunkodu


    def garanti_no (self):
        global garanti_number
        garanti_number = random.randint(10000000000000,99999999999999)
        dosyaisim = str(self.urunkodu)+"."+str(deger)
        dosya_time = "time."+str(deger)
        dosyaac = open (dosyaisim,"w+")
        dosya_act = open(dosya_time,"w+")
        dosyaac.write(str(garanti_number))
        garantisuresi = int (input ("Garanti Süresi Kaç Yıl  ? : "))
        dosya_act.write(str(time.localtime()[0]+garantisuresi))
        dosya_act.close()
        dosyaac.close()

    def yazdir (self):
        print ("""

        ! Garanti Belgeniz !
        Ürün Numaranız : {}
        Müşteri Numaranız : {}
        Garanti Belgesi Online İşlem Numaranız : {}


        """.format(self.urunkodu,deger,garanti_number))

    def kontrolet (self):
        dosyaisim = str(self.urunkodu)+"."+str(deger)
        a = os.path.exists(dosyaisim)
        if a is True :
            dosyaac = open(dosyaisim,"r+")
            oku = dosyaac.readline()
            dosyaac.close()
            if str(oku) == str(garanti_number) :
                print("Garanti işleme girdi.")
                return True
            else :
                print ("Garanti Başarısız Tekrar Deneyin")
        else :
            print ("Aradığınız ürün koduna ait bir değer yok")


class kontrol ():
    def __init__ (self,urunkodu,musteri_no,garanti_no):
        self.urunkodu = urunkodu
        self.musteri_no = musteri_no
        self.garanti_no = garanti_no
    def sorgula (self):
        dosyaisim = str(self.urunkodu)+"."+str(self.musteri_no)
        a = os.path.exists(dosyaisim)
        if a is True :
            dosya_oku = open(dosyaisim,"r+")
            oku = dosya_oku.readline()
            print (oku)
            dosya_oku.close()
            if oku == self.garanti_no :
                print ("Garantiniz Devam ediyor..")
                dosya_time = "time."+str(self.musteri_no)
                garanti_kontrol = open(dosya_time,"r+")
                garantisuresi = str(int(garanti_kontrol.readline()) - time.localtime()[0])
                print ("{} Yıl Garanti Süresi Var...".format(garantisuresi))

            else :
                print ("Garantiniz Geçersiz")
        else :
            print ("Garantiniz Yok.")
randomx()
