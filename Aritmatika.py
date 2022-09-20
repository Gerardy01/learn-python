


a = 10
b = 5
c = 3

result = a + b
print(result)


# operasi eksponen (pangkat) **
print(a ** b)

# operasi modulus (sisa pembagian) %
print(a % b)
print(a % c)

# operasi floor division (pembagian pembulatan kebawah) //
print (a // c)





# latihan konversi satuan temperatur

celcius_input = float(input("masukan suhu dalam celcius: "))

reamur = (4 / 5) * celcius_input
print ("reamur:", reamur)

fahrenheit = (9 / 5) * celcius_input + 32
print ("fahrenheit:", fahrenheit)

kelvin = celcius_input + 273
print ("kelvin:", kelvin)


farenheit_input = float(input("masukan suhu dalam farenheit: "))
celcius = (5 / 9) * (farenheit_input - 32)

kelvin = celcius + 273
print("kelvin:", kelvin)




kelvin_input = float(input("masukan suhu dalam kelvin: "))
celcius = kelvin_input -273

farenheit = (9 / 5) * celcius + 32
print("farenheit:", farenheit)

