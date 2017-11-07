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

my_function()