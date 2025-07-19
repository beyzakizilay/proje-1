def gunluk_girisi():
    print("yeni günlük girişi çalıştı")
def gunluk_hedef():
    print("günlük hedef belirlend")
def gorev_tamamlandı():
    print("gçrev tamamlandı")

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