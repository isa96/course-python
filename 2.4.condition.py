# materi condition

jumlah_penumpang = 3

if jumlah_penumpang > 10:
    pass # jika belum ada instruksi bisa diisi pass, supaya tidak error

if jumlah_penumpang < 10:
    pass

print("Di luar kondisi.")

if jumlah_penumpang > 10:
    print("Mobil berjalan...")
else:
    print("Mobil menunggu penumpang lain...")

# contoh lain
score = 88
if score >= 85:
    print("Predikat A/Sangat Memuaskan")
elif score >= 75:
    print("Predikat B/Memuaskan")
else:
    print("Tidak Lulus")

# contoh pakai fungsi input
num = float(input("Masukkan angka: "))

if num == 0:
    print("Nol")
else:
    print("Angka Positif")


