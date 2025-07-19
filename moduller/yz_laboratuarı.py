def sayi_tahmin():
    print("sayı tahmin deneyi çalıştı")
def renk_tahmin():
    print("renk tahmini çalıştı")  

def yzmenu():
    print("╔════════════════════════════╗")
    print("║   YZ LABORATUARI           ║")
    print("║                            ║")
    print("║  1-Sayı Tahmin Deneyi      ║")
    print("║  2-Renk Tahmini            ║")
    print("║  3-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        sayi_tahmin()
    
    elif secim=="2":
        renk_tahmin()  

    elif secim=="3":
        print("Anamenüye dönülüyor...")    
    #random sayı nasıl seçilecek???
        