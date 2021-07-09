sayi1 = 10
sayi2 = 30
sayi3 = 25
eb = 0

if sayi1 > sayi2 and sayi1 > sayi3:
    eb = sayi1
elif sayi2 > sayi1 and sayi2 > sayi3:
    eb = sayi2
else:
    eb = sayi3

print("En büyük sayı: " + str(eb))