# (Sığmayan yorumlar yorum gerektiren şeylerin üstlerine yazılmıştır.)
# Sabitler
NET_ASGARI = 2324.70  # Net asgari ücretin o seneki değeri.
KOTA_CARPANI = 10  # Kotanın maaşın ne kadar katı fazla olması gerektiğini belirten değer
IKRAMIYE_CARPANI = 1 / 2  # Belirlenmiş net asgari ücretin çarpılacağı değer.
PRIM_CARPANI = 0.1  # Emlak komisyonun prim hesaplaması için çarpılacağı değer.
SAT_KOM_CARPANI = 0.04  # Satışlarda acentenin kazanacağı değeri hesaplamak için çarpılacağı değer.
# O ay fazla kiralama yapmış  belirli danışmanların belirli gruba dahil olabilmesi için geçmesi gereken kiralama sayısı.
EN_AZ_SAYI = 10
# O ay fazla kiralama yapmış  belirli danışmanların belirli gruba dahil olabilmesi için geçmesi gereken kiralama bedeli.
EN_AZ_BEDEL = 25000
# Sayaçlar ve boş tanımlamalar
# Her bir emlak tipi için sayı ve bedelleri için  toplam sayaçlar başlatılır.
top_kon_kira = 0
top_is_kira = 0
top_ar_kira = 0
top_kon_satis = 0
top_is_satis = 0
top_ar_satis = 0
top_kon_kira_bed = 0
top_is_kira_bed = 0
top_ar_kira_bed = 0
top_kon_satis_bed = 0
top_is_satis_bed = 0
top_ar_satis_bed = 0
en_yuksek_sat = 0  # En yüksek satış bedeli için sayacı başlatır.
en_yuksek_sat_ad = ""  # En yüksek satış bedeline sahip emlağı satan kişinin adı ile değiştirelecek değişken.
en_yuksek_sat_tur = ""  # En yüksek satış bedeline sahip emlağın emlak tipi ile değiştirilecek değişken.
en_yuksek_kir = 0  # En yüksek kiralama bedeli için sayacı başlatır.
en_yuksek_kir_ad = ""  # En yüksek kiralama bedeline sahip emlağı kiralayan kişinin adı ile değiştirelecek değişken.
en_yuksek_kir_tur = ""  # En yüksek kiralama bedeline sahip emlağın emlak tipi ile değiştirilecek değişken.
kon_yuksek_asgar = 0  # Aylık asgari ücretten daha yüksek olan aylık kira bedeli sayısı için sayacı başlatır.
satmayan = 0  # Hiç emlak satmayan danışman sayısı için sayacı başlatır.
en_cok_satis = 0  # Toplam en fazla satış yapan kişinin satış sayısı için sayacı başlatır
en_cok_satis_ad = ""  # Toplam en fazla satış yapan kişinin adı ile değiştrirlecek değişken.
en_cok_satis_top_sat_bed = 0  # Toplam en fazla satış yapan kişin toplam satış bedeli için sayacı başlatır.
top_en_yuksek_sat_bed = 0  # Toplam en yüksek bedelle satış yapan kişinin toplam satış bedeli için sayacı başlatır.
top_en_yuksek_sat_bed_ad = ""  # Toplam en yüksek bedelle satış yapan kişinin adı ile değiştirelecek değişken.
top_en_yuksek_sat_bed_say = 0  # Toplam en yüksek bedelle satış yapan kişinin satış sayısı için sayacı başlatır.
kota_asmis = 0  # Kotasını aşmış kişi sayısı için sayacı başlatır.
buyuk_prim = 0  # Prim bedeli maaşından yüksek olanların  sayısı için sayacı başlatır.
cok_kiralayan = 0  # O ay fazla sayıda veya bedelde kiralama yapmış olan danışmanların saysı için sayacı başlatır.
max_prim = 0  # O ay en yüksek prime sahip kişinin primi için sayacı başlatır.
max_prim_ad = ""  # O ay en yüksek prime sahip kişinin adı ile değiştirilecek değişken.
max_prim_maas = 0  # O ay en yüksek prime sahip kişinin maaşı için sayacı başlatır.
max_prim_top_ucret = 0  # O ay en yüksek prime sahip kişinin toplam ücreti.
min_prim = float('inf')  # En düşük prime sahip kişinin prim bedeli için sonsuzluğa bağlı sayacı başlatır.
min_prim_ad = ""  # En düşük prime sahip kişinin adı ile değiştirilecek değişken.
min_prim_maas = 0  # En düşük prime sahip kişinin maaşı için sayacı başlatır.
min_prim_top_ucret = 0  # En düşük prime sahip kişinin toplam ücretini hesaplamak için sayacı başlatır
top_ucret = 0  # Bütün danışmanların ücretlerinin genel toplamı için sayacı başlatır.
genel_top_komisyon = 0  # Bütün danışmanların acenteye kazandırdıkları toplam komisyon için sayacı başlatır.
# Sayıların hata kontrolünün daha kolay yapılabilmesi için fonksiyon tanımlanır.


def araligi_kontrol(alt_sinir, sayi, durum):
    if durum == "a":
        while alt_sinir >= sayi:
            sayi = float(input("Hatalı veri girdiniz, lütfen tekrar giriniz: "))
    elif durum == "b":
        while alt_sinir > sayi:
            sayi = float(input("Hatalı veri girdiniz, lütfen tekrar giriniz: "))
    return sayi


danisman_sayisi = int(input("\nDanışman sayısını giriniz (0'dan büyük tam sayı): "))
while danisman_sayisi <= 0:
    danisman_sayisi = int(input("Hatalı veri girdiniz, lütfen tekrar giriniz: "))
for danisman in range(danisman_sayisi):  # Danışman sayısı kadar değer alınır.
    # Her bir emlak tipi için sayı ve bedelleri için   sayaçlar başlatılır.
    kon_kira = 0
    is_kira = 0
    ar_kira = 0
    kon_satis = 0
    is_satis = 0
    ar_satis = 0
    kon_kira_bed = 0
    is_kira_bed = 0
    ar_kira_bed = 0
    kon_satis_bed = 0
    is_satis_bed = 0
    ar_satis_bed = 0
    max_kira_bed = 0  # Danışman başı en yüksek kira bedeli için sayacı başlatır.
    top_komisyon = 0  # Danışmanın kazandırdığıdığı toplam komisyon miktarı için sayacı başlatır.
    ucret = 0  # Danışmanın ücreti için sayacı başlatır.
    islem_turu = ""
    islem_bedeli = ""
    isim = input("\nAdınızı soyadınızı giriniz: ")
    maas = float(input("Maaşınızı giriniz(TL)(0'dan ve o yılın net asgari ücretinden  büyük reel sayı): "))
    maas = araligi_kontrol(NET_ASGARI, maas, "b")
    kota = float(input("Belirtilen ay için kotanızı yazınız (maaşınızın 10 katı ya da daha büyük): "))
    kota = araligi_kontrol(KOTA_CARPANI * maas, kota, "b")

    flag = True
    # Atanmış flag daha fazla alınacak emlak olduğu sürece doğrudur ve doğru olduğu sürece döngü devam eder
    while flag:
        # Emlak tipi, işlem türü ve işlem bedeli dallandırma yapılarak alınırken
        # gerekli  sayaçlar arttırılması gerektiği durumlarda arttırılır.
        emlak_tipi = input("\nEmlak tipini belirtiniz: Konut, İş yeri, Arsa (K/k/İ/i/A/a karakterleri): ")
        while emlak_tipi not in ["K", "k", "İ", "i", "A", "a"]:
            emlak_tipi = input("Hatalı veri girdiniz, lütfen tekrar giriniz: ")
        if emlak_tipi == "K" or emlak_tipi == "k":
            islem_turu = input("İşlemin satış mı kiralama mı olduğunu giriniz(S/s/K/k karakterleri): ")
            while islem_turu not in ["S", "s", "K", "k"]:
                islem_turu = input("Hatalı veri girdiniz, lütfen tekrar giriniz: ")
            if islem_turu == "S" or islem_turu == "s":
                kon_satis += 1
                top_kon_satis += 1
                islem_bedeli = float(input("Satış/kira bedelini giriniz(TL)(0'dan büyük reel sayı): "))
                araligi_kontrol(0, islem_bedeli, "a")
                kon_satis_bed += islem_bedeli
                top_kon_satis_bed += islem_bedeli
                top_komisyon += islem_bedeli * SAT_KOM_CARPANI
            elif islem_turu == "K" or islem_turu == "k":
                kon_kira += 1
                top_kon_kira += 1
                islem_bedeli = float(input("Satış/kira bedelini giriniz(TL)(0'dan büyük reel sayı): "))
                araligi_kontrol(0, islem_bedeli, "a")
                kon_kira_bed += islem_bedeli
                top_kon_kira_bed += islem_bedeli
                top_komisyon += islem_bedeli
                if islem_bedeli > NET_ASGARI:
                    kon_yuksek_asgar += 1
                if max_kira_bed <= islem_bedeli:
                    max_kira_bed = islem_bedeli
        elif emlak_tipi == "İ" or emlak_tipi == "i":
            islem_turu = input("İşlemin satış mı kiralama mı olduğunu giriniz(S/s/K/k karakterleri): ")
            while islem_turu not in ["S", "s", "K", "k"]:
                islem_turu = input("Hatalı veri girdiniz, lütfen tekrar giriniz: ")
            if islem_turu == "S" or islem_turu == "s":
                is_satis += 1
                top_is_satis += 1
                islem_bedeli = float(input("Satış/kira bedelini giriniz(TL)(0'dan büyük reel sayı): "))
                araligi_kontrol(0, islem_bedeli, "a")
                is_satis_bed += islem_bedeli
                top_is_satis_bed += islem_bedeli
                top_komisyon += islem_bedeli * SAT_KOM_CARPANI
            elif islem_turu == "K" or islem_turu == "k":
                is_kira += 1
                top_is_kira += 1
                islem_bedeli = float(input("Satış/kira bedelini giriniz(TL)(0'dan büyük reel sayı): "))
                araligi_kontrol(0, islem_bedeli, "a")
                is_kira_bed += islem_bedeli
                top_is_kira_bed += islem_bedeli
                top_komisyon += islem_bedeli
        elif emlak_tipi == "A" or emlak_tipi == "a":
            islem_turu = input("İşlemin satış mı kiralama mı olduğunu giriniz(S/s/K/k karakterleri): ")
            while islem_turu not in ["S", "s", "K", "k"]:
                islem = input("Hatalı veri girdiniz, lütfen tekrar giriniz: ")
            if islem_turu == "S" or islem_turu == "s":
                ar_satis += 1
                top_ar_satis += 1
                islem_bedeli = float(input("Satış/kira bedelini giriniz(TL)(0'dan büyük reel sayı): "))
                araligi_kontrol(0, islem_bedeli, "a")
                ar_satis_bed += islem_bedeli
                top_ar_satis_bed += islem_bedeli
                top_komisyon += islem_bedeli * SAT_KOM_CARPANI
            elif islem_turu == "K" or islem_turu == "k":
                ar_kira += 1
                top_ar_kira += 1
                islem_bedeli = float(input("Satış/kira bedelini giriniz(TL)(0'dan büyük reel sayı): "))
                araligi_kontrol(0, islem_bedeli, "a")
                ar_kira_bed += islem_bedeli
                top_ar_kira_bed += islem_bedeli
                top_komisyon += islem_bedeli

        # Emlak tipi isismleri daha sonra yazdırılabilmesi için tanımlanır.
        if (islem_turu == "K" or islem_turu == "k") and en_yuksek_kir <= islem_bedeli:
            en_yuksek_kir = islem_bedeli
            en_yuksek_kir_ad = isim
            if emlak_tipi == "K" or emlak_tipi == "k":
                en_yuksek_kir_tur = "Konut"
            elif emlak_tipi == "I" or emlak_tipi == "i":
                en_yuksek_kir_tur = "İş yeri"
            elif emlak_tipi == "A" or emlak_tipi == "a":
                en_yuksek_kir_tur = "Arsa"
        elif (islem_turu == "S" or islem_turu == "s") and en_yuksek_sat <= islem_bedeli:
            en_yuksek_sat = islem_bedeli
            en_yuksek_sat_ad = isim
            if emlak_tipi == "K" or emlak_tipi == "k":
                en_yuksek_sat_tur = "Konut"
            elif emlak_tipi == "I" or emlak_tipi == "i":
                en_yuksek_dat_tur = "İş yeri"
            elif emlak_tipi == "A" or emlak_tipi == "a":
                en_yuksek_sat_tur = "Arsa"
        # Başka değeri in alıp alınmayacağı flag değerini doğru döndürebilmesi için sorulur.
        baska_emlak = input("\nBelirtilen ay için satılan/kiralanan başka emlak olup olmadığını giriniz"
                            "(E/e/H/h karakterleri): ")
        while baska_emlak not in ["E", "e", "H", "h"]:
            baska_emlak = input("Hatalı veri girdiniz, lütfen tekrar giriniz: ")
        if baska_emlak == "E" or baska_emlak == "e":
            flag = True
        elif baska_emlak == "H" or baska_emlak == "h":
            flag = False
    # flag değeri false olduğu durumda hesaplamalar yapılır, hesaplamalar dahilinde arttırılması gereken sayaçlar 
    # arttırılır ve kişi başı yazdırılması gereken çıktıların yazdırılır.
    if not flag:
        emlakci_satis = kon_satis + is_satis + ar_satis
        if emlakci_satis == 0:
            satmayan += 1
        emlakci_kira = kon_kira + is_kira + ar_kira
        emlakci_top = emlakci_satis + emlakci_kira
        satis_bed = kon_satis_bed + is_satis_bed + ar_satis_bed
        kira_bed = kon_kira_bed + is_kira_bed + ar_kira_bed
        bedel_top = kira_bed + satis_bed
        ikramiye = NET_ASGARI * IKRAMIYE_CARPANI
        prim = top_komisyon * PRIM_CARPANI
        genel_top_komisyon += top_komisyon
        ucret = maas + prim + ikramiye
        if prim > maas:
            buyuk_prim += 1
        if en_cok_satis <= emlakci_satis:
            en_cok_satis = emlakci_satis
            en_cok_satis_ad = isim
            en_cok_satis_top_sat_bed = satis_bed
        if top_en_yuksek_sat_bed <= satis_bed:
            top_en_yuksek_sat_bed = satis_bed
            top_en_yuksek_sat_bed_ad = isim
            top_en_yuksek_sat_bed_say = emlakci_satis
        if emlakci_kira >= EN_AZ_SAYI or kira_bed >= EN_AZ_BEDEL:
            cok_kiralayan += 1
        print("\nSayın " + isim)
        print("\nBelirtilen ay için " + str(emlakci_satis) + " adet emlak satmış, " + str(emlakci_kira) +
              " adet emlak ise kiralamaış bulunmaktasınız. Toplam işlemin  %" +
              format(emlakci_satis / emlakci_top * 100, ',.2f') + " satıştan   ve  %" +
              format(emlakci_kira / emlakci_top * 100, ',.2f') + " kiralamadan oluşmaktadır. ")
        print("\nBelirtilen ay toplam  " + format(kon_satis_bed, ',.2f') + " liralık  konut, " +
              format(is_satis_bed, ',.2f') + " liralık iş yeri ve " + format(ar_satis_bed, ',.2f') +
              " liralık arsa satmış bulunmatasınız.")
        print("\nBelitilen ay kiraladığınız konutların ortlama kira bedeli: ")
        if kon_kira != 0:
            print(format(kon_kira_bed / kon_kira, ',.2f') + " liradır.")
        elif kon_kira == 0:
            print("yoktur.")
        print("\nEn yüksek bedelle kiralamış olduğunuz konutun kira bedeli: " + format(max_kira_bed, ',.2f') +
              " liradır.")
        print("\nBelirtilen aylık maaşınız: " + format(maas, ',.2f') + "liradır.")
        print("\nBelirtilen ay için  aylık priminiz: " + format(prim, ',.2f') + " liradır.")
        print("\nBelirtilen ay için  aylık kotanız: " + format(kota, ',.2f') + " liradır.")
        print("\nBelirtilan ay için  ay emlak acentenize kazandırdığınız toplam komisyon tutarı: " +
              format(top_komisyon, ',.2f') + " liradır.")
        if top_komisyon >= kota:

            print("\nKotanızı doldurmuş bulunmaktasınız "
                  "Belirtilen ay alacağınız ikramiye: " + format(ikramiye, ',.2f') + " liradır.")
            kota_asmis += 1

        elif top_komisyon < kota:
            ucret -= ikramiye
            print("\nBelirtilen ay için aylık kotanızı maalesef dolduramadınız, ikramiye alamayacaksınız.")
        print("\nBelirtilen ay için  aylık toplam ücretiniz: " + format(ucret, ',.2f') +
              " liradır.")
        top_ucret += ucret
        # Ücret sonradan son haline geldiği yazdırıldığı için kişlerin prim değerleri bu bölümde karşılaştırılır.
        if max_prim <= prim:
            max_prim = prim
            max_prim_ad = isim
            max_prim_maas = maas
            max_prim_top_ucret = ucret
        if min_prim >= prim:
            min_prim = prim
            min_prim_ad = isim
            min_prim_maas = maas
            min_prim_top_ucret = ucret
# for döngüsü tamamlandığında acentenin genel değerleri için çıktılar sağlanır.
print("\n\n\nBelirtilen ay " + str(top_kon_satis) + " adet konut satılmış ve toplama oranı: %" +
      format(top_kon_satis / (top_kon_satis + top_kon_kira) * 100, ',.2f') + ", " +
      str(top_is_satis) + " adet iş yeri satılmış ve toplama  oranı: % " +
      format(top_is_satis / (top_is_satis + top_is_kira) * 100, ',.2f') + ", " +
      str(top_ar_satis) + " adet arsa satılmış ve toplama oranı: %" +
      format(top_ar_satis / (top_ar_satis + top_ar_kira) * 100, ',.2f') + ", " +
      str(top_kon_kira) + " adet konut kiralanmış ve toplama oranı: % " +
      format(top_kon_kira / (top_kon_satis + top_kon_kira) * 100, ',.2f') + ", " +
      str(top_is_kira) + " adet iş yeri kiralanmış ve toplama oranı: %" +
      format(top_is_kira / (top_is_satis + top_is_kira) * 100, ',.2f') + ", " +
      str(top_ar_kira) + " adet ise arsa kiralanmış ve toplama oranı: % " +
      format(top_ar_kira / (top_ar_satis + top_ar_kira) * 100, ',.2f') + " şeklindedir.")
print("\nBelirtilen ay toplam " + format(top_kon_satis_bed, ',.2f') + " liralık konut satılmış ve bedel  ortalamaları: "
      + format(top_kon_satis_bed / top_kon_satis, ',.2f') + " lira şeklindedir." +
      "Belirtilen  ay toplam " + format(top_is_satis_bed, ',.2f') + " liralık iş yeri satılmış ve bedel  ortalamaları: "
      + format(top_is_satis_bed / top_is_satis, ',.2f') + " lira şeklindedir." +
      "Belirtilen ay toplam " + format(top_ar_satis_bed, ',.2f') + " liralık arsa satılmış ve bedel  ortalamaları: " +
      format(top_ar_satis_bed / top_ar_satis, ',.2f') + " lira şeklindedir.")
print("\nBelirtilen ay için  aylık en yüksek fiyata satılmış emlağın tipi: " + en_yuksek_sat_tur + ", bedeli: " +
      format(en_yuksek_sat, ',.2f') + " lira ve onu satan kişi: " + en_yuksek_sat_ad + " şeklindedir.")
print("Belirtilen ay için  aylık en yüksek fiyata kiralanmış emlağın tipi: " + en_yuksek_kir_tur + ", bedeli: " +
      format(en_yuksek_kir, ',.2f') + " lira ve onu kiralayan kişi: " + en_yuksek_kir_ad + " şeklindedir.")
print("\nBelirtilen ay için  asgari ücretten yüksek bedelle kiralanan konut sayısı: " + str(kon_yuksek_asgar) +
      " ve tüm kirlanan konutlar içindeki oranı: %" + format(kon_yuksek_asgar / top_kon_kira * 100, ',.2f') +
      " şeklindedir.")
print("\nBelirtilen ay emlak satmayan danışman sayısı: " + str(satmayan) + " ve tüm danışmanların içindeki oranları: %"
      + format(satmayan / danisman_sayisi * 100, ',.2f') + " şeklindedir.")
print("\nBelirtilen ayda en çok satış yapan danışmanın adı: " + en_cok_satis_ad + ", sattığı toplam emlak sayısı: " +
      str(en_cok_satis) + " ve toplam satış bedeli: " + format(en_cok_satis_top_sat_bed, ',.2f') + " lira şeklindedir.")
print("Belirtilen ayda en yüksek toplam satış miktarını elde eden danışmanın adı: " + top_en_yuksek_sat_bed_ad +
      ", sattığı toplam emlak sayısı: " + str(top_en_yuksek_sat_bed_say) + " ve toplam satış bedeli: " +
      format(top_en_yuksek_sat_bed, ',.2f') + " lira şeklindedir.")
print("\nBelirtilen ayda kotasını doldurmuş olan danışmanların sayısı: " + str(kota_asmis) +
      " ve tüm danışmanlar içindeki oranları: %" + format(kota_asmis / danisman_sayisi * 100, ',.2f') +
      "  şeklindedir.")
print("\nBelirtilen ayda prim bedeli maaşından yüksek olan danışmanların sayısı: " + str(buyuk_prim) +
      " ve tüm danışmalar içindeki oranı: %" + format(buyuk_prim / danisman_sayisi * 100, ',.2f') + " şeklindedir.")
print("\nBelirtilen ayda en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı: " +
      str(cok_kiralayan) + " şeklindedir.")
print("\nBelirtilen ayda en yüksek primi alacak olan danışmanın adı: " + max_prim_ad + ", maaşı: " +
      format(max_prim_maas, ',.2f') + " lira , primi: " + format(max_prim, ',.2f') + " lira ve aylık toplam ücreti: " +
      format(max_prim_top_ucret, ',.2f') + " lira şeklindedir.")
print("Belirtilen ayda en düşük primi alacak olan danışmanın adı: " + min_prim_ad + ", maaşı: " +
      format(min_prim_maas, ',.2f') + " lira, primi: " + format(min_prim, ',.2f') + " lira ve aylık toplam ücreti: " +
      format(min_prim_top_ucret, ',.2f') + " lira şeklindedir.")
print("\nBelirtilen ayda tüm emlak danışmanlarına ödenecek ücretler toplamı: " + format(top_ucret, ',.2f') +
      " liradır ve ortalaması: " + format(top_ucret / danisman_sayisi, ',.2f') + " lira şeklindedir.")
print("\nBelirtilen ayda kazanılmış toplam komisyon: " + format(genel_top_komisyon, ',.2f') + "  lira şeklindedir.")
# Kod tamamlanmıştır.