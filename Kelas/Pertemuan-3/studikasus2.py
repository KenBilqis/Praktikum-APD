'''
Sebuah puskesmas meminta kalian untuk membuatkan program dimana mereka dapat 
memasukan umur dari para warga dan program pun akan otomatis memasukan mereka 
kedalam golongan muda, remaja, dewasa, dan lansia.
'''

# buat input untuk memasukkan umur warga
umur = int(input("Masukkan umur warga: "))

# buat pengkondisian untuk menentuka golongan umur
if umur <= 10:
    print("Warga termasuk golongan muda")
elif umur < 19:
    print("Warga termasuk golongan remaja")
elif umur < 50:
    print("Warga termasuk golongan dewasa")
else:
    print("Warga termasuk golongan lansia")
    
    
    