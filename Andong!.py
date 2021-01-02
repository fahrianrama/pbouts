import sqlite3
import random

databaseName = 'myDb.db'

conn = sqlite3.connect(databaseName)

conn.execute(
    "CREATE table IF NOT EXISTS Driver (ID_Driver int primary key, nama text, password text, nomor_telepon int)",
)
conn.execute(
    "CREATE table IF NOT EXISTS Customer (ID_Customer int primary key, nama text, password text, nomor_telepon int)",
)
conn.execute(
   "CREATE table IF NOT EXISTS Pesanan (ID_Pesanan int primary key, user text, total_biaya int)",
)
conn.execute(
    "CREATE table IF NOT EXISTS Gaji (ID_Driver int, total pesanan int, total_pendapatan int)",
)
conn.execute(
    "insert into Driver values(?,?,?,?)",(12345,'Jono','anu123',823213212)
)
conn.execute(
    "insert into Driver values(?,?,?,?)",(12121,'Joni','anu123',823659236)
)
conn.execute(
    "insert into Pesanan values(?,?,?)",(1111,'Joni',50000)
)
conn.execute(
    "insert into Gaji values(?,?,?)",(12345,13,500000)
)
class Login:
    a=1
    def __init__ (self, id_user, nama, telepon, password):
        self.pilihan = pilihan
        self.id_user = id_user
        self.nama = nama
        self.telepon = telepon
        self.password = password
    
    def signin(self):
        self.id_user = int(input('Masukkan ID Anda : '))
        self.password = str(input('Masukkan Password Anda : '))
        if self.pilihan == 'driver':
            cek = conn.execute('select * from Driver')
            for row in cek:
                if f'{row[0]}' == str(self.id_user):
                    if f'{row[2]}' == str(self.password):
                        print('Selamat datang ',f'{row[1]}')
                    else:
                        print('Password yang anda masukkan salah')
                else:
                    print('Maaf Anda Belum Terdaftar')
        else:
            cek = conn.execute('select * from Customer')
            for row in cek:
                if f'{row[0]}' == str(self.id_user):
                    if f'{row[2]}' == str(self.password):
                        print('Selamat datang ',f'{row[1]}')
                    else:
                        print('Password yang anda masukkan salah')
                else:
                    print('Maaf Anda Belum Terdaftar')

    def signup(self):
        self.id_user = random.randrange(0,1000000)
        self.nama = str(input('Masukkan Nama Anda : '))
        self.password = str(input('Masukkan Password yang Akan Anda Pakai : '))
        self.telepon = int(input('Masukkan Nomor HP Anda : '))
        if self.pilihan == 'driver':
            conn.execute('insert into Driver values (?,?,?,?)',(self.id_user,self.nama,self.password,self.telepon))
        else:
            conn.execute('insert into Customer values (?,?,?,?)',(self.id_user,self.nama, self.password, self.telepon))
        print('Selamat datang ',self.nama)

    def printer(self):
        if self.pilihan == 'driver':
            printer = conn.execute("select * from Driver")
            for row in printer:
                print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')
        else:
            printer = conn.execute("select * from Customer")
            for row in printer:
                print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')

class Andong:
    def __init__ (self,id_user, driver, customer, jarak):
        self.driver = driver
        self.customer = customer
        self.jarak = jarak
        self.id_user = id_user

    def ID_Pesanan(self):
        a = random.randrange(0,1000000)
        return a

class Bonceng(Andong):
    def __init__ (self, driver, customer, jarak):
        super().__init__(self, driver,customer,jarak)
    
    def biaya(self):
        total = self.jarak * 2500
        return total
    
class Maem(Andong):
    def __init__ (self, driver, customer, pesanan, harga_pesanan, jarak):
        super().__init__(self, driver,customer,jarak)
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
        super().__init__(self,driver,customer,jarak)
        self.berat_barang = berat_barang

    def biaya(self):
        ongkir = self.jarak * 3000
        harga = ongkir * self.berat_barang
        return harga

    def waktu(self):
        estimasi = self.jarak * 3
        return estimasi

pilihan = input('Apakah Anda ingin login sebagai Driver/Customer ? : ')
print ('Anda masuk sebagai',pilihan)
masuk = Login(None,None,None,None)
login = input('Apakah anda ingin daftar/masuk dengan akun yang tersedia? (Daftar/Masuk) : ')
if login == 'daftar':
    masuk.signup()
else:
    masuk.signin()     

print('Selamat datang di Andong')
if pilihan == 'driver':
    fitur=input('Apakah anda ingin mencari pesanan/cek pendapatan ? : ')    
    if fitur == 'pesanan':
        pesanan = conn.execute("select * from Pesanan")
        for row in pesanan:
            print(f'{row[0]}, {row[1]}, {row[2]}')
        pilih = int(input('Manakah pesanan yang anda pilih (ID)? : '))
        if f'{row[0]}' == str(pilih):
            print('Anda memilih pesanan :',f'{row[0]}','oleh :', f'{row[1]}')
        else:
            print('Pesanan yang anda pilih tidak tersedia')
    else:
        pendapatan = conn.execute("select * from Gaji")
        for row in pendapatan:
            print(f'{row[2]}')
else:
    fitur=input('Apakah anda ingin menggunakan fitur Bonceng, Maem, atau Kirim ? :')
    if fitur == 'bonceng':
        pesanan = Bonceng(None,None,int(input('Masukkan jarak : ')))
        print('Total biaya adalah :',pesanan.biaya())
    elif fitur == 'maem':
        pesanan = Maem(None,None,str(input('Masukkan nama pesanan : ')),int(input('Masukkan harga pesanan : ')),int(input('Masukkan jarak : ')))
        print('Total biaya adalah :',pesanan.biaya())
    else:
        pesanan = Kirim(None,None,int(input('Masukkan berat barang : ')),int(input('Masukkan jarak : ')))
        print('Total biaya adalah :',pesanan.biaya())
# pilihan.printer()


# pesanan1= Maem("Jono","Joni","Nasgor", 10000, 5)
# conn.execute("insert into Pesanan values(?,?,?,?)",(pesanan1.ID_Pesanan(),pesanan1.customer,pesanan1.driver,pesanan1.biaya()))
# printer = conn.execute("select * from Pesanan")
# for row in printer:
#     print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')
# pesanan2= Maem("Jono","Joni","Nasgor", 10000, 5)
# # conn.execute("insert into Pesanan values (?,?,?,?)",(pesanan1.ID_Pesanan(),pesanan1.customer,pesanan1.driver,pesanan1.biaya()))
# # pesanan2= Kirim("Anjas","Paijo",2,120)
# # conn.cursor().execute("select * from Pesanan")
