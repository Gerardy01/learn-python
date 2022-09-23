



dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

print(dictionary['key1'])

dictionary_length = len(dictionary)
print(dictionary_length)



# check if key exist or not

check_key_is_exist = "key1" in dictionary
print(check_key_is_exist)




# access dictionary value with get

print(dictionary.get("key2"))
print(dictionary.get("tidak ada"))




# update dictionary
# if data doesn't exist, add new data with inputed key and value

dictionary.update({"key1": "new value"})
dictionary.update({
    "key4": "value4"
})

print(dictionary)



# delete dictionary data

del dictionary["key1"]
print(dictionary)






# take all dictionary keys (iterable)

dictionary_keys = dictionary.keys()
print(dictionary_keys)

for data in dictionary.keys():
    print(data)





# take all dictionary values (iterable)

dictionary_values = dictionary.values()
print(dictionary_values)

for data in dictionary.values():
    print(data)





# take all dictionary key and value

items = dictionary.items()
print(items)

for item in items:
    print(item)

for item in dictionary.items():
    print(item)


for key, item in dictionary.items():
    print(f"key = {key}, value = {item}")






# pop dictionary data

data_key2 = dictionary.pop("key2")
print(data_key2)

print(dictionary)




