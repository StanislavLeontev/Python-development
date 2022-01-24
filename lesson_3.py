def type_logger(func):

    def func_arg(*args):
        for arg in args:
            print(f'{func.__name__} ({arg}: {type(arg)})')

        return

    return func_arg

@type_logger
def main(x):
    return

a = main(5, 2, 4.5, 'Hello', -5)

print(a)