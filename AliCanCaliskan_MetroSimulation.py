class MetroIstasyonu:
    """
    Metro istasyonlarını temsil eden sınıf.
    """
    def __init__(self, kod, ad, hat):
        self.kod = kod
        self.ad = ad
        self.hat = hat
        self.komsular = []
    
    def baglanti_ekle(self, komsu, sure):
        """
        İstasyonlar arasında bağlantı ekler.
        """
        self.komsular.append((komsu, sure))

class MetroAg:
    """
    Metro ağını yöneten sınıf. İstasyonları ve bağlantıları yönetir.
    """
    def __init__(self):
        self.istasyonlar = {}
    
    def istasyon_ekle(self, kod, ad, hat):
        """
        Yeni bir istasyon ekler.
        """
        self.istasyonlar[kod] = MetroIstasyonu(kod, ad, hat)
    
    def baglanti_ekle(self, kod1, kod2, sure):
        """
        İki istasyon arasında bağlantı ekler.
        """
        if kod1 in self.istasyonlar and kod2 in self.istasyonlar:
            self.istasyonlar[kod1].baglanti_ekle(self.istasyonlar[kod2], sure)
            self.istasyonlar[kod2].baglanti_ekle(self.istasyonlar[kod1], sure)
    
    def en_az_aktarma_bul(self, baslangic, hedef):
        """
        En az aktarma ile rotayı bulur. BFS algoritması kullanır.
        """
        from collections import deque
        kuyruk = deque([(self.istasyonlar[baslangic], [])])
        ziyaret_edilen = set()
        
        while kuyruk:
            mevcut, yol = kuyruk.popleft()
            
            if mevcut.kod == hedef:
                return " -> ".join([istasyon.ad for istasyon in yol + [mevcut]])
            
            ziyaret_edilen.add(mevcut.kod)
            
            for komsu, _ in mevcut.komsular:
                if komsu.kod not in ziyaret_edilen:
                    kuyruk.append((komsu, yol + [mevcut]))
        
        return "Rota bulunamadı"
    
    def en_hizli_rota_bul(self, baslangic, hedef):
        """
        En hızlı rotayı bulur. Dijkstra algoritması kullanır.
        """
        import heapq
        heap = [(0, self.istasyonlar[baslangic], [])]
        ziyaret_edilen = set()
        
        while heap:
            sure, mevcut, yol = heapq.heappop(heap)
            
            if mevcut.kod == hedef:
                return " -> ".join([istasyon.ad for istasyon in yol + [mevcut]]) + f" ({sure} dakika)"
            
            if mevcut.kod in ziyaret_edilen:
                continue
            ziyaret_edilen.add(mevcut.kod)
            
            for komsu, ek_sure in mevcut.komsular:
                if komsu.kod not in ziyaret_edilen:
                    heapq.heappush(heap, (sure + ek_sure, komsu, yol + [mevcut]))
        
        return "Rota bulunamadı"

# Metro ağı oluşturuluyor
metro = MetroAg()

# İstasyonların eklenmesi
metro.istasyon_ekle("M1", "AŞTİ", "Kırmızı Hat")
metro.istasyon_ekle("M2", "Kızılay", "Kırmızı Hat")
metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
metro.istasyon_ekle("M5", "Ulus", "Yeşil Hat")
metro.istasyon_ekle("M6", "Demetevler", "Yeşil Hat")
metro.istasyon_ekle("OSB", "OSB", "Yeşil Hat")
metro.istasyon_ekle("B1", "Batıkent", "Yeşil Hat")
metro.istasyon_ekle("B4", "Keçiören", "Yeşil Hat")

# Bağlantıların eklenmesi
metro.baglanti_ekle("M1", "M2", 5)
metro.baglanti_ekle("M2", "M3", 4)
metro.baglanti_ekle("M3", "M4", 6)
metro.baglanti_ekle("M4", "B4", 5)
metro.baglanti_ekle("M2", "M5", 3)
metro.baglanti_ekle("M5", "M6", 6)
metro.baglanti_ekle("M6", "OSB", 7)
metro.baglanti_ekle("B1", "M6", 6)
metro.baglanti_ekle("B4", "M4", 5)

# Test Senaryoları
print("=== Test Senaryoları ===")
print("1. AŞTİ'den OSB'ye:")
print("En az aktarmalı rota:", metro.en_az_aktarma_bul("M1", "OSB"))
print("En hızlı rota:", metro.en_hizli_rota_bul("M1", "OSB"))

print("\n2. Batıkent'ten Keçiören'e:")
print("En az aktarmalı rota:", metro.en_az_aktarma_bul("B1", "B4"))
print("En hızlı rota:", metro.en_hizli_rota_bul("B1", "B4"))

print("\n3. Keçiören'den AŞTİ'ye:")
print("En az aktarmalı rota:", metro.en_az_aktarma_bul("B4", "M1"))
print("En hızlı rota:", metro.en_hizli_rota_bul("B4", "M1"))
