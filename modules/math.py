



def sum_two_numbers(a, b):
    return a + b

def sum(*args):
    count = 0
    for e in args:
        count += e
    
    return count

def multiply(*args):
    i = 0
    while i < len(args):
        if i == 0:
            count = args[i]
            i += 1
            continue

        count *= args[i]
        i += 1
    
    return count