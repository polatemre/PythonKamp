fakt = int(input("Sayı: "))
if fakt >=0:
  sonuc = 1
  for sayi in range(1,fakt+1,1):
    sonuc = sonuc*sayi
  print(sonuc)
else:
  print("HATA: 0'dan küçük değer girdiniz.")