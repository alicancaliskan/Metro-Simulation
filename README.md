Metro Simülasyonu

Bu proje, Ankara metrosundaki istasyonlar arasında en az aktarmalı ve en hızlı rotaları bulan bir Python uygulamasıdır. Proje, yeni mezun bir bilgisayar programcılığı öğrencisinin anlayabileceği kadar sade ve temiz bir şekilde kodlanmıştır.

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


