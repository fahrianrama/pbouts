print('Nomor 2, Class Ikan')
class Ikan():
    'Ikan adalah hewan yang hidup di air'
    jumlah=0
    def __init__ (self, nama_ikan, jenis_ikan, umur_ikan, ukuran_ikan, harga):
        self.nama_ikan = nama_ikan
        self.jenis_ikan = jenis_ikan
        self.umur_ikan = umur_ikan
        self.ukuran_ikan = ukuran_ikan
        self.harga = harga
        Ikan.jumlah += 1
    
    def set_harga(self, harga_baru):
        self.harga = harga_baru

    def get_harga(self):
        return self.harga
    
    def total_ikan(self):
        return Ikan.jumlah

Ikan1 = Ikan('Anu','Lohan','12 Bulan','20 cm','100000')
Ikan2 = Ikan('Ane','Koi','2 Bulan', '10 cm','40000')
Ikan3 = Ikan('Ola','Cupang','5 Bulan','5 cm','25000')

Ikan1.set_harga('120000')
print('Harga Ikan2 : ',Ikan2.get_harga())
print('Jumlah dalam akuarium : ', Ikan1.total_ikan())