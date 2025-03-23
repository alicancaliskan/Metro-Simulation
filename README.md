Metro Simülasyonu

Proje Açıklaması

Bu proje, Ankara metrosundaki iki istasyon arasındaki en kısa ve en hızlı rotaları bulan bir Python programıdır. Yeni mezun bir bilgisayar programcısı olarak öğrendiğim algoritmaları uygulamak için geliştirdiğim bir proje. Rotaları hesaplamak için BFS ve Dijkstra algoritmalarını kullandım. 🚇

Özellikler

✅ Metro istasyonlarını ve hatlarını içeren bir veri yapısı
✅ İstasyonlar arası bağlantılar ve süre bilgileri
✅ En az aktarmalı rota bulma (BFS algoritması)
✅ En hızlı rota bulma (Dijkstra algoritması)
✅ Örnek test senaryoları ile doğrulama

Kullanılan Teknolojiler

Python 3 

Veri Yapıları: Listeler, sözlükler ve öncelik kuyruğu

Algoritmalar: BFS ve Dijkstra

Kurulum

Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsin:

Python 3 yüklü olduğundan emin ol.

Dosyayı indir veya projeyi klonla.

Terminal veya komut istemcisinde şu komutu çalıştır:

python metro_simulation.py

Örnek Çıktılar

Programı çalıştırdığında şöyle bir çıktı alacaksın:

=== Test Senaryoları ===
1. AŞTİ'den OSB'ye:
   En az aktarmalı rota: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
   En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB

2. Batıkent'ten Keçiören'e:
   En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
   En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören

3. Keçiören'den AŞTİ'ye:
   En az aktarmalı rota: Keçiören -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
   En hızlı rota (19 dakika): Keçiören -> Gar -> Sıhhiye -> Kızılay -> AŞTİ

Geliştirme ve Katkı

Projeyi geliştirmek istersen:

Kendi fork’unu oluştur.

Yeni özellik ekle veya hata düzeltmesi yap.

Pull Request açarak katkıda bulun! 😊

Lisans

Bu proje MIT lisansı ile paylaşılmıştır. İstediğin gibi geliştirip kullanabilirsin! 🚀

