The Python file at the top contains operations performed with the files listed below.

Machine Part Quantity Change and Forecasting
In this Python project, we merge the "ADET" (quantity) data from two Excel files and visualize it based on the "START" variable. Then, we make a forecast for the upcoming week using the Prophet library.

Requirements
The following libraries need to be installed for this code to work:

pandas
matplotlib
prophet
Steps

Data Loading:

Data is loaded from two Excel files named "ilksatirmakineparca.xlsx" and "ilksatir2.xlsx" using pandas.
The "ADET" column from the df1 DataFrame is selected as df1_adet.
Creating the Date Column:

A list of weekly dates is defined.
This list is converted into a DataFrame (tarih_sütunu) with a "Date" column, starting from the date 2024-09-01.
Merging DataFrames:
The tarih_sütunu, df1_adet, and df2 DataFrames are merged using the pd.concat() function.
The merged DataFrame is saved with the name MAKİNEBİRLESMİS.xlsx.

Visualizing the Data:

The data from the MAKİNEBİRLESMİS.xlsx file is loaded as df5.
A line graph is created to show the change in "ADET" based on different values of the "START" variable. The relationship between "Date" and "ADET" is plotted for each "START" value.
Forecasting with Prophet:

The Prophet library is used to make a 1-week ahead forecast for "ADET" based on the existing data.
The forecast results are visualized.
The last 5 rows of the forecast table are displayed, showing forecast columns like yhat, yhat_lower, and yhat_upper.






TÜRKÇE:


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



