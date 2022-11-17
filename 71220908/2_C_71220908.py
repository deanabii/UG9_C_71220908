kecepatan = int(input("Masukkan kecepatan tempuh:"))
waktu = int(input("Masukkan waktu yang diperlukan:"))

Bensin = kecepatan*waktu/10
Biaya = Bensin*15000

print("Teman Anda mengisi bensin sebanyak", Bensin, "liter")
print("Biaya yang dikeluarkan untuk mengisi bensin adalah Rp.", Biaya)
