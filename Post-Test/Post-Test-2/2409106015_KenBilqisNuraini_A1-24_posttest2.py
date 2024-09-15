# user memasukkan data yang di minta
nama_lengkap = input("Masukkan nama lengkap anda: ")
nama_panggilan = input("Masukkan nama panggilan anda: ")
nim = input("Masukkan NIM lengkap anda: ")
prodi = input("Masukkan prodi anda: ")
usia = int(input("Masukkan usia anda: "))
berat_badan = float(input("Berapa berat badan anda?(kg) "))
tinggi_badan = int(input("Berapa tinggi badan anda?(cm) "))

# buat 3 angka di belakang nim menjadi integer lalu moduluskan
nim_int = int(nim[7:])
modulus = nim_int % 6

# tampilkan semua inputan
print(f'''
Nama saya {nama_lengkap} bisa di panggil {nama_panggilan}, NIM saya adalah {nim}.
Saya berasal dari prodi {prodi}, sekarang saya berusia {usia}.
Saya memiliki berat badan {berat_badan} kg dan tinggi badan {tinggi_badan} cm.
Hasil modulus 6 dari 3 angka terakhir dari NIM adalah {modulus}''')