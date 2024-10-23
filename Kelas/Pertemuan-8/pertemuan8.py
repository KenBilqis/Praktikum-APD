'''Error Handling dan File Eksternal'''
# Ketika kita dihadapkan dengan error, kita perlu mengetahui jenis error apa yang terjadi dan di mana error itu terjadi

'''EROR BEDA TIPE DATA'''
# try:
#     angka = int(input("Masukkan angka: "))
# except ValueError: #eror kesini
#        #unruk jenis erornya, kalo ga pake semua eror akan tertangkap
#     print("Input yang anda masukkan bukan angka")
# else: #klo gada eror dia ke sini
#     print(angka)
# finally: #pasti dijalankan mau eror atau engga
#     print("final")

'''Membuat Kustom Error dengan Raise'''
# Keyword `raise` memungkinkan kita membuat error secara manual dan lebih detail.
# try:
#     nama = input("Hello, what's your name? ")
#     if len(nama) > 5:
#         raise ValueError("Nama tidak boleh lebih dari 5 karakter")
# except ValueError as a:
#     print(a)

'''Contoh'''
# try:
#     nim = input("nim: ")
#     if not nim:
#         raise ValueError("Jangan kosong")
#     if not nim.isdigit():
#         raise TypeError("harus angka bor")
#     if len(nim) != 10:
#         raise ValueError("nim harus 10 digit")
# except TypeError as t:
#     print(t)
# except ValueError as e:
#     print(e)
# else:
#     print(f"nim: {nim}")
# finally:
#     print("selesaii...")

'''FILE EXTERNAL'''
# File di luar file program yang di simpan di drive secara permanen
# STRUKTUR: file = open('nama_file.txt', 'r')
# r: Membuka file untuk dibaca
# w: Membuka file untuk ditulis
# a: Membuka file untuk menambah data

# path = '/Pertemuan-8/data.txt'
# file = open('data.txt', 'w')

# membaca semua
# Keyword `with`: File akan otomatis ditutup setelah selesai digunakan
# with open('data.txt', 'r') as file:
#     konten = file.read()
#     print(konten)
    
# # Membaca baris per baris
# with open('data.txt', 'r') as file:
#     for baris in file:
#         print(baris, end='')

# menambah isi file
# with open('data.txt', 'w') as file:
#     file.write("muthe")

with open('data.txt', 'r') as file:
    konten = file.read()
    print(konten)
