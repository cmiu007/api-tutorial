import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_than_runs_fun():
        print('In the decorator!')
        func()
        print('After the decorator')
    return function_than_runs_fun

@my_decorator
def my_function():
    print('I m the function!')

# my_function()

##

# accept arguments itself
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_than_runs_func(*args, **kwargs): # pt a face functia generica se pun args si kwargs
            print('In the decorator')
            if number == 56:
                print('Not running the function')
            else:
                func(*args, **kwargs)
            print('After the decorator!')
        return function_than_runs_func
    return my_decorator


@decorator_with_arguments(57) # poate fi ceva de genul isAdmin
def my_function_too(x, y):
    print('the sum is : {}'.format(x * y))

my_function_too(12, 33782)