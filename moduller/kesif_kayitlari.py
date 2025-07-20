#karısımları nasıl yapıcam???
def kaynama_noktası():
    print("/n *Suyun Kaynama Noktasını Bulma*")
    print("Su 100 derecede kaynar...")
    rakim=int(input("Bulunduğun rakımı gir: "))
    kaynama=100-(rakim/300)
    print("Tahmini Kaynama Noktası: ", kaynama)

def hız_olcumu():
    print("/n *Ses Hızı Deneyi*")
    mesafe=float(input("Şimşeği gördükten kaç saniye sonra gördün?: "))
    hiz=343
    uzaklik =hiz*mesafe
    print("Şimşek yaklaşık olarak", uzaklik,"metre uzaktaydı.")

def karısımlar():
    print

def kesifmenu():
    print("╔════════════════════════════╗")
    print("║     Keşifler               ║")
    print("║                            ║")
    print("║  1-Suyun Kaynama Noktası   ║")
    print("║  2-Ses Hızı Ölçümü         ║")
    print("║  3-Renk Karışımları        ║")
    print("║  4-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        kaynama_noktası()
    
    elif secim=="2":
        hız_olcumu()

    elif secim=="3":
        karısımlar() 

    elif secim=="4":
        print("Anamenüye dönülüyor...")  