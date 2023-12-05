# while loop
count = 0
while count < 9:
    print("Nilai count: ", count)
    count += 1
print("Selamat tinggal!")

# while loop harus ada statement yang membuat loopnya berhenti
# jika tidak ada count += 1, maka terjadi loop tak terhingga

# for loop
list_angka = [1,2,3,4,5]
for x in list_angka:
    print(x)

list_range = list(range(1, 9)) # membuat list dengan cepat (awal, increment, stop)
print(list_range)

# break dan continue
for val in "string":
    if val == "i":
        break
    print(val)
print("Loop berakhir!")

for val in "string":
    if val == "i":
        continue
    print(val)
print("Loop berakhir!")

# for else
daftar_murid = ["Angga", "Mardadi", "Rowi", "Farhan", "Hadi"]
nama_murid = "Farhan"

for nama in daftar_murid:
    if nama == nama_murid:
        print(f"Nama murid ditemukan yaitu {nama}")
        break
else:
    print("Nama murid tidak ditemukan!")

# pass
for nama in daftar_murid:
    pass
