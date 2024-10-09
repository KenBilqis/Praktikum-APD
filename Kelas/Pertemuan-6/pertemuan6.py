# DICTIONARY

# daftar_buku = {
#     # Key : Value
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }
# print(daftar_buku)
# print(daftar_buku["Buku3"])


# Sfiatnya: tidak berurutan, bisa diubah, key tidak boleh sama,
# bisa diisi berbagai macam tipe data

# biodata= {
#     "Nama" : "Ken",
#     "Generasi" : 2409106015,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@Pendxd",
#         "Discord" : "\'Pendxd"
#     }    
# }

# Bentuk lain dictionary
# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = "FPS")
# print(games)


# Cara panggil
# Pakai kurung siku [] buat manggil value lewat key
# print(biodata["KRS"][1])

# Pakai get buat manggil value lewat key
# print(biodata.get("Alamat"))
# Klo pke get misalnya key nya tidak ditemukan bakal tulisannya none, klo kurung siku hasilnya eror
# print(biodata.get("Alamat", "takde isi la"))
                            # untuk memberi pesan jika key tidak ada


# Perulangan Dictionary
# for i in biodata:
#     print(i)
# print("")
# # Ini bakal manggil key doang

# for i in biodata:
#     print(biodata[i])
# print("")
# # Manggil value doang

# for i, j in biodata.items():
#     print(f"Key = {i}, Value = {j}")
# print("")
# # Manggil key dan value pake items()



# Nambah item ke dictionary
# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)
# print("")

# # ada 2 cara nambah
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# #Setelah Ditambah
# print(Film)


# Ubah item di dictionary
# sama aja kek nambahkan bedanya key harus sama sama yg sudah ada
# #Sebelum Diubah
# print(Film)
# print("")
# Film["Sherlock Holmes"] = "Action"
# Film.update({"The Conjuring" : "Tragedy"})
# #Setelah diubah
# print(Film)


# Hapus item di dictionary
# data = {
#     "Nama" : "Ken",
#     "Umur" : 17,
#     "Jurusan" : "Informatika"
# }
# Del:  menghapus key dan value yang ingin di hapus

# pop(): seperti cut(ctr+x)

# clear() : hapus semua yang ada di dalam dictionary


# Fungsi di dlam dictionary
# len(): mengetahui panjang dari dictionary
# print("Jumlah data = ", len(data))
# copy(): membuat sebuah salinan dari dictionary yang ada ke variable baru

# biodata = data.copy()
# print("Dictionary yang Telah Disalin : ", biodata)

# fromkeys(): meembuat dic baru dengan key dan value yang sudah di siapkan
# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# key() & value(): buat manggil masing2
# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i)
#     print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)

# setdefault(): untuk nambah key dan vallue baru jika di dic tidak ada keynya
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)


# List didalam dictionary
# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
# for song in j:
#     print(song)
#     print("")


# Dictonary di dalam dictionary (NESTED DICTIONARY)
# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# manggil dic
# for i, j in mahasiswa.items():
#     print(f"ID : {i}")
#     for i_a, j_a in j.items():
#         print(i_a, " : ", j_a)
#     print("")

# Menambah isi nested dic
# mahasiswa[101]["Angkatan"] = 2023
# print(mahasiswa)

# mengubah isi nested dic
# mahasiswa[101]["Nama"] = "Rizal"
# print(mahasiswa)

# menghapus isi nested list
# del mahasiswa[101]["Umur"]
# print(mahasiswa)


# ====== STUDI KASUS =======
'''Buatlah sebuah dictionary yang memiliki 5 key (Nama, Umur, NIM,
Jurusan, Angkatan). Setelah itu buatlah dictionary ini dapat :
-Menampilkan value
-Mengubah key dan value'''

# biodata = {
#     "Nama" : "Ken",
#     "Umur" : "17",
#     "NIM" : "2409106015",
#     "Jurusan" : "Informatika"
# }

# print(biodata.get("Nama", "takde isi la"))
# biodata.update({"Nama" : "Muthe"})
# print(biodata)

'''CR sederhana'''
Biodata = {}

while True:
    print("1. Tambah")
    print("2. Tampilakan")
    print("3. Exit")
    pilihan =  int(input("(1/2/3) : "))

    if pilihan == 1:
        nama = input("Masukkan nama :")
        umur = input("Masukkan umur :")
        alamat = input("Masukkan alamat :")

        Biodata[nama] = { 
            'Umur' : umur,
            'Alamat' : alamat
        }

    elif pilihan == 2:
        for nama, info in Biodata.items():
            print(f"Nama : {nama}")
            print(f"Umur : {info['Umur']}")
            print(f"Alamat : {info['Alamat']}")

    elif pilihan == 3:
        print("exit ...")
        break

    else:
        print("Invalid ... ... ")