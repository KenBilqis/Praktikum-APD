# Variabel global
kesempatan_login = 0
data_tugas = {}
data_user = {}

# Prosedur untuk tampilan awal program
def tampilan_awal():
    print('''
=====================================
===== Selamat Datang diProgram ======
============ To Do List =============
=====================================''')

# Prosedur untuk menu pilihan login
def menu_login():
    print('''
=================================
|   Silahkan Pilih :            |
|   1. Login sebagai admin      |
|   2. Daftar sebagai user      |
================================= 
''')

# Prosedur tampilan jika berhasil login
def berhasil_login():
    print('''
----------------
 Login Berhasil
----------------''')

# Fungsi gagal login
def login_gagal():
    if kesempatan_login == 3:
        print('''
--------------------------------------------------------------
                !!!Program gagal dijalankan!!!
 karena anda telah melewati batas gagal login sebanyak 3 kali
--------------------------------------------------------------''')
        exit()
    print('''
-------------
 Gagal Login 
-------------''')

# Prosedur tampilan jika meinput angka yang salah
def invalid():
    print('''
-----------------
 Pilihan invalid
-----------------''')

# Fungsi mencari tugas dalam data
def cari_data(tugas):
    if tugas in data_tugas:
        return True
    else:
        return False

# Fungsi menambah tugas
def menambah_tugas():
    print('''
--------------------------------
 Silahkan isi data yang diminta
--------------------------------
''')
    matkul = input("Mata kuliah: ")
    tugas = input("Tugas: ")
    deadline = input("Deadline pengumpulan: ")
    data_tugas[matkul] = { 
    'Tugas' : tugas,
    'Deadline' : deadline
    }
    print('''
---------------------------
 Data berhasil ditambahkan
---------------------------
''')

# Fungsi menampilkan tugas
def menampilkan_tugas():
    if not data_tugas:
        print('''
----------------------------------
 Belum ada tugas yang ditambahkan
----------------------------------''')
    else:
        print('''
-----------------------------------
 Tugas-tugas yang harus dikerjakan
-----------------------------------''')
        for i, j in data_tugas.items():
            print(f'''
Mata Kuliah: {i}
  Detail Tugas: {j['Tugas']}
  Deadline Pengumpulan: {j['Deadline']}''')
        input("\nTekan enter untuk kembali ke menu...")

# Fungsi mengubah data tugas yang sudah ada
def mengubah_tugas():
    matkul_ganti = input("Nama mata kuliah tugas yang ingin diganti: ")
    if cari_data(matkul_ganti):
        print('''
-------------------------------
 Silahkan isi dengan data baru
-------------------------------
''')
        matkul_baru = input("Mata kuliah: ")
        tugas_baru = input("Tugas: ")
        deadline_baru = input("Deadline pengumpulan: ")
        data_tugas[matkul_baru] = data_tugas.pop(matkul_ganti)
        matkul_ganti = matkul_baru
        data_tugas[matkul_ganti]['Tugas'] = tugas_baru
        data_tugas[matkul_ganti]['Deadline'] = deadline_baru
        print('''
-----------------------
 Data berhasil diganti
-----------------------
''')
    else:
        print(f"{matkul_ganti} tidak ada dalam data tugas")


# Fungsi menghapus data tugas
def menghapus_tugas():
    hapus_matkul = input("Nama mata kuliah yang ingin dihapus: ")
    if cari_data(hapus_matkul):
        del data_tugas[hapus_matkul]
        print('''
-----------------------
 Data berhasil dihapus
-----------------------''')
    else:
        print(f"{hapus_matkul} tidak ada dalam data tugas")

# Fungsi keluar dari program
def keluar_program():
    print('''
===========================
===== Program Selesai =====
======= Terimakasih =======
===========================''')
    exit()

# Fungsi menu admin menggunakan fungsi rekursif
def menu_admin():
    print('''
===========================
|       TO DO LIST        |
===========================
|    1. Tambah Tugas      |           
|    2. Tampilkan Tugas   |      
|    3. Ubah Tugas        |     
|    4. Hapus Tugas       |      
|    5. Keluar Menu       |  
===========================''')
    pilih_menu = input("\nPilih[1/2/3/4/5]: ")
    if pilih_menu == "1":
        menambah_tugas()
    elif pilih_menu == "2":
        menampilkan_tugas()
    elif pilih_menu == "3":
        mengubah_tugas()
    elif pilih_menu == "4":
        menghapus_tugas()
    elif pilih_menu == "5":
        keluar_program()
    # eror handling jika menginput nomor yang salah
    else:
        invalid()
    
    menu_admin()

# Fungsi menu user menggunakan fungsi rekursif
def menu_user():
    print('''
===========================
|       TO DO LIST        |
===========================
|    1. Tambah Tugas      |           
|    2. Tampilkan Tugas   |           
|    3. Keluar Menu       |  
===========================''')
    pilih_menu = input("\nPilih[1/2/3]: ")
    if pilih_menu == "1":
        menambah_tugas()
    elif pilih_menu == "2":
        menampilkan_tugas()
    elif pilih_menu == "3":
        keluar_program()
    # eror handling jika menginput nomor yang salah
    else:
        invalid()
        
    menu_user()

# PROGRAM UTAMA
tampilan_awal()
while True:
    menu_login()
    pilihan_login = input("[1/2]: ") # Variabel global
    # Login sebagai admin
    if pilihan_login == "1":
        # Perulangan login sebagai admin
        while True:
            admin = input("\nNama admin: ") # Variabel global
            password_admin = input("Password admin: ") # Variabel global
            # Berhasil login sebagai admin
            if admin == "PendXD" and password_admin == "Mumuthe":
                berhasil_login()
                menu_admin()
            else:
                kesempatan_login +=1
                login_gagal()
    elif pilihan_login == "2":
        print('''
---------------------------------------------------
 Silahkan isi data yang diminta untuk membuat akun
---------------------------------------------------
''')
        # User melakukan register atau pendaftaran akun untuk login
        username = input("Buat username: ") # Variabel global
        password_user = input("Buat password: ") # Variabel global
        data_user[username] = password_user
        print(data_user)
        print('''
----------------------------------------------
 Silahkan login dengan akun yang sudah dibuat
----------------------------------------------
''')
        # Perulangan login sebagai user
        while True:
            nama_user = input("\nUsername: ") # Variabel global
            password_login_user = input("Password: ") # Variabel global
            # Berhasil login sebagai user
            if nama_user in data_user and password_login_user == data_user[nama_user]:
                menu_user()
            else:
                kesempatan_login +=1
                login_gagal()
    else:
        # eror handling jika menginput nomor yang salah
        invalid()