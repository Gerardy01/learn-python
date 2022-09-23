

data = [1, 2, 3, 4, 5]



data_range = range(1, 11)

change_to_list = list(data_range)
print(change_to_list)


list_data = []

for i in range(1, 11):
    list_data.append(i)


print(list_data)




# tambah data list

data2 = ["budi", "dono", "siti", "bambang"]

data2.insert(1, "yono") # data2.insert(posisi, item)
print(data2)


data2.append("gilang") # tambah data (mirip push)
print(data2)


# gabungkan data dari 2 list

data_angka_baru = [5, 6, 7, 8, 9]

data.extend(data_angka_baru)
print(data)



data2[3] = "danang"
print(data2)


# menghapus dari list

data2.remove("budi")
print(data2)



data2.pop()
print(data2)







data3 = [3, 5, 1, 4, 9, 8, 7, 7, 2, 3]

jumlah_data_7 = data3.count(7)
print(jumlah_data_7)



# urutkan data

data3.sort()
print(data3)



# sort terbalik (reverse)

data3.reverse()
print(data3)



# ambil posisi data

data2 = ["budi", "dono", "siti", "bambang"]

ambil_index_list = data2.index("siti")
print(ambil_index_list)





# duplicate list with copy

data4 = data2.copy()

data4[0] = "lala"

print(data2)
print(data4)




# enumerate (can get index and the data value)

data5 = [1, 4, 2, 64, 55, 89, 2]

for i, data in enumerate(data5):
    print(data)
    




list_book = []

while True:
    title = input("masukan judul buku\t: ")
    writer = input("masukan nama penulis\t: ")
    
    new_book = [title, writer]
    list_book.append(new_book)

    i = 1
    for book in list_book:
        print(f"buku {i}")
        print(f"nama buku\t: {book[0]}")
        print(f"penulis\t\t: {book[1]}\n")
        i += 1
    
    next = input("input next book? (y/n)\t: ")

    if next == "y":
        continue
    else:
        break







#  data tuoples
# mirip list tapi tidak bisa di ubah (fixed)

data_tuples = (1, 2, 3, 4, 5, 6)
print(data_tuples)




# sets
# collection tanpa index (bisa diubah2 tapi tidak bisa mengambil index nya)

data_sets = {1, 2, 3, 4, 5, 6, 7}
print(data_sets)







