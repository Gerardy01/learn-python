




from modules import module1



# get data from imported file

print(module1.data)

summed = module1.sum(2, 3)
print(summed)





# module

from modules import math

summed_data = math.sum(1, 2, 3, 4, 5, 6, 7)
print(summed_data)

multiplied_data = math.multiply(2, 4, 5)
print(multiplied_data)






from modules.math import multiply, sum_two_numbers as sumsum

multiplied2 = multiply(10, 10, 10)
print(multiplied2)

sum2num = sumsum(2, 4)
print(sum2num)





# standard library

import datetime

time = datetime.datetime.now()
print(time)
print(time.year)