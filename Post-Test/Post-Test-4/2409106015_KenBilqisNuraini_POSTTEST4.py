# membuat tampilan awal program
print('''
========================================
======= Selamat Datang diProgram =======
== Kalkulator Kebutuhan Kalori Harian ==
================= TDEE =================
''')

print('''
=====================================================
Silahkan Mengisi Data di Bawah Untuk Membuat Username
=====================================================  
''')

nama = input("Buat username baru dengan nama panggilan anda: ")
nim = input("Masukkan nim anda: ")
nim_int = int(nim[7:])
print("---------------Data Telah Dikonfirmasi---------------")

gagal_login = 0

while True:
    nama_user = input("\nMasukkan username: ")
    nim_user = int(input("Masukkan password berupa nim terakhir tanpa '0': "))
    if nama == nama_user and nim_int == nim_user:
        print("---------------Anda berhasil login!---------------")
        usia = int(input("\nUsia: "))
        # user memilih jenis kelamin
        print('''
Silahkan pilih jenis kelamin anda
1. Pria
2. Wanita''')
        jenis_kelamin = int(input("[1/2]: "))
        # pengkondisian jenis kelamin untuk menghitung bmr dan tdee
        if jenis_kelamin == 1:
            pilihan_jenis_kelamin = "Pria"
            # user menginput berat dan tinggi badan
            bb = float(input("\nBerat Badan dalam satuan gram: "))
            tb = float(input("Tinggi Badan dalam satuan kilometer: "))
            # mengkonversi satuan menjadi satuan standar
            bb_kg = bb / 1000
            tb_cm = tb * 100000
            bmr = (10 * bb_kg) + (6.25 * tb_cm) - (5 * usia) + 5
            # user memilihi level aktivitas harian
            print('''
Pilih Level Ativitas Harian:
1. Aktivitas Minimal => jarang bergerak
2. Aktivitas Sedang => olahraga 1-3 kali seminggu
3. Aktivitas Tinggi => olahraga 4-7 kali seminggu''')
            level_aktivitas_harian = int(input("[1/2/3]: "))
            # pengkondisian level aktivitas harian
            if level_aktivitas_harian == 1:
                poin_aktivitas_harian = 1.25
                tdee = bmr * poin_aktivitas_harian
                # output program
                print(f'''
{nama_user} berusia {usia} berjenis kelamin {pilihan_jenis_kelamin},
Memiliki berat badan {bb_kg} kg dan tinggi badan {tb_cm} cm.
Dengan perhitungan BMR {bmr} dan poin level aktivitas harian {poin_aktivitas_harian},
sehingga kalori yang dibutuhkan dalam sehari adalah {tdee:.0f} kalori''')
                ulang_program = input("Ulangi program?[ya/tidak]: ")
                if ulang_program == "tidak":
                    break
                elif ulang_program == "ya":
                    continue
                else:
                    print("Invalid")
                    exit()
            elif level_aktivitas_harian == 2:
                poin_aktivitas_harian = 1.36
                tdee = bmr * poin_aktivitas_harian
                # output program
                print(f'''
{nama_user} berusia {usia} berjenis kelamin {pilihan_jenis_kelamin},
Memiliki berat badan {bb_kg} kg dan tinggi badan {tb_cm} cm.
Dengan perhitungan BMR {bmr} dan poin level aktivitas harian {poin_aktivitas_harian},
sehingga kalori yang dibutuhkan dalam sehari adalah {tdee:.0f} kalori''')
                ulang_program = input("Ulangi program?[ya/tidak]: ")
                if ulang_program == "tidak":
                    break
                elif ulang_program == "ya":
                    continue
                else:
                    print("Invalid")
                    exit()
            elif level_aktivitas_harian == 3:
                poin_aktivitas_harian = 1.72
                tdee = bmr * poin_aktivitas_harian
                # output program
                print(f'''
{nama_user} berusia {usia} berjenis kelamin {pilihan_jenis_kelamin},
Memiliki berat badan {bb_kg} kg dan tinggi badan {tb_cm} cm.
Dengan perhitungan BMR {bmr} dan poin level aktivitas harian {poin_aktivitas_harian},
sehingga kalori yang dibutuhkan dalam sehari adalah {tdee:.0f} kalori''')
                ulang_program = input("Ulangi program?[ya/tidak]: ")
                if ulang_program == "tidak":
                    break
                elif ulang_program == "ya":
                    continue
                else:
                    print("Invalid")
                    exit()
            else:
                print("Invalid")
                exit()  
        elif jenis_kelamin == 2:
            pilihan_jenis_kelamin = "Wanita"
            # user menginput berat dan tinggi badan
            bb = float(input("\nBerat Badan dalam satuan gram: "))
            tb = float(input("Tinggi Badan dalam satuan kilometer: "))
            # mengkonversi satuan menjadi satuan standar
            bb_kg = bb / 1000
            tb_cm = tb * 100000
            bmr = (10 * bb_kg) + (6.25 * tb_cm) - (5 * usia) - 161
    
            # user memilihi level aktivitas harian
            print('''
Pilih Level Ativitas Harian:
1. Aktivitas Minimal => jarang bergerak
2. Aktivitas Sedang => olahraga 1-3 kali seminggu
3. Aktivitas Tinggi => olahraga 4-7 kali seminggu''')
            level_aktivitas_harian = int(input("[1/2/3]: "))
    
            # pengkondisian level aktivitas harian
            if level_aktivitas_harian == 1:
                poin_aktivitas_harian = 1.25
                tdee = bmr * poin_aktivitas_harian
                # output program
                print(f'''
{nama_user} berusia {usia} berjenis kelamin {pilihan_jenis_kelamin},
Memiliki berat badan {bb_kg} kg dan tinggi badan {tb_cm} cm.
Dengan perhitungan BMR {bmr} dan poin level aktivitas harian {poin_aktivitas_harian},
sehingga kalori yang dibutuhkan dalam sehari adalah {tdee:.0f} kalori''')
                ulang_program = input("Ulangi program?[ya/tidak]: ")
                if ulang_program == "tidak":
                    break
                elif ulang_program == "ya":
                    continue
                else:
                    print("Invalid")
                    exit()
            elif level_aktivitas_harian == 2:
                poin_aktivitas_harian = 1.36
                tdee = bmr * poin_aktivitas_harian
                # output program
                print(f'''
{nama_user} berusia {usia} berjenis kelamin {pilihan_jenis_kelamin},
Memiliki berat badan {bb_kg} kg dan tinggi badan {tb_cm} cm.
Dengan perhitungan BMR {bmr} dan poin level aktivitas harian {poin_aktivitas_harian},
sehingga kalori yang dibutuhkan dalam sehari adalah {tdee:.0f} kalori''')
                ulang_program = input("Ulangi program?[ya/tidak]: ")
                if ulang_program == "tidak":
                    break
                elif ulang_program == "ya":
                    continue
                else:
                    print("Invalid")
                    exit()
            elif level_aktivitas_harian == 3:
                poin_aktivitas_harian = 1.72
                tdee = bmr * poin_aktivitas_harian
                # output program
                print(f'''
{nama_user} berusia {usia} berjenis kelamin {pilihan_jenis_kelamin},
Memiliki berat badan {bb_kg} kg dan tinggi badan {tb_cm} cm.
Dengan perhitungan BMR {bmr} dan poin level aktivitas harian {poin_aktivitas_harian},
sehingga kalori yang dibutuhkan dalam sehari adalah {tdee:.0f} kalori''')
                ulang_program = input("Ulangi program?[ya/tidak]: ")
                if ulang_program == "tidak":
                    break
                elif ulang_program == "ya":
                    continue
                else:
                    print("Invalid")
                    exit()
            else:
                print("Invalid")
                exit()
        else:
            print("Invalid")
            exit()
    elif nama == nama_user and nim_int != nim_user:
        print("Anda salah memasukkan password")
        gagal_login += 1
        if gagal_login == 3:
            print("\n!!!Program gagal dijalankan karena anda telah melewati batas gagal login sebanyak 3 kali!!!")
            exit()
    elif nama != nama_user and nim_int == nim_user:
        print("Anda salah memasukkan username")
        gagal_login += 1
        if gagal_login == 3:
            print("\n!!!Program gagal dijalankan karena anda telah melewati batas gagal login sebanyak 3 kali!!!")
            exit()
    else:
        print("Tolong masukkan nama dan password dengan benar")
        gagal_login += 1
        if gagal_login == 3:
            print("\n!!!Program gagal dijalankan karena anda telah melewati batas gagal login sebanyak 3 kali!!!")
            exit()

print('''
=======================================
=========== Program Selesai ===========
============= Terimakasih =============
=======================================
''')
