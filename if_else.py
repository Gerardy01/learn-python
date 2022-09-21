




nama = input("masukan nama: ")


if nama=="gerardy":
    print("hey")

print("end")


nilai = int(input("masukan nilai anda: "))


if nilai < 40:
    print("maaf kamu belum lulus")
elif nilai >= 40 and nilai <= 60:
    print("kamu dapat nilai C")
elif nilai > 60 and nilai < 80:
    print("kamu dapat nilai B")
else:
    print("kamu dapat nilai A")




print("kalkulator")
a = float(input("masukan angka pertama: "))
b = float(input("masukan angka kedua: "))
operator = input("masukan operator bilangan: ")


if operator == "+":
    result = a + b
    print(f"{a} + {b} = {result}")
elif operator == "-":
    result = a - b
    print(f"{a} - {b} = {result}")
elif operator == "*":
    result = a * b
    print(f"{a} * {b} = {result}")
elif operator == "/":
    result = a / b
    print(f"{a} / {b} = {result}")
