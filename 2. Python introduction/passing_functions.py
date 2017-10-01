def methodception(another):
    return another()

def add_two_numbers():
    return 88 + 21

print(methodception(add_two_numbers))
print('--------------- ----------------')
#lambda fuction

def methodception2(another):
    return another()

print(methodception2(lambda: 88 + 21)) # lambda is one line only


print('--------------- ----------------')

my_list = [212, 23, 9998, 98099, 776, 67667]

# my_list.remove()

# remove odd names

# for item in my_list:
#     if item % 2 != 0:
#         my_list.remove(item)

# print('My list is: {}'.format(my_list))

print(list(filter(lambda x: x % 2 != 0, my_list)))

print('--------------- ----------------')

(lambda x: x * 8)(7)

# is the same as:

def f(x):
    return x * 8

f(5)