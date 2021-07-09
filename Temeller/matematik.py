class Matematik:
    def __init__(self, sayi1, sayi2):  # constructor
        self.s1 = sayi1
        self.s2 = sayi2

    def topla(self):
        return self.s1 + self.s2

    def cikar(self):
        return self.s1 - self.s2

    def bol(self):
        return self.s1 / self.s2

    def carp(self):
        return self.s1 * self.s2


matematik = Matematik(3, 5)
sonuc = matematik.topla()
print("Sonuç: " + str(sonuc))


class Istatistik(Matematik): # inheritance
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2) # super() = Matematik
    def varyansHesapla(self):
        return self.s1 * self.s2

istatistik = Istatistik(5,8)
istatistik.topla()