En üstteki python dosyası aşağıda verilen dosyalar ile yapılmış işlemler içermektedir.
Makine Parça ADET Değişimi ve Tahminleme
Bu Python projesinde, iki Excel dosyasındaki "ADET" (adet sayısı) verilerini birleştirip "START" değişkenine göre görselleştiriyoruz. Ardından, Prophet kütüphanesi kullanarak gelecek haftaya yönelik bir tahmin yapıyoruz.
Gereksinimler
Bu kodun çalışması için aşağıdaki kütüphanelerin kurulu olması gerekmektedir:

pandas
matplotlib
prophet

Adımlar
Veri Yükleme:

ilksatirmakineparca.xlsx ve ilksatir2.xlsx adlı iki Excel dosyasından veriler pandas ile yüklenir.
df1 adlı veri çerçevesinden sadece "ADET" sütunu df1_adet olarak seçilir.
Tarih Sütunu Oluşturma:

Haftalık tarihleri içeren haftalar listesi tanımlanır.
Bu liste, başlangıç tarihi 2024-09-01 alınarak bir "Tarih" sütunu olarak bir veri çerçevesine (tarih_sütunu) dönüştürülür.
Veri Çerçevelerini Birleştirme:

tarih_sütunu, df1_adet ve df2 veri çerçeveleri pd.concat() fonksiyonu kullanılarak birleştirilir.
Birleştirilen veri çerçevesi, MAKİNEBİRLESMİS.xlsx adıyla kaydedilir.
Veriyi Görselleştirme:

MAKİNEBİRLESMİS.xlsx dosyasındaki veri df5 olarak yüklenir.
START değişkeninin farklı değerlerine göre "ADET" değişimini göstermek için bir çizgi grafiği oluşturulur. Her bir START değeri için "Tarih" ve "ADET" ilişkisi çizdirilir.
Prophet ile Tahminleme:

Prophet kütüphanesi kullanılarak, mevcut verilerle 1 hafta ileriye yönelik "ADET" tahmini yapılır.
Tahmin sonuçları görselleştirilerek gösterilir.
Tahmin tablosunun son 5 satırı görüntülenir ve yhat, yhat_lower, ve yhat_upper gibi tahmin sütunları gösterilir.



SONUÇ:Model tahmin grafiği çalıştırılarak doğru model için daha fazla veri gerekli olduğuna karar verilmiştir. Prophet yöntemi yerine ML ve LSTM kullanmaya karar verildi.
