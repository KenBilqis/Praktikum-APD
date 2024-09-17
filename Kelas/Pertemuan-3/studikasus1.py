"""
Toko buku Violet ingin membuat diskon buku kepada pembelinya yang membeli 
minimal 5 buku dengan total pembelian lebih dari 100.000, sebesar 20%. Maka buatlah 
program diskon untuk membantu Toko buku violet
"""

# membuat inputan jumlah buku dan total pembelian
jumlah_buku = int(input("Masukkan jumlah buku yang di beli: "))
total_harga = int(input("Masukkan total harga yang harus dibayar: "))

# membuat pengkondisian diskon
if jumlah_buku >= 5:
    if total_harga > 100000:
        diskon = total_harga * 0.2
        total = total_harga - diskon
        print(f'''
Anda mendapat diskon
sehingga total pembelian anda menjadi Rp.{total}''')
    else:
        print(f'''
Anda tidak mendapat diskon karena total pembelian tidak memenuhi syarat
sehingga total pembelian anda adalah Rp.{total_harga}''')
else:
    print(f'''
Anda tidak dapat diskon karena kurangnya jumlah buku
sehingga total pembelian anda adalah Rp.{total_harga}''')
    

