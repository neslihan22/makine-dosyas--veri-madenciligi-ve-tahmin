import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
df1 = pd.read_excel("ilksatirexcel.xlsx")
df2 = pd.read_excel("ilksatir2.xlsx")
df1_adet = df1[['ADET']]

baslangic_tarihi = pd.to_datetime('2024-09-01')  # Başlangıç tarihi
haftalar = [baslangic_tarihi + pd.DateOffset(weeks=i) for i in range(4)]  # 4 hafta ileri

tarih_sutunu = pd.DataFrame({'Tarih': haftalar})

# df1_start yerine sadece df2'yi kullanarak birleştirme yapıyoruz
df_combined = pd.concat([tarih_sutunu, df1_adet, df2], axis=1)

df_combined.to_excel('MAKİNEBİRLESMİS.xlsx', index=False)

df6 = pd.read_excel('MAKİNEBİRLESMİS.xlsx')

df_prophet = df6[['Tarih', 'ADET', 'START']].copy()
df_prophet.columns = ['ds', 'y', 'START']  # Prophet modeli için sütun isimlerini ayarla


df_prophet['ds'] = pd.to_datetime(df_prophet['ds'], format='%Y-%m-%d')

# Start süresi sütununu sayısal (float) değere dönüştür
# Eğer saat formatında bir veri varsa, bunu dakikaya veya saate çevirin.
df_prophet['START'] = pd.to_timedelta(df_prophet['START']).dt.total_seconds() / 3600  # Saat cinsine çevirme


model = Prophet()
model.add_regressor('START')  
model.fit(df_prophet)


future = model.make_future_dataframe(periods=1, freq='W')  # 1 hafta ileriye tahmin
future['START'] = df_prophet['START'].iloc[-1]  # START değeri, son haftanın START süresi ile dolduruluyor

forecast = model.predict(future)


plt.figure(figsize=(10, 6))
model.plot(forecast)
plt.title('START Süresi ile 5. Hafta ADET Tahmini')
plt.xlabel('Tarih')
plt.ylabel('ADET')
plt.grid(True)
plt.show()


print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

