# fungsi non parameter
def halo_dunia():
    var = 'Halo Python!'
    print(var)

halo_dunia()

# fungsi parameter
def selamat_datang(nama, alamat):
    print(f"Halo {nama} dari {alamat}!")

selamat_datang("Branglor", "Kudus")

def selamat_datang(*daftar_nama): # tanda bintang untuk memasukkan banyak nama
    var = "Halo "
    for nama in daftar_nama:
        var += nama + ", "
    
    var += "welcome!"
    print(var)

selamat_datang("Nurul", "Siska", "Lukman", "Murdadi", "Rowi")

# fungsi anonim
kali_dua = lambda x: x*2
print(kali_dua(10))

# docstring
def selamat_datang(nama):
    '''
    ini adalah fungsi untuk
    menyapa nama yang telah disebutkan
    '''
    var = f"Halo {nama}, welcome!"
    print(var)

selamat_datang("Branglor")
print(selamat_datang.__doc__) # untuk mencetak komentar atau penjelasan dari fungsi tersebut

# scope dan return
def operasi(a, b, c):
    op1 = a + b
    op2 = op1 // c
    return op2 # saat memanggil fungsi yang ada return-nya ini, maka harus membuat variabel untuk menampung nilai return tsb.

hasil = operasi(a=10, b=5, c=3)
print(hasil)

def operasi(a, b, c=3): # bisa membuat default value, sehingga parameternya tidak diisi semua
    op1 = a + b
    op2 = op1 // c
    return op2 # saat memanggil fungsi yang ada return-nya ini, maka harus membuat variabel untuk menampung nilai return tsb.

hasil = operasi(a=10, b=5)
print(hasil)


# scope di luar fungsi dan scope di dalam fungsi nilainya berbeda, sehingga tidak tumpang tindih
# scope di luar fungsi bisa diakses ke dalam fungsi
# scope di dalam fungsi tidak bisa diakses ke luar fungsi

a, b = 10, 5
hasil = operasi(a, b)
print(hasil)
