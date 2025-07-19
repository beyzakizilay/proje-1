def bugunden_gecmise():
    print("yeni günlük girişi çalıştı")
def gelecege_zipla():
    print("günlük hedef belirlend")
def format_donustur():
    print("gçrev tamamlandı")

def zamanmenu():
    print("╔════════════════════════════╗")
    print("║        Zaman Bükücü        ║")
    print("║                            ║")
    print("║  1-Bugünden Geçmişe        ║")
    print("║  2-Geleceğe zıpla          ║")
    print("║  3-Tarih format Dönüştür   ║")
    print("║  4-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        bugunden_gecmise()
    
    elif secim=="2":
        gelecege_zipla()

    elif secim=="3":
        format_donustur() 

    elif secim=="4":
        print("Anamenüye dönülüyor...")  