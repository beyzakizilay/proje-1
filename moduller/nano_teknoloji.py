def nano_robot():
    print("Nano Robotlar aktive ediliyor...")
    print("Mikroskobik sesviyede tamir işlemi başlatıldı!!!")
    hedef= input("Hangi yapıyı onarmak istersin? (örnek:hücre, devre, uzay giysisi): ")
    print(f"{hedef} üzerinde onarım işlemi başladı. Nanobotlar çalışıyor...")

def parcacik_hizlandirici():
    print("Parçacık hızlandırıcı devrede!!!")
    hiz=input("Parçacıklara uygulanacak hızı gir (örnek: 3.0 x ışık hızı): ")
    print(f"Parçacıklar {hiz} hızında çalıştırılıyor... Enerji seviyeleri artıyor!!!")

def molekuler_tarama():
    print("Moleküler tarama başlatıldı...")
    madde=input("Hangi maddeyi taramak istersin? (örnek: kuantum jeli, yıldız tozu): ")
    print(f"{madde} analiz ediliyor... Moleküler yapı eşleştiriliyor... Tamamlandı!")


def nanomenu():
    print("╔════════════════════════════╗")
    print("║   Nano Teknoloji Odası     ║")
    print("║                            ║")
    print("║  1-Nano Robotları Gönder   ║")
    print("║  2-Parçacık Hızlandırıcı   ║")
    print("║  3-Moleküler Tarama        ║")
    print("║  4-Anamenüye dön           ║")
    print("╚════════════════════════════╝")
    secim=input("Seçiminiz: ")
    if secim=="1":
        nano_robot()
    
    elif secim=="2":
     parcacik_hizlandirici()

    elif secim=="3":
        molekuler_tarama()

    elif secim=="4":
        print("Anamenüye dönülüyor...")  