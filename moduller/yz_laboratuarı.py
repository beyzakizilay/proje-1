import random

def sayi_tahmin():
    print("SAYI TAHMİN DENEYİ")
    gizli_sayi= random.randint(1,10)
    hak=3

    while hak>0:
        tahmin=int(input("1 ile 10 arasında bir sayı tahmin et: "))
        if tahmin==gizli_sayi:
            print("Doğru tahmib, tebrikler!!!")
            break
        else:
            hak-=1
            if tahmin<gizli_sayi:
                print("Daha büyük bie sayı deneyiniz.")
            else:
                print("Daha küçük bir sayı deneyiniz.")
            if hak>0:
                print(f"Hakkınız bitti. Doğru cevap:{gizli_sayi}")
                        

def renk_tahmin():
    print("RENK TAHMİN DENEYİ")
    renkler=["kırmızı", "mavi", "yeşil", "sarı", "mor"]
    secilen_renk=random.choice(renkler)
    hak=3
    while hak>0:
        tahmin=input(f"Bir renk tahmin edin {renkler}: ").lower() 
        if tahmin==secilen_renk:
            print("Doğru tahmin,tebrikler!!!")
            break
        else:
            hak-=1
            print("Yanlış tahmin")
            if hak>0:
                print("Kalan hakkınız: {hak}")
            else:
                print(f"Hakkınız bitti. Doğru renk: {secilen_renk}")
                
def yzmenu():
    print("╔════════════════════════════╗")
    print("║   YZ LABORATUARI           ║")
    print("║                            ║")
    print("║  1-Sayı Tahmin Deneyi      ║")
    print("║  2-Renk Tahmini            ║")
    print("║  3-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        sayi_tahmin()
    
    elif secim=="2":
        renk_tahmin()  

    elif secim=="3":
        print("Anamenüye dönülüyor...")            