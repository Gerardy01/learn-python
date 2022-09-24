



def print_text(text, count):

    i = 0
    while i < count: 
        print(text)
        i += 1
    

print_text("hello world", 5)



def sum(a, b):
    return a + b

print(sum(1, 6))






# function with type hints

def multiplication(a: int, b: int) -> int:
    return a * b




print(multiplication(10, 2))




# *args
# parameter masuk dalam bentuk list

def function_with_args(*args):
    print(args)
    
    i = 0
    for data in args:
        i += data
    
    return i


print(function_with_args(1, 2, 3, 4, 5))




# **kwargs

def do_math(*args, **kwargs):
    
    count = 0
    if kwargs["option"] == "+":
        for e in args:
            count += e
    
    
    elif kwargs["option"] == "*":
        count = 1
        for e in args:
            count *= e
    
    return count




plus_option = do_math(1, 2, 3, 4, 5, option = "+")
print(plus_option)

multiply_option = do_math(1, 2, 3, 4, 5, option = "*")
print(multiply_option)






# lambda function
# one line function

kuadrat = lambda a: a**2 #auto return

print(kuadrat(2))



data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_data = list(filter(lambda data: data < 5, data_angka)) # filter angka < 5 di dalam data_angka

print(new_data)





# anonymous function

def pangkat(n):
    return lambda a: a**n

pangkat2 = pangkat(2) # pangkat2 merupakan fungsi (karena return dari pangkat(2) adalah fungsi)

print(pangkat2(4))

print(pangkat(2)(4)) # 2 mengisi n 4 mengisi a yang merupakan param dari fungsi hasil return pangkat(2)





# change global variable inside function

test = 0

def change():
    global test # access test as a global variable so can be change
    test = 1

change()
print(test)





