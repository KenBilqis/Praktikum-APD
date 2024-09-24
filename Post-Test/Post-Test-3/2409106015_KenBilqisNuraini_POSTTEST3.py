# membuat tampilan awal program
print('''
========================================
======= Selamat Datang diProgram =======
== Kalkulator Kebutuhan Kalori Harian ==
================= TDEE =================
''')

# user memasukkan nama dan usia
nama_user = input("Nama: ")
usia = int(input("Usia: "))

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
    elif level_aktivitas_harian == 2:
        poin_aktivitas_harian = 1.36
        tdee = bmr * poin_aktivitas_harian
        # output program
        print(f'''
{nama_user} berusia {usia} berjenis kelamin {pilihan_jenis_kelamin},
Memiliki berat badan {bb_kg} kg dan tinggi badan {tb_cm} cm.
Dengan perhitungan BMR {bmr} dan poin level aktivitas harian {poin_aktivitas_harian},
sehingga kalori yang dibutuhkan dalam sehari adalah {tdee:.0f} kalori''')
    elif level_aktivitas_harian == 3:
        poin_aktivitas_harian = 1.72
        tdee = bmr * poin_aktivitas_harian
        # output program
        print(f'''
{nama_user} berusia {usia} berjenis kelamin {pilihan_jenis_kelamin},
Memiliki berat badan {bb_kg} kg dan tinggi badan {tb_cm} cm.
Dengan perhitungan BMR {bmr} dan poin level aktivitas harian {poin_aktivitas_harian},
sehingga kalori yang dibutuhkan dalam sehari adalah {tdee:.0f} kalori''')
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
    elif level_aktivitas_harian == 2:
        poin_aktivitas_harian = 1.36
        tdee = bmr * poin_aktivitas_harian
        # output program
        print(f'''
{nama_user} berusia {usia} berjenis kelamin {pilihan_jenis_kelamin},
Memiliki berat badan {bb_kg} kg dan tinggi badan {tb_cm} cm.
Dengan perhitungan BMR {bmr} dan poin level aktivitas harian {poin_aktivitas_harian},
sehingga kalori yang dibutuhkan dalam sehari adalah {tdee:.0f} kalori''')
    elif level_aktivitas_harian == 3:
        poin_aktivitas_harian = 1.72
        tdee = bmr * poin_aktivitas_harian
        # output program
        print(f'''
{nama_user} berusia {usia} berjenis kelamin {pilihan_jenis_kelamin},
Memiliki berat badan {bb_kg} kg dan tinggi badan {tb_cm} cm.
Dengan perhitungan BMR {bmr} dan poin level aktivitas harian {poin_aktivitas_harian},
sehingga kalori yang dibutuhkan dalam sehari adalah {tdee:.0f} kalori''')
    else:
        print("Invalid")
        exit()
else:
    print("Invalid")
    exit()
