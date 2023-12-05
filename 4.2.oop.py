# nama classnya harus diawali dengan huruf Kapital (rekomendasi) untuk membedakan dengan fungsi
class Cat:
    """
    ini adalah class untuk membuat object kucing
    melalui kelas ini kita bisa mendefinisikan nama dan tipe kucing yang dibuat
    """

    spesies = "Kucing"

    # membuat atribute (sifat) Kucing: nama dan tipe
    # __init__ berfungsi sebagai konstruktor untuk menjalankan program secara otomatis begitu class dibuat
    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe

    # membuat method (perilaku) Kucing: run
    # untuk menjalankan method fungsinya harus dipanggil dulu
    # method bisa lebih dari 1 dalam 1 class
    def run(self, speed):
        print(f"Kucing {self.nama} berlari dengan {speed}...")
    
    # membuat method Kucing: play
    def play(self):
        print(f"Kucing {self.nama} bermain dengan kucing lainnya...")

    # membuat method Kucing: eat
    def eat(self):
        print(f"Kucing {self.nama} sedang makan...")
    
    """
    seperti ini sudah menjadi 1 blueprint class yang terdiri dari atribute dan method
    """

# 1 class bisa dibuat menjadi banyak object

# membuat object
kinako = Cat(nama="Kinako", tipe="Anggora")
minto = Cat(nama="Minto", tipe="Persia")

print(f"Kinako adalah seekor {kinako.__class__.spesies}.") # memanggil variabel spesies di dalam class kucing
print(f"{kinako.nama} merupakan kucing jenis {kinako.tipe}.")
print(f"{minto.nama} merupakan kucing jenis {minto.tipe}.")

kinako.run("cepat")
kinako.play()

print(kinako.__doc__)

# menghapus atribute tipe
del kinako.tipe
print(kinako.tipe)

# mengahpus object kinako
del kinako
print(kinako)

"""
konsep OOP ini dapat digunakan pada real case di industri,
misalnya untuk mengelola data-data karyawan
"""

# membuat class Employee
class Employee():
    """
    ini adalah class untuk memanipulasi data employee
    melalui class ini kita bisa memanipulasi data yang ada seperti baca, hapus, dan tambah
    """

    def __init__(self, lokasi_file):
        self.data_employee = open(f"{lokasi_file}", mode="r", encoding="utf-8")
        self.data_per_sesi = 10
    
    def baca_data(self):
        self.data_employee = self.data_employee[:self.data_per_sesi]
        return self.data_employee

    def hapus_data(self, baris, kolom):
        del self.data_employee[baris][kolom]

    def tambah_data(self, data_baru):
        nama, gaji, posisi, jabatan, domisili = data_baru
        self.data_employee.append([nama, gaji, posisi, jabatan, domisili])

# membuat object employee
it = Employee(lokasi_file="./karyawan_IT.xls")
marketing = Employee(lokasi_file="./karyawan_marketing.xls")
product = Employee(lokasi_file="./karyawan_product.xls")

# di bidang AI ada object yang abstrak contohnya algoritma Random Forest
class RandomForest():
    pass

