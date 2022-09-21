


a = "Hello world"
print(a)



print("don't")

# r for raw (to write raw string)
print(r"abc\asas\lol") 

print("line one\nline two")




nama_depan = "gerardy"
nama_tengah = "lucas"
nama_belakang = "paudianto"

full_name = nama_depan + " " + nama_tengah + " " + nama_belakang
print(full_name)


name_length = len(full_name) # .length using len()
print(name_length)



# to check if there is a specific character inside string
e = "e"
status = "e" in e

print(status)


print("wk" * 5)

print(full_name[0:10:2])



# smallest character
print(min(nama_depan))



# biggest character
print(max(nama_depan))






# operator method

data = "geRardy luCas paUdiaNto"
count = data.count("a")

print(count)


# upper and lower case

print(data.upper())
print(data.lower())



# join and split

sentence_list = ["hey", "this", "is", "me"]

joined = " ".join(sentence_list) # join with space
print(joined)


joined_sentence = "hello my friend"

splited = joined_sentence.split(" ")
print(splited)


# string formating (mirip `asakjsdk ${nama}`)

nama_ini = "Budi"

test_string = f"hello {nama_ini}"
print(test_string)



angka = 2000000
the_string = f"{angka:,}"
print(the_string)








