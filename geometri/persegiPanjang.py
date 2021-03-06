from geometri.bangunRuang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l): # method/fungsi yang mendefinisikan argumen class, (self-->merujuk ke objek)
        #fungsi yang pertama kali dipanggil saat objek dibuat
        self.p = p
        self.l = l
    def test(self):
        return 'test persegi panjang'

    def info(self):
        return f'Menghitung rumus persegi panjang dengan panjang {self.p} dan lebar {self.l}'

    def hitung_luas(self):
        return self.p * self.l