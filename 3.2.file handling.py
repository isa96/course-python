# read
#data = open('./data.txt', mode='r') # ./namafile lokasinya sama dengan file python ini
# perlu mengubah lokasi terminal dulu ke lokasi file data.txt disimpan

#print(data.read())

# menambahkan encoding='utf-8', encoding tersebut adalah rekomendasi umum untuk mengakses sebuah file
data = open('./data.txt', mode='r', encoding='utf-8')
string = data.read()
print(string)

# mengganti isi file
string = string.replace('adalah', 'merupakan')
print(string)

# append
data = open('./data.txt', mode='a', encoding='utf-8')
data.write("\nYuk belajar bahasa pemrograman Python!")
data.write("\nAgar jago harus sering berlatih!")
# kalau dirunning berkali-kali maka akan menambahkan berkali-kali

data.close() # untuk menghapus memori yang terpakai
