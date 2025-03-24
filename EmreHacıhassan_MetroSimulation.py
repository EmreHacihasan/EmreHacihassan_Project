from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx      # İstasyon kimliği
        self.ad = ad        # İstasyon adı
        self.hat = hat      # Bulunduğu metro hattı
        self.komsular: List[Tuple['Istasyon', int]] = []  # (Komşu istasyon, süre)

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        """İstasyona komşu ve geçiş süresi ekler."""
        self.komsular.append((istasyon, sure))

    def __lt__(self, other: 'Istasyon'):
        """heapq karşılaştırma için gerekli."""
        return self.idx < other.idx

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        """Yeni istasyon ekler."""
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        """İki istasyon arasında çift yönlü bağlantı ekler."""
        if istasyon1_id in self.istasyonlar and istasyon2_id in self.istasyonlar:
            istasyon1 = self.istasyonlar[istasyon1_id]
            istasyon2 = self.istasyonlar[istasyon2_id]
            istasyon1.komsu_ekle(istasyon2, sure)
            istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması ile en az aktarmalı rotayı bulur."""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edilen = set()

        while kuyruk:
            mevcut_istasyon, yol = kuyruk.popleft()

            if mevcut_istasyon == hedef:
                # Aynı adın tekrar etmesini engelle
                temiz_yol = []
                for ist in yol:
                    if not temiz_yol or temiz_yol[-1].ad != ist.ad:
                        temiz_yol.append(ist)
                return temiz_yol

            # Ziyaret edilenlere ekle
            ziyaret_edilen.add(mevcut_istasyon)

            # Komşuları kuyruğa ekle
            for komsu, _ in mevcut_istasyon.komsular:
                if komsu not in ziyaret_edilen:
                    kuyruk.append((komsu, yol + [komsu]))

        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """Dijkstra algoritması ile en hızlı rotayı bulur."""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        pq = [(0, baslangic, [baslangic])]
        ziyaret_edilen = set()

        while pq:
            mevcut_sure, mevcut_istasyon, yol = heapq.heappop(pq)

            if mevcut_istasyon == hedef:
                # Aynı adın tekrar etmesini engelle
                temiz_yol = []
                for ist in yol:
                    if not temiz_yol or temiz_yol[-1].ad != ist.ad:
                        temiz_yol.append(ist)
                return temiz_yol, mevcut_sure

            if mevcut_istasyon in ziyaret_edilen:
                continue

            ziyaret_edilen.add(mevcut_istasyon)

            for komsu, sure in mevcut_istasyon.komsular:
                heapq.heappush(pq, (mevcut_sure + sure, komsu, yol + [komsu]))

        return None

if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonlar ekleme
    istasyonlar = [
        ("K1", "Kızılay", "Kırmızı Hat"), ("K2", "Ulus", "Kırmızı Hat"),
        ("K3", "Demetevler", "Kırmızı Hat"), ("K4", "OSB", "Kırmızı Hat"),
        ("M1", "AŞTİ", "Mavi Hat"), ("M2", "Kızılay", "Mavi Hat"),
        ("M3", "Sıhhiye", "Mavi Hat"), ("M4", "Gar", "Mavi Hat"),
        ("T1", "Batıkent", "Turuncu Hat"), ("T2", "Demetevler", "Turuncu Hat"),
        ("T3", "Gar", "Turuncu Hat"), ("T4", "Keçiören", "Turuncu Hat")
    ]

    for idx, ad, hat in istasyonlar:
        metro.istasyon_ekle(idx, ad, hat)

    # Bağlantılar ekleme
    baglantilar = [
        ("K1", "K2", 4), ("K2", "K3", 6), ("K3", "K4", 8),
        ("M1", "M2", 5), ("M2", "M3", 3), ("M3", "M4", 4),
        ("T1", "T2", 7), ("T2", "T3", 9), ("T3", "T4", 5),
        ("K1", "M2", 2), ("K3", "T2", 3), ("M4", "T3", 2)
    ]

    for ist1, ist2, sure in baglantilar:
        metro.baglanti_ekle(ist1, ist2, sure)

    # Örnek Çıktı: En az aktarmalı ve en hızlı rotalar
    print("\nAŞTİ'den OSB'ye:")

    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

