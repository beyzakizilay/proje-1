def yakit_hesapla():
    print("\n *Yakıt Hesaplama Sistemi*")
    agırlık=int(input("Roketin Ağırlığı: " ))
    mesafe=int(input("Gidilecek Mesafe: "))
    yakit=agırlık*mesafe
    print("Gerekli Yakıt: ", yakit)

def agirlik_azaltma():
    print("\n *Ağırlık Azaltma*")
    toplam=int(input("Toplam Ağırlık: "))
    cikarma=int(input("Kaç Ton Çıkarılacak: "))
    agırlık=toplam-cikarma
    print("Yeni Ağırlık: ", agırlık)
    
    
def guc_katsayisi():
    print("\n *Güç Katsayısı*")
    yakit=int(input("Yakıt Gücü: "))
    motor=int(input("Motor Gücü: "))
    toplam=yakit+motor
    print("Toplam Güç: ", toplam)

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
          
    
        