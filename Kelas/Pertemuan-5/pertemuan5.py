# ============== LIST ==============
member = ["Feni", "Christy", "Muthe", "Gita", "Eli", "Gaby", "Celine", "Jinan"]
staff = ["Jabieb", "Babeh", "Iin", "Aziz"]

# print(type(member))

# print(member[2:5])

# Cara memanipulasi list, menambahkan isi di dalam list tersebut
# print("Sebelum ditambah: ")
# print(member)
# print("\nSesudah ditambah: ")
# member.append("Dey")
# print(member)

# Kalo mau menambah list di index ke berapa
# print("Sebelum ditambah: ")
# print(member)
# print("\nSesudah ditambah: ")
# member.insert(2, "Dey")
# print(member)

# Cara mengganti elemen di dalam list
# print("Sebelum ditambah: ")
# print(member)
# print("\nSesudah ditambah: ")
# member[1]= "Dey"
# print(member)

# Cara menghapus elemen di dalam list
# print("Sebelum ditambah: ")
# print(member)
# print("\nSesudah ditambah: ")
# del member[1]
# print(member)

# Cara memindahkan elemen di dalam list
# print("Sebelum ditambah: ")
# print(member)
# print("\nSesudah ditambah: ")
# pindah = member.pop(1)
# print(member)
# print(pindah)

# Cara memanggil beberapa list
# print("Sebelum ditambah: ")
# print(member)
# print("\nSesudah ditambah: ")
# print(member[0:2])
# 0 = mulai index ke 0, 2 = sampai elemen ke berapa

# Cara memanggil beberapa list tapi di langkahin (STEP)
# print("Sebelum ditambah: ")
# print(member)
# print("\nSesudah ditambah: ")
# print(member[1:6:2])
# 0 = mulai index ke 0, 6 = sampai elemen ke berapa, 2 = langkahin berapa

# Operator +, list di tambah
# print("Sebelum ditambah: ")
# print(member)
# print("\nSesudah ditambah: ")
# semua = member + staff
# print(semua)

# Operator *, list di kali/digandakan
# print("Sebelum ditambah: ")
# print(staff)
# print("\nSesudah ditambah: ")
# print(staff * 3)

# List di dalam list (Nested list)
# data = ["muthe", "eli", "gita", [1, "Hallooo"]]
# print("Sebelum ditambah: ")
# print(data)
# print("\nManggil nested list: ")
# print(data[3])
# print("\nManggil index ke 1 di dlm nested list: ")
# print(data[3][1])
# 3 = index ke bara, 2 = index ke berapa yang di dalam list nested list

# Perulangan buat list
# for i in member:
#     # print(i)
#     # print(i, end=' ')
# # end : untuk memberi spasi atau apapun yg kita mau setelah elemen, jadi elemen nya sampingan bukan ke bawah
#     for j in i:
#         print(j)

# ============== TUPLE ==============
# Mirip list tapi tidak bersifat dinamis, alias tidak bisa di manipulasi
member = ("Dey", "Muthe", "Gita", "Eli")

# print(member)
# print(member[1])

# unpacking tuple
# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")
# absen, prodi, nim, nama = mahasiswa
# print(prodi)

# ============== STUDI KASUS CRUD ==============
print( 
"""
===========================
|   DATA MAHASISWA A24    |
===========================
|    1. TAMBAH DATA       |           
|    2. TAMPILKAN DATA    |          
|    3. UBAH DATA         |     
|    4. HAPUS DATA        |      
|    5. KELUAR            |  
===========================
"""
)

data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA : ")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilih == 2:
        for i in range(len(data_mahasiswa)):
            print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
    elif pilih == 3:
        nama_lama = input("Nama Baru : ")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input("NAMA : ")
                nim_baru = input("NIM : ")
                kelas_baru = input("KELAS : ")
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru
    elif pilih == 4:
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Data Mahasiswa")
        break
    else:
        print("Anda Salah Input")