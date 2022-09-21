

import datetime
from re import A

today = datetime.date.today()

print(today)


date = datetime.date(2001,3,2)
print(date)


print("masukan tanggal lahir anda")
tanggal = int(input("tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("tahun \t\t: "))

tanggal_lahir = datetime.date(tahun, bulan, tanggal)
print(f"tanggal lahir anda adalah {tanggal_lahir:%A}, {tanggal_lahir}")

tanggal_sekarang = datetime.date.today()
umur = tanggal_sekarang.day

print(f"umur anda adalah {umur} tahun")