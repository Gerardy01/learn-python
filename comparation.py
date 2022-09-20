

#  is membandingkan dengan object identity yang sama

a = 5
b = 5
c = 10
print(a is b)
print(a is not c)



# not

a = True
b = not a

print(a)
print(b)


# or (||)

print(a or b)


# and (&&)

print(a and b) 



# XOR (^)
# akan true jika yang true hanya salah satu saja

print(a ^ b)







# user_input = int(input("masukan angka: "))

# a = user_input < 3
# b = user_input > 10

# print(a or b)


# print(user_input > 3 and user_input < 10)


user_input = int(input("masukan angka: "))

a = user_input > 0 and user_input < 5
b = user_input > 8 and user_input < 11

print(a or b)

user_input_two = int(input("masukan angka: "))

d = user_input_two < 0
e = user_input_two > 5 and user_input_two < 8
f = user_input_two > 11

print(d or e or f)






