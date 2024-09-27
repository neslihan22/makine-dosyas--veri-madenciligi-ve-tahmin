import pandas as pd 
import matplotlib.pyplot as plt
from prophet import Prophet

df1 = pd.read_excel("ilksatirmakineparca.xlsx")
df2 = pd.read_excel("ilksatir2.xlsx")
df1_adet = df1[['ADET']]

haftalar=['2024-09-01', '2024-09-08','2024-09-15','2024-09-22']

# Haftaları bir başlangıç tarihine göre hesaplama ( başlangıç tarihi 2024-09-01)
baslangic_tarihi = pd.to_datetime('2024-09-01')  # 2024 yılı başı olarak alındı
tarih_sütunu = pd.DataFrame({'Tarih': [baslangic_tarihi + pd.DateOffset(weeks=i) for i in range(len(haftalar))]})
tarih_sütunu = pd.DataFrame({'Tarih':haftalar })
df_combined=pd.concat([tarih_sütunu,df1_adet,df2], axis = 1)
df_combined.to_excel('MAKİNEBİRLESMİS.xlsx', index=False)

dosya_yolu = 'C:\\Users\\topra\\OneDrive\\Masaüstü\\YENİ\\MAKİNEBİRLESMİS.xlsx'
df5 = pd.read_excel(dosya_yolu)

plt.figure(figsize=(10, 6))

for start_value in df5['START'].unique():
    filtered_df = df5[df5['START'] == start_value]
    plt.plot(filtered_df['Tarih'], filtered_df['ADET'], marker='o', label=f'START = {start_value}')

plt.title('START Değişkenine Göre ADET Değişimi')
plt.xlabel('Tarih')
plt.ylabel('ADET')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
df6 = pd.read_excel('MAKİNEBİRLESMİS.xlsx')
df_prophet = df6[['Tarih', 'ADET']].copy()
df_prophet.columns = ['ds', 'y']
#Tarih formatını datetime döndürme

df_prophet['ds'] =pd.to_datetime(df_prophet['ds'] )

model =Prophet()
model.fit(df_prophet)


future = model.make_future_dataframe(periods=1, freq='W')  # 1 hafta ileriye tahmin yap
forecast = model.predict(future)

plt.figure(figsize=(10, 6))
model.plot(forecast)
plt.title('4 Hafta Verisi ile 5. Hafta ADET Tahmini')
plt.xlabel('Tarih')
plt.ylabel('ADET')
plt.grid(True)
plt.show()

# Tahmin tablosunu göster
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()





 
