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
    print("Renk Karışımı Deneyi")
    print("Mevcut renkler: kırmızı, mavi, sarı")
    renk1=input("1. rengi gir: ").lower
    renk2=input("2. rengi gir: ").lower
    if(renk1=="kırmızı" and renk2=="mavi") or (renk1=="mavi" and renk2=="kırmızı"):
        karisim= "mor"
        kod= "\033[45m"
    elif(renk1=="kırmızı" and renk2=="sarı") or (renk1=="sarı" and renk2=="kırmızı"):
        karisim="turuncu"
        kod= "\033[43m"
    elif(renk1=="mavi" and renk2=="sarı") or (renk1=="sarı" and renk2=="mavi"):
        karisim="yeşil"
        kod= "\033[42m"
    elif renk1=="kırmızı" and renk2=="kırmızı":
        karisim="kırmızı"
        kod="\033[41m"
    elif renk1=="mavi" and renk2=="mavi":
        karisim="mavi"
        kod="\033[44m"
    elif renk1=="sarı" and renk2=="sarı":
        karisim="sarı"
        kod="\033[43m"
    else:
        print("Geçersiz renk karışımı!!!")
        return

def kesifmenu():
    print("╔════════════════════════════╗")
    print("║         Keşifler           ║")
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