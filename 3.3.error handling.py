#nilai = 10
#pembagi = 0
#hasil = nilai/pembagi

#print("Instruksi setelahnya.") # instruksi ini tidak dijalankan karena instruksi di atasnya error pembagi nol

# try and except
# menjalankan instruksi selanjutnya meskipun instruksi di atasnya error, sehingga program tidak break
try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except:
    print("Oops! Terjadi error.")

print("Instruksi setelahnya.")

# pendetailan untuk menampilkan errornya
try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except Exception as e:
    print("Oops! Terjadi error ", e.__class__, ".")

print("Instruksi setelahnya.")

# contoh lain pendetailan, sama seperti susunan if-elif-else
try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except ZeroDivisionError:
    print("Oops! Terjadi ZeroDivisionError.")
except ValueError:
    print("Oops! Terjadi ValueError.")
except:
    print("Oops! Terjadi error yang tidak dikenali.")

# program sederhana tebak-tebakan
# mendefinisikan sendiri eksepsi error
class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

angka = 10

while True:
    
    try:
        tebak_angka = int(input("Masukkan angka: "))

        if tebak_angka < angka:
            raise ValueTooSmallError
        elif tebak_angka > angka:
            raise ValueTooLargeError
        break

    except ValueTooSmallError:
        print("Angka yang kamu tebak terlalu kecil, coba lagi!")
        print()
    except ValueTooLargeError:
        print("Angka yang kamu tebak terlalu besar, coba lagi!")
        print()

print("Betul! Kamu berhasil menebak dengan tepat.")


    


