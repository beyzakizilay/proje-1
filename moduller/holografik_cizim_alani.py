def yildiz_piramit():
    print("Yıldız Piramit: ")
    for a in range(1,100):
        print("*" * a)

def dalgali_galaksi():
    print("Dalgalı Galaksi:")
    for a in  range(100):
        print(" " * a + "*")

def dinamik_zigzag():
    print("Dinamik Zigzag: ")
    for a in range(100):
        if a % 2==0:
            print("\\")
        else:
            print("/")  

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