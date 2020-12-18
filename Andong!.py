class Andong:
    def __init__ (self, driver, customer, jarak):
        self.driver = driver
        self.customer = customer
        self.jarak = jarak
        
class Bonceng(Andong):
    def __init__ (self, driver, customer, jarak):
        super().__init__(driver,customer,jarak)
    
    def biaya(self):
        total = self.jarak * 2500
        return total
    
class Maem(Andong):
    def __init__ (self, driver, customer, pesanan, harga_pesanan, jarak):
        super().__init__(driver,customer,jarak)
        self.pesanan = pesanan
        self.harga_pesanan = harga_pesanan
        
    def biaya(self):
        ongkir = self.jarak * 2000
        harga = self.harga_pesanan + ongkir
        return harga
    
    def waktu(self):
        estimasi = self.jarak * 2
        return estimasi
    
class Kirim(Andong):
    def __init__ (self, driver, customer, berat_barang, jarak):
        super().__init__(driver,customer,jarak)
        self.berat_barang = berat_barang

    def biaya(self):
        ongkir = self.jarak * 3000
        harga = ongkir * self.berat_barang
        return harga

    def waktu(self):
        estimasi = self.jarak * 3
        return estimasi

 
pesanan1= Maem("Jono","Joni","Nasgor", 10000, 5)
print(pesanan1.driver,pesanan1.customer,pesanan1.biaya())