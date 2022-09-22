


data = ["siti", "budi", "bejo", "lala"]

for i in data:
    print(i)



for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(f"{i} Fizz")
    elif i % 3 != 0 and i % 5 == 0:
        print(f"{i} Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print(f"{i} FizzBuzz")
    else:
        print(i)



i = 0
while i < 10:
    print(i)
    i += 1



i = 0
while i < len(data):
    print(data[i])
    i += 1


# break similar to return but implemented in loop
i = 0
cust = ""
while i < len(data):
    if (data[i] == "bejo"):
        cust = data[i]
        break
    
    cust = ""
    i += 1

print(cust)


line = int(input("masukan panjang segitiga: "))
i = 0

stair = ""
while i < line:
    i += 1
    stair = "*"*i

    print(stair)
