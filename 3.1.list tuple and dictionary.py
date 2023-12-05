# materi list
fruit_list =["apple", "banana", "watermelon", "orange", "mango", "cerry", "pineapple"]

# mengakses list
print(fruit_list[1:4])
print(fruit_list[-3:])

# mengganti nilai list
fruit_list[2] = "avocado"
print(fruit_list)

# membership test (memeriksa apakah suatu nilai berada di dalam list yang dimaksud)
print("watermelon" in fruit_list)
print("watermelon" not in fruit_list)

# menambahkan list
fruit_list.append("grape")
print(fruit_list)

fruit_list.insert(1, "dragon")
print(fruit_list)

# menghapus list
fruit_list.remove("orange")
print(fruit_list)

fruit_list.pop(-1)
print(fruit_list)

del fruit_list[0]
print(fruit_list)

del fruit_list # menghapus list sampai tidak dikenali
#print(fruit_list)

# menghapus list menjadi list kosong
fruit_list2 =["apple", "banana", "watermelon"]
fruit_list2.clear()
print(fruit_list2)

# materi tuple
fruit_tuple =("apple", "banana", "watermelon", "orange", "mango")

# mengakses tuple
fruit_tuple[:3]
print(fruit_tuple)
# tuple tidak bisa diedit (mengubah, menambahkan, maupun dihapus) = immutable = permanen
# gunanya untuk menyimpan data-data yang bersifat tetap atau konstan

# materi dictionary
fruit_dict = {"nama" : "pisang",
              "jenis" : "tanduk",
              "kode" : 111,
              "harga" : 25000}

# mengakses dictionary
print(fruit_dict)
print(fruit_dict["jenis"])

# for loop pada dictionary
for key, value in fruit_dict.items():
    print(key, value)

for key in fruit_dict.keys():
    print(key, fruit_dict[key])

# lebih dari 1 dictionary
fruit_dict = [{"nama" : "pisang",
              "jenis" : "tanduk",
              "kode" : 111,
              "harga" : 25000},
              {"nama" : "mangga",
              "jenis" : "kuweni",
              "kode" : 112,
              "harga" : 30000}
              ]
print(fruit_dict)

# set = himpunan
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# union = pakai tanda "atau (|)"
print(A | B)

# intersection = pakai tanda "dan (&)"
print(A & B)

# difference = pakai tanda "-"
print(A - B)
print(B - A)

# symetric difference
print(A ^ B)



