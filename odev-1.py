

class Calisan:
    def __init__(self, _tcKimlikNo, _ad, _soyad, _yas, _maas, _calismaSaati):
        self.tcKimlikNo = int(_tcKimlikNo)
        self.ad = str(_ad)
        self.soyad = str(_soyad)
        self.yas = int(_yas)
        self.maas = float(_maas)
        self.calismaSaati = int(_calismaSaati)

    vergiMiktari = 0
    vergisizMaas = 0

    def vergiHesapla(self):
        global vergiMiktari
        if self.maas < 8000:
            vergiMiktari = self.maas * 0.12
        else:
            vergiMiktari = self.maas * 0.18
        # print('Vergi Miktarı: ' + str(vergiMiktari))
        self.vergiMiktari = vergiMiktari

    def sonDurumMaas(self):
        self.vergisizMaas = self.maas - self.vergiMiktari
        # print("Son Durum Maaş: " + str(vergisizMaas))

    def goster(self):
        self.vergiHesapla()
        self.sonDurumMaas()
        print("TC: ", self.tcKimlikNo, ", Ad Soyad: ", self.ad, " ", self.soyad, ", Yaş: ",
              self.yas, ", Maaş: ", self.maas, ", Çalışma Saati: ", self.calismaSaati, ", Vergisiz Maaş: ", self.vergisizMaas)


class PartTimeCalisan(Calisan):
    def __init__(self, _tcKimlikNo, _ad, _soyad, _yas, _saatlikUcret, _calismaSaati):
        super().__init__(_tcKimlikNo, _ad, _soyad, _yas,_saatlikUcret , _calismaSaati)
        self.saatlikUcret = int(_saatlikUcret)

    def sonDurumMaas(self):
        self.maas = self.saatlikUcret * self.calismaSaati
        super().sonDurumMaas()


class FullTimeCalisan(Calisan):
    def __init__(self, _tcKimlikNo, _ad, _soyad, _yas, _maas):
        super().__init__(_tcKimlikNo, _ad, _soyad, _yas, _maas, 0)

    def goster(self):
        self.vergiHesapla()
        self.sonDurumMaas()
        print("TC: ", self.tcKimlikNo, ", Ad Soyad: ", self.ad, " ", self.soyad, ", Yaş: ",
              self.yas, ", Maaş: ", self.maas, ", Vergisiz Maaş: ", self.vergisizMaas)

    def sonDurumMaas(self):
        super().sonDurumMaas()
        self.vergisizMaas = self.vergisizMaas - self.vergisizMaas * 0.08
        # print("Son Durum Maaş: ", str(self.vergisizMaas))


partTimeCalisan = PartTimeCalisan(56798776723, "Emre", "Cambolat", 23, 100, 32)
fullTimeCalisan = FullTimeCalisan(23478075633, "Veli", "Bacik", 27, 9000)


partTimeCalisan.goster()
fullTimeCalisan.goster()

