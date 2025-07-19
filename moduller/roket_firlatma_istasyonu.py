def yakit_hesapla():
    print("yakıt hesaplama çalıştı")
def agirlik_azaltma():
    print("ağırlık azaltma çalıştı")
def guc_katsayisi():
    print("güç katsaısı çalıştı")    

def roketmenu():
    print("╔════════════════════════════╗")
    print("║   Roket Fırlatma İstasyonu ║")
    print("║                            ║")
    print("║  1-Yakıt Hesapla           ║")
    print("║  2-Ağırlık Azalt           ║")
    print("║  3-Güç Katsayısı           ║")
    print("║  4-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        yakit_hesapla()
    
    elif secim=="2":
        agirlik_azaltma()

    elif secim=="3":
        guc_katsayisi()   

    elif secim=="4":
        print("Anamenüye dönülüyor...")    
    
        