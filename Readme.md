Ben Emre Hacıhassan 

# 🚇 **Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)**

Bu proje, bir metro ağı üzerinde iki istasyon arasındaki:  

- **En az aktarmalı rotayı (BFS algoritması kullanarak)**  
- **En hızlı rotayı (A* benzeri Dijkstra algoritmasını kullanarak)**  

bulan bir simülasyon geliştirmeyi amaçlar.

Bu simülasyon, sürücüsüz metro sistemlerinin optimizasyon problemlerine çözüm üretmek için tasarlanmıştır. Kullanıcılar başlangıç ve hedef istasyonlarını girerek ulaşım için en optimal rotayı görüntüleyebilir.

---

## 📌 **Proje Amacı**
Bu projenin temel hedefleri şunlardır:

1. **Graf (Graph) veri yapısını kullanarak metro ağını modellemek.**
2. **BFS (Breadth-First Search) algoritmasıyla en az aktarmalı rotayı bulmak.**
3. **A* (Dijkstra benzeri) algoritmasıyla en hızlı rotayı hesaplamak.**
4. **Gerçek dünya problemlerini algoritmik düşünce ile çözmek.**
5. **Geliştirilebilir ve genişletilebilir bir yapı sunmak.**

---

## 📁 **İçindekiler**
- [📌 Proje Amacı](#📌-proje-amacı)  
- [🛠️ Kullanılan Teknolojiler ve Kütüphaneler](#🛠️-kullanılan-teknolojiler-ve-kütüphaneler)  
- [📊 Algoritmaların Çalışma Mantığı](#📊-algoritmaların-çalışma-mantığı)  
  - BFS (En Az Aktarmalı Rota)  
  - A* (En Hızlı Rota)  
- [📜 Kod Yapısı](#📜-kod-yapısı)  
- [🧪 Örnek Kullanım ve Test Sonuçları](#🧪-örnek-kullanım-ve-test-sonuçları)  
- [💡 Projeyi Geliştirme Fikirleri](#💡-projeyi-geliştirme-fikirleri)  
- [📤 Yükleme ve Çalıştırma Talimatları](#📤-yükleme-ve-çalıştırma-talimatları)  

---

## 🛠️ **Kullanılan Teknolojiler ve Kütüphaneler**

| **Kütüphane**       | **Kullanım Amacı**                                      |
|---------------------|--------------------------------------------------------|
| `collections.deque` | BFS algoritmasında kuyruk yapısını kullanmak için.      |
| `heapq`             | A* (Dijkstra) algoritmasında öncelik kuyruğu kullanımı. |
| `typing`            | Tip ipuçları (List, Tuple, Dict, Optional) kullanımı.  |

✅ **Python programlama dili** kullanılarak geliştirilmiş olan bu proje, yalnızca Python'un standart kütüphanelerini kullanır. Ek bir kurulum gerektirmez.

---

## 📊 **Algoritmaların Çalışma Mantığı**

### 🔍 **1. BFS (Breadth-First Search) – En Az Aktarmalı Rota**
**BFS (Genişlik Öncelikli Arama)** algoritması, graf yapısında en kısa mesafeyi bulmak için kullanılan bir arama yöntemidir. Bu proje için BFS, **en az aktarmalı rotayı** bulmak amacıyla kullanılmıştır.

**Çalışma Prensibi:**
1. Başlangıç istasyonu bir **kuyruğa (deque)** eklenir.  
2. Kuyruktan her adımda bir istasyon alınır:  
   - Eğer hedef istasyona ulaşıldıysa, mevcut rota döndürülür.  
   - Ulaşılmadıysa, mevcut istasyonun tüm komşuları kuyruğa eklenir.  
3. **Ziyaret edilen istasyonlar** bir kümede saklanır ve aynı istasyona tekrar gidilmesi engellenir.  
4. Aynı isme sahip (aktarma noktası olan) istasyonlar sonuçta yalnızca bir kez gösterilir.

### 🔍 **2. A* (Dijkstra Benzeri) – En Hızlı Rota**
Bu projede, **A* algoritmasının özel bir durumu olan Dijkstra algoritması** kullanılarak en hızlı rota hesaplanmıştır.

**Çalışma Prensibi:**
1. Başlangıç istasyonu, geçiş süresi **0** olacak şekilde bir **öncelik kuyruğuna (heapq)** eklenir.  
2. Kuyruktan her seferinde **en düşük toplam süreye** sahip istasyon çekilir:  
   - Eğer hedef istasyona ulaşıldıysa, toplam süre ve rota döndürülür.  
3. Komşu istasyonlar için geçiş süresi hesaplanır ve toplam süreyle birlikte kuyruğa eklenir.  
4. **Aynı isme sahip** istasyonlar sonuçtan temizlenir.  

✅ **Neden Bu Algoritmalar?**
- BFS algoritması **en az adımda (aktarma sayısı)** ulaşımı sağladığı için kullanıldı.  
- Dijkstra algoritması **en düşük maliyetli (en hızlı)** rota bulduğu için tercih edildi.  

---

## 📜 **Kod Yapısı**
Bu proje aşağıdaki bileşenlerden oluşur:

1. **Istasyon Sınıfı**  
   - İstasyonun kimliği, adı ve bağlı olduğu hattı saklar.  
   - Komşu istasyonları ve geçiş sürelerini tutar.  
   
2. **MetroAgi Sınıfı**  
   - İstasyonlar ve bağlantılar oluşturur.  
   - BFS ve A* algoritmalarını uygular.  
   
3. **Ana Program**  
   - Test senaryolarını çalıştırır ve sonuçları ekrana yazdırır.

---

## 🧪 **Örnek Kullanım ve Test Sonuçları**

Bu projeyi çalıştırmak için:

1. Python ortamınızı hazırlayın:
```bash
python AdSoyad_MetroSimulation.py
```

**Örnek Çıktı:**
```
AŞTİ'den OSB'ye:
En az aktarmalı rota: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
```

**Test Senaryoları:**
1. **Başarılı Rota Bulma**:  
   Farklı başlangıç ve hedef istasyonlar arasında rota bulunur.  

2. **Ulaşılamayan İstasyon Durumu**:  
   Bağlantısı olmayan iki istasyon için `None` değeri döner.  

3. **Aktarma Kontrolü**:  
   Aynı istasyon birden fazla kez geçilmez.

---

## 💡 **Projeyi Geliştirme Fikirleri**
Bu projeyi geliştirmek için bazı öneriler:

1)Bir web arayüzü eklenerek daha gelişmiş hale getirilebilir.

2)Badece metro olması yerine farklı taşıtlarla kombinlenebilir mesela otobüs.

3)Farkllı taşıtlarla kombinlenmesi durumunda anlık trafiği takip eden bir sistem yapılabilir. 

4)Terminal üzerinden durakları değişebilir hale getirmek iyi bir fikir.



