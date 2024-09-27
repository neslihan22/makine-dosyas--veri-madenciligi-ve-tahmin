import pandas as pd 

def birlesik_satirlar_excel(dosya_liste):
 
     ilksatirlar = []
     
     for dosya in dosya_liste:
        df=pd.read_excel(dosya, dtype=str)
        zaman_sütunları =['MİNİMUM SÜRE','MAKSİMUM SÜRE','ORTALAMA SÜRE']
        for sütun in zaman_sütunları:
            try:
               df[sütun]=pd.to_datetime(df[sütun], format='%H:%M:%S', errors='coerce').dt.time

            except Exception as e:
                print(f"{sütun} format cevrilemedi:{e}")
        ilksatir=df.iloc[0]
        ilksatirlar.append(ilksatir)
        birlesmis=pd.DataFrame(ilksatirlar)
     return birlesmis

dosyalar=['makine verimadenciliğive tahmin\\Makine Parça Özet Rapor.xlsx','makine verimadenciliğive tahmin\\Makine Parça Özet Rapor (1).xlsx','makine verimadenciliğive tahmin\\Makine Parça Özet Rapor (2).xlsx','makine verimadenciliğive tahmin\\Makine Parça Özet Rapor (3).xlsx',]
birlesmisdosya=birlesik_satirlar_excel(dosyalar)
print(birlesmisdosya)
birlesmisdosya.to_excel('ilksatirmakineparca.xlsx', index=False)