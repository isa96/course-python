# encapsulation: untuk memproteksi class yang dibuat supaya tidak mudah diubah
# dengan menambah double underscore "__"
class Mobil:

    def __init__(self, plat):
        self.__plat = plat
        self.__tipe = "Avanza"
        self.__bensin = 40 # liter
    
    # getter
    def lihatMaxbensin(self):
        print(f"Maksimum bensin yaitu: {self.__bensin} liter")

    # setter
    def aturMaxbensin(self, bensin):
        self.__bensin = bensin


avanza = Mobil(plat="K 1234 DS")

avanza.__bensin = 20
print(avanza.__bensin) # instruksi ini memanggil di atasnya

# memakai fungsi getter
avanza.lihatMaxbensin()

# memakai fungsi setter
avanza.aturMaxbensin(bensin=100)

# lihat lagi perubahannya
avanza.lihatMaxbensin()
