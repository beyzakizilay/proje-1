def anamenu():
    print("Anamenu")
    print("╔════════════════════════════╗")
    print("║          ANAMENU           ║")
    print("║                            ║")
    print("║  1-Roket Fırlatma İstasyonu║")
    print("║  2-YZ Laboratuarı          ║")
    print("║  3-Bilimsel Hesap Merkezi  ║")
    print("║  4-Holografik Çizim Alanı  ║")
    print("║  5-Uzay Günlüğü            ║")
    print("║  6-Keşif Kayıtları         ║")
    print("║  7-Sistem Ayarları         ║")
    print("║  8-Zaman Bükücü            ║")
    print("║  9-Galaksi Haritası        ║")
    print("║  10-Görev Sonlandır        ║")
    print("║     Tercihiniz Nedir?      ║")
    print("╚════════════════════════════╝")

    secim=input("Seçiminiz nedir: ")
    if secim=="1":
       import moduller.roket_firlatma_istasyonu
       moduller.roket_firlatma_istasyonu.roketmenu()
    
    elif secim=="2":
        import moduller.yz_laboratuarı
        moduller.yz_laboratuarı.yzmenu()
    
    elif secim=="3":
        import moduller.bilimsel_hesap_merkezi
        moduller.bilimsel_hesap_merkezi.bilimselmenu()

    elif secim=="4":
        import moduller.holografik_cizim_alani
        moduller.holografik_cizim_alani.holografikmenu()

    elif secim=="5":
        import moduller.uzay_gunlugu
        moduller.uzay_gunlugu.uzaymenu()
        
    elif secim=="6":
        import moduller.kesif_kayitlari
        moduller.kesif_kayitlari.kesifmenu()

    elif secim=="7":
        import moduller.sistem_ayarlari
        moduller.sistem_ayarlari.sistemmenu()   

    elif secim=="8":
        import moduller.zaman_bukucu
        moduller.zaman_bukucu.zamanmenu()   

    elif secim=="9":
        import moduller.galaksi_haritasi
        moduller.galaksi_haritasi.galaksimenu()  

    elif secim=="10":
        print("Çıkış Yaptınız...")
        exit  

    elif secim>10:
        print("Hatalı Tuşlama Yaptınız, 1-10 arasında bir seçim yapınız...")         
anamenu() #değer döndüren fonksiyon