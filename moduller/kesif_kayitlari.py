def gunluk_listele():
    print("yeni günlük girişi çalıştı")
def filtrele():
    print("günlük hedef belirlend")
def kayıt_listele():
    print("gçrev tamamlandı")

def kesifmenu():
    print("╔════════════════════════════╗")
    print("║     Keşif Kayıtları        ║")
    print("║                            ║")
    print("║  1-Tüm günlükleri listele  ║")
    print("║  2-Filtrele                ║")
    print("║  3-Kayıtları Listele       ║")
    print("║  4-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        gunluk_listele()
    
    elif secim=="2":
        filtrele()

    elif secim=="3":
        kayıt_listele() 

    elif secim=="4":
        print("Anamenüye dönülüyor...")  