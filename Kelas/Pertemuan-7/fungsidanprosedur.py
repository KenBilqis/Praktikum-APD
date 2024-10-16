# FUNGSI DAN PROSEDUR

'''Fungsi & prosedur speerti templet biar bisa dipanggil terus
Fungsi membutuhkan pengembalian nilai (return)
Prosedur tidak mengembalikan nilai (return)'''
# def nama_fungsi(parameter):
# pernyataan

# contoh
# def salam():
#     print("selamat datang di python")
    
# salam()

# Parameter
# Parameter adalah variabel yang menampung nilai untuk diproses di dalam fungsi.
# def salam(salam):
#     print(salam)
# iso = "salam iso"
# salam(iso)

# Variabel Global dan Lokal
# Variabel Global adalah variabel yang bisa diakses dari semua fungsi
# Nama = "Informatika"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)
# # variabel lokal hanya bisa diakses di dalam fungsi tempat dia berada saja
# def info():
#     Nama = "Teknik Elektro"
#     Mata_Kuliah = "Pengantar Teknik ELektro"
#     # mengakses variabel lokal
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)
# info()
# # mengakses var global dengan fungsi
# def bio():
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)
# bio()

'''Program CRUD Menggunakan Fungsi'''
# buku =[]
# # fungsi untuk menampilkan semua data
# def show_data():
#     if len(buku) <= 0:
#         print ("Belum Ada data")
#     else:
#         print("ID", "Nama Buku")
#         for indeks in range(len(buku)):
#             print (indeks, buku[indeks])
# # fungsi untuk menambah data
# def insert_data():
#     buku_baru = input("Judul Buku : ")
#     buku.append(buku_baru)
# # fungsi untuk edit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         buku[indeks] = judul_baru
# # fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         buku.remove(buku[indeks])
# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")
#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")

# while (True):
#     show_menu()

# Posedur
# Fungsi yang tidak mengembalikan nilai

'''STUDI KASUS
buat fungsi menghitung luas segitiga, dengan angka dimasukkan user'''

# def luas_segitiga():
#     tinggi =  int(input("masukkan tinggi: "))
#     alas = int(input("masukkan alas: "))
#     luas = alas * tinggi / 2
#     return luas
# # Pake ruturn biar bisa memanggil luas
# print(luas_segitiga())

'''STUDI KASUS
persegi panjang lewat inputan user'''

def luas_pp():
    panjang = int(input("masukkan panjang: "))
    lebar = int(input("masukkan lebar: "))
    luas = lebar * panjang
    return luas
print(luas_pp())
