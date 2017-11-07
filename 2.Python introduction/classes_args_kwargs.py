def my_method(arg1, arg2):
    return arg1 + arg2

def my_long_method(arg1, arg2, arg3, arg4):
    return arg1 + arg2 + arg3 + arg4

my_long_method(8, 7, 9, 2)

def my_list_adition (list_arg):
    return sum(list_arg)

my_list_adition([3, 3, 22, 49, 87, 8, 77, 73])

def addition_simplified(*args):
    return sum(args)

addition_simplified(3, 88, 9, 77, 12, 3, 82, 99, 23)

def what_are_kwars(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwars(12, 32, 56, name='Jose', location='UK')

print('###################')
what_are_kwars(name='Anna', school='UCLA' )


def what_are_kwars2(name, location):
    print(name)
    print(location)

what_are_kwars2(location='Buc S4', name='Gigi')

def what_are_kwars3(arg1, name, location):
    print(name)
    print(location)
    print(arg1)

what_are_kwars3(12, location='Buc S4', name='Gigi')