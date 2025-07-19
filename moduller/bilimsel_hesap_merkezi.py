def ort_hesapla():
    print("ortalama hesaplama çalıştı")
def indeks_hesapla():
    print("indeks hesaplama çalıştı")
def isi_enerjisi():
    print("ısı enerjisi hesaplama çalıştı")    

def bilimselmenu():
    print("╔════════════════════════════╗")
    print("║   Bilimsel Hesap Merkezi   ║")
    print("║                            ║")
    print("║  1-Not Ortalaması          ║")
    print("║  2-Kitle İndeks Hesabı     ║")
    print("║  3-Isı Enerjisi Hesabı     ║")
    print("║  4-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        ort_hesapla()
    
    elif secim=="2":
        indeks_hesapla()

    elif secim=="3":
        isi_enerjisi()   

    elif secim=="4":
        print("Anamenüye dönülüyor...")  