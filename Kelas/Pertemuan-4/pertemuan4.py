# PERULANGAN FOR
# ulang = 15
# for i in range(ulang):
#     print(f"perulangan ke-{str(i)}")

# array
# simpan = [12, "udin petot", 14.5, True, 'A']
# for i in simpan:
    # print(i, end=' ') # end berguna agar for tidak berurut di bawah, tapi kesamping

# lompatan
# for i in range(1, 10, 2): # (awal, akhir, lompatan)
#     print(i)

# for di dalam for
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")
#     print()
    
# PERULANGAN WHILE
# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total perulangan: {hitung}")

# break
# hitung = 0
# while True:
#     hitung += 1
#     ulang = input("Masih ingin mengulang? ")
#     if ulang == "tidak" or ulang == "Tidak":
#         break
# print(f"Total perulangan: {hitung}")

# continue
# print("Daftar bilangan ganjil dari 1-10")
# for i in range(10):
#     if i % 3 == 0:
#         continue
#     print(i)

# STUDI KASUS
'''Buatlah program perulangan while yang menjumlahkan semua inputan 
integer positif, jika diinput negatif maka program berhenti!'''
# JAWAB
# bilangan = 0
# while True:
#     angka = int(input("Masukkan angka: "))
#     if angka < 0:
#         break
#     bilangan += angka
# print("Total bilangan: " + str(bilangan))

# STUDI KASUS
'''Buat penglangan 1-20 lompatan 3 jika dimoduluskan 2=0 dia continue'''
# JAWAB
# for i in range(1, 20, 3): # (awal, akhir, lompatan)
#     if i % 2 == 0:
#         continue    
#     print(i)

# STUDI KASUS
# buah = ["apel", 'pisang', 'jeruk', 'melon', 'semangka']
# buah_baru = []
# for i in buah:
#     if "e" in i:
#         buah_baru.append(i)
# print(buah_baru)
# cara singkatnya
# buah_baru = [i for i in buah if "e" in i]
# print(buah_baru)