kitaplar = []

def admin_girisi():
    kullanici_adi = input("KULLANICI ADI: ")
    sifre = input("ŞİFRE: ")
    dosya_yolu = "admin.txt"
    try:
        with open(dosya_yolu, "r") as dosya:
            for satir in dosya:
                admin_kullanici_adi, admin_sifre = satir.strip().split(", ")
                if admin_kullanici_adi == kullanici_adi and admin_sifre == sifre:
                    print("/// ADMİN GİRİŞİ BAŞARIYLA YAPILDI ///")
                    return
            print("/// BU BİLGİLERE AİT BİR ADMİN BULUNAMADI ///")
            print("/// TEKRAR DENEYİN ///")
            admin_girisi()
    except FileNotFoundError:
        print("/// DOSYA BULUNAMADI ///")
        exit(0)

def kullanici_guncelleme():
    print("BİLGİLERİNİ GÜNCELLEMEK İSTEDİĞİNİZ KULLANICININ KULLANICI ADINI GİRİN")
    print("KULLANICI ADI GİRMEK İÇİN --> 1")
    print("KULLANICI ADINI İSİMLE ARATMAK İÇİN --> 2")
    secim = input("BİR SEÇİM YAPIN: ")
    if secim == "1":
        kullanici_adi_güncelleme = input("KULLANICI ADI:")

        with open("Kullanıcılar.txt", "r") as dosya:
            for satir in dosya:
                kayitli_kullanici, kayitli_sifre_dosya, isim, soyisim = satir.strip().split(", ")
                if kayitli_kullanici == kullanici_adi_güncelleme:
                    print("KAYITLI KULLANICI BİLGİLERİ")
                    print(f"KULLANICI ADI: {kayitli_kullanici}")
                    print(f"ŞİFRE: {kayitli_sifre_dosya}")
                    print(f"AD SOYAD: {isim} {soyisim}")
                    print("DEĞİŞTİRMEK İSTEDİĞİNİZ BİLGİ HANGİSİ")
                    print("KULLANICI ADI --> 1")
                    print("ŞİFRE --> 2")
                    print("AD SOYAD --> 3")
                    secim_iki = input("BİR SEÇİM YAPIN: ")
                    if secim_iki == "1":
                        yeni_kullanici_adi = input("YENİ KULLANICI ADINI GİRİN:")

def kitap_ekle():
    global kitaplar
    isbn = input("* ISBN NUMARASI: ")
    kitap_adi = input("* KİTAP ADI: ")
    kitap_yazari = input("* KİTAP YAZAR ADI: ")
    kitap_sayfasi = input("* KİTAP SAYFA SAYISI: ")

    kitap = {
        "ISBN": isbn,
        "Kitap Adı": kitap_adi,
        "Yazar": kitap_yazari,
        "Sayfa Sayısı": kitap_sayfasi
    }

    kitaplar.append(kitap)

    try:
        with open("Kitaplar.txt", "a") as dosya:
            dosya.write(f"{isbn}, {kitap_adi}, {kitap_yazari}, {kitap_sayfasi}\n")
            print("/// KİTAP KAYDI BAŞARIYLA OLUŞTURULDU ///")
    except FileNotFoundError:
        print("/// DOSYA BULUNAMADI ///")

def kitap_sil(isbn):
    with open("Kitaplar.txt", "r") as dosya:
        kitaplar = dosya.readlines()

    silinen_indeksler = []
    for i, kitap in enumerate(kitaplar):
        if isbn in kitap:
            silinen_indeksler.append(i)

    if len(silinen_indeksler) > 0:
        with open("Kitaplar.txt", "w") as dosya:
            for indeks in sorted(silinen_indeksler, reverse=True):
                del kitaplar[indeks]
            dosya.writelines(kitaplar)
        print("/// KİTAP SİLME İŞLEMİ BAŞARILI ///")
    else:
        print("!!! KİTAP SİLİNEMEDİ !!!")

def kitap_arama(kitaplar):
    anahtar_kelime = str(input("* ANAHTAR KELİME GİR:"))
    eslesen_kitaplar = []
    for kitap in kitaplar:
        if anahtar_kelime.lower() in kitap["Kitap Adı"].lower() or anahtar_kelime.lower() in kitap["Yazar"].lower():
            eslesen_kitaplar.append(kitap)
    if eslesen_kitaplar:
        print("/// KİTAPLAR:")
        for kitap in eslesen_kitaplar:
            print(f"ISBN: {kitap['ISBN']}, Kitap Adı: {kitap['Kitap Adı']}, Yazar: {kitap['Yazar']}, Sayfa Sayısı: {kitap['Sayfa Sayısı']}")
    else:
        print("/// BULUNAMADI ///")

def kitap_guncelle():
    with open("Kitaplar.txt", "r") as dosya:
        kitaplar = dosya.readlines()

    while True:
        print("------------------------------------------------------------")
        isbn = input("GÜNCELLENECEK KİTABIN ISBN SİNİ GİRİN: ")

        for index, kitap_str in enumerate(kitaplar):
            kitap_bilgileri = kitap_str.strip().split(", ")
            if kitap_bilgileri[0] == isbn:
                print("------------------------------------------------------------")
                print("* GÜNCELLEMEK İSTEDİĞİNİZ KİTAP BİLGİLERİ:")
                print(f"ISBN: {kitap_bilgileri[0]}, Kitap Adı: {kitap_bilgileri[1]}, Yazar: {kitap_bilgileri[2]}, Sayfa Sayısı: {kitap_bilgileri[3]}")
                print("------------------------------------------------------------")
                yeni_isbn = input("* YENİ ISBN NUMARASINI GİRİN: ")
                kitap_bilgileri[0] = yeni_isbn

                with open("Kitaplar.txt", "w") as dosya:
                    for i, satir in enumerate(kitaplar):
                        if i == index:
                            dosya.write(", ".join(kitap_bilgileri) + "\n")
                        else:
                            dosya.write(satir)
                print("/// KİTAP BAŞARIYLA GÜNCELLENDİ ///")
        print("------------------------------------------------------------")
        print("KİTAP GÜNCELLEME MENÜSÜNE DÖNMEK İÇİN --> 1")
        print("ADMIN MENÜSÜNE DÖNMEK İÇİN --> 2")
        print("------------------------------------------------------------")
        secim = input("BİR SEÇİM YAPIN: ")
        if secim == "1":
            continue
        if secim == "2":
            break
