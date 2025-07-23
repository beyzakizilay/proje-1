galaksiler=["Andromeda", "Samanyolu", "Messier 87", "NGC 1300"]
def galaksi_sistemi():
    print("\n *Galaksi Sistemi*")
    print("Keşfedilen Galaksiler: ")
    for galaksi in galaksiler:
        print("-", galaksi)
def karadelik():
    print("\n *Karadelik Noktası*")
    print("Karadelikler ışığı bile yutar. Peki sen karadeliğe ne fırlatmak istersin?")
    nesne=input("Karadeliğe ne fırlatmak istersin?: ")
    print(f"{nesne} karadeliğe fırlatıldı. Geri dönüşü yok!!!" )

def yildiz_gecidi():
    print("\n *Yıldız Geçidi*")
    gezegen=input("Hangi gezegene ışınlanmak istersin?: ")
    saniye=input("Kaç saniyede geçiş yapmak istersin: ")
    print(f"{gezegen} gezegenine {saniye} saniyede geçiş başlatıldı!!!")

def galaksimenu():
    print("╔════════════════════════════╗")
    print("║        Galaksi Haritası    ║")
    print("║                            ║")
    print("║  1-Galaksi Sistemi         ║")
    print("║  2-Karadelik Noktası       ║")
    print("║  3-Yıldız Geçidi           ║")
    print("║  4-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        galaksi_sistemi()
    
    elif secim=="2":
        karadelik()

    elif secim=="3":
        yildiz_gecidi() 

    elif secim=="4":
        print("Anamenüye dönülüyor...")  