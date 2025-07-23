def bugunden_gecmise():
    print("Geçmişe yolculuk başlıyor...")
    gun=input("Kaç gün geçmişe gitmek istersin?: ")
    print(f"{gun} gün öncesine ışınlandın!")

def gelecege_zipla():
    print("Geleceğe zıplıyoruz...")
    gun=input("Kaç gün ileri gitmek istersin?: ")
    print(f"{gun} gün sonrasına ışınlandın!")
    
def format_donustur():
    print("Tar,h formatı dönüştürülüyor...")
    tarih=input("Tarihi şu şekilde gir (gg.aa.yyyy): ")
    yeni_format=tarih.replace(".", "-")
    print(f"Yeni tarih formatı:{yeni_format}")

def zamanmenu():
    print("╔════════════════════════════╗")
    print("║        Zaman Bükücü        ║")
    print("║                            ║")
    print("║  1-Bugünden Geçmişe        ║")
    print("║  2-Geleceğe zıpla          ║")
    print("║  3-Tarih format Dönüştür   ║")
    print("║  4-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        bugunden_gecmise()
    
    elif secim=="2":
        gelecege_zipla()

    elif secim=="3":
        format_donustur() 

    elif secim=="4":
        print("Anamenüye dönülüyor...")  