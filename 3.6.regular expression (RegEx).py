# RegEx berfungsi untuk memanipulasi data teks secara efektif

import re

# melihat kecocokan pola dari suatu data teks
teks1 = "regex"
x1 = re.match("^r...x$", teks1)
print(x1)

# memisah data teks per kata
teks2 = "saya senang belajar regex"
x2 = re.split("\s", teks2)
print(x2)

# substitusi karakter angka apapun menjadi double "="
teks3 = """
        ada 3 tipe loop atau perulangan di bahasa pemrograman Python yaitu while loop,
        for loop, dan nested loop 2022
        """
x3 = re.sub("\d+", "--", teks3)
print(x3)

# mencari kecocokan pola pada suatu data teks
teks4 = "hujan deras di kawasan depok"
x4 = re.search("^hujan.*depok$", teks4)
if  x4:
    print("YES! We have a match.")
else:
    print("No match!")

# mencari format yang diinginkan
teks5 = "23 oct 2019 23 oct,2019 23 october,2019 0ct 26,2020"
x5 = re.findall("\d{2} [a-z]{3} \d{4}", teks5)
print(x5)

# substitusi teks harga berapapun menjadi triple "_"
teks6 = "harga 1 mobil antik tersebut yaitu $1000"
x6 = re.sub("\$\d+", "___", teks6)
print(x6)

# substitusi teks url apapun menjadi triple "_"
teks7 = "akan dialihkan ke http://twitter.com"
x7 = re.sub("http[s]?\://\S+", "___", teks7)
print(x7)

# mencari tagar atau hashtag saja
teks8 = "luar biasa! banyak anak-anak muda traveling tahun ini, begini tanggapan lesley #travel #_lesley #viral #gadget"
x8 = re.findall("#[_]*[a-z]+", teks8)
print(x8)

