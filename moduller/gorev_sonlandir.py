tema="Koyu"
dil="Türkçe"
ses="Açık"
def tema_degistir():
    print("\n *Tema Değiştirme*")
    global tema
    tema=input("Tema (Koyu/Açık): ")
    print("Tema ayarlandı:", tema)

def dil_degistir():
    print("\n *Dil Değiştirme*")
    global dil
    dil=input("Dil(TR/EN): ")
    print("Dil ayarlandı:", dil)

def ses_degistir():
    print("\n *Ses Değiştirme*")
    global ses
    ses=input("Ses (Açık/Kapalı: )")
    print("Ses ayarlandı: ", ses)

def sonlandirmamenu():
    print("╔════════════════════════════╗")
    print("║       Görev Sonlandır      ║")
    print("║                            ║")
    print("║  1-Tema Değiştir           ║")
    print("║  2-Dil Değiştir            ║")
    print("║  3-Ses Değiştir            ║")
    print("║  4-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        tema_degistir()
    
    elif secim=="2":
        dil_degistir()

    elif secim=="3":
        ses_degistir() 

    elif secim=="4":
        print("Anamenüye dönülüyor...")          