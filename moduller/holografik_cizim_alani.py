def yildiz_piramit():
    print("yıldız piramit çalıştı")
def dalgali_galaksi():
    print("dalgalı galaksi çalıştı")
def dinamik_zigzag():
    print("dinamik zigzag çalıştı")    

def holografikmenu():
    print("╔════════════════════════════╗")
    print("║   Holografik Çizim Alanı   ║")
    print("║                            ║")
    print("║  1-Yıldız Piramit          ║")
    print("║  2-Dalgalı Galaksi         ║")
    print("║  3-Dinamik Zigzag          ║")
    print("║  4-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        yildiz_piramit()
    
    elif secim=="2":
        dalgali_galaksi()

    elif secim=="3":
        dinamik_zigzag()   

    elif secim=="4":
        print("Anamenüye dönülüyor...")  