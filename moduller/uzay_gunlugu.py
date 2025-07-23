def gunluk_girisi():
    print("\n * Yeni Günlük Girişi Sistemi*")
    notlar=input("Bugün neler öğrendin?: ")
    print("Günlük Kaydın Tamamlandı:", notlar)

def gunluk_hedef():
    print("\n *Günlük Hedef Belirleme Sistemi*")
    hedef=input("Bugünki Hedeflerin Neler?: ")
    print("Bugünki Hedeflerini Listeledim: ", hedef)

def gorev_tamamlandı():
    print("\n *Görev Tamamlandı Notu Sistemi*")
    gorev=input("Görevleriniz yapıldı mı?:")
    if gorev==("evet"):
        print("Görevleriniz Tamamlandı")
    elif gorev==("hayır"):
        print("Görevleriniz tamamlanmadı...")
    else:
        print("geçerli bir cevap giriniz-evet/hayır")    

def uzaymenu():
    print("╔════════════════════════════╗")
    print("║     Uzay Günlüğü           ║")  
    print("║                            ║")
    print("║  1-Yeni Günlük Girişi      ║")
    print("║  2-Günlük Hedef Belirle    ║")
    print("║  3_Görev Tamamlandı Notu   ║")
    print("║  4-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        gunluk_girisi()
    
    elif secim=="2":
        gunluk_hedef()

    elif secim=="3":
        gorev_tamamlandı()   

    elif secim=="4":
        print("Anamenüye dönülüyor...")  