def ort_hesapla():
    print("\n *Not Ortalaması Hesaplama")
    not1=float(input("Birinci Notu Giriniz: "))
    not2=float(input("İkinci Notu Giriniz: "))
    ortalama=not1+not2/2
    print("Not Ortalamanız:", ortalama)

def indeks_hesapla():
    print("\n *Vücut Kitle Endeksi Hesaplama*")
    boy=float(input("Boyunuzu Girin: "))
    kilo=float(input("Kilonuzu Girin: "))
    indeks=kilo/(boy**2)
    print("Vücut Kitle Endeksiniz: ", indeks)

def isi_enerjisi():
    print("\n *Isı Enerjisi Hesaplama*")
    celcius=float(input("sıcaklığı Celcius Cinsinen Giriniz: "))
    fahrenheit=(celcius*9/5)+32
    print("Fahrenheit: ", fahrenheit)

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