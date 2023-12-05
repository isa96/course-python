# materi variabel dan tipe data

# eksekusi python adalah berurutan dari atas ke bawah
angka = 100
print(angka)

angka = 1000
print(angka)

email = "fatah.ai.engineer@gmail.com"
print(email)

# cara lain membuat multi variabel
angka1, angka2, email = 100, 1000, "fatah.ai.engineer@gmail.com"
print(angka1)
print(angka2)
print(email)

angka1 = angka2 = angka3 = 100
print(angka1)
print(angka2)
print(angka3)

# constant (konstanta)
# penulisan konstanta penulisannya menggunakan huruf KAPITAL
nama_saya = "Fatah" # variabel
NAMA_SAYA = "Jalil" # konstanta

PI = 3.14 # konstanta
GRAVITY = 9.8 # konstanta

print(nama_saya)
print(NAMA_SAYA)

# dilarang memakai simbol -, !, @, $, angka di awal saat penulisan variabel

angka_eksponen = 8.9e3 # artinya 8.9 x 10^3
print(angka_eksponen)

# memeriksa tipe data
a = 4
b = 3.14
c = 3/4
d = "Nama"
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# mengubah tipe data pada suatu variabel
f = float(a)
g = int(b)
h = str(b)
print(f)
print(type(f))
print(g)
print(type(g))
print(h)
print(type(h))

# f string
nama = "Jalil"
s = f"Nama saya adalah {nama}"
print(s)

