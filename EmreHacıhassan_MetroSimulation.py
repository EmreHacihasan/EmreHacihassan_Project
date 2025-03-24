from collections import defaultdict, deque
import heapq
from typing import List, Tuple, Dict, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre)

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        if istasyon1_id in self.istasyonlar and istasyon2_id in self.istasyonlar:
            istasyon1 = self.istasyonlar[istasyon1_id]
            istasyon2 = self.istasyonlar[istasyon2_id]
            istasyon1.komsu_ekle(istasyon2, sure)
            istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS kullanarak en az aktarmalı rotayı bulur"""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        kuyruk = deque([(baslangic, [baslangic])])  # (mevcut istasyon, yol)
        ziyaret_edildi = set()

        while kuyruk:
            mevcut, yol = kuyruk.popleft()

            if mevcut == hedef:
                return yol  # Hedefe ulaştık

            if mevcut not in ziyaret_edildi:
                ziyaret_edildi.add(mevcut)
                for komsu, _ in mevcut.komsular:
                    kuyruk.append((komsu, yol + [komsu]))

        return None  # Rota bulunamadı

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur"""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        pq = [(0, baslangic, [baslangic])]  # (toplam süre, istasyon, yol)
        ziyaret_edildi = {}

        while pq:
            toplam_sure, mevcut, yol = heapq.heappop(pq)

            if mevcut == hedef:
                return (yol, toplam_sure)  # Hedefe ulaştık

            if mevcut in ziyaret_edildi and ziyaret_edildi[mevcut] <= toplam_sure:
                continue  # Daha kısa bir yol zaten bulundu

            ziyaret_edildi[mevcut] = toplam_sure

            for komsu, sure in mevcut.komsular:
                yeni_sure = toplam_sure + sure
                heapq.heappush(pq, (yeni_sure, komsu, yol + [komsu]))

        return None  # Rota bulunamadı

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonlar ekleme
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar ekleme
    metro.baglanti_ekle("K1", "K2", 4)
    metro.baglanti_ekle("K2", "K3", 6)
    metro.baglanti_ekle("K3", "K4", 8)
    metro.baglanti_ekle("M1", "M2", 5)
    metro.baglanti_ekle("M2", "M3", 3)
    metro.baglanti_ekle("M3", "M4", 4)
    metro.baglanti_ekle("T1", "T2", 7)
    metro.baglanti_ekle("T2", "T3", 9)
    metro.baglanti_ekle("T3", "T4", 5)
    metro.baglanti_ekle("K1", "M2", 2)
    metro.baglanti_ekle("K3", "T2", 3)
    metro.baglanti_ekle("M4", "T3", 2)

    # Test Senaryoları
    print("\n=== Test Senaryoları ===")

    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
