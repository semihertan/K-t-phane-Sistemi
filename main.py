import admin
import kullanicilar
global kitaplar
def kitaplari_oku():
    kitaplar = []
    try:
        with open("Kitaplar.txt", "r") as dosya:
            for satir in dosya:
                isbn, kitap_adi, kitap_yazari, kitap_sayfasi = satir.strip().split(", ")
                kitap = {
                    "ISBN": isbn,
                    "Kitap Adı": kitap_adi,
                    "Yazar": kitap_yazari,
                    "Sayfa Sayısı": kitap_sayfasi
                }
                kitaplar.append(kitap)
    except FileNotFoundError:
        print("DOSYA BULUNAMADI")
    return kitaplar

kitaplar = kitaplari_oku()

print("          KÜTÜPHANE ENVANTER SİSTEMİNE HOŞGELDİNİZ")
print("------------------------------------------------------------")
print("ADMİN GİRİŞİ --> 1")
print("KULLANICI GİRİŞİ --> 2")
print("------------------------------------------------------------")
secim = input("BİR SEÇİM YAPIN: ")

if secim == "1":
    admin.admin_girisi()
    while True:
        print("------------------------------------------------------------")
        print("KİTAP EKLE --> 1")
        print("KİTAP SİL --> 2")
        print("KİTAP GÜNCELLE --> 3")
        print("ÇIKIŞ YAP --> 4")
        print("------------------------------------------------------------")
        admin_secim = input("BİR SEÇİM YAPIN: ")

        if admin_secim == "1":
            admin.kitap_ekle()
            while True:
                print("------------------------------------------------------------")
                print("KİTAP EKLEMEYE DEVAM ETMEK İÇİN --> 1")
                print("ADMIN MENÜSÜNE DÖNMEK İÇİN --> 2")
                print("------------------------------------------------------------")
                secim_kitap_ekle = input("BİR SEÇİM YAPIN: ")

                if secim_kitap_ekle == "1":
                    admin.kitap_ekle()
                    continue
                elif secim_kitap_ekle == "2":
                    break
                else:
                    print("LÜTFEN SADECE BELİRTİLEN SAYILARI GİRİN")
                    continue

        while True:
            if admin_secim == "2":
                print("------------------------------------------------------------")
                print("!!! KİTAP SİLME İŞLEMİ YALNIZCA ISBN NUMARASI ÜZERİNDEN YAPILABİLMEKTEDİR !!!")
                print("* ISBN NUMARASINI GİRMEK İÇİN --> 1")
                print("* ISBN NUMARASI BİLİNMİYORSA ARAMA YAPMAK İÇİN --> 2")
                print("* ADMIN MENÜSÜNE DÖNMEK İÇİN --> 3")
                print("------------------------------------------------------------")
                secim_isbn_ogrenme = input("SEÇİM YAPIN: ")
                if secim_isbn_ogrenme == "1":
                    print("------------------------------------------------------------")
                    isbn = str(input("* SİLİNMESİNİ İSTEDİĞİNİZ KİTABIN ISBN NUMARASINI GİRİN: "))
                    admin.kitap_sil(isbn)

                elif secim_isbn_ogrenme == "2":
                    secim_arama = 0
                    while secim_arama != "2":
                        admin.kitap_arama(kitaplar)
                        print("------------------------------------------------------------")
                        print("* TEKRAR ARAMA YAPMAK İÇİN --> 1")
                        print("* KİTAP ARAMA MENÜSÜNDEN ÇIKMAK İÇİN --> 2")
                        print("------------------------------------------------------------")
                        secim_arama = input("BİR SEÇİM YAPIN: ")

                elif secim_isbn_ogrenme == "3":
                    break
                else:
                    break
            else:
                break

        if admin_secim == "3":
            admin.kitap_guncelle()
        if admin_secim == "4":
            print("------------------------------------------------------------")
            print("                     ÇIKIŞ YAPILDI")
            print("------------------------------------------------------------")
            break

if secim == "2":
    print("------------------------------------------------------------")
    print("KAYIT OL--> 1")
    print("GİRİŞ YAP--> 2")
    print("------------------------------------------------------------")
    secim_iki = input("BİR SEÇİM YAP: ")
    while True:
        if secim_iki == "1":
            print("------------------------------------------------------------")
            kullanicilar.yeni_kayit()
            secim_iki = "2"
        if secim_iki == "2":
            print("------------------------------------------------------------")
            kullanicilar.giris_yap()

            while True:
                print("------------------------------------------------------------")
                print("* KİTAP ÖDÜNÇ ALMA EKRANI --> 1")
                print("* KİTAP İADE ETME EKRANI --> 2")
                print("* KİTAP ARAMA EKRANI --> 3")
                print("* ÇIKIŞ YAP --> 4")
                print("------------------------------------------------------------")
                secim_uc = input("BİR SEÇİM YAPIN: ")
                if secim_uc == "1":
                    kullanicilar.kitap_odunc_al()
                    continue
                elif secim_uc == "2":
                    kullanicilar.kitap_iade()
                    continue
                elif secim_uc == "3":
                    admin.kitap_arama(kitaplar)
                    continue
                elif secim_uc == "4":
                    print("------------------------------------------------------------")
                    print("                     ÇIKIŞ YAPILDI")
                    print("------------------------------------------------------------")
                    exit(0)
                else:
                    print("GEÇERLİ BİR DEĞER GİRİN")