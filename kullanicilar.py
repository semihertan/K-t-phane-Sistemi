from datetime import datetime, timedelta
odunc_alinan_kitaplar = {}
def yeni_kayit():
    while True:
        kullanici_adi = input("* KULLANICI ADI: ")
        if len(kullanici_adi) < 4 or " " in kullanici_adi:
            print("/// KULLANICI ADI MİNİMUM 4 KARAKTERDEN VE BOŞLUK KARAKTERİ OLMADAN OLUŞTURULMALIDIR ///")
        else:
            break
    while True:
        sifre = input("* ŞİFRE: ")
        if len(sifre) < 8:
            print("ŞİFRENİZİN UZUNLUĞU EN AZ 8 KARAKTER OLMALIDIR")
        else:
            break

    print("KULLANICI BİLGİLERİNİZİ GİRİN")
    isim = input("* AD: ")
    soyisim = input("* SOYAD: ")

    dosya_yolu = "Kullanıcılar.txt"
    try:
        with open(dosya_yolu, "a") as dosya:
            dosya.write(f"{kullanici_adi}, {sifre}, {isim}, {soyisim}\n")
            print("/// KAYDINIZ BAŞARIYLA OLUŞTURULDU ///")
    except FileNotFoundError:
        print("/// DOSYA BULUNAMADI ///")

def giris_yap():
    print("------------------------------------------------------------")
    print("GİRİŞ YAPMAK İÇİN KULLANICI ADINIZI VE ŞİFRENİZİ GİRİN")
    kayitli_kullanici_adi = input("KULLANICI ADI: ")
    kayitli_sifre = input("ŞİFRE: ")
    print("------------------------------------------------------------")
    dosya_yolu = "Kullanıcılar.txt"
    try:
        with open(dosya_yolu, "r") as dosya:
            for satir in dosya:
                kayitli_kullanici, kayitli_sifre_dosya, kayitli_ad, kayitli_soyad = satir.strip().split(", ")
                if kayitli_kullanici == kayitli_kullanici_adi and kayitli_sifre_dosya == kayitli_sifre:
                    print("GİRİŞ YAPILDI")
                    break
            else:
                print("BU BİLGİLERE AİT BİR KULLANICI BULUNAMADI")
                giris_yap()
    except FileNotFoundError:
        print("DOSYA BULUNAMADI")


def kitap_odunc_al():
    isbn = input("* ÖDÜNÇ ALINACAK KİTABIN ISBN NUMARASINI GİRİN: ")

    with open("KitapDurumu.txt", "r") as dosya:
        for satir in dosya:
            kitap_bilgileri = satir.strip().split(", ")
            if kitap_bilgileri[0] == isbn:
                print("/// BU KİTAP ZATEN ÖDÜNÇ ALINMIŞ ///")
                return


    with open("Kitaplar.txt", "r") as dosya:
        kitaplar = dosya.readlines()

    for index, kitap_str in enumerate(kitaplar):
        kitap_bilgileri = kitap_str.strip().split(", ")
        if kitap_bilgileri[0] == isbn:

            iade_tarihi = datetime.now() + timedelta(days=7)
            iade_tarihi_str = iade_tarihi.strftime("%d-%m-%Y")


            with open("KitapDurumu.txt", "a") as dosya:
                dosya.write(f"{isbn}, {iade_tarihi_str}\n")
            print("/// KİTAP ÖDÜNÇ ALINDI ///")
            print("KİTAP BİLGİLERİ:")
            print(f"ISBN: {kitap_bilgileri[0]}, Kitap Adı: {kitap_bilgileri[1]}, Yazar: {kitap_bilgileri[2]}, Sayfa Sayısı: {kitap_bilgileri[3]}")
            print("------------------------------------------------------------")
            print("**KİTABI 7 GÜN İÇİNDE TESLİM ETMENİZ GEREKMEKTEDİR**")
            print("**SON İADE TARİHİ --> ", iade_tarihi)
            print("------------------------------------------------------------")
            break
    else:
        print("------------------------------------------------------------")
        print("BÖYLE BİR KİTAP BULUNAMADI")
        kitap_odunc_al()

def kitap_iade():
    isbn = input("* İADE EDİLECEK KİTABIN ISBN NUMARASINI GİRİN: ")

    with open("KitapDurumu.txt", "r") as dosya:
        kitap_durumu_satirlar = dosya.readlines()

    kitap_bulundu = False
    for satir in kitap_durumu_satirlar:
        if isbn in satir:
            kitap_bulundu = True
            break

    if kitap_bulundu:
        with open("KitapDurumu.txt", "w") as dosya:
            for satir in kitap_durumu_satirlar:
                if isbn not in satir:
                    dosya.write(satir)
            print("------------------------------------------------------------")
            print("/// KİTAP İADE EDİLDİ ///")
    else:
        print("------------------------------------------------------------")
        print("** GİRİLEN ISBN NUMARASINA SAHİP KİTAP BULUNAMADI. LÜTFEN TEKRAR DENEYİN **")
        kitap_iade()







