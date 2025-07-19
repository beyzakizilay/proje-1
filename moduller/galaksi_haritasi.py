def nova_sistemi():
    print("yeni günlük girişi çalıştı")
def karadelik():
    print("günlük hedef belirlend")
def yildiz_gecidi():
    print("gçrev tamamlandı")

def galaksimenu():
    print("╔════════════════════════════╗")
    print("║        Galaksi Haritası    ║")
    print("║                            ║")
    print("║  1-Nova Sistemi            ║")
    print("║  2-Karadelik Noktası       ║")
    print("║  3-Yıldız Geçidi           ║")
    print("║  4-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        nova_sistemi()
    
    elif secim=="2":
        karadelik()

    elif secim=="3":
        yildiz_gecidi() 

    elif secim=="4":
        print("Anamenüye dönülüyor...")  