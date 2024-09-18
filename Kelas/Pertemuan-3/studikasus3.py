'''
Pak Kades sedang mendata penduduknya berdasarkan jenis kelamin, buatlah program
sederhana untuk menentukan jenis kelamin seseorang dengan menggunakan ternary operator
'''

# buat inputan nama dan pertanyaan jenis kelamin
nama = input("Masukkan nama: ")
gender = input("Masukkan jenis kelamin[L/P]: ")

# buat pengkondisian dengan ternary operator
result = "Laki-Laki" if gender == "L" else "Perempuan" 

# buat otput result
print(f"{nama} berjenis kelamin {result}")