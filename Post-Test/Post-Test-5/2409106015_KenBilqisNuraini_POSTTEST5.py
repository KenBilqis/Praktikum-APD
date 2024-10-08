# Tampilan awal program
print('''
=====================================
===== Selamat Datang diProgram ======
============ To Do List =============
=====================================''')
    
gagal_login = 0

# Menu login dan perulangan untuk menu login
while True:
    print('''
=================================
|   Silahkan Pilih :            |
|   1. Login sebagai admin      |
|   2. Daftar sebagai user      |
================================= 
''')
    pilihan_login = input("[1/2]: ")
    # Login sebagai admin
    if pilihan_login == "1":
        # Perulangan login sebagai admin
        while True:
            admin = input("\nNama admin: ")
            password_admin = input("Password admin: ")
            # Berhasil login sebagai admin
            if admin == "PendXD" and password_admin == "Mumuthe":
                print('''
------------------------------
 Login sebagai admin berhasil
------------------------------''')
                data_tugas = []
                # Perulangan untuk pemilihan menu admin
                while True:
                    # Tampilan menu admin
                    print('''
===========================
|       TO DO LIST        |
===========================
|    1. TAMBAH TUGAS      |           
|    2. TAMPILKAN TUGAS   |      
|    3. UBAH TUGAS        |     
|    4. HAPUS TUGAS       |      
|    5. KELUAR            |  
===========================''')
                    pilih_menu = input("\nPilih[1/2/3/4/5]: ")
                    # Menambahkan tugas ke dalam data
                    if pilih_menu == "1":
                        print('''
--------------------------------
 Silahkan isi data yang diminta
--------------------------------
''')
                        matkul = input("Mata kuliah: ")
                        tugas = input("Tugas: ")
                        deadline = input("Deadline pengumpulan: ")
                        data_tugas.append([matkul,tugas,deadline])
                        print('''
---------------------------
 Data berhasil ditambahkan
---------------------------
''')
                    # Menampilkan tugas dari data
                    elif pilih_menu == "2":
                        print('''
-----------------------------------
 Tugas-tugas yang harus dikerjakan
-----------------------------------''')
                        for i in range(len(data_tugas)):
                            print(f'''
{i+1}. Data Tugas ke-{i+1}
Mata Kuliah: {data_tugas[i][0]}
Detail Tugas: {data_tugas[i][1]}
Deadline Pengumpulan: {data_tugas[i][2]}''')
                        kembali = input("\nTekan enter untuk kembali ke menu...")
                    # Mengubah data tugas yang sudah ada
                    elif pilih_menu == "3":
                        matkul_ganti = input("Nama mata kuliah tugas yang ingin diganti: ")
                        for i in range(len(data_tugas)):
                            if data_tugas[i][0] != matkul_ganti:
                                tidak_ditemukan = 1
                                continue
                            else:
                                for i in range(len(data_tugas)):
                                    if data_tugas[i][0] == matkul_ganti:
                                        print('''
-------------------------------
 Silahkan isi dengan data baru
-------------------------------
''')
                                        matkul_baru = input("Mata kuliah: ")
                                        tugas_baru = input("Tugas: ")
                                        deadline_baru = input("Deadline pengumpulan: ")
                                        data_tugas[i][0] = matkul_baru
                                        data_tugas[i][1] = tugas_baru
                                        data_tugas[i][2] = deadline_baru
                                        tidak_ditemukan = 0
                                        break
                        # Tampilan untuk pengkondisian jika tidak menemukan data yang ingin diganti dan jika berhasil mengganti data
                        if tidak_ditemukan == 1:
                            print(f"{matkul_ganti} tidak ada dalam data tugas")
                        else:
                            print('''
-----------------------
 Data berhasil diganti
-----------------------
''')
                    # Menghapus data tugas yang sudah ada
                    elif pilih_menu == "4":
                        hapus_matkul = input("Nama mata kuliah yang ingin dihapus: ")
                        for i in range(len(data_tugas)):
                            if data_tugas[i][0] == hapus_matkul:
                                del data_tugas[i]
                                tidak_ditemukan = 0
                                break
                            else:
                                for i in range(len(data_tugas)):
                                    if data_tugas[i][0] != hapus_matkul:
                                        tidak_ditemukan = 1
                                        continue
                        # Tampilan untuk pengkondisian jika tidak menemukan data yang ingin dihapus dan jika berhasil menghapus data
                        if tidak_ditemukan == 1:
                            print(f"{hapus_matkul} tidak ada dalam data tugas")
                        else:
                            print('''
-----------------------
 Data berhasil dihapus
-----------------------''')
                    # Keluar dari program
                    elif pilih_menu == "5":
                        print('''
===========================
===== Program Selesai =====
======= Terimakasih =======
===========================''')
                        exit()
                    # Error handling jika menginput nomor yang salah
                    else:
                        print('''
-----------------
 Pilihan invalid
-----------------''')
                        continue
            # Gagal login sebagai admin
            else:
                # batas gagal login 3 kali
                gagal_login += 1
                if gagal_login == 3:
                    print('''
---------------------------------------------------------------------------------------------
 !!!Program gagal dijalankan karena anda telah melewati batas gagal login sebanyak 3 kali!!!
---------------------------------------------------------------------------------------------''')
                    exit()
                # tampilan jika gagal login sebagai admin
                print('''
----------------------------
 Gagal login sebagai admin!
----------------------------''')
                # Pertanyaan apakah ingin tetap login sebagai admin atau tidak
                login_admin = input("Tetap ingin login sebagai admin?[y/n]: ")
                if login_admin == "y":
                    continue
                elif login_admin == "n":
                    break
                else:
                    print('''
-----------------
 Pilihan invalid
-----------------''')
                    continue
    # Login sebagai pengguna biasa atau disebut user
    elif pilihan_login == "2":
        print('''
---------------------------------------------------
 Silahkan isi data yang diminta untuk membuat akun
---------------------------------------------------
''')
        # User melakukan register atau pendaftaran akun untuk login
        username = input("Buat username: ")
        password_user = input("Buat password: ")
        print('''
----------------------------------------------
 Silahkan login dengan akun yang sudah dibuat
----------------------------------------------
''')
        # Perulangan login sebagai user
        while True:
            nama_user = input("Username: ")
            password_login_user = input("Password: ")
            # Berhasil login sebagai user
            if nama_user == username and password_login_user == password_user:
                print('''
----------------
 Login berhasil
----------------''')
                data_tugas = []
                # Perulangan untuk pemilihan menu user
                while True:
                    # Tampilan menu user
                    print('''
===========================
|       TO DO LIST        |
===========================
|    1. TAMBAH TUGAS      |           
|    2. TAMPILKAN TUGAS   | 
|    3. KELUAR            | 
===========================''')
                    pilih_menu = input("\nPilih[1/2/3]: ")
                    # Menambahkan tugas ke dalam data
                    if pilih_menu == "1":
                        print('''
--------------------------------
 Silahkan isi data yang diminta
--------------------------------
''')
                        matkul = input("Mata kuliah: ")
                        tugas = input("Tugas: ")
                        deadline = input("Deadline pengumpulan: ")
                        data_tugas.append([matkul,tugas,deadline])
                        print('''
---------------------------
 Data berhasil ditambahkan
---------------------------
''')
                    # Menampilkan tugas dari data
                    elif pilih_menu == "2":
                        print('''
-----------------------------------
 Tugas-tugas yang harus dikerjakan
-----------------------------------''')
                        for i in range(len(data_tugas)):
                            print(f'''
{i+1}. Data Tugas ke-{i+1}
Mata Kuliah: {data_tugas[i][0]}
Detail Tugas: {data_tugas[i][1]}
Deadline Pengumpulan: {data_tugas[i][2]}''')
                        kembali = input("\nTekan enter untuk kembali ke menu...")
                    # Keluar dari program
                    elif pilih_menu == "3":
                        print('''
===========================
===== Program Selesai =====
======= Terimakasih =======
===========================''')
                        exit()
                    # Error handling jika menginput nomor yang salah
                    else:
                        print('''
-----------------
 Pilihan invalid
-----------------''')
                        continue
            # Gagal login sebagai user
            else:
                # tampilan jika gagal login sebagai admin
                print("Tolong masukkan username dan password dengan benar")
                # Batas gagl login 3 kali
                gagal_login += 1
                if gagal_login == 3:
                    print('''
---------------------------------------------------------------------------------------------
 !!!Program gagal dijalankan karena anda telah melewati batas gagal login sebanyak 3 kali!!!
---------------------------------------------------------------------------------------------''')
                    exit()
    # Error handling jika menginput nomor yang salah
    else:
        print('''
--------------------------------------
 Maaf anda menginput angka yang salah
    Tolong masukkan dengan bernar
--------------------------------------''')