import numpy as np



list_a = [1, 2, 3, 4]
vector_a = np.array(list_a)


print(f"list_a = {list_a}")
print(f"vector_a = {vector_a}")


print(vector_a**2) # bisa langusng dilakuakn operasi bilangan ke dalam list nya



zeros = np.zeros((3, 3))
print(zeros)



a = np.arange(6)
print(a)

a2 = a[np.newaxis, :]
print(a2)


print(a2.shape)







