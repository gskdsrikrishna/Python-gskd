my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list):
    print(index, val)
my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list, start=1):
    print(index, val)
my_list = [21, 44, 35, 11]

for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = []
for sublist in my_list:
    for num in sublist:
        flat_list.append(num)

print(flat_list)
import itertools

my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = list(itertools.chain(*my_list))
print(flat_list)
from functools import reduce

my_list = [[1], [2, 3], [4, 5, 6, 7]]
print(reduce(lambda x, y: x+y, my_list))
my_list = [1, 2, 3, 4, 5]

print(my_list[:])
my_list = [1, 2, 3, 4, 5]

print(my_list[2:])

my_list = [1, 2, 3, 4, 5]

print(my_list[:2])
my_list = [1, 2, 3, 4, 5]

print(my_list[2:4])
my_list = [1, 2, 3, 4, 5]

print(my_list[::2])

my_list = [1, 2, 3, 4, 5]

print(my_list[::2])

my_list = [1, 2, 3, 4, 5]

print(my_list[::2])v

